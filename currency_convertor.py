import ClointFusion as cf
import helium
import locale
import time
import os 
locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 

#scraping info on the given website to notepad
cf.browser_activate("link")
path = os.path.join(os.getcwd(),"generated_files")
cf.scrape_save_contents_to_notepad(folderPathToSaveTheNotepad=path)
cf.browser_quit_h()


class WebScrape:
    
    def get_converted_value(value_list:list[list[str,str,int]])->list[int]:
        """Get the converted values for passed required conversions in a list
        Args : list containing the conversion details 
        returns conversion values for the given list"""

        cf.browser_activate()
        this_list = []
        for val_list in value_list:
            helium.go_to(f"https://www.xe.com/currencyconverter/convert/?Amount={val_list[2]}&From={val_list[0]}&To={val_list[1]}")
            value = cf.browser_locate_element_h(selector=r"//*[@id='__next']/div[2]/div[2]/section/div[2]/div/main/form/div[2]/div[1]/p[2]",get_text = True)
            this_list.append(round(locale.atof(value.split()[0]),3))
        cf.browser_quit_h()
        return this_list
    
    

class ExcelSheet:
   
    def __init__(self,pathtofolder:str,filename:str,sheet_name:str,pathtosourcefolder=None)->None:
        """Initialising function to create an excel doc at the given location (which acts as an object of the class throughout)
            if source folder path is mentioned then it will be copied into the newly created excel document
            Params : pathtofolder : Path where the excel sheet has to be created
                    filename : filename of the excel document
                    sheet_name :Sheet name of the sheet created in excel sheets by default
                    pathtosourcefolder :Path from which the excel sheet is to be copied (None by default)

            Returns : None
                    """
        self.path = cf.os.path.join(pathtofolder, filename)
        self.name = sheet_name
  
        cf.excel_create_excel_file_in_given_folder(fullPathToTheFolder=pathtofolder,excelFileName=filename,sheet_name=sheet_name)
        print(f"New Excel Sheet created at {pathtofolder} with name {self.name}")
        if pathtosourcefolder:
            cf.shutil.copyfile(pathtosourcefolder,self.path)


    def insert_data(self,data_list:list)->None:
        """Inserts the given data in dictionary format into the excel sheet
            Params : data list
            Returns : None"""
        row_count,_ = cf.excel_get_row_column_count(excel_path = self.path,sheet_name = self.name,header = 0)
    
        if row_count==1:
            for i in range(len(data_list)):
                cf.excel_set_single_cell(excel_path = self.path, sheet_name = self.name,header = 0, columnName = "",cellNumber = i,setText = data_list[i])

#opening the notepad in which the content is scraped and filtering that content for the data
with open(path) as file:
    content = file.readlines()
    file.close()
#filtering
filtered_content = [content[i].strip().split() for i in range(len(content)) if i%2==0 and i>2]

#getting the converted values into a list
value_list = WebScrape.get_converted_value(filtered_content)

#merging the converted values
for i in range(len(filtered_content)):
    filtered_content[i].append(value_list[i])
#converting the amount to int
flitered_content =  [int(i[2]) for i in filtered_content]

#excel file generation
filtered_content.insert(0,['From',"To","Amount","Converted"])
excel_path  = os.path.join(path,"Conversions.xlsx")
cf.excel_copy_paste_range_from_to_sheet(excel_path=excel_path, startCol=1, startRow=1, endRow=6, endCol=4, copiedData=filtered_content)


