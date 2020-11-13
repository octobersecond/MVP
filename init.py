import os
import smtplib
import tqdm
import time
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

contacts = []
mail_count = 0
    
# open file and read the contacts mailing address and append them as items to a list.
with open('resources/mailing_list.txt', 'r') as filehandle:
    for line in filehandle:
        currentMail = line[:-1]
        contacts.append(currentMail)
# open external html files and write to a local variable
with open('resources/index.html','rb') as f:
   file_data = f.read()
   file_string = file_data.decode(encoding='UTF-8')
   f.close()
# open external message file, decode it and store it to a variable
with open('resources/message.txt','rb') as f:
    message_body = f.read()
    message = message_body.decode(encoding='UTF-8')
    f.close()

def mail_final():
    i = mail_count
    msg = EmailMessage()
    msg['Subject'] = 'Test Message'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts[i]
    msg.set_content(message)
    #msg.add_alternative(file_string, subtype='html')
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) 
        #smtp.send_message(msg)
        tqdm.tqdm.write("[" + str(i) + "] " + contacts[i] )

for one in tqdm.trange(len(contacts), desc ="Progress "):
    mail_final()
    mail_count += 1
    time.sleep(0.1)
        




