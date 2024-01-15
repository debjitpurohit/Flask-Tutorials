# # Importing flask module in the project is mandatory
# # An object of Flask class is our WSGI application.
# from flask import Flask

# # Flask constructor takes the name of 
# # current module (__name__) as argument.
# app = Flask(__name__)

# # The route() function of the Flask class is a decorator, 
# # which tells the application which URL should call with
# # the associated function(bounded function).
# @app.route("/")  #this is decoretor # here within route we use rule that means path where the webpage want to go
# # ‘/’ URL is bound with welcome() function.
# def welcome():
#     return "welcome to my desktop debjit2"

# # hom epage 
# @app.route("/home")
# def home(): # here insted of home we can use anything 
#     return "welcome to my home page"


# @app.route("/about")
# def about():
#     return "welcome to my about page"

# @app.route('/hello/<name>') # here we use variable name
# def hello_name(name):
#     return 'Hello %s!' % name

# # main driver function
# if __name__ == "__main__":
#     # run() method of Flask class runs the application 
#     # on the local development server.
#     app.run(debug=True) 
#     # if we used this as just app.run() then if we change our code then we have to restart our server again and again to get rid of this we use debug mode = true



###############################################2nd chapter
### building URL dynamically
### flask variable rules and URL building

from flask import Flask , redirect , url_for # here we import redirect and url_for to redirect to another page
app= Flask(__name__)


@app.route('/') 
def home():
    return "welcome to my home page"

@app.route('/success/<int:score>') # here we use variable name . int is used to convert the string to integer if we just write <score> then it will take it as string
def success(score):
    return "the person has passed and the marks is "+ str(score) # if we concatinate string with integer then we have to convert integer to string

@app.route('/fail/<int:score>') 
def fail(score):
    return "</head><body><h1>You failed the exam</h1></body></html>" # if we use %s then we dont have to convert integer to string



##result checker
@app.route('/result/<int:marks>') 
def results(marks):
    result = ""
    if marks<50:
        result = "fail"
    else:
        result = "success"   
    return redirect(url_for(result,score=marks))   

if __name__ == "__main__": 
    app.run(debug=True)