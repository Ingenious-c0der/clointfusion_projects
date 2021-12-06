from selenium import webdriver
import time 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from loguru import logger
import keyboard
from instabot import Bot 
import glob
import os


class Facebook:
    """Selenium Driven Facebook Posting"""
    def __init__(self,email_id:str,password:str):
        self.email_id = email_id
        self.password = password
        logger.debug("Initializing Facebook ...")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        logger.debug("Facebook initialized ...")


    def login(self):
        self.driver.get("https://www.facebook.com/login/")
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys(self.email_id)
        self.driver.find_element_by_xpath("//input[@id='pass']").send_keys(self.password)
        self.driver.find_element_by_id("loginbutton").click()
        logger.debug("Logged in to Facebook ...")
        time.sleep(3)
        self.driver.get("https://www.facebook.com/")
        time.sleep(3)
        elements = self.driver.find_elements_by_xpath("//div[@class='bp9cbjyn j83agx80 taijpn5t dfwzkoeu ni8dbmo4 stjgntxs']")
        elements[1].click()
        time.sleep(2)
        logger.debug("Logged in to Facebook ...")


    def upload(self,caption,image_path,image_link):
        logger.debug("Creating your post ...")
        if image_path == "" and image_link == "":
            post_content = self.driver.find_element_by_class_name('notranslate._5rpu')
            post_content = self.driver.switch_to.active_element
            post_content.send_keys(caption)
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class = 'rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq s1i5eluu tv7at329']").click()
            self.driver.close()
            logger.debug("Facebook post created successfully ...")
            time.sleep(2)
        elif image_path != "" and image_link=="":
            post_content = self.driver.find_element_by_class_name('notranslate._5rpu')
            post_content = self.driver.switch_to.active_element
            post_content.send_keys(caption)
            new_elements = self.driver.find_elements_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t buofh1pr tgvbjcpo muag1w35 enqfppq2 taijpn5t']")
            new_elements[0].click()
            time.sleep(1)
            keyboard.write(image_path)
            keyboard.press_and_release('enter')
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class = 'rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq s1i5eluu tv7at329']").click()
            logger.debug("Facebook post created successfully ...")
            time.sleep(2)
         
        elif image_path!="" and image_link!="":
            caption = caption + "\n" + image_link
            post_content = self.driver.find_element_by_class_name('notranslate._5rpu')
            post_content = self.driver.switch_to.active_element
            post_content.send_keys(caption)
            time.sleep(1)
            new_elements = self.driver.find_elements_by_xpath("//div[@class='rq0escxv l9j0dhe7 du4w35lb j83agx80 cbu4d94t buofh1pr tgvbjcpo muag1w35 enqfppq2 taijpn5t']")
            new_elements[0].click()
            time.sleep(1)
            keyboard.write(image_path)
            keyboard.press_and_release('enter')
            time.sleep(1)
            self.driver.find_element_by_xpath("//div[@class = 'rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq s1i5eluu tv7at329']").click()
            logger.debug("Facebook post created successfully ...")
            time.sleep(2)
            
        else:
            caption = caption + "\n" + image_link
            post_content = self.driver.find_element_by_class_name('notranslate._5rpu')
            post_content = self.driver.switch_to.active_element
            post_content.send_keys(caption)
            time.sleep(2)
            self.driver.find_element_by_xpath("//div[@class = 'rq0escxv l9j0dhe7 du4w35lb j83agx80 pfnyh3mw taijpn5t bp9cbjyn owycx6da btwxx1t3 kt9q3ron ak7q8e6j isp2s0ed ri5dt5u2 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 d1544ag0 tw6a2znq s1i5eluu tv7at329']").click()
            logger.debug("Facebook post created successfully ...")
            time.sleep(2)
          

        logger.debug("Posted on Facebook ✓")
    
    def close(self):
        self.driver.close()
        


class Twitter:
    """Selenium driven Twitter post"""
    def __init__(self,username,email_id,password):
        logger.debug("Initializing twitter ...")
        self.username = username
        self.email_id = email_id
        self.password = password
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)

    def login(self):
        self.driver.get("https://twitter.com/login")
        logger.debug("Logging in to twitter ...this takes about 15 seconds")
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']").send_keys(self.email_id)
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']").send_keys(self.username)
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr']").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("//input[@class='r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu']").send_keys(self.password)
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-peo1c r-1ps3wis r-1ny4l3l r-1guathk r-o7ynqc r-6416eg r-lrvibr r-13qz1uu']").click()
        logger.debug("Logged in to twitter")
        time.sleep(2)
    def post(self,caption,image_link):
        logger.debug("Creating the tweet ...")

        self.driver.find_element_by_xpath("//div[@class= 'public-DraftStyleDefault-block public-DraftStyleDefault-ltr']").click()
        self.driver.find_element_by_xpath("//div[@class= 'public-DraftStyleDefault-block public-DraftStyleDefault-ltr']").send_keys(caption+"\n"+image_link)

        self.driver.find_element_by_xpath("//div[@class= 'css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr']").click()
        logger.debug("Posted on twitter ✓")
        time.sleep(2)
    
    def close(self):
        self.driver.close()




class Instagram:
    """Using InstaBot Module."""
    """Class to Upload content to instagram
       methods: upload_content"""
    def __init__(self,username:str,password:str)->None:
      
        cookie_del = glob.glob("config/*cookie.json")
        if cookie_del:
            os.remove(cookie_del[0])

        """Initialize the instagram bot
        Args:
            username: instagram username
            password: instagram password
        Returns:
            None
        Attributes:
            bot: instagram bot
        
        """
        logger.debug("Logging in to instagram ...")
        self.bot = Bot()
        self.bot.login(username=username, password=password)

    def upload_content(self,image_path:str,caption:str,image_link:str="")->None:
        """Upload content to instagram
        Args:
            image_path: path to image
            caption: caption to be added
        
            """
        if image_path:
            self.bot.upload_photo(image_path, caption=caption+"\n"+image_link)
            logger.debug("Posted on instagram ✓")
        else:
            logger.error("Image path is empty")


class LinkedIn:
    def __init__(self,email_id:str,password:str):
        self.email_id = email_id
        self.password = password
        logger.debug("Initializing LinkedIn ...")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--log-level=3")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
        logger.debug("LinkedIn initialized")

    def login(self):
        logger.debug("Logging in to LinkedIn ...")
        self.driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
        time.sleep(2)
        self.driver.find_element_by_id("username").send_keys(self.email_id)
        self.driver.find_element_by_id("password").send_keys(self.password)

        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        try:
            self.driver.find_element_by_xpath("//button[@type='button']").click()
        except:
            pass
        logger.debug("Logged in to LinkedIn")

    def post(self,caption:str,image_link:str):
        logger.debug("Creating the LinkedIn post ...")
        element = self.driver.find_element_by_xpath("//button[@class = 'artdeco-button artdeco-button--muted artdeco-button--4 artdeco-button--tertiary ember-view share-box-feed-entry__trigger']")
        self.driver.execute_script("arguments[0].click();", element)
        
        time.sleep(2)
        self.driver.find_element_by_xpath("//div[@class='ql-editor ql-blank']").send_keys(caption+"\n"+image_link )
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[@class='share-actions__primary-action artdeco-button artdeco-button--2 artdeco-button--primary ember-view']").click()

        logger.debug("Posted on LinkedIn ✓")
        time.sleep(1)


    def close(self):
        self.driver.close()

        


