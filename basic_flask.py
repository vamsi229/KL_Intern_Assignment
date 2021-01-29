from flask import Flask
app=Flask(__name__)
@app.route('/vamsi/<int:POSTid>')
def hello(POSTid):
   return 'hello %d' %POSTid
@app.route('/harika/<name>')
def arna(name):
   return 'this is %s' %name
if __name__=='__main__':
   app.run()