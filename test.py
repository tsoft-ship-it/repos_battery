import psutil 

import smtplib 

from email.mime.text import MIMEText 

  

# Function to check battery level 

def check_battery(): 

    battery = psutil.sensors_battery() 

    percent = battery.percent 

    return percent 

  

# Function to send email alert 

def send_email(): 

    sender_email = "rtr.anjali9819@gmail.com" 

    receiver_email = "anjaliprasad1823@gmail.com" 

    aws_smtp_server = "email-smtp.ap-southeast-2.amazonaws.com" 

    aws_smtp_port = 587 

    aws_smtp_username = "ses-smtp-user.20250517-171631" 

    aws_smtp_password = "BP/vP0wGSCHs6g5RBDMTwKn/4pxlGFSAQbx+tKJjbddF" 

  

    subject = "Laptop Battery Low Warning!" 

    message = f"Warning: Your laptop battery is at {check_battery()}%. Please charge it soon!" 

  

    msg = MIMEText(message) 

    msg["Subject"] = subject 

    msg["From"] = sender_email 

    msg["To"] = receiver_email 

  

    try: 

        server = smtplib.SMTP(aws_smtp_server, aws_smtp_port) 

        server.starttls() 

        server.login(aws_smtp_username, aws_smtp_password) 

        server.sendmail(sender_email, receiver_email, msg.as_string()) 

        server.quit() 

        print("Email alert sent successfully!") 

    except Exception as e: 

        print(f"Error sending email: {e}") 

  

# Run monitoring 

battery_percentage = check_battery() 

if battery_percentage <= 20: 

    send_email() 

else: 

    print(f"Battery Level: {battery_percentage}%, no action needed.") 
