# Covid19VaccineFinder
Vaccine finder using python

main.py

Here in this python file, I have also implemented a part of code which will user selenium_auto.py and open vaccine portal, enter mobile number and send otp, once u give otp manually and press continue, it will automatically select a particular state(here we have hardcoded to gandhinagar in Gujarat) and then it will filter for vaccines for 18+.

get_state_id(statename) - can be used to get the state code from state name

get_dist_id(statecode, dist_list) - can be used to get the list of district ids based on the list of names of district

calenderByDistrict_searchByDose(distcode, dose) - to get the available dates of appointment with timings based on the requirements such as for which district and for which dose(1st or 2nd).

get_beneficieries(token) - to get beneficieries details based on token generated. Check https://apisetu.gov.in/public/marketplace/api/cowin

sendOtp() - to send otp to the given mobile number

verifyOtp(txnId)- u can also verify otp and generate token by giving transaction id and sha 256 hashed otp.

The difference between main.py and mainWOseleniumauto.py is just that main.py will open cowin portal but mainWOseleniumauto.py will not open cowin portal.

selenium_auto.py - used to just access cowin website and do the automations.