import random
from twilio.rest import Client
password="secure123"
max_attempts=5

account_sid=""
auth_token=""
twilio_number= "+ "
user_phone_number="+"

user_input=""
attempts=0
while user_input!=password and attempts<max_attempts:
    try:
        user_input=input("Enter the password:")
        attempts+=1
        if user_input==password:
            print("Generating otp:")
            otp=str(random.randint(100000,999999))
            try:
                client=Client(account_sid,auth_token)
                message=client.messages.create(
                    body=f"your otp is:{otp}",
                    from_=twilio_number,
                    to=user_phone_number
                )
                print("otp sent.Please check your phone.")
            except Exception as e:
                print(f"failed to send otp:{e}")
                break
            try:
                entered_otp=input("Enter the otp:")
                if entered_otp==otp:
                    print("logged in")
                else:
                    print("incorrect otp.access denied")
                break
            except Exception as e:
                print(f"Error while entering otp {e}")
                break
        elif attempts==max_attempts:
            print("too many failed attempts.you are locked out.")
            break
        else:
            print(f"incorrect password.You have {max_attempts-attempts} left out.")
    except Exception as e:
        print(f"An error occured :{e}")
        break
            
            


