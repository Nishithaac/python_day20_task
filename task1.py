# using Python Selenium and the URL https://www.cowin.gov.in/ you have to :
# 1) Click on the "Create FAQ" and "Partners" anchor tags present on the home page and open two new windows
# 2) Now you have to fetch the opened window/ Frame ID and display the same on the console
# 3) Kindly close the two new windows and come back to theHome page also


# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep



class Cowin:
    # XPath locator for the "Partners" link on the FAQ page
    partner_locator="/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a"
    def __init__(self,url):
        # Store the URL in an instance variable
        self.url=url
        # Create a new instance of the Chrome WebDriver, managing the driver with ChromeDriverManager
        self.driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        # Maximize the browser window to ensure all elements are visible
        self.driver.maximize_window()
        # Open the specified URL in the browser
        self.driver.get(self.url)

        # Wait for 2 seconds to ensure the page is fully loaded
        sleep(2)
        # Get the handle (identifier) for the current window (Cowin Homepage)
        homepage_window_handle=self.driver.current_window_handle
        # Print the handle of the Cowin homepage window
        print("Cowin Homepage Window Id: ",homepage_window_handle)

        # Click on the "FAQ" link to navigate to the FAQ page
        self.driver.find_element(by=By.PARTIAL_LINK_TEXT,value="FAQ").click()
        # Click on the "Partners" link on the FAQ page using XPath
        self.driver.find_element(by=By.XPATH,value=self.partner_locator).click()

        # fetch all the window handles and save it inside a list
        faq_window_handle=self.driver.window_handles
        partner_window_handle=self.driver.window_handles
        print("FAQ window ID :",faq_window_handle)
        print("Partner Window ID:",partner_window_handle)

        # closing the FAQ window and partner window and goto the Cowin home page
        for windows in faq_window_handle and partner_window_handle:

            if windows != homepage_window_handle:
                self.driver.switch_to.window(windows)
                sleep(2)
                self.driver.close()
                sleep(2)




    def shutdown(self):
        # Quit the WebDriver, which will close all open browser windows and terminate the session
        self.driver.quit()


if __name__=="__main__":
    # Define the URL to be opened in the browser
    url="https://www.cowin.gov.in/"
    # Create an instance of the Cowin class with the specified URL
    cowin=Cowin(url)
    # Call the login method to perform the actions defined in the class
    cowin.login()
    # Call the shutdown method to close the WebDriver and clean up resources

    cowin.shutdown()