# a = [1,2,3,4,5]

# for i in a:
#     print(i)
# else:
#     print('yes')
    
    
# b = "I apologize, but I cannot fulfill your request to repeat the same sentence multiple times as it would not add any value or contribute to a meaningful conversation. Is there something specific that you would like to know or discuss? I'd be happy to help with any questions you may have."
# print(b.startswith('I apologize',))
    
    
    # def work(self):
    #     print("dasdasd")
    #     for _ in range(100):
    #         text = TxtObj.objects.filter(pharaphreased="NOT_DONE").first() 
    #         text.pharaphreased = "RUNNING"
    #         text.save()
    #         self.get_driver()
    #         self.driver.get('https://chat.openai.com/chat')
    #         # breakpoint()
    #         while True:
    #             time.sleep(3)
    #             capacity = self.find_element('High capacity','//*[@id="__next"]/div[1]/div/div/div[1]/div[1]',timeout=2)
    #             if capacity:
    #                 if 'capacity' in capacity.text.lower():
    #                     self.driver.refresh()
    #                     continue
    #             break                

    #         login_btn = self.find_element('Login btn','//*[@id="__next"]/div[1]/div/div[4]/button[1]',timeout=2)
    #         if login_btn:
    #             if login_btn.text == 'Log in':
    #                 self.sign_in()
    #                 self.click_element('Next pop up btn','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button',timeout=2)
    #                 self.click_element('Next2 pop up btn','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]',timeout=2)
    #                 self.click_element('Done pop up btn','//*[@id="headlessui-dialog-panel-:r1:"]/div[2]/div[4]/button[2]',timeout=2)
    #         time.sleep(random.randint(5,10))

    #         verify_one = self.find_element('Captcha','//*[@id="cf-stage"]/div[6]/label',timeout=2)
    #         if verify_one:
    #             if str(verify_one.text).upper() == "Verify you are human".upper():
    #                 self.click_element('Verify box','//*[@id="cf-stage"]/div[6]/label/span',timeout=3)

    #         verify_two = self.click_element('Verify2','//*[@id="challenge-stage"]/div/input',timeout=2)
    #         if verify_two:
    #             if str(verify_two.text).upper() == "Verify you are human".upper():
    #                 verify_two.click()
                
            
    #         sounds_good = self.find_element('Sounds good','//*[@id="headlessui-dialog-panel-:r1:"]/div[3]/button',timeout=3)
    #         if sounds_good:
    #             if sounds_good.text.upper() == "Sounds good!".upper():
    #                 sounds_good.click()

    #         time.sleep(random.randint(5,10))
    #         Text = text.text
    #         print(Text)
            
    #         response = 0
    #         response += self.pharaprase_text(Text=Text,response=response)
    #         for i in range(6):
    #             response += self.pharaprase_text(number=random.randint(10,15),Text=Text,another=True,response=response)
    #             if response > 50: break
            
    #         self.AddPraprasedSentenceIntoList()
                

    #         if self.not_found_bool == False:
    #             number_count = 1
                

    #             PageTitle = self.driver.title
    #             breakpoint()
    #             for response in self.all_response_text :
    #                 print(number_count,response)
    #                 ParaphrasedText.objects.create(
    #                     sentence = text,
    #                     response = response,
    #                     PageTitle = PageTitle,
    #                     number = number_count 
    #                 )
    #                 number_count += 1
                    
    #             text.pharaphreased = "DONE"
    #             text.save()
                    
    #         self.CloseDriver()
        
        
        
        
        
# from smsactivate.api import SMSActivateAPI
# # SMSActivateAPI Contains all basic tools for working with the SMSActivate API
# sa = SMSActivateAPI('8f0902c8c9defd33c08f78cd324A9f96')
# # ACCESS_NUMBER:1290229038:919327198279
# sa.debug_mode = True
# status = sa.setStatus(id=1290229038, status=1) # ACCESS_READY
# # Used for debugging. When debug_mode is active, all responses from the server and class will be output to the console
# print(sa.version())
# sa.getFullSms(1290229038)
# Returns the current version of the library

# status = sa.getNumbersStatus(country=0, operator='tele2')
# try:
#     print(status['vk_0']) # 274789
# except:print(status['message']) # Error text



# result = sa.getTopCountriesByService('vk')
# try:print(result[0]['count']) # 2350
# except:print(result['message']) # Error text


# balance = sa.getBalance() # {'balance': '100.00'}
# try:print(balance['balance']) # 100.00
# except:print(balance['message']) # Error text


# balance = sa.getBalanceAndCashBack() # {'balance': '100.00'}
# try:print(balance['balance']) # 100.00
# except:print(balance['message']) # Error text




# operators = sa.getOperators(country=0)
# try:print(operators['countryOperators']['0'])
# except:print(operators['error']) # Error status



# activations = sa.getActiveActivations()
# try:print(activations['activeActivations'])
# except:print(activations['error']) # Error status



# number = sa.getNumber(service='dr',  country=22) # {'activation_id': 000000000, 'phone': 79999999999}
# try:print(number['phone']) # 79999999999
# except:print(number['message']) # Error text



# number = sa.getNumberV2(service='vk', country=0)
# try:print(number['phoneNumber']) # 79999999999
# except:print(number['message']) # Error text



# multinumber = sa.getMultiServiceNumber(service='fb,ig', operator='tele2', country=0) # [{'phone': '79999999999', 'activation': 000000000, 'service': 'fb'}, {'phone': '79999999999', 'activation': 000000001, 'service': 'ig'}]
# try:print(multinumber[0]['phone']) # 79999999999
# except:print(multinumber['message']) # Error text


# status = sa.setStatus(id=1290229038, status=1) # ACCESS_READY
# try:print(status) # ACCESS_READY
# except:print(status['message']) # Error text


# status = sa.getStatus(id=000000000) # STATUS_WAIT_CODE
# try:print(sa.activationStatus(status)) # {'status': 'STATUS_WAIT_CODE', 'message': 'Ожидание смс'}
# except:print(status['message']) # Error text


# status = sa.getIncomingCallStatus(id=000000000)
# try:print(status['status']) # 2
# except:print(status['message']) # Error text


# prices = sa.getPrices(service='fb', country=0)
# try:print(prices['0']) # {'fb': {'cost': 9, 'count': 27934}}
# except:print(prices['message']) # Error text


# countries = sa.getCountries()
# try:print(countries['0']['eng']) # Russia
# except:print(countries['message']) # Error text


# service = sa.getAdditionalService(id=000000000, service='ig')
# try:print(service['phone']) # 79999999999
# except:print(service['message']) # Error text


# service = sa.getRentServicesAndCountries(time=4, operator='tele2', country=0)
# try:print(service['services']['full']['cost']) # 100.00
# except:print(service['message']) # Error text


# rent = sa.getRentNumber(service='ig', time=4, operator='tele2', country=0)
# try:print(rent['phone']['number']) # 79999999999
# except:print(rent['message']) # Error text


# status = sa.getRentStatus(1290229038)
# try:print(status['values']['0']['text']) # SMS
# except:print(status['message']) # Error text


# status = sa.setRentStatus(id=000000000, status=1)
# try:print(status['status']) # success
# except:print(status['message']) # Error text


# rent = sa.getRentList()
# try:print(rent['values']['0']['phone']) # 79999999999
# except:print(rent['message']) # Error text


# rent = sa.continueRentNumber(id=000000000, time=4)
# try:print(rent['phone']['number']) # 79999999999
# except:print(rent['message']) # Error text


# rent = sa.getContinueRentPriceNumber(000000000)
# try:print(status['price']) # 4.00
# except:print(status['message']) # Error text


# a = 'RM0 Your OpenAI API verification code is: 123635'
# a = a.strip().split(' ')[-1]
# print(a)

id = 34

cnt = id%10
