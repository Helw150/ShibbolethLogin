from selenium import webdriver
from selenium.webdriver.support.ui import Select # for <SELECT> HTML form

driver = webdriver.PhantomJS()
# On Windows, use: webdriver.PhantomJS('C:\phantomjs-1.9.7-windows\phantomjs.exe')

# Service selection
# Here I had to select my school among others 
driver.get("https://students.nyuad.nyu.edu")

# Login page (https://cas.ensicaen.fr/cas/login?service=https%3A%2F%2Fshibboleth.ensicaen.fr%2Fidp%2FAuthn%2FRemoteUser)
# Fill the login form and submit it
driver.find_element_by_id('netid').send_keys("USERNAME")
driver.find_element_by_id('password').send_keys("PASSWORD")
driver.find_element_by_name('_eventId_proceed').click()

#page = driver.find_element('body')
# # Now connected to the home page
# # Click on 3 links in order to reach the page I want to scrape
# driver.find_element_by_id('tabLink_u1240l1s214').click()
# driver.find_element_by_id('formMenu:linknotes1').click()
# driver.find_element_by_id('_id137Pluto_108_u1240l1n228_50520_:tabledip:0:_id158Pluto_108_u1240l1n228_50520_').click()

# # Select and print an interesting element by its ID
page = driver.find_element_by_id('announceContainer')
driver.save_screenshot('screenshot.png')
print page.get_attribute('innerHTML')
