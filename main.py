from flask import Flask
from twilio.rest import TwiloRestClient
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def root():

if __name__ == '__main__':
    app.run(debug = True)