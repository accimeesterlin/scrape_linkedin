from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
import re
import json


driver = webdriver.Chrome()


""" Navigate and login with Credentials """


def navigate_and_login():

    driver.get("https://www.linkedin.com/")
    email = driver.find_element_by_id("login-email")
    password = driver.find_element_by_id("login-password")
    email.send_keys("") # email here
    print("Typing credentials...")
    password.send_keys("") # password here
    driver.find_element_by_id("login-submit").click()
    print("Login successful...")
    


navigate_and_login()


""" Navigate to the Connections """
def all_connections():
    driver.find_element_by_css_selector("a[href='/mynetwork/']").click()
    time.sleep(3)
    driver.find_element_by_css_selector(
        "a:first-child[href='/mynetwork/invite-connect/connections/']").click()
    time.sleep(1)
    
all_connections()



all_linkedin_contacts = []


""" Scraping all contacts """


def get_contacts(people):
    for person in people:
        contacts = {}
        name = person.find_element_by_class_name("mn-person-info__name").text
        occupation = person.find_element_by_class_name("mn-person-info__occupation").text
        link = person.find_element_by_class_name("mn-person-info__link").get_attribute("href")
        contacts["name"] = name
        contacts["link"] = link
        contacts["occupation"] = occupation
        all_linkedin_contacts.append(contacts)



def scroll_down():
    count = 0
    for i in range(1, 210):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(4)
        count += 1
        print("___________________________________________________")
        print("___________ COUNT INCREMENTED _____________________")
        print("___________________________________________________")
        print("Count: ", count)
    if count >= 208:
        people = driver.find_elements_by_class_name('mn-person-info__details')    
        get_contacts(people)    
    return count    

scroll_down() 
print("___________________________________________________")
print("________________ CONTACTS _________________________")
print("___________________________________________________")
print("CONTACTS: ", all_linkedin_contacts)

print("___________________________________________________")
print("__________________ LENGTH__________________________")
print("___________________________________________________")
print("CONTACT LENGTH", len(all_linkedin_contacts))

with open("contacts.json", "w") as outfile:
    json.dump(all_linkedin_contacts, outfile)


