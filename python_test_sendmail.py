import smtplib
import ssl

if __name__=='__main__':
    context=ssl.create_default_context()
    SUBJECT='Python test'
    TEXT='TEXT SEND MAIL PYTHON'
    message='Subject:{}\n\n{}'.format(SUBJECT,TEXT)
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo() #kiem tra ket noi
    #server.starttls()
    server.ehlo()
    server.login('nodejs35@gmail.com','An240287@@')
    
    server.sendmail('nodejs35@gmail.com','nguyenangsoft@gmail.com',message)
    server.quit()
    