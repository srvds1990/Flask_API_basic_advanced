from flask import Flask,render_template
'''
It creates the  instance of the  Flask Class
which will be used as wsgi applicaions

'''
### WSGI Application 
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Home Page</h1>"



@app.route("/index")
def welcomindexe():
    return render_template("index.html")



@app.route("/about")
def about():
    return render_template("about.html")


# Entry point starts here 
if __name__ =="__main__":
    app.run(debug=True)