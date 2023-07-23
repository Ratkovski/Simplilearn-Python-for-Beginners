import smtplib

smtObj = smtplib.SMTP('smtp.gmail.com', 587)
smtObj.ehlo()
smtObj.starttls()
smtObj.login('email', 'password')
smtObj.send("email", "email2", 'Subject: SMTP check. \n This is a test email')
smtObj.quit()