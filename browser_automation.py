import ClointFusion as cf 
import pyautogui as pg
import time


class Browser:
    def __init__(self,browser_name:str,initial_site:str = "")->None:
        """Opens up the browser with the given name and the initial site if the name is provided and acts as the constructor.
        Args : browser name 
               initial site
        Returns : None"""
        cf.launch_any_exe_bat_application(browser_name)

        cf.key_write_enter(text_to_write=initial_site, write_to_window="New Tab - Google Chrome", delay_after_typing=1,key="e")
    
    def get_user_info()->tuple[str,str]:
        """Function to get the user details like password and mobile number using clointfusion gui
        Args: None
        Returns : Tuple containing mobile_no and password of the user"""
        mobile_no = cf.gui_get_any_input_from_user("Enter your mobile number ")
        password = cf.gui_get_any_input_from_user("Enter your password")
        return (mobile_no,password)
       

    def click_on_image(self,imagepath:str,no_of_clicks:int = 1,confidence:int= 0.8,wait=40)->None:
        """Function which finds the given image on the imagepath on the screen and clicks it
        Args : path of the image
               Number of times the image has to be clicked
               Confidence : The paramter which decides how accurately the image has to be compared with the one on the screen
               1:higest accuracy
               0:lowest accuracy (almost everything matches)
               wait : Time for which the function waits before the given image is found
        Returns : None

        """
        current_time = time_start = time.time()
        # x,y =cf.mouse_search_snip_return_coordinates_x_y(img=imagepath,wait = 30) removed because it did not have a confidence parameter which was needed since the two searchbars although looked same were different i.e the searchbar on homepage and the one on the cart page
        while pg.locateCenterOnScreen(imagepath,confidence=confidence)==None and current_time-time_start<=wait:
                current_time = time.time()
                print(current_time-time_start)
        try:
            x,y = pg.locateCenterOnScreen(imagepath,confidence=confidence)
            cf.mouse_click(x,y,no_of_clicks= no_of_clicks)
        except:
            print("Image not found")

    def enter_info(self,text:str)->None:
        """Function used to enter the details in an active message box/area and press enter inherently
        Args : Text which needs to be entered
        Returns : None
        """
        cf.key_write_enter(text_to_write=text)

    def add_item_to_cart(self,name:str,imagepath:str)->None:
        """Function which adds an item to cart on Flipkart.com
        Args : name :Name of the object/item (should be flipkart searchable for better results)
               iamgepath : Path to the image of the object
        Returns : None"""
        self.click_on_image(r"C:\Users\sagar\Desktop\clointfusion_work\images\searchbar.png")
        
        self.enter_info(name)
        
        self.click_on_image(imagepath)
      
        self.click_on_image(r"C:\Users\sagar\Desktop\clointfusion_work\images\addtocart.png")

    def place_order(self)->None:
        """Function used to hit the place order button on flipkart once all the items have been added. 
        Args : None
        Returns :None"""
        self.click_on_image(r"C:\Users\sagar\Desktop\clointfusion_work\images\placeorder.png")




#example use of the class according to the given problem statement. session is an object of the Browser class.
info = Browser.get_user_info()
session = Browser("Chrome","www.flipkart.com")
time.sleep(1)
session.click_on_image(r"path")
session.enter_info(info[0])
session.click_on_image(r"path")
session.enter_info(info[1])
session.add_item_to_cart(r"boAt Airdopes 131 Bluetooth Headset",r"path")
session.add_item_to_cart(r"boAt Airdopes 402 Bluetooth Headset",r"path")
session.place_order()

time.sleep(6) #doesn't have any use.Just to have the page stall at a point before the chrome tab is closed
#closing chrome browser 
cf.key_press(key_1='alt',key_2='f4')

