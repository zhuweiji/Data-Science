import smtplib


sender = "wzhu002@e.ntu.edu.sg" #"pigoichicken@gmail.com"
pingword = "1012973312wG" #'1012978179tT'
recipient = ""
subject = ""
body = ""


def get_user_input():
    recipient = input("Sending message to:")
    subject = input("Subject:")
    body = input("Body:")
    return recipient, subject, body


smtpObj = smtplib.SMTP('smtp-mail.outlook.com', 587)
smtpObj.ehlo()  # initiate server connection
smtpObj.starttls()  # initiate TTLS encryption

try:
    smtpObj.login(sender, pingword)
except smtplib.SMTPException as error:
    print('Program failed, login error \nError code:{}'.format(error))
    exit(-1)

if not recipient or not subject or not body:
    print("Empty fields in email, enter email here:")
    recipient, subject, body = get_user_input()

try:
    smtpObj.sendmail(sender, recipient, "{0} \n {1}".format(subject, body))
    print("Email sent! \nClosing Program")
    smtpObj.quit()
except smtplib.SMTPException as error:
    print("Email not sent:\nError code:{}".format(error))
    smtpObj.quit()
    exit(-1)



