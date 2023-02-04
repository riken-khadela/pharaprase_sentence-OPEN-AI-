from django.core.management.base import BaseCommand
from app.bot import YoutubeBot
import pandas as pd, random
import threading
import concurrent.futures

class Command(BaseCommand):
    help = '''to add accounts in database and profile directory
            add accounts in 
            '''
    def add_arguments(self, parser):
        parser.add_argument(
            "--n",
            type=int,
            nargs="?",
            default=1,
        )
    
    def handle(self, args, *options):
        ThreadNumber = int(options.get('n'))
        for i in range(ThreadNumber):
            x = threading.Thread(target= self.open_chrome)
            x.start()

    def open_chrome(self):
        # while True:
            bot = YoutubeBot()
            try:
                bot.work()
            except:
                print("Error in open_chrome()")
                bot.CloseDriver()

