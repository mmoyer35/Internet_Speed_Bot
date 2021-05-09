from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

#Update with your specific contract limits
PROMISED_UP = 20
PROMISED_DOWN = 500

# Input your twitter email and pass. Windows Chrome version and installed version of chromedriver must match
TWITTER_EMAIL = "YOURTWITTEREMAIL@EMAIL.COM"
TWITTER_PASS = "YOURTWITTERPASSWORD"
chrome_driver_path = "C:\Development\chromedriver.exe"


class InternetSpeedTwitterBot():
    #Set up driver, download and upload speed set to 0
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.up = 0
        self.down = 0

    # Test the internet speed, can take up to 1m
    def get_internet_speed(self):

        self.driver.get("https://speedtest.net")
        #Xpath to the start button
        start_btn = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_btn.click()
        time.sleep(60)
        #Xpath to close button
        close_btn = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[8]/div/div/div[2]/a')
        close_btn.click()
        #Download speed
        self.down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        #Upload speed
        self.up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def login_to_twitter(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(5)
        #Locate and input user email on login page
        twitter_email = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
        twitter_email.send_keys(TWITTER_EMAIL)
        #Locate and input password
        twitter_password = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
        twitter_password.send_keys(TWITTER_PASS)
        time.sleep(5)
        twitter_password.send_keys(Keys.ENTER)
        time.sleep(3)

    # Complaint template
    def complain_to_isp(self):
        complaint_template = f"Hey Internet Provider, why is my internet speed {speed_check_bot.down}down / {speed_check_bot.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_compose.send_keys(complaint_template)
        time.sleep(5)
        tweet_send = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_send.click()
        time.sleep(3)
        self.driver.quit()

    # Thank you template, update with your own ISP
    def thank_isp(self):
        thank_you_template = f"Hey Internet Provider, I wanted to say thanks! My internet speed is {speed_check_bot.down}down / {speed_check_bot.up}up and I pay for {PROMISED_DOWN}down/{PROMISED_UP}up, keep up the good work!"
        tweet_compose = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
        tweet_compose.send_keys(thank_you_template)
        time.sleep(5)
        tweet_send = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_send.click()
        time.sleep(3)
        self.driver.quit()

#Creates the speed_checker class and get internet speed
speed_check_bot = InternetSpeedTwitterBot()
speed_check_bot.get_internet_speed()
speed_check_bot.login_to_twitter()
# Debug
# print(f"Download: {speed_checker.down}")
# print(f"Upload: {speed_checker.up}")

# If the upload/download speeds are less than what was promised by internet provider, tweets at them and complains.
# If the speeds are at least 90% of what was promised, thank them!
if float(speed_check_bot.down) < int(PROMISED_DOWN * 0.90) or float(speed_check_bot.up) < int(PROMISED_UP * 0.90):
    speed_check_bot.complain_to_provider()
else:
    speed_check_bot.thank_provider()