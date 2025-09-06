from flask import Flask
'''
It creates the  instance of the  Flask Class
which will be used as wsgi applicaions

'''
### WSGI Application 
app=Flask(__name__)


@app.route("/")
def welcome():
    return "zWelcome to y webpage . This should be an amazing "


@app.route("/index")
def welcomindexe():
    return "How about my Index . Stay Tune for more update "


# Entry point starts here 
if __name__ =="__main__":
    app.run(debug=True)