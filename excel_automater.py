import ClointFusion as cf

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


    def get_all_headers_columns(self,header = 0)->list:
        """Function which returns all the headers in the given excel sheet
        Parameters : header = 0 (default arg)
        Returns : list of header column names
        """
        
        return cf.excel_get_all_header_columns(excel_path=self.path,sheet_name = self.name,header=header)

    def get_row_and_column_count(self,header = 0)->tuple[int,int]:
        """Function which returns the row and column count in the given excel document 
        Params : header (=0 default)
        Returns : tuple (row_count , column_count)
        """
        row_count,column_count = cf.excel_get_row_column_count(excel_path = self.path,sheet_name = self.name,header = header)
        return row_count,column_count

    def get_all_sheet_names(self)-> list:
        """Returns the list of all sheet names present in the excel doc
            Params : none 
            returns :list 
        """
        return cf.excel_get_all_sheet_names(excelFilePath= self.path)

    def remove_duplicates(self,column_name:int)->None:
        """Removes the duplicate elements for the specified column name
        Params : Column name 
        Returns : None

        """

        cf.excel_remove_duplicates(excel_path=self.path,sheet_name=self.name, header=0, columnName=column_name, saveResultsInSameExcel=True, which_one_to_keep="first")

    def sort_data_column(self,column_name:int)->None:
        """Sorts the data in the specified column name 
        Params : Column name
        returns : None 
        {Over simplified version of cf.excel_sort_columns.}
        """
        cf.excel_sort_columns(excel_path=self.path,sheet_name=self.name, header=0, firstColumnToBeSorted=column_name, firstColumnSortType=int)

    def insert_data(self,dict:dict)->None:
        """Inserts the given data in dictionary format into the excel sheet
            Params : Information dict
            Returns : None"""
        row_count,_ = cf.excel_get_row_column_count(excel_path = self.path,sheet_name = self.name,header = 0)

        for key in dict:
            cf.excel_set_single_cell(excel_path = self.path, sheet_name = self.name,header = 0,columnName = str(key),cellNumber = row_count-1,setText = str(dict[key]))

    def split_sheet_at_row(self,row_number:int)->None:
        """Splits the sheet at the given row number into separate documents 
        Params :Row number at which the excel sheet is to be split 
        Returns : None"""
        cf.excel_split_the_file_on_row_count(excel_path=self.path, sheet_name = self.name, rowSplitLimit=row_number, outputTemplateFileName ="Split")

    def get_data(self,key_header:str,value_header:str)->dict[str,str]:
        """Function to retrieve information from an excel sheet in the form of a dictionary 
        Params : key_header:  Name of the key_column to be retrived 
                 value_header : Name of the value_column to be retrived
        Returns : dictionary[key_header_values:value_header_values]"""
        data_dict = dict()
        row_count,_ = cf.excel_get_row_column_count(excel_path = self.path,sheet_name = self.name,header = 0)
        for i in range(row_count-1):
            data_dict[cf.excel_get_single_cell(excel_path=self.path,sheet_name=self.name,header=0, columnName=key_header,cellNumber=i)] = cf.excel_get_single_cell(excel_path=self.path,sheet_name=self.name,header=0, columnName=value_header,cellNumber=i)
        
        return data_dict



#example of the working of the class. 
Sheet = ExcelSheet(r'path','name','Sheet_name',r'sourcepath')

print("The headers in the excel sheet are")
header_list  = Sheet.get_all_headers_columns()

for header in header_list:
    print(header)

print(f"The row and column count are {Sheet.get_row_and_column_count()[0],Sheet.get_row_and_column_count()[1]} respectively")

print("All the sheet names in the excel sheet are :")
print(Sheet.get_all_sheet_names())

Sheet.remove_duplicates('ID ')
print("Removed duplicated with respect to ID...")
Sheet.sort_data_column('OrderDate')
print("Sorted column according to OrderDate...")


print("The following data was retrived from the excel sheet : ")
print(Sheet.get_data('ID ','Units'))

Sheet.insert_data({'ID ': 1027,
'OrderDate': '4/14/2020',
'Region': 'Easast',
'Rep': 'Jones',
'Item': 'Binder',
'Units': 60,
'UnitCost': 4.99,
'Total': 449.1
}
)
print("Inserted the given dict into the excel sheet")
Sheet.split_sheet_at_row(12)
print("Done splitting the sheet")

print("Program task Completed")
