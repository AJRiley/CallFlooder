from twilio.rest import Client




# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234" 
# for a UK phone it would be +44 remove the first 0. e.g 01344595572 would become +441344595572
TWILIO_PHONE_NUMBER = ["YOUR TWILIO NUMBER"]

# list of one or more phone numbers to dial, in "+19732644210" format
# for UK mobile numbers add +44 and remove the first 0.  e.g 07123123123 would be +447123123123
# this is the same principle for actual phone numbers (landline)
DIAL_NUMBERS = ["YOUR/VICTIMS PHONE NUMBER"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "https://handler.twilio.com/twiml/EH4b418971e2cd05506fd3f99831a9b14c"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = Client("YOUR SID HERE", "YOUR AUTH TOKEN HERE")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")
        


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)
