import pywhatkit as kit
import time

# Get phone number and message from user input
phone_number = input("Enter the phone number (with country code, e.g., +1234567890): ")
message = input("Enter the message you want to send: ")

while True:
    # Get current time
    current_hour = int(time.strftime("%H"))
    current_minute = int(time.strftime("%M"))
    
    # Calculate the next minute and handle rollover
    next_hour = current_hour
    next_minute = current_minute + 1
    if next_minute == 60:
        next_hour += 1
        next_minute = 0
        if next_hour == 24:
            next_hour = 0
    
    # Send the message
    kit.sendwhatmsg(phone_number, message, next_hour, next_minute)
    
    # Wait for 10 seconds before sending the next message
    time.sleep(10)

