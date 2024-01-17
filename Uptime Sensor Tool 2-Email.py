import ping3
import time
import smtplib

# Function to send an email notification
def send_notification(sender_email, sender_password, receiver_email, subject, message):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            email_message = f"Subject: {subject}\n\n{message}"
            server.sendmail(sender_email, receiver_email, email_message)
            print("Email notification sent successfully!")
    except Exception as e:
        print("Error sending email notification:", str(e))

# Function to check and send notifications for host status changes
def check_and_notify_status(destination_ip, sender_email, sender_password, receiver_email):
    prev_status = None

    while True:
        response = ping3.ping(destination_ip, timeout=1, unit="s")
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        if response is not None:
            status = "up"
        else:
            status = "down"

        if prev_status is not None and prev_status != status:
            subject = f"Host Status Changed: {destination_ip}"
            message = f"Host status changed from {prev_status} to {status} at {timestamp}"
            send_notification(sender_email, sender_password, receiver_email, subject, message)

        prev_status = status

        print(f"{timestamp} Host is {status} to {destination_ip}")
        time.sleep(2)

# Ask the user for email credentials
sender_email = input("Enter your email address: ")
sender_password = input("Enter your email password: ")
receiver_email = input("Enter the administrator's email address: ")

# Replace 'destination_ip' with the IP you want to monitor
destination_ip = '8.8.8.8'
check_and_notify_status(destination_ip, sender_email, sender_password, receiver_email)