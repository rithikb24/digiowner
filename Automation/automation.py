from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # To get hold of various keyboard keys like 'Enter'


browser = webdriver.Chrome()
browser.get('https://www.selenium.dev/')

download_object = browser.find_element_by_link_text('Downloads')
# download_link = download_object.get_attribute('href') # For Method 1

# For clicking a particular button
# To go to download page
# Method 1
# browser.get(download_link)

# Method 2
# After creating download object 'download_object' just code the following line to click on 'Downloads' button:
download_object.click()

# For going back to projects
project_object = browser.find_element_by_link_text('Projects')
project_object.click()


# Searching
# How to put text in search box

# Step 1) Inspect the box and get it's 'id'
searchBar = browser.find_element_by_id('gsc-i-id1')
# Step 2) to enter text into it
searchBar.send_keys('download')
# Step 3) To press Enter
searchBar.send_keys(Keys.ENTER)

