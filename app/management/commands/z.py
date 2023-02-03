from django.core.management.base import BaseCommand
from app.bot import YoutubeBot
import pandas as pd, random
from app.models import Text
import json
class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        # from aa import TextList
        # for text in TextList:
        a =Text.objects.create(
            text = 'where is the movie theater?'
        )
        print(a.id,a.text)
        
        with open('abc.json', 'r') as openfile:
            json_file_data = json.load(openfile)

        print(json_file_data)
        for text in json_file_data:
            text = text['text']
        
            a =Text.objects.create(
                text = f'''{text}'''
            )
            print(a.id)
        
