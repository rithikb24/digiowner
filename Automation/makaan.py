# view_phone = browser.find_element_by_class_name('txtbtn')
# view_phone.click()

# mobile_no = browser.find_element_by_xpath('//*[@id="client-phone-num"]/div[1]/div/input')
# mobile_no.send_keys('9302185966')


# view_phone = browser.find_element_by_xpath('//*[@id="lead-popup"]/div/div/div[2]/div[3]/span[2]')
# view_phone.click()

# OTP
# otp = browser.find_element_by_xpath('//*[@id="lead-popup"]/div/div/div[2]/div/div[2]
# otp.send_keys('6351')

# Phone
# seller_np = browser.find_element_by_class_name('class')



# browser = webdriver.Chrome()
# browser.get('https://www.makaan.com/indore-property/vijay-nagar-rental-flats-52245')

# view_phone = browser.find_element_by_class_name('.cbtn-p')
# view_phone.click()
# time.sleep(20)

""" After verifying phone number through OTP """
# Main Loop
# time.sleep(2)
# view_phone = browser.find_elements_by_class_name('txtbtn')
# seller_contacts = []
# for i in view_phone[:]:
#      i.click()
#      time.sleep(2)

#      seller_np = browser.find_element_by_class_name('phone')

#      time.sleep(2)
#      seller_contacts.append(seller_np.text)

#      close = browser.find_element_by_xpath('//*[@id="lead-popup"]/div/div/div[1]/div[2]/i')
#      close.click()
#      time.sleep(2)

# print('Following is the list of sellers contact details: ')
# for i,seller_no in enumerate(seller_contacts):
#     print('{}: {}'.format(i, seller_no))

# ------------------- IMPORT Packages ------------------------------

from twilio.rest import Client
from selenium import webdriver
import time
# --------------- Getting Access of twilio api ----------------------

account_sid = ''
auth_token = ''
_twilio_no = '+121*****251'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_ = '+15017122661',
         to = _twilio_no 
     )

print(message.sid)

# --------------- Automation Starts from here ----------------

browser = webdriver.Chrome()
time.sleep(1)

browser.get('https://www.makaan.com/listings?propertyType=apartment,builder-floor,villa,independent-house,studio-apartment&postedBy=owner&sortBy=date-desc&listingType=buy&pageType=LISTINGS_PROPERTY_URLS&cityName=Indore&localityName=Rajendra%20Nagar,Rau&cityId=13&localityId=53044,52211&templateId=MAKAAN_MULTIPLE_LOCALITY_LISTING_BUY&localityOrSuburbId=53044,52211&page=1')
time.sleep(2)

connect_now = browser.find_elements_by_class_name('callwrap')
seller_contacts = []

# --------------- Entering OTP ------------------------------

connect_now[0].click()
time.sleep(3)

select = browser.find_element_by_xpath('//*[@id="mod-singleSelectDropdown-3"]/div[2]')
select.click()

us = browser.find_element_by_xpath('//*[@id="mod-singleSelectDropdown-3"]/div[2]/div[2]/ul/li[2]')
us.click()

enter_no = browser.find_element_by_xpath('//*[@id="client-phone-num"]/div[1]/div/input') 
enter_no.send_keys(_twilio_no)

otp_connect_now = browser.find_element_by_xpath('//*[@id="lead-popup"]/div/div/div[2]/div[3]/span[1]') 
otp_connect_now.click()
otp_input.send_keys('5133')  

verify = browser.find_element_by_xpath('//*[@id="lead-popup"]/div/div/div[3]')                                
verify.click()

skip = browser.find_element_by_xpath('//*[@id="lead-popup"]/div/div/div/div[2]/div[2]/a[1]')
skip.click()

# --------------- Starts extracting Numbers ----------------

for i in connect_now[:]:
     i.click()
     time.sleep(3)

     seller_np = browser.find_element_by_class_name('phone')

     time.sleep(2)
     seller_contacts.append(seller_np.text)

     close = browser.find_element_by_xpath('//*[@id="lead-popup"]/div/div/div[1]/div[2]/i')
     close.click()
     time.sleep(3)

print('Following is the list of sellers contact details: ')
for i,seller_no in enumerate(seller_contacts):
    print('{}: {}'.format(i, seller_no))


