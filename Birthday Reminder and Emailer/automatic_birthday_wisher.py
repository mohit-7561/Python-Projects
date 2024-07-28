import pandas as pd
import datetime
import smtplib #smtplib, you can use its functions to send email programmatically from your Python scripts.

Gmail_id = "myntrasinghania@gmail.com"
Gmail_pass = "myat grjj xuee khyr" 

def sendEmail(to, sub, msg):
    print(f"Email sent to {to} with the subject:{sub} and Message is: {msg}")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    #port = 587  # Port number for your SMTP server (587 for TLS, 465 for SSL)
    server.starttls() # Start a secure connection
    server.login(Gmail_id, Gmail_pass)
    server.sendmail(Gmail_id, to, f"Subject: {sub}\n\n{msg}")
    server.quit()

if __name__=="__main__":
    df = pd.read_excel("data.xlsx") #pd.read_excel() function is used to read the data of excel
    
    today = datetime.datetime.now().strftime("%d-%m")
    YearNow = datetime.datetime.now().strftime("%Y")
    indexData = []
    for index, item in df.iterrows(): #function is used to give the index and items of the dataframe
        bday = item["Birthday"].strftime("%d-%m")
        # print(bday)
        if (today == bday) and YearNow not in str(item["Year"]):
            sendEmail(item["Email"], "Happy Birthday", item["Dialogue"])
            indexData.append(index)
            
            
    # print(indexData)
    for i in indexData:
        yr = df.loc[i, "Year"] #df.loc[row_label, column_label] function is used to  select 
        #rows and columns from a DataFrame using labels or boolean arrays. It allows you 
        # to select data based on the labels of the rows and columns rather than using numeric indices.
        # print(yr)
        df.loc[i, "Year"] = str(yr) + "," + str(YearNow)
        # print(df.loc[i, "Year"])
    # print(df)
    df.to_excel("data.xlsx", index = False)