from flask import Flask, request, redirect
import twilio.twiml
app = Flask(__name__)


@app.route('/',methods = ['GET','POST'])
def root():
	resp = twilio.twiml.Response()
	evaluated = None
	try:
		evaluated = eval(str(request.form.get('Body')))
	except:
		exec(str(request.form.get('Body')))
	if evaluated:
		resp.message(">> " + str(evaluated))
	else:
		resp.message(">> Your statement has been interpreted correctly.")
	return str(resp)
if __name__ == '__main__':
    app.run(debug = True)