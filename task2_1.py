#
# using Python Selenium visit the URL https://labour.gov.in/ and do the following tasks given below:
# 1) Goto the Menu whose name is Documents and Download the Monthly Progress report
# 2) Goto the menu Whose name is Media where you will find a sub-menu whose name is
# Photo Gallery. Your task is to download the 10 photos from the webpage and store them in a folder.
# Kindly create the folder using Python only

# Importing necessary modules
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# 1) Goto the Menu whose name is Documents and Download the Monthly Progress report


# Class to handle downloading documents from a specific URL
class Documents:
    def __init__(self,url):
        # Store the URL in an instance variable
        self.url=url
        # Create a new instance of the Chrome WebDriver, managing the driver with ChromeDriverManager
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        # Maximize the browser window to ensure all elements are visible

        self.driver.maximize_window()
        # Open the specified URL in the browser
        self.driver.get(self.url)


    def download_documents(self):
        # Click on the "Documents" link to navigate to the documents page
        self.driver.find_element(by=By.LINK_TEXT,value="Documents").click()
        # Wait for 2 seconds to ensure the documents page is fully loaded
        sleep(2)
        # Click on the link to download the "Monthly Progress report" (identified by title)
        self.driver.find_element(by=By.XPATH,value="//a[@title='Download(7.66 MB)']").click()
        # Switch to the alert that appears when the download starts
        alert=self.driver.switch_to.alert
        # Accept the alert to proceed with the download
        alert.accept()
        # Wait for 2 seconds to ensure the download has started
        sleep(2)
        # Get the current URL of the browser
        url=self.driver.current_url
        # Print the URL for debugging purposes
        print(url)
        # Send a GET request to the URL to download the file
        response=requests.get(url)
        # Check if the request was successful
        if response.status_code==200:
            # Open a file in binary write mode to save the downloaded content
            f=open("monthlyProgressReport","wb")
            # Write the content of the response to the file
            f.write(response.content)
            f.close()
        else:
            # Print an error message if the download failed
            print("error")

    def shutdown(self):
        # Close the current browser window
        self.driver.close()


if __name__=="__main__":
    # Define the URL to be opened in the browser
    url="https://labour.gov.in/"
    # Create an instance of the Documents class with the specified URL
    documents=Documents(url)
    # Call the start method to open the URL and maximize the window
    documents.start()
    # Call the download_documents method to navigate to the documents page and download the report
    documents.download_documents()
    # Call the shutdown method to close the WebDriver and clean up resources
    documents.shutdown()