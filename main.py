#!/bin/python3

import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options


class TinderBot:
    def init(self):
        options = Options()
        options.add_argument("--user-data-dir=/home/kali/.config/google-chrome/Profile 2") #you need to change the profile path (you cand find this on chrome://version/ )
        chrome_path = r"/home/kali/Bureau/chromedriver"
        options.page_load_strategy = 'normal'
        self.driver = webdriver.Chrome(chrome_path, options=options)
        self.driver.get('https://tinder.com')

    def login(self):
        time.sleep(random.randint(1,2))

    def like(self):
        like_btn = self.driver.find_element_by_css_selector('.Bgc\(\$c-like-green\)\:a > span:nth-child(1) > span:nth-child(1)')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_css_selector('.Bgc\(\$c-pink\)\:a > span:nth-child(1) > span:nth-child(1)')  # not sure
        dislike_btn.click()

    def close_popup1(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/button[2]')  # super like popup
        popup_3.click()

    def close_popup2(self):
        popup_4 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')  # super like popup
        popup_4.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath(
            '//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')  # not sure
        match_popup.click()
    def close_pop_up(self):
        match_pop_up_tinder =  self.driver.find_element_by_xpath('//*[@id="o1827995126"]/div/div/div[3]/button/svg')
        match_pop_up_tinder.click()


    def auto_swipe(self):
        input("Press any key to continue")

        while True:
            counter_like = 0
            counter_dislike = 0
            count = 0

            n = random.random() * 3
            sleep(n)
            self.like()
            try:
                if(n>1) :
                    self.like() #67% of like
                    counter_like = counter_like+1
                else :
                    if(count %10 == 0) :
                        self.dislike()
                    else :
                        self.like()
                    time.sleep(0.5)
                    counter_dislike = counter_dislike + 1


            except Exception as e:
                print(e)

                try :
                    self.close_pop_up()
                except Exception as e:
                    try:
                        print(e)
                        self.close_popup2()
                    except Exception as e:
                        try :
                            print(e)
                            self.close_match()
                        except Exception as e :
                            print(e)
                            sleep(3)

            if((counter_like % 100 )== 0) :
                print(counter_dislike)


bot = TinderBot()
bot.init()
bot.login()
bot.auto_swipe()
