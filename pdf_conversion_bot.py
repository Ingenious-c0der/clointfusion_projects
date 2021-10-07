import ClointFusion as cf
import clipboard
import time

#getting the path from the user
path = cf.gui_get_any_file_from_user()

#getting the extension of the input file from the user
ext = cf.gui_get_dropdownlist_values_from_user(msgForUser='Select the file extension',dropdown_list=['jpg','doc','png'],multi_select=False)

path1="\\".join(path.split("/"))



#going to respective sites for conversion based on the type of input file
if ext[0]=="doc":
        clipboard.copy(path1)
        cf.browser_activate()
        cf.browser_navigate_h("https://smallpdf.com/word-to-pdf")
        cf.browser_mouse_click_h("CHOOSE FILES")
        time.sleep(1)
        cf.key_write_enter(path1)
        cf.browser_wait_until_h("PREVIEW")
        time.sleep(1)
        cf.browser_mouse_click_h("Download")
      


elif ext[0]=="png":
        clipboard.copy(path1)
        cf.browser_activate()
        cf.browser_navigate_h("https://png2pdf.com/")
        cf.browser_mouse_click_h("UPLOAD FILES")
        time.sleep(1)
        cf.key_write_enter(path1)
        cf.browser_wait_until_h("DOWNLOAD")
        time.sleep(1)
        cf.browser_mouse_click_h("DOWNLOAD")

elif ext[0]=="jpg":
        clipboard.copy(path1)
        cf.browser_activate()
        cf.browser_navigate_h("https://smallpdf.com/jpg-to-pdf")
        cf.browser_mouse_click_h("CHOOSE FILES")
        time.sleep(1)
        cf.key_write_enter(path1)
        cf.browser_wait_until_h("CONVERT")
        cf.browser_mouse_click_h("CONVERT")
        cf.browser_wait_until_h("PREVIEW")
        cf.browser_mouse_click_h("DOWNLOAD")

