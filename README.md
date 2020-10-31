# MVP - Mail Via Python
**A cross-platform Python based utility to send automated emails for personal use**


## Requirements
1. Email account with Unrestricted access to send Emails
2. Device to run a Python Script 
3. [Optional] Device with Administrator Previlege to run the script securely.
4. Basic understanding of Python Syntax ( Just enough to comment a line !!)

## Download & Installation
- ` git clone https://github.com/octobersecond/MVP.git `
- That's it !! You're ready to go.
***
## Email Setup
We are using Gmail as the mailing service, You are free to choose other services as well.
### - For Gmail users
1. Head over to https://myaccount.google.com 
2. Under ' **Security** ' > ' **2-Step Verification** '. Activate 2-Step Verification.
3. Next up - Go to https://myaccount.google.com/lesssecureapps and toggle the switch to **ON** to allow Python to send Emails.
4. Now - Go to https://myaccount.google.com/apppasswords . Click on ' **Select App** ' and choose ' **Other (Custom Name)** ' and type ' MVP ' or name of your choice and Click on ' **Generate** '. This will generate an ' **App Password** ', Copy it to a Secure place.

### - For Other Mail services
Contribute to this section by a Pull request.
***
## Local Environment Setup [ *optional* ]
It is entirely optional but Secures the whole process of sending emails and working on the script by Hiding the Credentials as Environment Variables. Read the Note below.
- Create two Variables - `EMAIL_USER` & `EMAIL_PASS`
- Assign your Email Address to `EMAIL_USER` | EMAIL_USER='username@gmail.com'
- Assign the Generated Password to `EMAIL_PASS` | EMAIL_PASS="nfdjkdcbssbjs"

Note: This Process differs greatly from OS to OS and even within Distros. Hence do some Googling on `How to setup Environment variables in [Your Operating System / Distro]` and proceed further.
***
## Project Environment Setup
The Cloned / Downloaded directory contains `init.py`, which is the script to start sending emails, but still we have got lot of things to do..\
The folder also contains `resources/` directory, which inturn contains `index.html` `mailing_list.txt` & `message.txt`

- `mailing_list.txt` should be written with Email addresses of the recievers
- `message.txt` should be written with the body of the message
- `index.html` In case if you are upto sending HTML Messages / Pages

### Customisations inside script
- The script is intended for secure use, hence the script contains
```pyhton3
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')
```
If you haven't followed the section on `Local Environment Setup` change that code to
```python3
EMAIL_ADDRESS = "username@gmail.com"
EMAIL_PASSWORD = "generatedpassword"
```
- The Python script can send Text message & HTML message. By default it is set to send both, If you are about to send only one of them then comment the other one out. i.e, By typing # before every line shown below. 
- `for Text Message` 
```python3
with open('resources/message.txt','rb') as t:
    message_body = t.read()
    message = message_body.decode(encoding='UTF-8')
```
```python3
msg.set_content(message)
```
- `for HTML Message`
```python3
with open('resources/index.html','rb') as f:
   file_data = f.read()
   file_string = file_data.decode(encoding='UTF-8')
```
```python3
msg.add_alternative(file_string, subtype='html')
```
***
## Usage 

```bash
python3 init.py
```
or
```bash
python init.py
```
Congragulations!! You have run the script successfully. There will be errors of course, try to analyse them and create a pull request to add common errors and their solutions to this page.\
***

### Special thanks to Corey Schafer ❤️
- **Youtube** Video : [How to Send Emails Using Python - Plain Text, Adding Attachments, HTML Emails, and More](https://www.youtube.com/watch?v=JRCJ6RtE3xU)
- Recommended **Youtube** Playlist : [Python Tutorial for Beginners - Corey Schaffer](https://www.youtube.com/watch?v=YYXdXT2l-Gg)






 


