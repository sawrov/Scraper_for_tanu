import pickle
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#Tried looking at the network-log to find ajax requests.
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#capabilities = DesiredCapabilities.CHROME
#capabilities["goog:loggingPrefs"] = {"performance": "ALL"}  # chromedriver 75+
options=Options()
options.page_load_strategy = 'eager'

driver=webdriver.Chrome(ChromeDriverManager().install(), options=options)


driver.maximize_window()
url="https://www.---.com.au/robots.txt"
root_urls=[['September','https://www.---.com.au/--/'],['August','https://www.---.com.au/---/']]
unit_lecture_links=[]
august_session=[]
september_sesion=[]


try:
    if not os.path.isfile("cookies.pkl"):
        _ = input("A Browser window will open as soon as you Press Enter,\n Please login to the website to proceed furthur")
        driver.get(url+"/login")
        _ = input("Press Enter once you have logged in successfully")
        pickle.dump(driver.get_cookies(),open("cookies.pkl","wb"))

    wget_cookie="cookie: "
    driver.get(url)
    cookies = pickle.load(open("cookies.pkl","rb"))
    for cookie in cookies:
        wget_cookie=wget_cookie+cookie['name']+"="+cookie['value']+";"
        driver.add_cookie(cookie)
    f=open("wget_cookie.txt",'w')
    f.write(wget_cookie)


    for url in root_urls:

        if os.path.isfile(str(url[0])+"_lectures_list.txt"):
            print("\nFILE ALREADY EXISTS, SKIPPING EXTRACTON")
            print("IF NEED TO UPDATE, DELETE FILE  "+str(url[0])+"_lectures_list.txt\n")
            continue

        print("PLEASE WAIT...INFORMATION BEING EXTRACTED FROM:  "+str(url[0])+"")
        driver.get(url[1])
        element_professors=driver.find_elements_by_xpath('//div[@class="fusion-builder-row fusion-builder-row-inner fusion-row"]//a')

        print("Extracting Info From:\n")
        for i,element in enumerate(element_professors):
            print(str(i+1)+": "+element.text)
            august_session.append([element.text,element.get_attribute('href')])

        f=open(str(url[0])+"_lectures_list.txt",'w+')

        for session in august_session:
            driver.get(session[1])
            unit_lectures_element=driver.find_elements_by_xpath('//section[@id="content"]//a')
            lectures_list=[]
            print("Extracting Lectures By: "+str(session[0])+"\n")
            print("Number of Lectures Found: "+str(len(unit_lectures_element)-1)+"")
            f.write("--------------------Lectures By: "+session[0]+"---------------------------\n")
            for lecture in unit_lectures_element[1:]:
                print(lecture.text+"\n")
                link=lecture.get_attribute('href')
                lectures_list.append(link)
                f.write(link+"\n")
            if(len(unit_lectures_element)<1):
                f.write(session[1])
            print("---------")



        f.close()

except:
    print("DID YOU LOGIN??")
    raise
finally:
    driver.quit()
    print("DONE")
