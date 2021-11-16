import win32com.client
from loguru import logger
import os
logger.add("logs/task5.log", rotation="1 day",backtrace=True)
class easyExcel:
    """A utility to make it easier to get at Excel. Remembering
    to save the data is your problem, as is error handling.
    Operates on one workbook at a time."""

    def __init__(self, filename=None,path = None):
        try:
            self.xlApp = win32com.client.Dispatch('Excel.Application')
            if filename and path:
                logger.debug("Opening file {}".format(filename))
                self.filename = filename
                self.xlBook = self.xlApp.Workbooks.Open(path)
            else:
                logger.debug("Creating new file at {}".format(os.getcwd()))
                self.xlBook = self.xlApp.Workbooks.Add()
                self.filename = ''
        except:
            logger.error("Failed to create excel object")
            raise 

    def save(self, newfilename=None):
        """Saving the generated file object"""
        try:
            if newfilename:
            
                self.filename = newfilename
                self.xlBook.SaveAs(os.path.join(os.getcwd(),newfilename))
                logger.debug("Saved file {0} at {1}".format(newfilename,os.getcwd()))
                self.close()
            else:
                self.xlBook.Save()
                self.close()
        except:
            logger.error("Failed to save file")
            raise

    def close(self):
        """Closing the excel file object"""
        try:
            filename = self.filename
            self.xlBook.Close(SaveChanges=0)
            del self.xlApp
            logger.debug("Closed file {0} at {1}".format(filename,os.getcwd()))
        except:
            logger.error("Failed to close file")
            raise

    def copy_paste(self,sheet_name1,other_workbook,other_sheetname):
        """Copying Pasting one file from another"""
        #highly custom copy paste for now , can be generalised easily using parameters like row col etc
        try:
            other_workbook.xlBook.Sheets(other_sheetname).Range("a2:b44").Copy()
            self.xlBook.Sheets(sheet_name1).Range("A2").PasteSpecial()
            other_workbook.xlBook.Sheets(other_sheetname).Range("d2:g44").Copy()
            self.xlBook.Sheets(sheet_name1).Range("C2").PasteSpecial()
            logger.debug("Copied and pasted data from {0} to {1}".format(other_sheetname,sheet_name1))
        except:
            logger.error("Failed to copy and paste data")
            raise

    def resize_column(self,sheetname,col_num,width):
        """Resizing a particular column """
        try:
            logger.debug("Resizing column {} of sheet {} to {}".format(col_num,sheetname,width))
            self.xlBook.Worksheets(sheetname).Columns(col_num).ColumnWidth = width
        except:
            logger.error("Failed to resize column")
            raise

def fail_function(stage:str):
    #emailing developer team and client the error logs

    logger.error("Failed at stage : {}".format(stage))
   
    olApp = win32com.client.Dispatch("Outlook.Application")
    olNS = olApp.GetNamespace("MAPI")
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = "The bot ran into an error during runtime!"
    mailItem.BodyFormat = 1
    mailItem.Body = f"Please find the error logs.\nThe bot failed at {stage}.\nThe error will be solved and reverted in 24 hours.\nRegards"
    mailItem.Attachments.Add(os.path.join(os.getcwd(),r'logs\task5.log'))
    mailItem._oleobj_.Invoke(*(64209,0,8,0,olNS.Accounts.Item('mail')))
    mailItem.To = "mail"
    
    mailItem.Save()
    mailItem.Send()
    logger.debug("Sent email to developer team , program exited with status 1.")
    
    raise


if __name__ == "__main__":
    #making the required excel file
    try:
        template_file = easyExcel('Template.xlsx',os.path.join(os.getcwd(),'Template.xlsx'))
        rawdata_file = easyExcel('RAWDATA.xls',os.path.join(os.getcwd(),'RAWDATA.xls'))
        template_file.copy_paste('Sheet1',rawdata_file,'SalesOrders')
        template_file.resize_column('Sheet1',6,12)
        template_file.save('task5.xlsx')
        rawdata_file.close()
        logger.debug("Successfully created required file")
    except:
        template_file.close()
        rawdata_file.close()
        fail_function("Creating required file")

    
    #mailing it using vba python
    try:
        logger.debug("Sending email")
        olApp = win32com.client.Dispatch("Outlook.Application")
        olNS = olApp.GetNamespace("MAPI")
        mailItem = olApp.CreateItem(0)
        mailItem.Subject = "subject"
        mailItem.BodyFormat = 1
        mailItem.Body = "body"
        mailItem.Attachments.Add(os.path.join(os.getcwd(),'task5.xlsx'))
        mailItem.To = "mail"
        mailItem._oleobj_.Invoke(*(64209,0,8,0,olNS.Accounts.Item('mail')))
        mailItem.Save()
        mailItem.Send()
        logger.debug("Successfully sent email")
    except:
        fail_function("Sending email")

    
    



