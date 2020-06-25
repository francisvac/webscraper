#!/usr/bin/env python3
# coding: utf-8

import os
from linkedin_scraper import Person
from linkedin_scraper import actions
from selenium import webdriver
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

email = ""
password = ""
file_p = open("table.csv", "a+")
driver = webdriver.Chrome("/usr/bin/chromedriver",chrome_options=chrome_options)
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal

# people_jaana.txt is a text file which has the links for each profile
with open("people_jaana.txt") as fp:
    lines = fp.readlines()
    for line in lines:
        try:
            person = Person(line, driver=driver)
            file_str = person.name
            if (len(person.experiences)):
                file_str +=  "," + person.experiences[0].position_title.decode("utf-8") +","+ person.experiences[0].institution_name.decode("utf-8")
            else:
                file_str +=  "," + ","
            file_str += "," + line 
            print(file_str)
            file_p.write(file_str)
        except:
            print(line)
file_p.close()
driver.close()

