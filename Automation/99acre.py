from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.99acres.com/search/property/rent/residential-all/saket-nagar-indore?search_type=QS&refSection=GNB&search_location=NRI&lstAcn=NR_R&lstAcnId=-1&src=CLUSTER&preference=R&selected_tab=4&city=142&res_com=R&property_type=R&isvoicesearch=N&keyword_suggest=Saket%20Nagar%20%2C%20Indore%3B&fullSelectedSuggestions=Saket%20Nagar%20%2C%20Indore&strEntityMap=W3sidHlwZSI6ImxvY2FsaXR5In0seyIxIjpbIlNha2V0IE5hZ2FyICwgSW5kb3JlIiwiQ0lUWV8xNDIsIExPQ0FMSVRZXzk0MTAsIFBSRUZFUkVOQ0VfUiwgUkVTQ09NX1IiXX1d&texttypedtillsuggestion=saket&refine_results=Y&Refine_Localities=Refine%20Localities&action=%2Fdo%2Fquicksearch%2Fsearch&suggestion=CITY_142%2C%20LOCALITY_9410%2C%20PREFERENCE_R%2C%20RESCOM_R&searchform=1&locality=9410&price_min=null&price_max=null')

# view_phone = browser.find_element_by_xpath('//*[@id="N50989432"]/div[2]/div[2]/div[1]/a/button/span')
# view_phone.click()

main_div = browser.find_element_by_xpath('//*[@id="app"]/div/div/div[2]/div[2]/div[2]')
                                          
main_view_phone = browser.find_element_by_xpath('//*[@id="K51197412"]/div[2]/div[2]/div[1]/a/button/span')
