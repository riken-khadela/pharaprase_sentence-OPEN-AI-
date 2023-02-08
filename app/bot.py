import profile
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
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Bot:
    # def __init__(self):
    #     ...
            
    def get_driver(self) :
        options = webdriver.ChromeOptions()
        
        options.add_argument(f"--user-data-dir=Profiles") 
        options.add_argument(f'--profile-directory=Default')
        # options.headless = True
        # self.driver = uc.Chrome(use_subprocess=True,options=options)
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        
        # profile = webdriver.FirefoxProfile('Profiles_FF')
        # self.driver = webdriver.Firefox(profile)
        # self.driver.maximize_window()
        
        
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
    
    def login_account(self):

        login_page = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[3]')
        login_page_text = login_page.text

        if str(login_page_text).upper() == "Log in with your OpenAI account to continue".upper():

            login_button = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[4]/button[1]')
            login_button.click()

            while True:
                try:
                    login_next_page = self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/header/h1')
                    login_next_page_text = login_next_page.text
                    if str(login_next_page_text).upper() == "Welcome back".upper():
                        break
                except:
                    pass
            
            email_box = self.driver.find_element(By.XPATH,'//*[@id="username"]')
            email_box.send_keys("lathipushpa024@gmail.com")

            continue_btn_one = self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/form/div[2]/button')
            continue_btn_one.click()
            
            while True:
                try:
                    password_page = self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/header/h1')
                    password_page_text = password_page.text
                    if str(password_page_text).upper() == "Enter your password".upper():
                        break
                except:
                    pass
            
            password_box = self.driver.find_element(By.XPATH,'//*[@id="password"]')
            password_box.send_keys("Bhavin@123")

            continue_btn_two = self.driver.find_element(By.XPATH,'/html/body/main/section/div/div/div/form/div[2]/button')
            continue_btn_two.click()
            
            time.sleep(random.randint(5,10))

            label_find = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[1]/h2/b')
            label_find_text = label_find.text
            if str(label_find_text).upper() == "ChatGPT".upper():
                next_buttom_one = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button')
                next_buttom_one.click()
                time.sleep(random.randint(1,3))
                next_buttom_two = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]')
                next_buttom_two.click()
                
                time.sleep(random.randint(1,3))
                next_buttom_three = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]')
                next_buttom_three.click()

            time.sleep(random.randint(5,10))
            # label # //*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[1]/h2/b # <b>ChatGPT</b>
            # //*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button

            # //*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]
            # //*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]

    def singup(self):
        self.get_driver()
        self.driver.get('https://chat.openai.com/chat')
        time.sleep(random.randint(5,10))

        login_page = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[3]')
        login_page_text = login_page.text

        if str(login_page_text).upper() == "Log in with your OpenAI account to continue".upper():

            signup_button = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[4]/button[2]')
            signup_button.click()

            signup_lable = self.driver.find_element(By.XPATH, "/html/body/main/section/div/div/header/h1")
            signup_lable_text = signup_lable.text

            if signup_lable_text.upper() == "Create your account".upper():
                email_box = self.driver.find_element(By.XPATH,'//*[@id="email"]')
                email_box.send_keys("email")

                continue_button_one = self.driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/form/div[2]/button")
                continue_button_one.click()

                password_box = self.driver.find_element(By.XPATH,'//*[@id="password"]')
                password_box.send_keys()

                continue_button_two = self.driver.find_element(By.XPATH,"/html/body/main/section/div/div/div/form/div[2]/button")
                continue_button_two.click()

                verify_label = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[2]/h1')
                verify_label_text = verify_label.text

                if verify_label_text.upper() == "Verify your email".upper():

                    self.driver.refresh()

                    tell_name_page_label = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[2]/h1')
                    tell_name_page_label_text = tell_name_page_label.text

                    if tell_name_page_label_text.upper() == "Tell us about you".upper():

                        first_name_box = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[2]/form/div/div/div[1]/input')
                        first_name_box.send_keys("fisrt name")

                        last_name_box = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[2]/form/div/div/div[2]/input')
                        last_name_box.send_keys("fisrt name")

                        continue_button_three = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[2]/form/button')
                        continue_button_three.click()

                        verify_phonenumber_label = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[2]/h1')
                        verify_phonenumber_label_text = verify_phonenumber_label.text

                        if verify_phonenumber_label_text.upper() == "Verify your phone number".upper():

                            phone_number_box = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[2]/form/div[1]/div/div[2]/input')
                            phone_number_box.send_keys("phone number")

                            whatsapp_no_btn = self.driver.find_element(By.XPATH,'//*[@id="whatsapp-opt-in-radio-no"]')
                            whatsapp_no_btn.click()

                            sendcode_button = self.driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div/div[2]/form/button')
                            sendcode_button.click()
                            

            

    def work(self):
        print("dasdasd")
        for i in TxtObj.objects.all() :
            print("dasdasd---",i)
            self.get_driver()
            self.driver.get('https://chat.openai.com/chat')
            breakpoint()
            self.driver.close()
            break
            time.sleep(random.randint(5,10))
            while True:
                print('111')
                try:
                    print('1')

                    verify_one = self.driver.find_element(By.XPATH,'//*[@id="cf-stage"]/div[6]/label')
                    verify_text = verify_one.text
                    if str(verify_text).upper() == "Verify you are human".upper():
                        verify_box = self.driver.find_element(By.XPATH,'//*[@id="cf-stage"]/div[6]/label/span')
                        verify_box.click()
                except:
                    print('2')
                    try:
                        verify_two = self.driver.find_element(By.XPATH,'//*[@id="challenge-stage"]/div/input')
                        verify_two_text = verify_two.get_attribute("value")

                        if str(verify_two_text).upper() == "Verify you are human".upper():
                            verify_two.click()
                    except:
                        print('3')
                        pass
                
                try:
                    print('4')
                    home_page = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[1]/main/div[1]/div/div/div/div[1]/h1')
                    home_page_text = home_page.text
                    if str(home_page_text).upper() == "ChatGPT".upper():
                        break
                except:
                    print('5')
                    try:
                        session_expired = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-title-:r4:"]')
                        session_expired_text = session_expired.text
                        if str(session_expired_text).upper() ==  "Your session has expired".upper():
                            break
                    except:
                        print('6')
                        try:
                            login_page = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[3]')
                            login_page_text = login_page.text
                            print(":::----->",login_page_text)
                            if str(login_page_text).upper() == "Log in with your OpenAI account to continue".upper():
                                break
                        except Exception as e:
                            print(str(e))
                            print('7')
                            try:
                                sound_btn = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[3]/button')
                                sound_btn_text = sound_btn.text
                                if str(sound_btn_text).upper() == "Sounds good!".upper():
                                    break
                            except:
                                print('8')
                                pass

            try:
                print('9')
                session_expired = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-title-:r4:"]')
                session_expired_text = session_expired.text
                if str(session_expired_text).upper() ==  "Your session has expired".upper():
                    session_expired_loginbtn = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r3:"]/div[2]/button')
                    session_expired_loginbtn.click()
                    time.sleep(random.randint(5,10))
                    self.login_account()
            except:
                print('10')
                pass

            try:
                print('11')
                login_page = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[3]')
                login_page_text = login_page.text
                print(":::----->",login_page_text)
                if str(login_page_text).upper() == "Log in with your OpenAI account to continue".upper():
                    self.login_account()
            except Exception as e:
                print('12')
                print(str(e))

            # input("sdbasjkd")
            # try:
            #     login_page = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div/div[3]')
            #     login_page_text = login_page.text
            #     if str(login_page_text).upper() == "Log in with your OpenAI account to continue".upper():
            #         self.login_account()
            # except:
            #     pass

            try:
                print('13')
                sound_btn = self.driver.find_element(By.XPATH,'//*[@id="headlessui-dialog-panel-:r1:"]/div[3]/button')
                sound_btn_text = sound_btn.text
                if str(sound_btn_text).upper() == "Sounds good!".upper():
                    sound_btn.click()
            except:
                pass


            time.sleep(random.randint(5,10))
            # input("jbb")
            Text = i.text
            # Text = "where is the park?"
            print(Text)

            # if ('document.querySelector("#cf-stage > div.ctp-checkbox-container > label > span").click();')
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
            not_found_bool = False
            while True:
                print('222')
                try:
                    abc = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[1]/main/div[1]/div/div/div/div[2]/div/div[2]/div[1]/div/div/p')
                    if abc!= None:
                        if "I'm sorry" in abc.text :
                            not_found_bool = True
                            break
                        if "Too many requests in 1 hour. Try again later." in abc.text:
                            time.sleep(60)
                            break
                        if "I apologize" in abc.text:
                            not_found_bool = True
                            break
                        if "Sorry" in abc.text:
                            not_found_bool = True
                            break
                except:
                    try:
                        abc = self.driver.find_element(By.XPATH,'//*[@id="__next"]/div[1]/div[1]/main/div[1]/div/div/div/div[2]/div/div[1]/div[1]/span')
                        if abc != None:
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



# label # //*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[1]/h2/b # <b>ChatGPT</b>
# //*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button

# //*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]
# //*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]

# verify box # //*[@id="cf-stage"]/div[6]/label

# verify box click # //*[@id="cf-stage"]/div[6]/label/span

# verify input # //*[@id="challenge-stage"]/div/input # document.querySelector("#challenge-stage > div > input[type=button]") # <input type="button" value="Verify you are human" style="margin: 0px; cursor: pointer;">

# session expired # label:- //*[@id="headlessui-dialog-title-:r4:"] # <h3 class="text-lg font-medium leading-6 text-gray-900 dark:text-gray-200" id="headlessui-dialog-title-:r4:" data-headlessui-state="open">Your session has expired</h3>
# session expired # login button:- //*[@id="headlessui-dialog-panel-:r3:"]/div[2]/button # <button class="btn flex justify-center gap-2 btn-neutral" tabindex="0">Log in</button>


# login page # label :- //*[@id="__next"]/div[1]/div/div[3] # <div class="mb-4 text-center">Log in with your OpenAI account to continue</div>
# login page # login button :- //*[@id="__next"]/div[1]/div/div[4]/button[1]  #  <button class="btn flex justify-center gap-2 btn-primary">Log in</button>

# login next page # label:- /html/body/main/section/div/div/header/h1 # <h1 class="cc9990aac c3216fce5">Welcome back</h1>
# login next page # email box:- //*[@id="username"] #<input class="input ce09e4a4b ca6b0879c" inputmode="email" name="username" id="username" type="text" value="" required="" autocomplete="username" autocapitalize="none" spellcheck="false" autofocus="">
# login next page # continue button:- /html/body/main/section/div/div/div/form/div[2]/button # <button type="submit" name="action" value="default" class="c8fca5323 cb6b7c993 cee1c07cc c850d9a60 _button-login-id">Continue</button>


# login next page # google button:- /html/body/main/section/div/div/div/div[3]/form[2]/button # <button type="submit" class="c5b8edce6 c426c38e7 c723b33d7" data-provider="google"><span class="c7fe15dc1 c3bee28ca" data-provider="google"></span><span class="cc341260d">Continue with Google</span></button>
# google next page # google login:- //*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div # <div class="lCoei YZVTmd SmR8" role="link" tabindex="0" jsname="MBVUVe" data-authuser="0" data-identifier="rikenkhadela777@gmail.com" data-item-index="0" null=""><div class="d2laFc"><div class="tgnCOd"><div class="qQWzTd" aria-hidden="true"><img src="https://lh3.googleusercontent.com/-2kvS9bl5i3k/AAAAAAAAAAI/AAAAAAAAAAA/APmPUbFjJvsr9BTLfidWQxR1XgEb26lL5g/s128-c/photo.jpg" alt="" class="r78aae TrZEUc"></div><div class="WBW9sf"><div class="w1I7fb" jsname="V1ur5d">O - 154 Riken Khadela</div><div class="wLBAL" jsname="bQIQze" data-email="rikenkhadela777@gmail.com">rikenkhadela777@gmail.com</div></div></div></div><div class="n3x5Fb" aria-hidden="true"><svg aria-hidden="true" class="stUf5b" fill="currentColor" focusable="false" width="24px" height="24px" viewBox="0 0 24 24" xmlns="https://www.w3.org/2000/svg"><path d="M7 11v2h10v-2H7zm5-9C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"></path></svg></div></div>

# sounds good popup # sounds good button # //*[@id="headlessui-dialog-panel-:r1:"]/div[3]/button # <button class="btn flex justify-center gap-2 btn-primary" tabindex="0">Sounds good!</button>
#sounds good popup box html # <div class="fixed inset-0 z-50 overflow-y-auto"><div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0"><div class="relative transform overflow-hidden rounded-lg bg-white px-4 pt-5 pb-4 text-left shadow-xl transition-all dark:bg-gray-900 sm:my-8 sm:w-full sm:p-6 sm:max-w-sm opacity-100 translate-y-0 sm:scale-100" id="headlessui-dialog-panel-:r1:" data-headlessui-state="open"><div class="flex items-center sm:flex"><div class="mt-3 text-center sm:mt-0 sm:text-left"></div></div><div class="mb-6 flex flex-col gap-6"><div class="text-gray-800 dark:text-white">Jan 30 version update</div><div class="text-2xl">Here's what's new</div><div class="prose text-base dark:prose-invert"><ul><li>We’ve upgraded the ChatGPT model with improved factuality and mathematical capabilities.</li></ul></div></div><div class="mt-5 flex flex-col gap-3 sm:mt-4 sm:flex-row-reverse"><button class="btn flex justify-center gap-2 btn-primary" tabindex="0">Sounds good!</button></div></div></div></div>