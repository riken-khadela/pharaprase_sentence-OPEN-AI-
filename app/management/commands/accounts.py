from django.core.management.base import BaseCommand
import pandas as pd
from app.models import user

class Command(BaseCommand):

    def handle(self, *args, **options):
        # user_obj = user.objects.get_or_create(
        #         email = 'noborderz49@gmail.com',
        #         password = 'No@12345',
        #         profile = f'Profile 1076560'
        #         )
        # print(user_obj)
        df = pd.read_csv('accounts2.csv')
        print(df)
        for i in range(len(df)):
            email = df.loc[i]['email']
            print(email,'-----')
            password = df.loc[i]['password']
            profile = str(df.loc[i]['profile']).replace('Profile ','').strip()
            
            user_obj = user.objects.get_or_create(
                email = str(email).strip(),
                password = str(password).strip(),
                profile = f'Profile {profile}'
                )
            print(user_obj)