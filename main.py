#!/usr/bin/python

import hashlib
import requests
from datetime import datetime
import pandas as pd
import winsound
import time
import selenium_auto as sa
import threading, time


duration = 2000  # milliseconds
freq = 1000  # Hz
mobile = "9737931913"
main = "https://cdn-api.co-vin.in/api/v2/"
state = 'Gujarat'
dist_list = ['Ahmedabad Corporation', 'Gandhinagar Corporation']

def sendOtp():
    res = requests.post(main+'auth/public/generateOTP', json={"mobile": mobile})
    if res.status_code == 200:
        print("OPT sent to", mobile)
        return True, res
    else:
        print("Problem whilesending OTP", res.text)
        return False, res

def verifyOtp(txnId):
    otp = input("Enter OTP:")
    otp_hash = hashlib.sha256(otp.encode())
    res = requests.post(main+'auth/public/confirmOTP', 
                        json={"txnId": txnId,
                              "otp": otp_hash.hexdigest()})
    if res.status_code == 200:
        print("OPT Verified", mobile)
        return True, res
    else:
        print("Problem while verifying OTP", res.text)
        return False, res

def get_state_id(statename):
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res = requests.get(url =main+'admin/location/states', headers=headers)
    if res.status_code == 200:
        data=res.json()
        for state in data['states']:
            if state['state_name'] == statename:
                return state['state_id']
    else:
        print("error while getting statecode")
        raise Exception("error while getting statecode")

def get_dist_id(statecode, dist_list):
    result = dict()
    headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    res = requests.get(url=main+'admin/location/districts/'+str(statecode), headers=headers)
    if res.status_code == 200:
        for dist in res.json()['districts']:
            if dist['district_name'] in dist_list:
                result[dist['district_name']] = dist['district_id']
        return result
    else:
        raise Exception("Error while extracting dist code", res.text)
        
def calenderByDistrict_searchByDose(distcode, dose):
    available = []
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'cache-control': "no-cache",
        'Accept-Language': 'en_US'
        }
    date = datetime.now().strftime("%d-%m-%Y")
    res = requests.get(url=main+'appointment/sessions/calendarByDistrict?district_id='+str(distcode)+'&date='+date, 
                       headers=headers)
    if res.status_code == 200:
        for center in res.json()['centers']:
            for session in center['sessions']:
                if session['min_age_limit'] == 18:
                    session['center_id'] = center['center_id']
                    session['pincode'] = center['pincode']
                    session['center_name'] = center['name']
                    session['district_name'] = center['district_name']
                    if dose == 1 and session['available_capacity_dose1'] > 0:
                        available.append(session)
                    elif dose == 2 and session['available_capacity_dose2'] > 0:
                        available.append(session)
                    # dose zero means check all total availability
                    elif dose == 0 and session['available_capacity'] > 0:
                        available.append(session)
        return available
    else:
        if res.text == "Unauthenticated access!":
            print(res.text)
            return []
        raise Exception("Error while extracting appointments", res.text)

# here json obj returned from calenderByDistrict_searchByDose 
def list_available_to_df(lst):
    df = pd.DataFrame(columns=["Center", "District", "PinCode", "Dose1", "Dose2", "All"])
    for session in lst:
        df2 = pd.DataFrame({"Center": [session["center_name"]],
                            "District" : [session["district_name"]],
                            "PinCode" : [session["pincode"]],
                            "Dose1" : [session['available_capacity_dose1']],
                            "Dose2" : [session['available_capacity_dose2']],
                            "All" : [session['available_capacity']]
                            })
        df = df.append(df2, ignore_index = True)    
    return df

def get_beneficieries(token):
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'cache-control': "no-cache",
        'Accept-Language': 'en_US',
        'authorization': 'Bearer '+token
        }
    res = requests.get(url=main+'appointment/beneficiaries', 
                       headers=headers)
    if res.status_code == 200:
        print(res.json)
    else:
        raise Exception("Error while extracting beneficiaries", res.text)
print("Checking vaccine at gandhinagar")
start = datetime.now()
count = 0
openchrome = False
while(True):
    count += 1
    # hardcoded with a particular city as I wated to just check for them
    gnagar = list_available_to_df(calenderByDistrict_searchByDose(772, 1))
    print(str(count)+": ", str(datetime.now() - start))
    if len(gnagar) > 0 :
        print(gnagar)
        if not openchrome:
            openchrome = True
            threading.Thread(target=sa.open_chrome).start()
        winsound.Beep(freq, duration)
        print('\n\n\n\n\n\n\n')
    time.sleep(5)
    # ahmedabad = list_available_to_df(calenderByDistrict_searchByDose(770, 1))
    # if len(ahmedabad) > 0 :
    #     print(ahmedabad)
    #     if not openchrome:
    #         openchrome = True
    #         threading.Thread(target=sa.open_chrome).start()
    #     winsound.Beep(freq, duration)
    #     print('\n\n\n\n\n\n\n')            
    # time.sleep(4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# print(get_dist_id(11, dist_list))
# print(get_state_id(state))
# response = requests.request("GET", main, headers=headers)
# token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX25hbWUiOiI4ODJiYTQwMC0yYzFhLTRjNTEtYWY5Yi1jYzFhNGM2YTY5N2QiLCJ1c2VyX3R5cGUiOiJCRU5FRklDSUFSWSIsInVzZXJfaWQiOiI4ODJiYTQwMC0yYzFhLTRjNTEtYWY5Yi1jYzFhNGM2YTY5N2QiLCJtb2JpbGVfbnVtYmVyIjo5NzM3OTMxOTEzLCJiZW5lZmljaWFyeV9yZWZlcmVuY2VfaWQiOjY4OTExMzI3NTA2NTkwLCJ0eG5JZCI6IjkxYzI1YjE0LTQzYmEtNDFmZC04OTQxLWQ4NGJmZTY1ZWEzOSIsImlhdCI6MTYyMTEzNzAyNywiZXhwIjoxNjIxMTM3OTI3fQ.We_ayt2_hz5-0rqAYDaug_xtxTj3yzR2n9wnycYayJg'
# get_beneficieries(token)
# print(response.text)
# flg, res = sendOtp()
# print(res.json()['txnId'])
# if flg:
#     flg, res = verifyOtp(res.json()['txnId'])
#     if res:
#         print(res.json())
#         token = res.json()['token']
#         print(token)
#         get_beneficieries(token)
#         headers = {
#             'authorization': "Bearer "+token,
#             'cache-control': "no-cache",
#             'Accept-Language': 'hi_IN'
#         }
#         response = requests.request("GET", main, headers=headers)
        

# flg, res = verifyOtp('3e28ae84-18c4-48bf-ac4d-e428a0c0d847')
# if res:
#     print(res.json())
