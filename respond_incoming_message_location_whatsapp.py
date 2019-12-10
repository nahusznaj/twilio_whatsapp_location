from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()
    
    #when sharing location with Whatsapp, latitude (and longitude) will always be present. While Address may not be. That's why the distinction.
    
    if "Address" in request.values and "Latitude" in request.values:
        latitude = request.values.get('Latitude', None) 
        address = request.values.get('Address', None) 
        resp.message("The Robots are coming! Head for the hills!, your location is " + latitude + " and address is " + address)
        
    elif "Latitude" in request.values:
        latitude = request.values.get('Latitude', None) 
        resp.message("The Robots are coming! Head for the hills!, your location is " + latitude + " and no address!")
    else:
        resp.message("The Robots are coming! Head for the hills! You didn't send any address or latiture")

    return str(resp)



if __name__ == "__main__":
    app.run(debug=True)
