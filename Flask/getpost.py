from flask import Flask,render_template,request
'''
It creates the  instance of the  Flask Class
which will be used as wsgi applicaions

'''
### WSGI Application 
app=Flask(__name__)


## Starting with the Decorators - through which you want to move your router 
@app.route("/")
def welcome():
    return "<h1>Home Page</h1>"


### Which page it should go and By default its a get request 
@app.route("/index",methods=['GET'])
def welcomindexe():
    return render_template("index.html")

# if you want to put something in post and then you put post request also both in the html and here in .py 
@app.route("/form",methods=['POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        pass
    return render_template("form.html")

#render_template used for the integrate the HTMl with your applicatons 
@app.route("/about")
def about():
    return render_template("about.html")


# Entry point starts here 
if __name__ =="__main__":
    # Debug = True _ always provides the real time application update 
    app.run(debug=True)
