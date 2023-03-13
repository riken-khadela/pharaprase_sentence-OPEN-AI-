from django.core.management.base import BaseCommand
from app.bot import Bot
import pandas as pd, random

class Command(BaseCommand):
    help = '''to add accounts in database and profile directory
            add accounts in 
            '''
    
    def handle(self, *args, **options):
        
        
        profile_name = ''
        bot = Bot()
        bot.email_check()
            
    