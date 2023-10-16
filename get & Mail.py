import requests
# BeautifulSoup used to pull data from website
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, os
#News website url
url="https://indianexpress.com/section/india/"

#GET TOP 5 NEWS HEADING FROM INDIAN EXPRESS
def heading():
  response= requests.get(url)
  html=response.text
  soup=BeautifulSoup(html,'html.parser')
  find=soup.find_all('h2',{'class':'title'})
  return find

content=''
x=1
find=heading()
for heading in find:
  title=heading.text
  if 6>x:
    ans=f"{x}. {title}\n\n"
    content+= ans
    x+=1

#MAKE MAIL TO USER

def sendMail():
  global content
  mail_id=  os.environ['uname']
  password=  os.environ['PASSWORD'] # Search 'app password' in google account & create app and get password
  txt=content
  host='smtp.gmail.com'
  port=968
  s=smtplib.SMTP(host=host, port=port)
  s.starttls()
  s.login(mail_id,password)

  
  msg=MIMEMultipart()
  msg['To']='rsnsram7@gmail.com'
  msg['From']= mail_id
  msg['Subject']='Top 5 News From Indian Express'
  msg.attach(MIMEText(txt, 'html'))

  s.send_message(msg)
  del msg
  
sendMail()
print('DONE')

