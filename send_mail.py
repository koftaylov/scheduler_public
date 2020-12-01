# todo redesign functions for taking mail credentials

def send_mail(message):
    import smtplib, ssl

    # port = 465 #587  # For SSL
    port = 587
    smtp_server = "smtp.gmail.com"
    sender_email = "scheduler.hnkl@gmail.com"  # Enter your address
    receiver_email = "koftaylov@gmail.com"  # Enter receiver address
    password = "password"

    # message = """\
    # Subject: Hi there
   #
   # This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def send_mail_attach(receiver_email,subject,body,filename):
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    #subject = "An email with attachment from Python"
    #body = "This is an email with attachment sent from Python"
    sender_email = "scheduler.hnkl@gmail.com"
    #receiver_email = "scheduler.hnkl@gmail.com"
    password = "password"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    # message["To"] = ["koftaylov@gmail.com"]
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    #filename = "Schedule_2019-09-17-22-48-34 223.xlsx"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


if __name__=='__main__':

    receiver_email = "scheduler.hnkl@gmail.com"
    filename = "Schedule_2019-09-17-22-48-34 223.xlsx"
    subject = "Result schedule"
    body = """
        
        """
    # send_email(message)
    send_mail_attach(receiver_email,subject,body,filename)
