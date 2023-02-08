""" Transferred Patients"""
#--------------------------------------------------------------------

import glob, os, os.path
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import RMAcreds
from PIL import Image
from fpdf import FPDF
import requests

""" Importing personal credentials from a python file having a dict."""
myRMAEmail = RMAcreds.RMA_user['email']
myRMAPassword = RMAcreds.RMA_user['password']


options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
"download.default_directory": "D:\RMA\screenshots", #Change default directory for downloads
"download.prompt_for_download": False, #To auto download the file
#"download.directory_upgrade": True,
"plugins.always_open_pdf_externally": True, #It will not show PDF directly in chrome
"download.extensions_to_open": "applications/pdf",
})

#from selenium.webdriver.chrome.options import Options
options.headless=True
driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.implicitly_wait(10)


driver.maximize_window()
driver.delete_all_cookies()

# LOGIN
def login(rma_url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(rma_url)
   driver.find_element_by_id(usernameId).send_keys(username)
   driver.find_element_by_id(passwordId).send_keys(password)
   driver.find_element_by_name(submit_buttonId).click()

login("https://mshh.rma.healthcare/sessions/new/", "user_email", myRMAEmail, "user_password", myRMAPassword, "commit")

"""After this step , it will get signed IN and current control goes to OTP verification page ."""

# import time
# def otp_handler(url1):
#    print('#---------------------------------------------#')
#    GA_OTP = int(input('Enter Google-Authenticator OTP:'))
#    driver.find_element_by_name("otp_code").send_keys(GA_OTP)
#    driver.find_element_by_name("commit").click()
#    time.sleep(2)
#    driver.get(url1)

# otp_handler("https://mshh.rma.healthcare/transferred_patients")
# time.sleep(2)
#--------------------------------------------

#OTP

import time
import datetime

import pyotp
def otp_verify(TPatients_url):
   totp = pyotp.TOTP("X6KC2FSNUMRE7VNGQ3G4NC5AGAG4TQ5P")
   #totp = pyotp.TOTP("5ipefwhku5t4tkelqe7bjdirakmz6ugy")
   current_OTP = totp.now()
   print("current_OTP - " , current_OTP)
   driver.find_element_by_name("otp_code").send_keys(current_OTP)
   driver.find_element_by_name("commit").click()
   time.sleep(2)
   print("Logging into Transferred Patients Page~~~~~~")
   time.sleep(2)
   driver.get(TPatients_url)

otp_verify("https://mshh.rma.healthcare/transferred_patients")
time.sleep(3)
# potp = pyotp.totp.TOTP('<secret code>').provisioning_uri(name='neeraj.kumar@mountsinai.org', issuer_name='relevant.healthcare')

#---------------------------------------------------

medicaidId = 'WH18907T'
url= "https://mshh.rma.healthcare/transferred_patients?utf8=%E2%9C%93&filter%5Bmedicaid_cins%5D=WH18907T&commit=Filter"









#-----------------------------------------------------------
"""
Beautiful Soup - Python library that is used for web scraping purposes to pull the data out of HTML and XML files. 
Soup each time loads the page .Untill driver not load .
"""

from bs4 import BeautifulSoup

html = driver.page_source
soup = BeautifulSoup(html)
total_page_no = soup.find("li",{"class":"last next"}).find("a").get("href").split("=")[-1]

first_fourth = int(total_page_no)/4
print('first_fourth' , first_fourth)#-144

second_fourth = 2*first_fourth
print(second_fourth)

third_fourth = 3*first_fourth
print(third_fourth)

directory = "D:/RMA/screenshots/"
#directory = 'C:/Work/RMA/output/'




for i in range(1,int(first_fourth)):
   all_table = soup.find("table",{"class":"table table-striped table-bordered table-condensed"}).find("tbody").find_all("tr")
   
   """Below for loop will enter into each patients and under each patients it will loop through all tabs(8)"""
   for lnk in all_table:
      Patient_url = lnk.find("td").find("a").get("href")
      Unique_Id = str(Patient_url).split("/")[-1]
      Medicaid_Id = lnk.find_all("td")[-1].get_text().strip()
      Patient_name = lnk.find_all("td")[0].get_text().strip()
      print('Patient_name : - ' , Patient_name)
      print("Medicaid_Id :- ", Medicaid_Id)

      time.sleep(5)
      
      ## OVERVIEW

      #ovr_link = "https://mshh.rma.healthcare" + Patient_url 
      ovr_link = "https://mshh.rma.healthcare/patients/286501"  #-----------------change for testing for particular Patient 
      driver.get(ovr_link)
      
      #Screenshot of "overview" tab
      S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
      driver.set_window_size(1200 , S('Height'))
      driver.find_element_by_tag_name('body')
      #driver.save_screenshot(directory + ' a_' + Medicaid_Id + "_" + Patient_name + "_" + Unique_Id + "_" + "overview.png")
      driver.save_screenshot(directory + 'a_'+Medicaid_Id+'.png')
      #print(driver.get_window_size()) #Added by Vinay
      driver.set_window_size(783,941)
   

   ## OVERVIEW Details/View

   html = driver.page_source
   soup = BeautifulSoup(html)
   Ov_d = soup.find_all("table",{"class":"table table-striped table-bordered table-condensed"})
   if Ov_d:
      for o in Ov_d:
         link_0 = o.find("tbody").find_all("tr")

         for lnk2_ in link_0:
            lnk00 = lnk2_.find_all("td")[-1].find_all("a")[-1].get_text()
            ## Detail
            if lnk00 == "Details" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               time.sleep(2)
               driver.get("https://mshh.rma.healthcare"+ lnk2)

               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'a_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)
            ## View
            elif lnk00 == "view" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               # r = requests.get("https://mshh.rma.healthcare"+ lnk2 +".pdf" , stream=True)
               # with open(directory+"assessment_view_"+".pdf" , 'wb') as f:
               #    f.write(r.content)
               # f.close()   
               # Download pdf
   else:
      pass



   ## DOCUMENT

   doc_link = ovr_link + "/documents"
   driver.get(doc_link)
   time.sleep(2)

   #Screenshot of "document" tab
   S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
   driver.set_window_size(1200 , S('Height'))
   driver.find_element_by_tag_name('body')
   #driver.save_screenshot(directory+ ' b_' +Medicaid_Id+"_"+Patient_name+"_"+Unique_Id+"_"+"document.png")
   driver.save_screenshot(directory + 'b_'+Medicaid_Id+'.png')
   driver.set_window_size(783,941)


   ##Document Details/View

   html = driver.page_source
   soup = BeautifulSoup(html)
   doc_d = soup.find_all("table",{"class":"table table-striped table-bordered table-condensed table-light-header table-internally-unbordered"})
   
   if doc_d:
      for m in doc_d:
         link_0 = m.find("tbody").find_all("tr")

         for lnk2_ in link_0:
            lnk00 = lnk2_.find_all("td")[-1].find_all("a")[-1].get_text()

            if lnk00 == "details" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               time.sleep(2)
               driver.get("https://mshh.rma.healthcare"+ lnk2)

               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'b_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)

            elif lnk00 == "view" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               driver.get("https://mshh.rma.healthcare"+ lnk2 )
               # Download pdf
               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'b_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)
   else:
      pass



   # ENCOUNTER

   enc_link = ovr_link + "/encounters"
   driver.get(enc_link)
   time.sleep(2)

   #Screenshot of "encounter" tab
   # S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
   # driver.set_window_size(1200 , S('Height'))
   # driver.find_element_by_tag_name('body')
   #driver.save_screenshot(directory+ ' c_' +Medicaid_Id+"_"+Patient_name+"_"+Unique_Id+"_"+"encounter.png")
   #driver.save_screenshot(directory + ' c_'+Medicaid_Id+'.png')

   
   #Encounter Details

   html = driver.page_source
   soup = BeautifulSoup(html)

   total_page_ = soup.find("li",{"class":"last next"})
   enc_d = soup.find("table",{"class":"table table-striped table-bordered table-condensed table-internally-unbordered patient-encounters-index-table"})
   if enc_d :
      for n in enc_d:
         enc_det = n.find("tbody").find_all("tr")
         for i in enc_det:
            det_link = i.find_all("td")[-1].find("a").get("href")
            detail_Id = str(lnk2).split("/")[-1]
            time.sleep(2)
            driver.get("https://mshh.rma.healthcare"+ det_link)

            S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
            driver.set_window_size(1200 , S('Height'))
            driver.find_element_by_tag_name('body')
            driver.save_screenshot(directory +'c_(' +detail_Id+").png")
            driver.set_window_size(783,941)
            time.sleep(2)

      if total_page_:
         total_page = total_page_.find("a").get("href").split("=")[-1]
         #all_enc = soup.find("table",{"class":"table table-striped table-bordered table-condensed table-internally-unbordered patient-encounters-index-table"}).find("tbody").find_all("tr")

         for i in range(1,int(total_page)+1):
            if i != 1:
               driver.get(enc_link+"?page="+str(i))
               html = driver.page_source
               soup = BeautifulSoup(html)

            all_enc = soup.find("table",{"class":"table table-striped table-bordered table-condensed table-internally-unbordered patient-encounters-index-table"}).find("tbody").find_all("tr")
            for j in all_enc:
               lnk2 = j.find_all("td")[-1].find("a").get("href")
               detail_Id = str(lnk2).split("/")[-1]
               time.sleep(2)
               driver.get("https://mshh.rma.healthcare"+ lnk2)

               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'c_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)
      else:
         pass
   else:
      pass
              
#120-291

   ## ASSESSMENT

   assessments_link = ovr_link + "/assessments"
   driver.get(assessments_link)
   time.sleep(2)

   #Screenshot of "assessment" tab
   S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
   driver.set_window_size(1200 , S('Height'))
   driver.find_element_by_tag_name('body')
   #driver.save_screenshot(directory+ ' d_' +Medicaid_Id+"_"+Patient_name+"_"+Unique_Id+"_"+"assessment.png")
   driver.save_screenshot(directory + 'd_'+Medicaid_Id+'.png')
   driver.set_window_size(783,941)

   ## ASSESSMENT Details

   html = driver.page_source
   soup = BeautifulSoup(html)
   A_d = soup.find_all("table",{"class":"table table-striped table-bordered table-condensed"})
   if A_d:
      for a in A_d:
         link_0 = a.find("tbody").find_all("tr")
         
         for lnk2_ in link_0:
            lnk00 = lnk2_.find_all("td")[-1].find_all("a")
            Number_of_links = len(lnk00)
            print('Number_of_links:',Number_of_links) 
            # Based on Number of links("download" , "view") i.e 2 here ,capturing screenshot or pdf .

            if Number_of_links == 2:
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               time.sleep(2)
               driver.get("https://mshh.rma.healthcare"+ lnk2)

               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'d_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)

            elif Number_of_links == 1 :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               time.sleep(2)
               driver.get("https://mshh.rma.healthcare"+ lnk2)

               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'d_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)
               # url = "https://mshh.rma.healthcare"+ lnk2+ ".pdf"
               # x = url.split("/")[-1]
               # print("url=====",url)
               # driver.get(url)
               # time.sleep(5)
               # source = 'D:/RMA/screenshots/patient_assessment.pdf'
               # dest = 'D:/RMA/screenshots/'+ Medicaid_Id +"_"+ Patient_name +"_"+ Unique_Id +"_"+ "Assesments_"+str(x) +".pdf"
               # os.rename(source,dest)
               # time.sleep(5)


   else:
      pass




   ## CARE_PLANS

   care_plans_link = ovr_link + "/care_plans"
   driver.get(care_plans_link)
   time.sleep(2)

   #Screenshot of "care_plans" tab
   S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
   driver.set_window_size(1200 , S('Height'))
   driver.find_element_by_tag_name('body')
   #driver.save_screenshot(directory+ ' e_' +Medicaid_Id+"_"+Patient_name+"_"+Unique_Id+"_"+"carePlans.png")
   driver.save_screenshot(directory + 'e_'+Medicaid_Id+'.png')
   driver.set_window_size(783,941)


   ## CARE_PLANS Details

   html = driver.page_source
   soup = BeautifulSoup(html)
   CP_d = soup.find_all("table",{"class":"table table-striped table-bordered table-condensed"})
   if CP_d:
      for cp in CP_d:
         link_0 = cp.find("tbody").find_all("tr")

         for lnk2_ in link_0:
            lnk00 = lnk2_.find_all("td")[-1].find_all("a")[-1].get_text()

            if lnk00 == "Details" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               time.sleep(2)
               driver.get("https://mshh.rma.healthcare"+ lnk2)

               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'e_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)

            elif lnk00 == "view" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               driver.get("https://mshh.rma.healthcare"+ lnk2  )

               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'e_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)
               # Download pdf   -- no pdf here
   else:
      pass




   ## GAPS_IN_CARE

   gaps_in_care_link = ovr_link + "/mco_gaps_in_care"
   driver.get(gaps_in_care_link)
   time.sleep(2)

   #Screenshot of "gaps_in_care" tab
   S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
   driver.set_window_size(1200 , S('Height'))
   driver.find_element_by_tag_name('body')
   #driver.save_screenshot(directory+ ' f_' +Medicaid_Id+"_"+Patient_name+"_"+Unique_Id+"_"+"gapsInCare.png")
   driver.save_screenshot(directory + 'f_'+Medicaid_Id+'.png')
   driver.set_window_size(783,941)

   ##GAPS_IN_CARE Details

   html = driver.page_source
   soup = BeautifulSoup(html)
   GIC_d = soup.find_all("table",{"class":"table table-striped table-bordered table-condensed"})
   if GIC_d:
      for g in GIC_d:
         link_0 = g.find("tbody").find_all("tr")

         for lnk2_ in link_0:
            lnk00 = lnk2_.find_all("td")[-1].find_all("a")[-1].get_text()

            if lnk00 == "Details" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               time.sleep(2)
               driver.get("https://mshh.rma.healthcare"+ lnk2)

               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'f_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)

            elif lnk00 == "view" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               driver.get("https://mshh.rma.healthcare"+ lnk2 )
               # Download pdf
               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'f_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)
   else:
      pass




   ## clinical_notifications

   clinical_notifications_link = ovr_link + "/clinical_notifications"
   driver.get(clinical_notifications_link)
   time.sleep(2)

   #Screenshot of "clinical_notification" tab
   S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
   driver.set_window_size(1200 , S('Height'))
   driver.find_element_by_tag_name('body')
   #driver.save_screenshot(directory+ ' g_' +Medicaid_Id+"_"+Patient_name+"_"+Unique_Id+"_"+"clinicalNotification.png")
   driver.save_screenshot(directory + 'g_'+Medicaid_Id+'.png')
   driver.set_window_size(783,941)


   ##Clinical Notification Details

   html = driver.page_source
   soup = BeautifulSoup(html)
   CN_d = soup.find_all("table",{"class":"table table-striped table-bordered table-condensed"})
   if CN_d:
      for c in CN_d:
         link_0 = c.find("tbody").find_all("tr")

         for lnk2_ in link_0:
            lnk00 = lnk2_.find_all("td")[-1].find_all("a")[-1].get_text()

            if lnk00 == "Details" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               time.sleep(2)
               driver.get("https://mshh.rma.healthcare"+ lnk2)

               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'g_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)

            elif lnk00 == "view" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               driver.get("https://mshh.rma.healthcare"+ lnk2)
               # Download pdf
               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'g_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)
   else:
      pass


   ## BILLING

   billing_link = ovr_link + "/billing"
   driver.get(billing_link)
   time.sleep(2)

   #Screenshot of "billing" tab
   S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
   driver.set_window_size(1200, S('Height'))
   driver.find_element_by_tag_name('body')
   #driver.save_screenshot(directory+ ' h_' +Medicaid_Id+"_"+Patient_name+"_"+Unique_Id+"_"+"billing.png")
   driver.save_screenshot(directory + 'h_'+Medicaid_Id+'.png')
   driver.set_window_size(783,941)
   time.sleep(2)
 

   ##Billing_Details

   html = driver.page_source
   soup = BeautifulSoup(html)
   bill_d = soup.find_all("table",{"class":"table table-condensed"})
   if bill_d:
      for i in bill_d:
         link_0 = i.find("tbody").find_all("tr")

         for lnk2_ in link_0:
            lnk00 = lnk2_.find_all("td")[-1].find_all("a")[-1].get_text()

            if lnk00 == "details" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               time.sleep(2)
               driver.get("https://mshh.rma.healthcare"+ lnk2)

               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'h_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)

            elif lnk00 == "view" :
               lnk2 = lnk2_.find_all("td")[-1].find_all("a")[-1].get("href")
               detail_Id = str(lnk2).split("/")[-1]
               driver.get("https://mshh.rma.healthcare"+ lnk2)

               # Download pdf
               S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
               driver.set_window_size(1200 , S('Height'))
               driver.find_element_by_tag_name('body')
               driver.save_screenshot(directory +'h_(' +detail_Id+").png")
               driver.set_window_size(783,941)
               time.sleep(2)
   else:
      pass

   

#-------------------------------------------------------------------------------------------------------------------------

## Handling Images to PDF :-

   filelist=os.listdir(directory)
   for fichier in filelist[:]: # filelist[:] makes a copy of filelist.
      if not(fichier.endswith(".png")):
         filelist.remove(fichier)
      


   directories = []
   for i in filelist:
      dir = directory + i
      directories.append(dir)
   print("directories : ",directories)

   print(datetime.datetime.now())

   pdf = FPDF()
   pdf.set_auto_page_break(0)
   # imagelist is the list with all image filenames

   for image in directories:
      cover = Image.open(image)
      width, height = cover.size

      # convert pixel in mm with 1px=0.264583 mm
      width, height = float(width * 0.264583), float(height * 0.264583)

      # given we are working with A4 format size 
      pdf_size = {'P': {'w': 210, 'h': 297}, 'L': {'w': 297, 'h': 210}}

      # get page orientation from image size 
      orientation = 'P' if width < height else 'L'

      #  make sure image size is not greater than the pdf format size
      width = width if width < pdf_size[orientation]['w'] else pdf_size[orientation]['w']
      height = height if height < pdf_size[orientation]['h'] else pdf_size[orientation]['h']

      pdf.add_page(orientation=orientation)

      pdf.image(image, 0, 0, width, height)

   cover.close()
   
   pdf.output(directory + Medicaid_Id + "_" + Patient_name + "_" + Unique_Id + ".pdf", "F")
   print("successfull created PDF")
   print(datetime.datetime.now())
   time.sleep(10)


   for f in os.listdir(directory):
      if f.endswith(".png"):
         os.remove(os.path.join(directory, f))
      else:
         print('".png" Not Found')



## VIEW & Detail in every tabs
"""
Medicaid ID - URL

SP46136R -   https://mshh.rma.healthcare/patients/322412 - Robert Abreu

KR28626G - https://mshh.rma.healthcare/patients/286501 - Michael Alen

KB45536Y - https://mshh.rma.healthcare/patients/214524 - Floyd Allen

QC36951G - https://mshh.rma.healthcare/patients/145614 - Mary Brady

"""