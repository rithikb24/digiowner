from selenium import webdriver
from selenium.webdriver.support.ui import Select # For dealing with dropdown

browser = webdriver.Chrome()
browser.get('https://graph.tips/beta/')

search_type = browser.find_element_by_id('select_search_type')
browser.find_element_by_class_name()

select = Select(browser.find_element_by_id('select_search_type'))

# After getting the id there are two methods to select the text from drop dwon
# 1) select by visible text
pages = select.select_by_visible_text('Pages')
posts = select.select_by_visible_text('Posts')

# 2) select by value
# pages = select.select_by_value('pages')

# We'll work with public posts, therefore we after selecting 'Posts', we'll 'add filter'
# of 'Posts from public(needs a keyword)'

public_filter = browser.find_element_by_class_name()

