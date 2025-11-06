import smtplib
from email.mime.text import MIMEText

sender_email = ""
app_password = "" 
receiver_email = "ddimitrov@elsys-bg.org"

body = f"Открий нови възможности днес. Време е да направиш следващата крачка – ние ще ти помогнем да я осъществиш с намаления до 50%."

message = MIMEText(body)
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Zadacha"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login(sender_email, app_password)
    server.send_message(message)
    
print("Email sent successfully!")