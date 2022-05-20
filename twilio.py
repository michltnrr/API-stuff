from twilio.rest import Client 

account_sid = ' '
auth_token = ' '
client = Client(account_sid, auh_token)

for msg in client.messages.list():
    print(msg.body)

msg = client.messages.create(
    to='+13880028936',
    from_= '+17406886695',
    body='Waddup jit, twilio message sent from python boi!',
)

