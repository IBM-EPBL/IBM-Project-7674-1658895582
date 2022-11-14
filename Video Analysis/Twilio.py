from twilio.rest import Client


SID = 'AC153cd036f84d1a7a72baf185e662b651'

Auth_Token = '***************************'

cl = Client(SID, Auth_Token)

cl.messages.create(body="vasanth.mm", from_= '+13605838875',to='+917550155332')
