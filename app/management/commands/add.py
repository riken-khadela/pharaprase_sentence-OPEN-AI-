from django.core.management.base import BaseCommand
from app.bot import Bot
import pandas as pd, random
import concurrent.futures


class Command(BaseCommand):
    help = '''to add accounts in database and profile directory
            add accounts in 
            '''
            
    def scraping(self):
        print()
        # bot = Bot()
        # try:bot.work()
        # except Exception as e:
        #     print(e)
        #     breakpoint()
    
    def handle(self, *args, **options):
        
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=50)

        # Submit the function to the executor 50 times
        futures = [executor.submit(self.scraping) for i in range(50)]

        # Wait for each future to complete and start a new one
        for future in concurrent.futures.as_completed(futures):
            new_future = executor.submit(self.scraping)
            futures.append(new_future)

        
        bot = Bot()
        try:bot.work()
        except Exception as e:
            print(e)
            breakpoint()
        # bot.work()
    
    