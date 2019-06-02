import smtplib

gmail_user = '@gmail.com'  
gmail_password = ''


sent_from = gmail_user  
to = 'amirhosein.simoorgh@gmail.com'
subject = 'OMG Super Important Message'  
body = 'Test mail for SMTP '

email_text = " this is just for test"

try:  
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print ('Email sent!')
except:  
    print ('Something went wrong...')
