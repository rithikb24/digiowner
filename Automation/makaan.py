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

# -------------------------------------------------------------------------------------------
# for Connect Now button

from selenium import webdriver
import time


browser = webdriver.Chrome()
time.sleep(1)

browser.get('https://www.makaan.com/listings?postedBy=owner&sortBy=date-desc&listingType=rent&pageType=LISTINGS_PROPERTY_URLS&cityName=Pune&localityName=wakad&suburbName=PCMC&cityId=21&localityId=50118&suburbId=10244&templateId=MAKAAN_LOCALITY_LISTING_RENT&page=2')
time.sleep(2)

connect_now = browser.find_elements_by_class_name('callwrap')
seller_contacts = []
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


