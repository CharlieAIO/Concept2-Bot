import requests 
import urllib3
from bs4 import BeautifulSoup
import random
from colorama import init
from termcolor import colored
import time
import threading
import datetime

init()

singupurl = 'https://log.concept2.com/signup?'
logurl = 'https://log.concept2.com/log'
mmurl = 'https://log.concept2.com/challenges/prizes/mmc/1/row'

headers1 = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"
}

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

firstnames = ["Liam", "Noah","William", "James," "Logan," "Benjamin", "Mason", "Elijah", "Oliver", "Jacob", "Lucas", "Michael", "Alexander", "Ethan", "Daniel", "Matthew", "Aiden", "Henry", "Joseph", "Jackson"]
lastnames = ["Brown", "White", "Blue", "Black", "Yellow", "Orange", "Cyan", "Green", "Purple", "Navy", "Mustard"]

#info 
catchall = ""


passwor = "Password001"
gender = "M"
country_id = "247"
month = "5"
day = "13"
year = "1980"
distance = "1000000"
hours = "100"
minutes = "33"
seconds = "22"
tenths = "7"






def signup():
    print(colored("Enter Number Of Tasks", "cyan"))
    number_of_tasks = input()
    for i in range(int(number_of_tasks)):
        session = requests.session()

        global firstn
        firstn = random.choice(firstnames)
        global lastn
        lastn = random.choice(lastnames)
        global email
        email =  f"{firstn}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{catchall}"
        global username
        username = f"{firstn}{lastn}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}{random.choice(numbers)}"
    
        global log
        log = open(f"Log.txt", "w")
    
        urllib3.disable_warnings()
    
        r = session.get(singupurl, verify=False, headers=headers1)
        soup = BeautifulSoup(r.text, "html.parser")
        tokenfind = soup.find("input", {"name":"_token"})
        global token
        token = tokenfind["value"]
        print(colored(f"[{datetime.datetime.now()}] Successfully Collected Token  [{token}] \n", "cyan"))
    
        signupdataload ={
            "_token": token,
            "first_name": firstn,
            "last_name": lastn,
            "email": email,
            "username": username,
            "password": passwor,
            "gender": gender,
            "country_id": country_id,
            "month": month,
            "day": day,
            "year": year
        }

        senddata = session.post(singupurl, data=signupdataload, verify=False, allow_redirects = True)
        global cookie_jar
        cookie_jar = session.cookies
    
        print(colored(f"[{datetime.datetime.now()}] Account Successfully Created, Proceeding to next stage... \n", "magenta"))
        log.write("Account Created \n")
        log.write(f"{token} \n")
        log.write(f"{firstn} \n")
        log.write(f"{lastn} \n")
        log.write(f"{email} \n")
        log.write(f"{username} \n")
        log.write(f"{passwor} \n")
        

        logload = {
        "_token": token,
        "date": "06/11/2019",
        "type": "1",
        "distance": distance,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "tenths": tenths,
        "weight_class": "H",
        "comments": "",
        "verification_code": "",
        "format":"m/d/Y"
        }
    
        r = session.post(logurl ,data=logload, verify=False, headers=headers1, cookies=cookie_jar)
        
        print(colored(f"[{datetime.datetime.now()}] Meters Successfully Logged! \n", "yellow"))
        log.write("Meters Logged! \n")

        prizeload = {
        "_token": token,
        "prizes[pin]": "1",
        "prizes[tshirt]": "",
        "prizes[tshirt]": "M",
        "country_id_postal": "247",
        "address1": "",
        "address2": "",
        "city_postal": "",
        "state_id_postal": "",
        "postcode": "",
        "phone": ""
        }
    
        r = session.post(mmurl, data=prizeload, verify=False, cookies=cookie_jar, headers=headers1, allow_redirects = False)
    
    
        print(colored(f"[{datetime.datetime.now()}] Request Successfully Sent!", "green"))

signup()




