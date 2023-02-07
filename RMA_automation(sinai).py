  
#!/usr/bin/env python
# coding: utf-8

# # RMA Export
# This script logs in to RMA (training or prod environment) and downloads all files from one or more patient charts. It was converted from `rma-export.ipynb` using `jupyter nbconvert --to python rma-export.ipynb`.
#
# The code is hosted at Mount Sinai's GitHub Enterprise at [CDO/rma-export](https://github.mountsinai.org/CDO/rma-export/), and [an HTML rendering of the notebook can be found on that repo's associated GitHub Pages site][rma-export.html].
#
# ## Python script / command-line interface
# This script exposes a command-line interface and a `rma-export` Bash-wrapper:
#
# ```bash
# ./rma-export -h
# ```
# ```
# usage: rma-export.py [-h] [--cin CIN] [-F CIN_FILE] [-c CIN_FILE_COL] [-l {ignore,warn,raise}] [-f] [-o OUT_DIR] [-p] [--prod]
#                      [-s SLEEP_INTERVAL]
#
# optional arguments:
#   -h, --help            show this help message and exit
#   --cin CIN             Comma-delimited list of CINs to pull (can be repeated)
#   -F CIN_FILE, --cin-file CIN_FILE
#                         File to load CINs from
#   -c CIN_FILE_COL, --cin-file-col CIN_FILE_COL
#                         Column in `cin_file` containing CINs (optional; if absent, and `cin_file` is provided, the first column in `cin_file`
#                         is used)
#   -l {ignore,warn,raise}, --level {ignore,warn,raise}
#                         How to handle missing documents: "ignore", "warn", or "raise"
#   -f, --overwrite       Overwrite files already found on disk (default: False)
#   -o OUT_DIR, --out-dir OUT_DIR
#                         Directory to save downloaded files to (default: current directory)
#   -p, --pdfs            Convert all downloaded files to PDFs
#   --prod                Use production instance (rma.healthcare; default: training.rma.healthcare)
#   -s SLEEP_INTERVAL, --sleep-interval SLEEP_INTERVAL
#                         Sleep interval between patients
# ```
#
# To update `rma-export.py` based on the contents of the notebook:
#
# ```bash
# jupyter nbconvert --to python rma-export.ipynb
# ```
#
# Note that this will overwrite the Python script's CLI configs with the [Papermill] configs used by this notebook, so you should use `git add -p` to only Git-commit intended changes to the Python script.
#
# ## GitHub Pages site
# [The HTML version of the notebook hosted on GitHub Pages][rma-export.html] can be updated like:
# ```bash
# jupyter nbconvert --to html --stdout rma-export.ipynb > docs/index.html
# ```
#
# ## Executing via [Papermill]
# The notebook can also be executed programmatically via [Papermill] (using with parameters in the first cell below configurable from the command-line):
#
# ```bash
# papermill -p cin MA32105M,RT58473R rma-export.ipynb nbs/2_cin_test.ipynb
# ```
#
# This is equivalent to the following `rma-export` run:
#
# ```bash
# ./rma-export --cin MA32105M,RT58473R
# ```
#
# but the Papermill version outputs an executed notebook (to `nbs/2_cin_test.ipynb`), which can be useful for debugging or auditing purposes down the line.
#
# This example output notebook can also be viewed on the GH Pages site: https://github.mountsinai.org/pages/CDO/rma-export/nbs/2_cin_test.ipynb
#
# ## Building / Running in Docker
# A Docker container, with `pip` dependencies installed from [`requirements.txt`](https://github.mountsinai.org/CDO/rma-export/blob/master/requirements.txt) and other configs from [`gsmo.yml`](https://github.mountsinai.org/CDO/rma-export/blob/master/gsmo.yml), can be booted up, and a Jupyter server running inside it opened, using [`gsmo`]:
#
# ```bash
# gsmo j  # short for `gsmo jupyter`
# ```
#
# For a Bash shell instead, run:
#
# ```bash
# gsmo sh
# ```
#
# ## `config.py` / RMA Credentials
# Both the notebook and script versions assume the existence of a `config.py` that defines a `creds` dict with `user`, `pswd`, and – in the case of running against a prod or staging instance – `otp` keys:
#
# ```python
# creds = {
#     'user': …,
#     'pswd': …,
#     'otp' : …,  # apparently required for staging/prod, but hasn't been tested / is not currently passed to scraper anywhere
# }
# ```
#
# ## Original script
# This notebook is a port of Jose Cruz's original [`rma_full_chart_download.py`](rma_full_chart_download.py) script. Some of the functionality found there has not been tested since refactoring into this notebook:
#
# ### HARP page screenshotting
# - ported over, but not tested
# - training site doesn't appear to include applicable test patients
#
# ### Merging all documents into one PDF per patient
# - converting Microsoft Office formats (`.doc{,x}`, `.xls{,x}`) requires Windows APIs; imports of `comtypes.client` and `win32api` will crash on macOS/Linux.
# - by default, files are downloaded as-is into per-CIN directories
# - the `convert_to_pdf` (`-p` CLI flag) enables PDF conversion; otherwise files are downloaded as-is
# - merging all files into one PDF needs to be reimplemented / ported over to this version of the script
#
# ## Overview
# 1. [Inputs](#inputs)
# 1. [Imports](#imports)
# 1. [Load/Parse CINs](#load-cins)
# 1. [Log in](#login)
# 1. [Download files](#download)
#
# ## Inputs <a id="inputs"></a>
# These variables can be passed in to [Papermill] from the command-line (for programmatic running of this notebook):
#
# [Papermill]: https://papermill.readthedocs.io/en/latest/
# [`gsmo`]: https://github.com/runsascoded/gsmo/
# [rma-export.html]: https://github.mountsinai.org/pages/CDO/rma-export/

# ### Command-line Interface <a id="cli"></a>
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument('--cin',action='append',help='Comma-delimited list of CINs to pull (can be repeated)')
parser.add_argument('-F','--cin-file',help='File to load CINs from')
parser.add_argument('-c','--cin-file-col',help='Column in `cin_file` containing CINs (optional; if absent, and `cin_file` is provided, the first column in `cin_file` is used)')
parser.add_argument('-l','--level',default='warn',choices=['ignore','warn','raise',],help='How to handle missing documents: "ignore", "warn", or "raise"')
parser.add_argument('-f','--overwrite',action='store_true',help='Overwrite files already found on disk (default: False)')
parser.add_argument('-o','--out-dir',help='Directory to save downloaded files to (default: current directory)')
parser.add_argument('-p','--pdfs',action='store_true',help='Convert all downloaded files to PDFs')
parser.add_argument('--prod',action='store_true',help='Use production instance (rma.healthcare; default: training.rma.healthcare)')
parser.add_argument('-s','--sleep-interval',default=0.5,type=float,help='Sleep interval between patients')
args = parser.parse_args()
overwrite = args.overwrite
convert_to_pdf = args.pdfs
level = args.level
out_dir = args.out_dir
prod = args.prod
cin = [ cin for arg in (args.cin or []) for cin in arg.split(',') ]
cin_file = args.cin_file
cin_file_col = args.cin_file_col
sleep_interval = args.sleep_interval


# Hard-coded inputs for testing:

if not cin_file and not cin:
    cin_file = 'RHH-Patients.csv'
    if not cin_file_col:
        cin_file_col = 'Medicaid ID'


# Toggle "training" vs. production RMA instance:

if prod:
    domain = 'https://rma.healthcare'
else:
    domain = 'https://training.rma.healthcare'


if not level in {'ignore','warn','raise'}:
    raise ValueError(level)


# ## Imports <a id="imports"></a>
# Import [utz](https://pypi.org/project/utz/) helpers + login credentials.
#
# The credentials should be in a file called `config.py` in this directory:
# ```python
# creds = {
#     'user': …,
#     'pswd': …,
#     'otp' : …,  # apparently required for staging/prod, but hasn't been tested / is not currently passed to scraper anywhere
# }
# ```
# Additionally, "staging" or "prod" environments apparently require an MFA or OTP token. If this can be hard-coded, you can add it to the `config.py:creds` as above, but note that the scraper still needs to be updated to pass it in the appropriate place.

from utz import *
import config
user = config.creds['user']
pswd = config.creds['pw']
otp = config.creds.get('otp')  # required for staging/prod! TODO: use this in scraper below


# File download/conversion imports:

from fpdf import FPDF
import img2pdf
import openpyxl as xl
from openpyxl import load_workbook
from PIL import Image
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
from selenium import webdriver
import time


# Default `out` directory to current directory:

if not out_dir:
    out_dir = getcwd()


# ## Load/Parse CINs <a id="load-cins"></a>
# Load CINs from `cin` string and/or `cin_file`:

cins = []
if cin_file:
    ext = splitext(cin_file)[1]
    if ext == '.csv':
        df = read_csv(cin_file)
        if not cin_file_col:
            cin_file_col = df.columns[0]
        cins = df[cin_file_col].values.tolist()
if isinstance(cin, str):
    # `cin` is a string which contains 1 or more (comma-delimited) CINs
    cins += cin.split(',')
elif isinstance(cin, list):
    # `cin` is a list of strings, each of which contains 1 or more (comma-delimited) CINs
    cins += [ cin for s in cin for cin in s.split(',') ]
cins = list(set(cins))


# ## Log in <a id="login"></a>
# Initialize headless browser, load login page:

import mechanicalsoup
browser = mechanicalsoup.StatefulBrowser()
browser.open(f"{domain}/sessions/new")


# Fill in login info, log in:

browser.select_form('form[action="/sessions"]')
browser["user[email]"] = user
browser["user[password]"] = pswd
if prod:
    browser["user[otp]"] = otp  # TODO: this is probably not the right way to do this; update once we have staging/prod access.
browser.submit_selected()


def check_resp(resp):
    if resp.ok:
        return True
    else:
        msg = f'Missing document: {domain}/{href}'
        if level == 'raise':
            raise RuntimeError(msg)
        elif level == 'warn':
            stderr.write('%s\n' % msg)
            return False
        else:
            assert level == 'ignore'
            return False


# ## Load patient pages, download documents <a id="download"></a>

def txt2pdf(path, out_path):
    # .txt to PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    with open(path,'r') as f:
        pdf.cell(0,0, txt = f.read())
        pdf.output(out_path)

def word2pdf(path, out_path):
    # MS Word (.doc AND .docx) to PDF
    import comtypes.client
    wdFormatPDF = 17
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(path)
    doc.SaveAs(out_path, FileFormat = wdFormatPDF)
    doc.Close(True)
    word.Quit()

def excel2pdf(path, out_path):
    # Excel to PDF
    from win32com import client
    excel = client.DispatchEx("Excel.Application")
    excel.Visible = 0
    wb = excel.Workbooks.Open(path)
    ws = wb.Worksheets[0]
    wb.SaveAs(abspath(out_path), FileFormat = 57)
    wb.Close(True)

def jpg2pdf(path, out_path):
    with Image.open(path) as image:
        pdf_bytes = img2pdf.convert(image.filename)
        with open(out_path, "wb") as file:
            file.write(pdf_bytes)

def png2pdf(path, out_path):
    rgb_path = f'{dir}/rgb.{ext}'
    with Image.open(path) as image:
        rgb = image.convert('RGB')
        rgb.save(rgb_path)

    with Image.open(rgb_path) as image:
        pdf_bytes = img2pdf.convert(image.filename)
        with open(out_path, "wb") as f:
            f.write(pdf_bytes)

def download_file(resp, path):
    print(f'Saving {resp.url} to {path}')
    with open(path, 'wb') as f:
        f.write(resp.content)


downloaded_files = []  # Tracker for PDF Merging
harp_patients = []
cins_with_excel_files = []

for cin in cins:
    browser.open(f"{domain}/sessions/new")

    # Load patient page
    browser.select_form('form[action="/patients"]')
    browser["q"] = cin
    print(browser.submit_selected())

    # Check that program is logged in, verify patient URL/ID
    patient_url = browser.get_url()
    print(f'Patient URL: {patient_url}')

    # Load patient's "documents" page
    patient_documents_tab = f'{browser.get_url()}/documents'
    browser.open(patient_documents_tab)

    print(f"Downloading chart for: {cin}")

    document_link_tags = browser.get_current_page().find_all(["a"], text = "download")
    print(f"{len(document_link_tags)} total documents found. Downloading now.")

    cin_dir = f'{out_dir}/{cin}'
    mkdir(cin_dir)

    doc_idx = 1

    # Open each link and save the file as a pdf
    for tag in document_link_tags:
        href = tag['href']
        name = basename(href)
        base, ext = splitext(name)
        assert ext[0] == '.'
        ext = ext[1:]

        # Compute ultimate destination path
        if convert_to_pdf:
            out_path = f'{cin_dir}/{base}.pdf'
        else:
            out_path = f'{cin_dir}/{base}.{ext}'

        # Check whether it already exists
        if exists(out_path):
            if overwrite:
                print(f'Overwriting {out_path}…')
            else:
                print(f'Found {out_path}; skipping…')
                continue

        # Open the file URL, verify it exists / is loaded successfully
        resp = browser.open(f"{domain}/{href}")
        if not check_resp(resp): continue
        url = resp.url

        # Ensure parent directory of output path exists
        mkpar(out_path)

        if not convert_to_pdf:
            download_file(resp, out_path)
            doc_idx += 1
        else:
            # Download various file types and convert to PDF:
            if ext == 'pdf':
                download_file(resp, out_path)
            else:
                with TemporaryDirectory() as dir:
                    with cd(dir):
                        tmp_path = f'tmp.{ext}'
                        download_file(resp, tmp_path)

                        converters = {
                            'txt' : txt2pdf,
                            'doc' : word2pdf,  # windows only!
                            'docx': word2pdf,  # windows only!
                            'xls' : excel2pdf, # windows only!
                            'xlsx': excel2pdf, # windows only!
                            'jpg' : jpg2pdf,
                            'jpeg': jpg2pdf,
                            'png' : png2pdf,
                            'tiff': png2pdf,
                        }
                        converter = converters.get(ext)
                        if converter:
                            converter(tmp_path, out_path)
                            if converter is excel2pdf:
                                if cin not in cins_with_excel_files:
                                    cins_with_excel_files.append(cin)
                        else:
                            msg = f'Unrecognized extension {ext}: {url}'
                            stderr.write('%s\n' % msg)
                            continue
            downloaded_files.append(saved_file)
            print(f"Document {doc_idx}: {url}")
            doc_idx += 1

    ## Download Harp Files (if patient is HARP)
    browser.open(patient_url)
    if len(browser.get_current_page().find_all(["a"], text = "HARP")) > 1:
        # TODO: respect `overwrite` flag for HARP files

        # patient's harp page
        harp_patients.append(cin)
        harp_url = f"{patient_url}/harp_status"

        #screenshot harp page - using Selenium
        driver = webdriver.Chrome()
        driver.get(f"{domain}/sessions/new")
        driver.find_element_by_id("session_email").send_keys(user)
        driver.find_element_by_id ("session_password").send_keys(pswd)
        driver.find_element_by_name("commit").click()
        driver.get(harp_url)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("document.body.style.zoom='80%'")
        driver.save_screenshot(f'{cin_dir}/harp_screen.png')
        driver.close()
        im = Image.open(f'{cin_dir}/harp_screen.png')
        rgb_im = im.convert('RGB')
        rgb_im.save("pngtojpg.jpg")
        pdf_path = f'{cin_dir}/harp_screenshot.pdf'
        with Image.open("pngtojpg.jpg") as image:
            pdf_bytes = img2pdf.convert(image.filename)
            with open(pdf_path, "wb") as f:
                f.write(pdf_bytes)
        os.remove('pngtojpg.jpg')
        os.remove(f'{cin_dir}/harp_screen.png')
        downloaded_files.append(f'{cin_dir}/harp_screenshot.pdf')
        print("Harp Screenshot downloaded")

        ### - Download HARP Files - ###
        browser.open(harp_url)
        harp_download_links = browser.get_current_page().find_all(["a"], text = "download")
        harp_care_plans = browser.get_current_page().find_all(["a"], text = "view")
        harp_file = 1
        for link in harp_download_links:
            harp_file_name = "harp_" + str(harp_file)
            resp = browser.open(f"{domain}{link['href']}")
            with open(f'{cin_dir}/{harp_file_name}.pdf', 'wb') as f:
                f.write(resp.content)
            downloaded_files.append(f'{cin_dir}/{harp_file_name}.pdf')
            print(f'{harp_file} harp file downloaded.')
            harp_file += 1
        print(f'{harp_file - 1} total harp files downloaded for {cin}')

        harp_plans = 1
        for plan in harp_care_plans:
            harp_plan_name = f"harp_plan_{harp_plans}"
            resp = browser.open(f"{domain}/{plan['href']}.pdf")
            with open(f'{cin_dir}/{harp_plan_name}.pdf', 'wb') as f:
                  f.write(resp.content)
            downloaded_files.append(f'{cin_dir}/{harp_plan_name}.pdf')
            print(f'{harp_plans} harp plans downloaded.')
            harp_plans += 1
        print(f'{harp_plans - 1} total harp care plans downloaded for {cin}')

    ## Download encounters
    resp = browser.open(f'{patient_url}/encounters.pdf')
    if check_resp(resp):
        print("Downloading encounters…")
        out_path = f'{cin_dir}/encounters.pdf'
        # Check whether it already exists
        download = True
        if exists(out_path):
            if overwrite:
                print(f'Overwriting {out_path}…')
            else:
                print(f'Found {out_path}; skipping…')
                download = False
        if download:
            with open(out_path, 'wb') as f:
                f.write(resp.content)
            downloaded_files.append(out_path)
            print("Encounter file downloaded.")

    print(f"{doc_idx-1} total documents downloaded for {cin}")
    sleep(sleep_interval)












