from flask import Flask,render_template,request
import sqlite3 as sql
import model
app=Flask(__name__)
model.create()

@app.route('/') #our main page has a signup form and a link to signin form
def main():
	return render_template('index.html')

@app.route('/signup',methods=['POST','GET'])
def adduser():
	msg,error=model.addUser(request)
	print error
	return render_template('signupfailed.html',message=msg)

@app.route('/signin')
def signin():
	return render_template('signin.html')


if __name__ == '__main__' :
	app.debug=True
	app.run(threaded=True)
