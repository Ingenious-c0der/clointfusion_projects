from google_sheets import GoogleSheets
from social_media_apps import Instagram, Twitter, Facebook
import os
from dotenv import load_dotenv, find_dotenv
from loguru import logger

load_dotenv(os.path.join(os.getcwd(),"secret.env"))
def poster(gsheet_data):
    facebook_list = []
    twitter_list = []
    instagram_list = []

    for data in gsheet_data:
        caption = data['Post Message']
        image_link = data["Image Link (should be small)"]
        image_path = data["local Image path (works only for instagram right now)"]
        if data["Facebook"]=="Yes":	
            facebook_list.append((caption,image_link))
        if data["Twitter"]=="Yes":
            twitter_list.append((caption,image_link))
        if data["Instagram"]=="Yes":
            instagram_list.append((caption,image_path,image_link))
        
    fb = Facebook(os.getenv("FACEBOOK_EMAIL_ID"),os.getenv("FACEBOOK_PASSWORD"))
    fb.login()

    for post in facebook_list:
        fb.upload(post[0],"",post[1])
    fb.close()
    
    tw = Twitter(os.getenv("TWITTER_USERNAME"),os.getenv("TWITTER_EMAIL_ID"),os.getenv("TWITTER_PASSWORD"))
    tw.login()
    for post in twitter_list:
        tw.post(post[0],post[1])
    tw.close()

    ig = Instagram(os.getenv("INSTAGRAM_USERNAME"),os.getenv("INSTAGRAM_PASSWORD"))
    for post in instagram_list:
        ig.upload_content(post[1],post[0],post[2])
    



        



g_sheet = GoogleSheets("social_media_posting","Sheet1",r"social-media-posting-bot-91104e5a13bd.json")
poster(g_sheet.get_sheet_data())
