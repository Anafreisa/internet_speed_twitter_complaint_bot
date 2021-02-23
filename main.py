from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = YOUR INTERNET DOWNLOAD PLAN
PROMISED_UP = YOUR INTERNET UPLOAD PLAN
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_LOGIN = YOUR TWITTER LOGIN
TWITTER_PASSWORD = YOUR TWITTER PASSWORD


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get('https://www.speedtest.net/pt')

        time.sleep(3)
        start_button = self.driver\
            .find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_button.click()

        time.sleep(60)
        close_popup = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div['
                                                        '3]/div[3]/div/div[8]/div/div/div[2]/a')
        close_popup.click()

        time.sleep(10)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                      '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                    '3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get('https://twitter.com/login/')

        time.sleep(2)
        name_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                       '2]/form/div/div[1]/label/div/div[2]/div/input')
        name_input.send_keys(TWITTER_LOGIN)

        password_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div['
                                                           '2]/form/div/div[2]/label/div/div[2]/div/input')
        password_input.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password_input.send_keys(Keys.ENTER)

        time.sleep(4)
        if PROMISED_DOWN < float(self.down) or PROMISED_UP < float(self.up):
            tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                      '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                      '1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div['
                                                      '2]/div/div/div/div/span')

            tweet.send_keys(f"Oi YOUR INTERNET PROVIDER, por que a velocidade da minha internet está em {self.down}/{self.up} "
                            f"se meu pacote é de 240 download/20 upload?")

            time.sleep(2)
            tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                          '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                          '4]/div/div/div[2]/div[3]/div/span/span')
            tweet_btn.click()
            time.sleep(2)
            self.driver.quit()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
