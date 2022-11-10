import os
from flask import Flask, request

app = Flask(__name__) #create an instance of the Flask library

@app.route('/') #whenever this webserver is called with <hostname:port>/hello then this section is called
def hello(): #The subroutine name that handles the call
	output = 'Hello World'
	return output #Whatever is returned from this subroutine is what is returned to the requester and is shown on the browser page

if __name__ == '__main__':
	# port = int(os.environ.get('PORT', 8000)) #The port to be listening to — hence, the URL must be <hostname>:<port>/ inorder to send the request to this program
	app.run(host='127.0.0.1',port=8000,debug=True)  #Start listening