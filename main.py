import numpy as np
data = {"username":["password",["name","phones","emaili"],["security1","security2"],["backupcode"]]}
print(data)
import random as rn
def backupcode():
    bc_list = []
    for i in range(4):
        code = rn.randrange(1000,10000)
        bc_list.append(code)
    return bc_list
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
       if username in li:
           print("User name already taken")
       else:
           li.append(username)
           count = 0  
    print("PASSWORD SHOULD FOLLOW THE FOLLOWING RULES:\n 1. INITIAL LETTER SHOULD BE CAPITAL\n 2.SHOULD CONTAINS A SPECIAL SYMBOL\n 3.SHOULD CONTAINS A NUMERIC DIGIT \n 4.MUST BE OF 8 LETTERS")
    password = input("Enter your password:")
    password = passwordcheck(password)
    if password == "0":
        print("signUp Failed...........")
        return
    else :
        data[username] = [password]
    print("ENTER YOUR PERSONAL DETAILS:")
    name = input("ENTER YOUR NAME")
    ph = 1
    while ph == 1:
            phones = int(input("ENTER YOUR PHONE NUMBER"))
            if len(str(phones)) != 10:
                print("Phone number is invalid")
                ph = 1
            else: ph = 0
    emaili = input("ENTER YOUR VALID EMAIL- ID") 
    print("SECUTIRY QUESTIONS")
    security1 = input("ENTER YOUR BLOOD GROUP")
    security2 = input("ENTER YOUR SCHOOL NAME")
    security_list = [security1,security2]
    personal_list = [name,phones,emaili]
    data[username].append(personal_list)
    data[username].append(security_list)
    
    print("HENCE YOUR  PERSONAL DETAILS ARE AS FOLLOWS:")
    print("username",username,"\n name",name,"\n phone",phones,"\nemail id",emaili,"\n","SECURITY QUESTIONS ARE \n","ENTER YOUR BLOOD GROUP:",security1,"\n","ENTER YOUR SCHOOL NAME:",security2)
    backuplist = backupcode()
    data[username].append(backuplist)
    print("YOUR BACKUP CODES ARE:",backuplist)
    return li
    
def signin():
   user = input("ENTER A VALID USERNAME:")
   if user  in data:
       print("USER NAME IN DATA:")
       pas = input("ENTER THE PASSWORRD FOR LOG-IN")
       print("SECUTIRY QUESTIONS")
       security1 = input("ENTER YOUR BLOOD GROUP")
       security = input("ENTER YOUR SCHOOL NAME") 

    
print("-----------WELCOME TO THE LOGIN - PAGE----------")
print("1-SIGN-UP TO OUR AUTHENTICATION SYSTEM")
print("2- ALREADY HAVE AN ACCOUNT SIGN-IN")
print("0-EXIT THE SYSTEM")
n = int(input("ENTER YOUR OPTION"))
if n ==1:
    print("---------------WELCOME TO THE SIGN-UP PAGE OF AUTHENTICATION SYSTEM----------------")   
    signup()
elif n==2:
    print("-------------------WELCOME TO THE SIGN-IN PAGE OF AUTHENTICATION SYSTEM------------")
    signin()
elif n ==0:
    exit(0)
else:
    print("ENTER THE VALID OPTION")
