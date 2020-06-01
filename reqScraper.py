import os
import selenium
from selenium import webdriver
import time
from variables import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

preferences = {"download.default_directory": r"C:\Users\Harshit Bansal\PycharmProjects\seleniumScraping"}
options.add_experimental_option("prefs", preferences)
driver = webdriver.Chrome(options=options)
driver.get("https://www.amfiindia.com/ter-of-mf-schemes")


def Solve(type,category,subCategory):
    for m in range(len(mutual_funds)):
        driver.find_element_by_xpath("//div[6]//span[1]//a[1]//span[2]").click()

        if (mutual_funds[m]!='Mahindra Mutual Fund'):
            driver.find_element_by_xpath(f"//a[contains(text(),'{mutual_funds[m]}')]").click()
        else:
            driver.find_element_by_xpath("//li[27]//a[1]").click()
        time.sleep(0.25)

        driver.find_element_by_xpath("//a[@id='hrfGo']").click()
        time.sleep(0.25)

        try:
            ter = WebDriverWait(driver, 5).until(
                lambda x: x.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[6]/div[1]/form/input[2]"))
            ter.click()
            time.sleep(1.5)
            for filename in os.listdir():
                if filename.startswith("AMFI"):
                    currName = filename
                    newName = f"{mutual_funds[m]}_{type}_{category}_{subCategory}_{month_dictionary[year[i]][j]}.xls"
                    os.rename(currName, newName)

        except:
            print(f"NO DATA {mutual_funds[m]}_{type}_{category}_{subCategory}_{month_dictionary[year[i]][j]}")
            continue


for i in range(len(year)):
    driver.find_element_by_xpath("//div[@id='divFinTER']//span[@class='ui-button-text']").click()
    driver.find_element_by_xpath(f"//a[contains(text(),'{year[i]}')]").click()
    time.sleep(1)

    for j in range(len(month_dictionary[year[i]])):
        driver.find_element_by_xpath("//div[@class='common-content']//div[2]//span[1]//a[1]//span[2]").click()
        driver.find_element_by_xpath(f"//a[contains(text(),'{month_dictionary[year[i]][j]}')]").click()
        time.sleep(1)

        for j in range(len(dummy1)):
            if (j == 0):
                driver.find_element_by_xpath("//div[@id='divNav']//span[@class='ui-button-text']").click()
                driver.find_element_by_xpath(f"//a[contains(text(),'{dummy1[j]}')]").click()
                time.sleep(1)
                for k in range(len(dummy2)):
                    driver.find_element_by_xpath("//div[@id='divMFScheme']//span[@class='ui-button-text']").click()
                    driver.find_element_by_xpath(f"//a[contains(text(),'{dummy2[k]}')]").click()
                    time.sleep(1)
                    for l in range(len(typeOfMF[dummy1[0]][dummy2[k]])):
                        driver.find_element_by_xpath(
                            "//div[@class='ui-widget auto-select FYear third']//span[@class='ui-button-text']").click()
                        driver.find_element_by_xpath(
                            f"//a[contains(text(),'{typeOfMF[dummy1[0]][dummy2[k]][l]}')]").click()
                        time.sleep(1)
                        Solve(dummy1[j],dummy2[k],typeOfMF[dummy1[0]][dummy2[k]][l])

            if (j == 1 or j == 2):
                for l in range(len(typeOfMF[dummy1[j]])):
                    driver.find_element_by_xpath(f"//a[contains(text(),'{typeOfMF[dummy1[j]][l]}')]")
                    Solve(dummy1[j],typeOfMF[dummy1[j]][l])



