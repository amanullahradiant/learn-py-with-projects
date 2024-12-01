import smtplib as smtp

to = input("enter recipient email address: \n")
content = input("write your message: \n")


def sendMail(to, contnt):
    server = smtp.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(
        'senderemail@gmail.com',
        '1234')  # make sure you enabled less secure apps in your gmail account
    server.sendmail('senderemail@gmail.com', to, content)
    server.close()


sendMail(to, content)
