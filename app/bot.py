from django.core.management.base import BaseCommand
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException,InvalidElementStateException
import time, random, pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui, json
from .models import Text as TxtObj, ParaphrasedText

class YoutubeBot:
    # def __init__(self):
    #     ...
            
    def get_driver(self) :
        options = uc.ChromeOptions()
        
        options.add_argument(f"--user-data-dir=/home/nikunj/Downloads/open_ai/profiles") 
        options.add_argument(f'--profile-directory=Profile') 
        # options.headless = True
        self.driver = uc.Chrome(use_subprocess=True,options=options)
        self.driver.maximize_window()
        
        
    def find_element(self, element, locator, locator_type=By.XPATH,
            page=None, timeout=10,
            condition_func=EC.presence_of_element_located,
            condition_other_args=tuple()):
        """Find an element, then return it or None.
        If timeout is less than or requal zero, then just find.
        If it is more than zero, then wait for the element present.
        """
        try:
            if timeout > 0:
                wait_obj = WebDriverWait(self.driver, timeout)
                #  ele = wait_obj.until(
                #          EC.presence_of_element_located(
                #              (locator_type, locator)))
                ele = wait_obj.until(
                        condition_func((locator_type, locator),
                            *condition_other_args))
            else:
                print(f'Timeout is less or equal zero: {timeout}')
                ele = self.driver.find_element(by=locator_type,
                        value=locator)
            if page:
                print(
                        f'Found the element "{element}" in the page "{page}"')
            else:
                print(f'Found the element: {element}')
            return ele
        except (NoSuchElementException, TimeoutException) as e:
            if page:
                print(f'Cannot find the element "{element}"'
                        f' in the page "{page}"')
            else:
                print(f'Cannot find the element: {element}')
                
    def click_element(self, element, locator, locator_type=By.XPATH,
            timeout=10):
        """Find an element, then click and return it, or return None"""
        ele = self.find_element(element, locator, locator_type, timeout=timeout)
        if ele:
            ele.click()
            print(f'Clicked the element: {element}')
            return ele

    def input_text(self, text, element, locator, locator_type=By.XPATH,
            timeout=10, hide_keyboard=True):
        """Find an element, then input text and return it, or return None"""
        
        ele = self.find_element(element, locator, locator_type=locator_type,
                timeout=timeout)
        if ele:
            ele.clear()
            ele.send_keys(text)
            print(f'Inputed "{text}" for the element: {element}')
            return ele    
    
    def work(self):
        print("dasdasd")
        for i in TxtObj.objects.all() :
            print("dasdasd---",i)
            self.get_driver()
            self.driver.get('https://chat.openai.com/chat')
            time.sleep(random.randint(5,10))
            # input("jbb")
            Text = i.text
            # Text = "where is the park?"
            print(Text)
            textArea = self.find_element('text area','/html/body/div/div/div[1]/main/div[2]/form/div/div[2]/textarea') # /html/body/div/div/div[1]/main/div[2]/form/div/div[2]/textarea
            action = ActionChains(self.driver)
            action.move_to_element(textArea)
            action.click()
            par = 'paraphrase thirty times the following sentence '
            for letter in par:
                # time.sleep(0.5)
                action.send_keys(letter)
                action.pause(0.1)
                action.perform()
            
            # action.perform()
            # breakpoint()
            # action.keyDown(Keys.SHIFT).sendKeys(Keys.RETURN).build().perform()
            # action.send_keys(Keys.SHIFT + Keys.ENTER)
            # action.perform()
            action.send_keys('"')
            for letter in Text:
                # time.sleep(0.5)
                action.send_keys(letter)
                action.pause(0.1)
                action.perform()
            action.send_keys('".')
            action.perform()
            self.click_element('send btn','//*[@id="__next"]/div/div[1]/main/div[2]/form/div/div[2]/button')
            # time.sleep(120)
            self.click_element('scroll down','//*[@id="__next"]/div/div[1]/main/div[1]/div/div/button',timeout=1)
            
            all_chat = self.driver.find_elements(By.XPATH,'//*[@id="__next"]/div/div[1]/main/div[1]/div/div/div/*')
            last_ele = all_chat.pop()
            print("sfdd")
            not_found_bool = False
            while True:
                try:
                    abc = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[1]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/p')
                    if abc!= None:
                        if "I'm sorry" in abc.text :
                            not_found_bool = True
                            break
                        if "Too many requests in 1 hour. Try again later." in abc.text:
                            time.sleep(60)
                            break
                except:
                    pass

                latest_responses = all_chat[-1].find_elements(By.XPATH,'//div/div[2]/div[1]/div/div/ol/*')
                print(len(latest_responses))
                if len(latest_responses) >= 30: break
                else : time.sleep(10)
            if not_found_bool == False:
                number_count = 1
                PageTitle = self.driver.title
                breakpoint()
                for response in latest_responses :
                    print(response.text)
                    ParaphrasedText.objects.create(
                        sentence = i,
                        response = response.text,
                        PageTitle = PageTitle,
                        number = number_count 
                    )
                    number_count += 1
                    
                    
            self.CloseDriver()
        
    def CloseDriver(self):
        # breakpoint()
        # input('Enter :')
        self.driver.quit()