import numpy as np
import pandas as pd
import pyrebase as pb
import random 
import string
import random as rn
def backupcode():
    bc_list = []
    for i in range(4):
        code = rn.randrange(1000,10000)
        bc_list.append(code)
    return bc_list
loi=[]
def secQuestion(username):
    questionDb = ['Your first school ?','your first crush name ?']
    ans1 = input(f'Question: {questionDb[0]}').lower()
    ans2 = input(f'Question: {questionDb[1]}').lower()
    ansList = [ans1,ans2]
    return ansList
def passwordcheck(password):
    while True:
        specChar = '!@#$%^&*_-+=<>'
        ac = uc = lc = dc = sc = 0
        strength = 0
        if len(password)>=8:
            for char in password:
                if char.isalpha():
                    ac += 1
                    if char.isupper(): uc += 1
                    else             : lc += 1
                elif char.isdigit()  : dc += 1
                elif char in specChar: sc += 1
        
            if ac > 0 and dc > 0     : strength += 1
            else                     : print('Combination of alpha and digit is a must')
            
            if uc > 0 and lc > 0     : strength += 1 
            else                     : print('Combination of alpha and digit is a must')
            
            if sc > 0                : strength += 1
            else                     : print('Special Character is a must')
            
            if strength == 3:
                print('password is strong')
                return password
            else:
                e = 1
        else:
            print('password should be atleast 8 characters')
            e = 1
        
        if e == 1:
                # password = passSuggest()
                # print(f'''Password not strong. Suggested password is {password}
                #     press 0 to Exit
                #     or''')
                password = input('please enter a strong password again:')
                if password == '0': return 0  
def signup():
    l = []
    count = 1
    while count:       
       username=  input("ENTER NEW USERNAME ")
       li = ["ayush","@","#","a"]    
       if username in data:
           print("User name already taken")
       else:
           li.append(username)
           loi.append(username)
           count = 0  
    print("PASSWORD SHOULD FOLLOW THE FOLLOWING RULES:\n 1. INITIAL LETTER SHOULD BE CAPITAL\n 2.SHOULD CONTAINS A SPECIAL SYMBOL\n 3.SHOULD CONTAINS A NUMERIC DIGIT \n 4.MUST BE OF 8 LETTERS")
    ran = input("Do you want to automatically create password: Y/N").upper()
    if ran == 'Y':
        try:
            n = int(input("Enter the length of your password between 8 and 32"))
        except:
            print("Enter the valid input")
        if(n>=8 and n<=32):
            characters = ''
            characters += string.ascii_uppercase
            characters += string.ascii_lowercase
            characters += string.digits
            characters += string.punctuation
            password = ''.join(random.choice(characters) for _ in range(n))
            print(password)
            loi.append(password)
        else:
            print("Enter the valid number")
    else:
        password = input("Enter your password:")
        password = passwordcheck(password)
        if password == "0":
            print("signUp Failed...........")
            return
        else :
             loi.append(password)
    print("ENTER YOUR PERSONAL DETAILS:")
    name = input("ENTER YOUR NAME")
    ph = 1
    while ph == 1:
            phones = int(input("ENTER YOUR PHONE NUMBER"))
            if len(str(phones)) != 10:
                print("Phone number is invalid")
                ph = 1
            else: 
                ph = 0
                loi.append(phones)
    em = 1
    while em:
        emaili = input("ENTER YOUR VALID EMAIL- ID") 
        if '@'and '.com' in emaili : 
            print("valid email")
            loi.append(emaili)
            em = 0
        else                       : 
            print("invalid email") 
            em = 1
    print("SECUTIRY QUESTIONS")
    security1 = input("ENTER YOUR BLOOD GROUP")
    security2 = input("ENTER YOUR SCHOOL NAME")
    security_list = [security1,security2]
    personal_list = [name,phones,emaili]
    loi.append(security_list)
    loi.append(personal_list)
    print("HENCE YOUR  PERSONAL DETAILS ARE AS FOLLOWS:")
    print("USERNAME:",username,"\nNAME:",name,"\nPHONE:",phones,"\nEMAIL-ID",emaili,"\n","SECURITY QUESTIONS ARE: \n","BLOOD GROUP:",security1,"\n","SCHOOL NAME:",security2)
    backuplist = backupcode()
    print("YOUR BACKUP CODES ARE:",backuplist)
