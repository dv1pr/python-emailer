import smtplib

email = "USERS EMAIL"
first_name = "USERS FIRST NAME"
msg = "HTML/TEXT MESSAGE"


def send_email(subject, message):
    from smtplib import SMTP_SSL as SMTP
    from email.mime.text import MIMEText

    sender = 'FROM_EMAIL'
    destination = ['TO_EMAIL', email] #send to 2 emails
    password = 'PASSWORD_FOR_FROM_EMAIL_ACCOUNT'
    SMTPserver = 'smtpout.secureserver.net:465'

    try:
        msg = MIMEText(message, 'html')
        msg['Subject']= subject
        msg['From']   = sender

        conn = SMTP(SMTPserver)
        conn.set_debuglevel(False)
        conn.login(sender, password)
        try:
            conn.sendmail(sender, destination, msg.as_string())
            print("Mail sent to %s" % (destination))
        finally:
            conn.quit()

    except Exception as exc:
        print( "mail failed; %s" % str(exc) )

send_email("Update Credentials", msg)
