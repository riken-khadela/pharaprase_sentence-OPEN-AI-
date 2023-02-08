from django.core.management.base import BaseCommand
from tqdm import tqdm
import re
import json
from app.models import Text
from app.utils import SeprateText

# filename = 'data.json'
# with open(filename, 'r', encoding='utf-8') as f:
#     data = f.readlines()
#     # print(data)
# new_data = []
# for line in data:
#     # print(json.loads(line)['text'])
#     new_data.append(json.loads(line)['text'].replace('\n', ' '))
# alphabets = "([A-Za-z])"
# prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
# suffixes = "(Inc|Ltd|Jr|Sr|Co)"
# starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
# acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
# websites = "[.](com|net|org|io|gov)"
# digits = "([0-9])"




# def split_into_sentences(text):
#     text = " " + text + "  "
#     text = text.replace("\n", " ")
#     text = re.sub(prefixes, "\\1<prd>", text)
#     text = re.sub(websites, "<prd>\\1", text)
#     text = re.sub(digits + "[.]" + digits, "\\1<prd>\\2", text)
#     if "..." in text:
#         text = text.replace("...", "<prd><prd><prd>")
#     if "Ph.D" in text:
#         text = text.replace("Ph.D.", "Ph<prd>D<prd>")
#     text = re.sub("\s" + alphabets + "[.] ", " \\1<prd> ", text)
#     text = re.sub(acronyms+" "+starters, "\\1<stop> \\2", text)
#     text = re.sub(alphabets + "[.]" + alphabets + "[.]" +
#                   alphabets + "[.]", "\\1<prd>\\2<prd>\\3<prd>", text)
#     text = re.sub(alphabets + "[.]" + alphabets +
#                   "[.]", "\\1<prd>\\2<prd>", text)
#     text = re.sub(" "+suffixes+"[.] "+starters, " \\1<stop> \\2", text)
#     text = re.sub(" "+suffixes+"[.]", " \\1<prd>", text)
#     text = re.sub(" " + alphabets + "[.]", " \\1<prd>", text)
#     if "”" in text:
#         text = text.replace(".”", "”.")
#     if "\"" in text:
#         text = text.replace(".\"", "\".")
#     if "!" in text:
#         text = text.replace("!\"", "\"!")
#     if "?" in text:
#         text = text.replace("?\"", "\"?")
#     text = text.replace(".", ".<stop>")
#     text = text.replace("?", "?<stop>")
#     text = text.replace("!", "!<stop>")
#     text = text.replace("<prd>", ".")
#     sentences = text.split("<stop>")
#     sentences = sentences[:-1]
#     sentences = [s.strip() for s in sentences]
#     return sentences




class Command(BaseCommand):
    help = '''to add accounts in database and profile directory
            add accounts in 
            '''
    
    def handle(self, *args, **option):

        SeprateText()
        
        # max_len = 0
        # max_word = ''
        # ind = 0
        # for sentences in tqdm(new_data):
        #     for sentence in split_into_sentences(sentences):
        #         ind += 1
        #         # print(len(sentence))
        #         # if ind < 55000 :                     
        #         #     continue
                
        #         # if len(sentence) > 500:
        #         #     print(".......")
        #         #     continue
        #         print(sentence)
        #         matches = re.findall(
        #             r'(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])', sentence)
        #         print(matches,"mmmm")
        #         # if len(matches) > 0:
        #         #     continue
        #         # if len(sentence) < 10:
        #         #     continue    
                
        #         print("--->",sentence)
                
        #         aa=Text.objects.create(
        #             text = sentence
        #         )
        #         print(aa)
        #         # print(text)
        #         # session.add(Original(sentence=sentence, text_number=ind))
        #     # break
        
    