#q1
'''
Access tokens are the thing that applications use to make API requests on behalf of a user.
The access token represents the authorization of a specific application to access specific parts of a user’s data.
Access tokens must be kept confidential in transit and in storage.
The only parties that should ever see the access token are the application itself, the authorization server, and resource server.

ACCESS TOKEN FOR TWITTER:
Access_Token="1009300331086266368-ceaBZy9YLbC49pAZen30jZ9piFNJV3"
Access_Token_Secret	="Pf8u6iuEiEfIZ7eZ8lSvLLR2PdGNp1SuCOOUpzYOsi7Yw"


#q2
IP Address of google is =	216.58.217.132
IP Address of facebook is =  216.58.217.132

#q3

in key
Consumer_Key="qxpLZYtoMPCkmKYWXUw50SbBa"
Consumer_Secret="8GGYdKUCNUliuAF81mmqKZ2FNIBPWfdixPfYd81F0XKSg1PeZP"
Access_Token="1009300331086266368-ceaBZy9YLbC49pAZen30jZ9piFNJV3"
Access_Token_Secret	="Pf8u6iuEiEfIZ7eZ8lSvLLR2PdGNp1SuCOOUpzYOsi7Yw"
'''
from key import Consumer_Key,Consumer_Secret,Access_Token,Access_Token_Secret
import tweepy

oauth=tweepy.OAuthHandler(Consumer_Key,Consumer_Secret)
oauth.set_access_token(Access_Token,Access_Token_Secret)
api = tweepy.API(oauth)
print(api.search("#modi"))

'''
#q4
A library is a collection of functions / objects that serves one particular purpose.
you could use a library in a variety of projects. (Various specialized services in our case)
An API is an interface for other programs to interact with your program or library  without having direct access.
( giving specifications for our need to various vendors in our case)
API is a part of library which defines how an application communicates with external code.
API can be written in any language.
Library is written in same language which is a collection of all the functionalities required for the use case.
For example : Numpy is a library of Python, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.
We can create our own APIs using Python Framework like Django and Flask which can be used in websites.

'''
#q5
import sendgrid
import os
from sendgrid.helpers.mail import *

sg = sendgrid.SendGridAPIClient(apikey="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")
from_email = Email("richasood120@gmail.com")
to_email = Email("surbhirajpal88@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)