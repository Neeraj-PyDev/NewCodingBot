
#--------------------------------HR----------------------------------------#
"""
Expected Salary Hike:=
----------------------
I want to join your company to work on a long term basis.
For that I need to be paid remuneration equivalent with my qualification,experience and equal to the average 
salary in the industry for such jobs.
If I am paid this (expected amount) salary, I will be motivated to perform to the best of my ability .


# how much you are offering for me , what is there on table
# I have already informed to Manager @ interview .
# I have some offers pipelined , waiting from them .

# And as I have to relocate from bangalore to hyderabad , is there any travelling allowance or charges ?

# Including all the PF deductions and all , I am asking for around 1,10,000rs monthly pay .

"""



#--------------------------------Interview Question-----------------------------------------#

#MYSQL 
#go to mysql bin folder and type "mysql -u root -p"
# create database neerdb;  //  use neerdb;


# import mysql.connector
# mydb = mysql.connector.connect(host="localhost" , user = "root" , passwd = "Iloveyou@1")
# print(mydb)
# if (mydb):
#     print('connected successfully')
# else:
#     print('Dismissed')
    


"""
import mysql.connector
mydb = mysql.connector.connect(host = "localhost" , user = "root" , passwd = "Iloveyou@1")
print(mydb)
if (mydb):
    print("connection successful")
else:
    print('Not Successful')

"""  

#----------------------------------------------------------------------------------------------------------

"""
#To Reverse a string.

# 5 different ways to reverse string in python

# 1> For loop

def rev_for(s):
    r=''
    for i in s:
        r=i+r
    return r

#print(rev_for('Neeraj'))


"""


# def rev(s):
#     w=''
#     x=list(s)
#     for i in x:
#         w=w+i
#     return w



"""

#--------------------------------------------------
# 2> while loop

def reverse_while(rstring):
    s=''
    length=len(rstring) - 1
    while length>=0:
        s=s+rstring[length]
        length=length-1
    return s

#print(reverse_while('Neeraj'))

#-----------------------------------------------------------

# 3> Slicing




def rev_str(s):
    return s[:-1]

print(rev_str('Neeraj'))




#-----------------------------------------------------------

# 4> Join() and reversed() method

def r_string(s):
    a = ''.join(reversed(s))
    return a

#print(r_string('Neeraj'))


#-------------------------------------------------------

# 5> list Reverse

def list_reverse(s):
    x=list(s)
    print(x)
    x.reverse()
    z=''.join(x)
    return z


#print(list_reverse('Neeraj'))



#-------------------------------------------------------------------

Palindrome 

def func(word):
    str = ''
    for i in word:
        str = i+str
    if list(word)==list(str):
        print('Palindrome')
    else:
        print('Not Palindrome')

func('oppow')



#-------------------------------------------------------------------
#Fibonacci

def foo(nterms):
    count = 0
    n1 = 0
    n2 = 1
    
    while count<nterms :                                      
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count+=1
    return count

foo(9)

# or #

x,y = 0,1
while y<300:
    print(y)
    x,y = y,x+y

# or #


#fibo(n) -> return value of fibo at index n
#recursive

# def fibo(n):
#     if n<=1:
#         return n
#     else:
#         return( fibo(n-1) + fibo(n-2))


#-------------------------------------------------------------------
#Prime Numbers


def prime(n):

    for i in range(2,n):
        if n%i == 0:
            return False
        
    return True

print(prime(117))



#Prime numbers b/w given range

lower =  int(input('Enter lower limit:'))
upper = int(input('Enter upper limit: '))

for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                break
        else:
            print(num)

#-----------------------------------------------------

## FACTORIAL


# 4!=4*3*2*1

def factorial(n):
    fact = 1
    if n<0:
        print('sry factorial is not exist for negative number.')
    elif n==0:
        print(1)
    else:
        for i in range(1,n+1):
            fact = fact*i
        print('Factorial: ',fact)

factorial(10)

#------------------------------------------------------------------------------


##Armstrong number

def digit(x):
  n=0
  while (x!=0):
    n=n+1
    x=x//10
  return n


def power(x,y):

  if y==0:
    return 1
  if y%2 == 0:
    return power(x,y//2) * power(x,y//2)
  
  return x*power(x,y//2)*power(x,y//2)


def isarmstrong(a):

  x=digit(a)
  temp=a
  sum=0
  while(temp!=0):
    r=temp%10
    sum=sum+power(r,x)
    temp=temp//10

  #if condition satisfies
  return (sum == a)

print(isarmstrong(1634))



#-------------------------------------------------------------------

#Even Numbers

def even_odd(n):
    if n%2==0:
        return True
    return False
    
print(even_odd(112))



#-------------------------------------------------------------------
#Occurance


list1 = [2,3,2,1,0,9,8,0]

def occ(l):
    dict = {}
    for i in list1:
        keys = dict.keys()
        if i in keys:
            dict[i] +=1
        else:
            dict[i] = 1
    return dict

print(occ(list1))


#--------------------------------------------------------------------

# REverse  a Number

n = int(input('Number:'))

rev = 0
while n>1:
    a=n%10                                  # % - Remainder
    rev = rev*10+a                          # // - Quotient  [floor division]
    n=n//10
print(rev)


#-------------------------------------------------------------------------

# Total of a Number                      

n = int(input())

s = [int(i) for i in str(n)]
sum = 0
for j in s:
    sum = sum+j
print(sum)


#-------------------------------------------------------------------------





#-------------------------------------------------------------------------

def k(*args , **kwargs):
    for i in kwargs:
        print(i)
    for j in args:
        print(j)
    

k('aap','bjp', 'jdu' ,kao='jack' , fla='wrot' , asa='rof')





#------------------------------------------------------------------

# DECORATORS

def check(func):
    def inside(a,b):
        if a<b:
            a,b = b,a
        func(a,b)
    return inside

@check
def div(a,b):
    return a/b

#------------------------------------------------------------------

import secrets
import string

pass_code = ("".join(secrets.choice(string.digits + string.ascii_letters + string.punctuation) for i in range(100)))

print(pass_code)



#-------------------------------------------------------------
# custom attribute middleware

def my_middlewares(get_response):
    # one time configuration and initialization

    def my_function(request):
        #code to be executed for each request before view are called .
        response = get_response(request)

        # code to be executed for each request/response after view are called .

        return response
    return my_function


#-------------------------------------------------------------



# ASGI - Asynchronous Server Gateway Interfce .
# WSGI - Web Server Gateway Interface .

#---------------------------------------------------
#Closure 
# A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

def outer():
    school = 'DAV'
    def inner():
        return school
    return inner

a = outer()
print(a())

def o(msg):
    def i():
        print(msg)

    return i

a = o('Hello')
a()

def multiplier_of(x):

    def multiply(n):
        print(x*n)

    return multiply

num = multiplier_of(3)
num(2)


#--------------------------------------------------------------------

#check if list is sorted or not

original_list = [12,39,70,920]

print('Given List' , str(original_list))

flag = 0
i=1

while i<len(original_list):
    if(original_list[i]<original_list[i-1]):
        flag=1
    i+=1

if (not flag):
    print('Yes,the given list is sorted')
else:
    print('No the list is not sorted.')

"""








#----------------------------------------------------------------------------------
    # StartUp Interview Qsn
#-----------------------------------------------------------------------------------
"""
1. Lets work on a recursive implementation of fibonacci series
2. Once we have a working implementation, we want to try and optimise it.

3. Write a decorator that logs the functions arguments.

4. Given a string and and a bunch of sub strings can we check if the given string can be created from the substring. and if so can we generate them..
Eg. "aaaaaaaa", ["a", "aaa", "aa"]
"string", ["s", "tr", ng", "t", "i"]


Design - 
Let's say we are designing a feed for our app (thing along the lines of LinkedIn feed or Facebook feed). How will we design such a feed 
making sure that we are rotating Feeds upon refresh/app open_close/ etc.
Entities
Feed - A list of POSTS which is tailored to the user's profile.
Post - A article/link/news along with some metadata..
User - The interacting user
Connections - Other User's that have a connection with the user



Eg.
 0 1 1 2 3 5 8 13 21....
fibo(n) -> return value of fibo at index n
"""
# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return ( fib(n-1) + fib(n-2) )

#print(fib(4))


# #Write a decorator that logs the functions arguments.

# def logger(n):
#     def decorator(f):
#         def wrapper(*args,**kwargs):
#             print(n,f.__name__,"args",args,"kwargs",kwargs)
#             c=f(*args,**kwargs)
#             print(n,f.__name__,'result',c)
#             return c
#         return wrapper
#     return decorator

# @logger('test')
# def p(a,b,foo='foo'):
#     return a+b

# #print(p(2,3))


# # To hide class attribute
# class cl:
#     def __init__(self,a,b):
#         self.__a=a
#         self.__b=b

#     def display(self):
#         return self.a,self.b
# c=cl(3,2)
# #c.a


# def info(name='Himad'):
#     return 'hi '+name

# print(info())

# a =info

# print(a())


# Global & Local Variable

# x=3
# def foo():
#     print(x)

#foo()
# x=3
# def gl():
#     global x
#     x+=3
#     print(x)







#---------------------------------------------------------------
#fynd interview :

# import copy
# a={'name': 'Pravin', 'hobbies': ['read','write','code']}
# b=copy.copy(a)
# a['hobbies'].append('dance')
# # Output:
# #a = {'name': 'Pravin', 'hobbies': ['read', 'write', 'code', 'dance']}
# #b = {'name': 'Pravin', 'hobbies': ['read', 'write', 'code', 'dance']}

# #Why does b change?
# a=[12,13]
# b=a
# print(b)
# #json
# import copy
# a={'name': 'Pravin', 'hobbies': 'read'}
# b=copy.copy(a)
# a['hobbies']= 'dance'
# Output:
#a = {'name': 'Pravin', 'hobbies': 'dance'}
#b = {'name': 'Pravin', 'hobbies': 'read'}

#Why does not b change now?
# with open("input.txt") as f:

#     data = f.readlines()
#     for line in data:
#         print(line)

#----------------------------------------------------------------

#Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
#Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

Input = [('452', 10), ('256', 5), ('100', 20), ('135', 15)]

def sort_tup(tup):
    tup.sort(key=lambda X:X[1])
    return tup

#print(sort_tup(Input))

#--------------------------------------------------------

# PICKLING
#It is a process where a python object hierarchy is converted into a byte stream .

d1 = {'key':'Omkar' , 'name':'Omkar pathak' , 'age':21 , 'pay':40000}

d2 = {'key':'Jagdish' , 'name':'Jagdish pathak' , 'age':50 , 'pay':50000}

#database

db = {}

db['omkar'] = d1
db['jagdish'] = d2

import csv
from multiprocessing.sharedctypes import Value
import pickle
from typing import no_type_check
from unicodedata import name

#for storing
b = pickle.dumps(db)

#for loading
c = pickle.loads(b)

#print(c)



#--------------------------------------------------------------------------------
#----------------------hcl Interview------------
## FLATTEN a LIST
# x=[1,2,3,[4,5,6],[7,8,9],[[0,10]]]
# # output - 1,2,3,4,5,6,7,8,9,0,10

# def flatten_list(x):
#     flat_list = []
#     for i in x:
#         if type(i) is list:
#             for item in i:
#                 flat_list.append(item)
#             if type(item) is list:
#                 for j in item:
#                     flat_list.append(j)
#         else:
#             flat_list.append(i)
#     return flat_list
#print(flatten_list(x))


#--------------------------------------------------------------------------------

# lis = [1,2,3,19,31,40,5,21,'neeraj']

# def odd_n(lis):
#     for i in lis:
#         if type(i) is int and i%2!=0 and i>15:
#             yield i

# for j in odd_n(lis):
#     print(j)




#----------------------------------------------------------------------


# PYTHON HANDLING CSV file

# import csv

# with open('employee_birthday.txt', mode='r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         print(f'/t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
#         line_count += 1
#     print(f'Processed {line_count} lines.')


#------------------------------------------------------------------------------------------------

#Connecting Python with MySQL
#--------------------------------
"""
/////////
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='neerdb',
                                         user='root',
                                         password='Iloveyou@1')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        #cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        for i in tables:
            print(i)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

"""



###-------------------------------------------------------------------------------------------------------------------------------###
#-----------------------------Handling Images with PDF in PYTHON------------------------------------------##

"""
from PIL import Image

PNG_FILE1 = ("D:/RMA/screenshots/overview_321300.png")
PNG_FILE2 = ("D:/RMA/screenshots/document_321300.png")

PDF_FILE1 = "D:/RMA/screenshots/bbd.pdf"
im_list = (PNG_FILE1 , PNG_FILE2)

from fpdf import FPDF
pdf = FPDF()
# imagelist is the list with all image filenames
pdf.add_page()
for image in im_list:
    pdf.image(image)

pdf.output("D:/RMA/screenshots/yourfile1.pdf", "F")

"""

#------------------------------------------------------------------------------------------------------------------

                                            #DELLOITE INTRVW QSN                                
# 1.
# s1={1, 2, 0, 4, 3, 0, 5, 0}
# out = {1, 2, 4, 3, 5, 0, 0, 0}


#Simple answer - A set can not contain duplicate .

# 2.
# N=3
# str='paradox'
# out='paizwlc'

# This is called mirroring character in Python .


# def compute(string1 , n):
#     reverseAlphabet = "zyxwvutsrqponmlkjihgfedcba"
#     l=len(string1)
#     answer = ''
#     for i in range(0,n):
#         answer = answer+string1[i]

#     for i in range(n,l):
#         answer = (answer+reverseAlphabet[ord(string1[i]) - ord('a')])
#     return answer
#print(compute("paradox" , 2))




# decorators
# picking & Unpickling
# Tuple
# file handling
# negative indexing
# range & xrange
# shuffle in python 
# remove whitespace from string in python



#----------------------------------------------------------------------------------------------------------------------
#``````````````````````````EPAM Interview Question````````````````````````````````````````

"""
# MRO

class A:
    def __init__(self):
        print('A init')
    def func1(self):
        print('In Func A')

class B:
    def __init__(self):
        print('B init')
    def func2(self):
        print('In B func')

class C(A,B):
    def __init__(self):
        super().__init__()
        print('C init')
    def func3(self):
        print('C func')

class D(C,B):
    def __init__(self):
        super().__init__()
        print('D init')
    def f(self):
        print('in D')

d = D()
d.func3()

"""
#================================================================================


"""

#sort a list of numbers without using sort or max,min

given_list = [12,33,21,35,30,9,29]
new_list = []
while given_list:
    minimum_value = given_list[0]
    for elements in given_list:
        if elements<minimum_value:
            minimum_value = elements
    new_list.append(minimum_value)
    given_list.remove(minimum_value)


#print(new_list)
"""

#========================================================================


"""
# TIC-TAC-TOE Game

import random


class TicTacToe:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            # taking user input
            row, col = list(
                map(int, input("Enter row and column numbers to fix spot: ").split()))
            print()

            # fixing the spot
            self.fix_spot(row - 1, col - 1, player)

            # checking whether current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game!")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Match Draw!")
                break

            # swapping the turn
            player = self.swap_player_turn(player)

        # showing the final view of board
        print()
        self.show_board()


# starting the game
# tic_tac_toe = TicTacToe()
# tic_tac_toe.start()

"""
#````````````````````````````````````````````````````````````````````````````````

"""
#Days-Weeks Problem

def change(num_of_days):
    days_in_a_week = 7
    year = int(num_of_days/365)
    week = int((num_of_days%365) /days_in_a_week)
    days = (num_of_days%365) % days_in_a_week

    print("year : {} , week : {} , days : {}".format(year,week,days))

change(32)
"""



#-------------------------------------------------------------------------------------

"""
x = 2
y=10
z=15

#return count of numbers which is not having common digits when multiplied from x with range(y,z+1) .
res_list = []
num = []
for i in range(y,z+1):
    num.append(i)
    res = x*i
    res_list.append(res)
    e = '%s'%y
    f = '%s'%res

print(num)
print(res_list)


"""
#--------------------------------------------------------------------------
"""
# Anagrams------------

def anagram(s1 , s2):
    if sorted(s1) == sorted(s2):
        print('Anagrams!')
    else:
        print("Not Anagram!")
print(anagram('land' , 'nasd'))

"""

#---------------------------------------------------------------------------------------------
# ABSTRACTION
#Python provides the abc module to use the abstraction in the Python program.

"""
from abc import ABC , abstractmethod

class car(ABC):
    def speed(self):
        pass

class Tesla(car):
    def speed(self):
        print('speed of Tesla is 300km/h')

class Mercedez(car):
    def speed(self):
        print('speed of Mercedez is 350km/h')

class Scorpio(car):
    def speed(self):
        print('Speed of Scorpio is 180km/h')

t = Tesla()
t.speed()

m = Mercedez()
m.speed()

"""


#----------------------------------------------------------------------------------------
# Python3 program to check for balanced brackets.

"""
def areBracketsBalanced(expr):
	stack = []

	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:

			# Push the element in the stack
			stack.append(char)
		else:

			# IF current character is not opening
			# bracket, then it must be closing.
			# So stack cannot be empty at this point.
			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	# Check Empty Stack
	if stack:
		return False
	return True


# Driver Code
if __name__ == "__main__":
	expr = "{()}[]"

	# Function call
	if areBracketsBalanced(expr):
		print("Balanced")
	else:
		print("Not Balanced")

"""



#-------------------------------------------------------------------


# nested_list = [1,2,3,[4,5,6],7,[8,9,10,0]]

# def nested_l(l):
#     flatten_list = []
#     for i in l:
#         if type(i) is list:
#             for j in i:
#                 flatten_list.append(j)
#             if type(j) is list:
#                 for a in j:
#                     flatten_list.append(a)
#                 if type(a) is list:
#                     for k in a:
#                         flatten_list.append(k)
#         else:
#             flatten_list.append(i)
#     return flatten_list

#print(nested_l(nested_list))




#-------------------------------------------------------------------------------------------------

#Wipro Interview


# -----L1-----
"""
1.Templates
2.API tools
3.
Let's say you have a REST API to GET details of a specific student from the server that runs Django.
How will you map the URL to the implementation? Note that the API must be authenticated.
4. Van Eck Sequence
5. Git Version Control
"""

# ------L2-----
"""
1.Lambda
2.Filter vs Reduce
3.Set
4.Abstract class in Python
5.MRO concepts
6.Class Method vs Static Method
7.Super Keyword
8.Sort vs Sorted
9.Exception(Value Error)
10.Frequency of elements in list (output in dict)
"""

# l=[1,1,1,1,1,2,2,2,2,3,3,3,4,4,4,4,5,5,5,5]

# def countfreq(l):
#     frq = {}
#     for items in l:
#         if items in frq:
#             frq[items]+=1
#         else:
#             frq[items] =1
#     return frq

#print(countfreq(l))

#-----------------------------------------------------------------------------------

s='Python'
p = [s[:i] for i in range(len(s)+1)]
#print(*(p+p[::-1]) , sep='\n')

#------------------------------------------------------------------------

"""
UNPACKING

we use  two operators *(for tuples) & **(for dictionaries) to unpack 
"""


# l=[i for i in 'neeraj']
# print(*l)

# d = {'a':12,'b':20,'c':49}



# def fun(a,b,c,d):
#     print(a,b,c,d)
    
# x = [1,2,3,4]
# fun(*x)

# def funx(a,b,c,d):
#     print(a,b,c,d)

# d = {'a':10,'b':20,'c':30,'d':40}

# funx(**d)
#-------------------------------------------------------------------------------------
"""
to print all MIDs

directory = "C:/Users/HP/Desktop/mid"

import os

filelist=os.listdir(directory)
for fichier in filelist: # filelist[:] makes a copy of filelist.
    if not(fichier.endswith(".pdf")):
        filelist.remove(fichier)
      


directories = []
for i in filelist:
    x = i.split('_')
    directories.append(x)
#print(directories)

for i in directories:
    print(i[0])

"""





#----------------------------------------------------------------------------------




"""
num=int(input('enter a num'))

def prime_check(n):
    flag=False
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                flag=True
                break

    if flag:
        print(num,"is not a prime")
    else:
        print(num,"is a prime")

prime_check(num)
"""



#---------------------------------------------------------------------
# Capitalize first letter of names

# def solve(s):

#     for i in s.split():
#         s = s.replace(i,i.capitalize())
#     return s

# print(solve("neeraj kumar"))



#-------------------------------------------------------------------------




# text = open('ctsProjects.txt' , 'r')

# d=dict()

# for line in text:
#     line=line.strip()

#     line=line.lower()

#     words=line.split(' ')

#     for i in words:
#         if i in d:
#             d[i] = d[i]+1
#         else:
#             d[i]=1




# # s=[]
# # for w in l:
# #     if w.startswith('a'):
# #         s.append(w)



# print(s)

#----------------------------------------------------------------------------


""" CSV and file Reading """


# Write a Python program to read each row from a given csv file and print a list of strings .

# import csv

# with open('input.txt' , newline='') as csvfile:
#     data = csv.reader(csvfile , delimiter = ' ' , quotechar = '|')
#     for row in data:
#         print(''.join(row))


#  Write a Python program to read a given CSV file having tab delimiter .

# import csv 

# with open('csvv.csv' , newline='') as csvfile:
#     data = csv.reader(csvfile , delimeter = '\t')
#     for row in data:
#         print(''.join(row))




# import os
# print(os.getcwd())




# Write a Python program to read a given CSV file as a list.

# with open ('input.txt' , newline='') as file :
#     data = csv.reader(file )
#     result = list(data)
#     print(result)





#--------------------------------------------------------------------------------------------------------

######################------------HCL interview---------------------###############



# d = {"a": 1, "b": 2, "c": 3}


# d = dict((k, v) for k, v in d.items() if v > 1)


# print(d)

#------------------------------------------------------------------------------------------------------

# Python program using the List slicing approach to rotate the array


# def rotateList(arr,d,n):
#   arr[:]=arr[d:n]+arr[0:d]
#   return arr


# # Driver function to test above function


# arr = [1, 2, 3, 4, 5, 6]
# print(arr)
# print("Rotated list is")
# print(rotateList(arr,2,len(arr))) 


#--------------------------------------------------------------------------------------------------------------------------------------


"""

////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////

"""



# --------------------------- J . P Morgan Interview --------------------------------------------------





# Memory Management in Python
# Ternary Operators  --------------------------      >>x,y = 3,4    >>print(x if x<y else y)
# with open() -- why to write 'with' keyword
# What is Exceptions in Python .
# Difference between exception and error .
# Exception Handling .
# Difference between Delete , Remove & pop in lists .
# Difference between Append() & Extend() .
# Enumerate 
# Self 

# Add new column with rownumber in Pandas
# search a name in column of dataframe
# Mongo Db connection with Python

# Django:--- Architecture of Django / Mixins / Django supports Multiple Inheritance / Authentication /

# s='1257-345' ==== sum ??

#------------------------------------------------------------------------------------


#list1 = [1,4,2,3,8,6]

#sort the list without using sorted() or any inbuilt method

# for i in range(len(list1)):
#     for j in range(i+1 , len(list1)):
#         if list1[i]>list1[j]:
#             list1[i] , list1[j] = list1[j] , list1[i]

# print(list1)

#--------------------------------------------------------------------------



#sort dict by keys


# dict1 = {1:'a' , 6:'e' , 3:'t'}

# print(dict(sorted(dict1.items())))



#---------------------------------------------------------------

# Remove Duplicates from list

# l1 = [1,2,4,3,3]
# res = []

# for i in l1:
#     if i not in res:
#         res.append(i)

# print(res)

#----------------------------------------------------------

# Append a list to another list

'''Note:- A list is a n object.if you append another list onto a list , the patrameter list will be a single object at the end of list .

        Extend() iterates over its argument,adding each element to list extends the list .
'''


# l1=[1,2,3,4]
# l2=[5,6,7,8]

# #l1.append(l2)

# #print(l1)

# l1.extend(l2)
# print(l1)



#------------------------------------------------------------------------------------------------------------------------------

#////////////////////////////////////////////////////////////////////////////
#----------------------------------------------------------------



""" PROPERTY METHOD """



# class person:
#     def __init__(self):
#         self.__name = ''
#     def set_name(self,name):
#         print('setname called')
#         self.__name = name
#     def get_name(self):
#         print('getname called')
#         return self.__name
#     name = property(get_name , set_name)


# p1=person()

# p1.name='steve'

# p1.name


#---------------------------------------------------------------------------------

"""Find a Position of a character in a given string ."""

# s='SWATI'

# c = 'I'

# res = None
# for i in range(0,len(s)):
#     if s[i] == c:
#         res = i+1
#         break
# if res == None:
#     print('No such character available in string')
# else:
#     print("Character {} is present at {}".format(c , str(res)))




#------------------FIDELITY Interview------------------------------

"""
1.APIs
2.Pandas Dataframe
3.Lambda Fn
4.
"""

#-----------------------------------------------------------------------------------------------------------





# String all ascii values----------

# import string
# print(string.printable)

# print(string.printable[10:36]) ----------- all alphabets in lowercase //  print(string.ascii_lowercase)

#---------------------------------------------------





# # d = {1:1, 2:4, 3:9, 4:12}


# # req_dict = {x:x**2 for x in range(1,5)}


# # print(req_dict)

# class A:
#     def __init__(self,name):
#         self.name = name

#     def func1(self):
#         print(self.name)

# class B(A):
#     def __init__(self,name,roll):
#         super().__init__(self)
#         self.roll = roll
#     def func2(self):
#         print(self.roll)

# a=A('name')
# a.func1()

# b=B('name',23)
# b.func2()



# a=lambda x:x**2
# print(a(3))


#-------------------------------------------------------------------------------------------------



#-----------------------------DELOITTE INTERVIEW---------------------------

# l1=[12,13,16,70,98,45,98]


# t = set(l1)
# x=list(t)
# print(x)
# z = sorted(x)[-2]
# print(z)

# l1 = [2,6,7,18,90,300]

# def fooo(l1,n):
#     if len(l1)==0:
#         return False
#     else:
#         middle = len(l1)//2
#         if l1[middle] ==n:
#             return l1.index(n)
#         elif n<l1[middle]:
#             return fooo(l1[middle] , n)
#         else:
#             return fooo(l1[middle+1] , n)
            

    
# print(fooo(l1,90))
    


# twitter dev acc
# tweepy - pckg
# fetching tweets
# sentim analysis





#---------------------------------------------------------------------------------------------------------------------------

""" TECH MAHINDRA { APPLIED MATERIALS }"""

# 1. FASTAPI
# 2. GIL
# 3. CAP Theoram
# 4. RDBMS vs NOSQL
# 5. Why Lambda is faster than for loop
# 6. MultiThreading
# 7. How parallel threads work in multithreadfing
# 8. process vs threads





l = [1,2,3,4,5,6,7]

if 3 not in l:
    print('n')
print('p')


