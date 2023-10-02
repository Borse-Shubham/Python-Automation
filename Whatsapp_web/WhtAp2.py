import pywhatkit as kit

# Set the phone number and message you want to send
phone_number = "+919881424021"
message = "Hello, this is an automated message from your Python script!"

# Schedule the message (hour, minute)
kit.sendwhatmsg(phone_number, message, 00, 10)  # Sends the message at 2:30 PM
