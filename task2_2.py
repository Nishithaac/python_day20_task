# using Python Selenium visit the URL https://labour.gov.in/ and do the following tasks given below:
# 1) Goto the Menu whose name is Documents and Download the Monthly Progress report
# 2) Goto the menu Whose name is Media where you will find a sub-menu whose name is
# Photo Gallery. Your task is to download the 10 photos from the webpage and store them in a folder.
# Kindly create the folder using Python only


# Importing necessary modules
import os
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Define a class to handle media operations
class Media:
    def __init__(self, url):
        # Store the URL to be used in methods
        self.url = url
        # Initialize the Chrome WebDriver using ChromeDriverManager to handle driver installation
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        # Maximize the browser window
        self.driver.maximize_window()
        # Navigate to the provided URL
        self.driver.get(self.url)

    def download_images(self):
        # Path where images will be saved
        # Ensure this path exists or create it if it doesn't
        download_path = r'C:\Users\pranavi\download_folder'  # Make sure this path exists

        # Check if the download directory exists, if not, create it
        if not os.path.exists(download_path):
            os.makedirs(download_path)

        # URL of the webpage containing the pictures
        url = 'https://labour.gov.in/photo-gallery'

        # Navigate to the webpage
        self.driver.get(url)
        # Wait for the page to load
        sleep(3)

        # Locate the elements containing the pictures
        picture_elements = self.driver.find_elements(By.XPATH,
                                                     '//*[@id="fontSize"]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody//div/img')

        # Counter to keep track of downloaded pictures
        downloaded_count = 0

        # Iterate through the picture elements
        for idx, picture_element in enumerate(picture_elements, start=1):
            # Get the URL of the picture
            picture_url = picture_element.get_attribute('src')

            # Send a GET request to download the image
            response = requests.get(picture_url)

            # Construct the file path where the image will be saved
            file_path = os.path.join(download_path, f'picture_{idx}.jpg')
            # Write the image data to a file
            with open(file_path, 'wb') as f:
                f.write(response.content)

            # Increment downloaded count
            downloaded_count += 1

            # Break loop if 10 pictures have been downloaded
            if downloaded_count == 10:
                break

        # Print a confirmation message
        print("10 photos downloaded successfully")


    def shutdown(self):
        # Close the browser
        self.driver.quit()

# Main execution block
if __name__ == "__main__":
    # URL of the website to be scraped
    url = "https://labour.gov.in/"
    # Create an instance of the Media cla
    media = Media(url)
    # Start the browser and navigate to the URL
    media.start()
    # Download images from the specified webpage
    media.download_images()
    # Close the browser
    media.shutdown()
