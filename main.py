import time

def send_SMTP(String):
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # Next logon th server
    server.login("mohammad.a.attar","Clausema3loz0197")
    # Send the mail
    msg = "Hello!"
    # Send email
    server.sendmail("Mohammad.A.Attar@gmail.com","ali.attar96@gmail.com", msg)

for _ in range(3):
    # The following is a command used to send the message three times
    send_SMTP("msg")
    # This is t0 wait 10 seconds before sending the next letter
    time.sleep(10)