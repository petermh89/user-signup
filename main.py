from flask import Flask,request,redirect,render_template
# import jinja2
# import os 

# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    # template = jinja_env.get_template('user.html')
    return render_template('user.html')




@app.route("/", methods=["POST"])
def fields_val():

   
    user_name = request.form['username']
    print("username")
    
    password = request.form['password']
    
    ver_pass = request.form['verify_password']
    
    email = request.form['email']
    
    user_error = ""
    pass_error = ""
    ver_error = ""
    email_error = ""

   

    

    if user_name == "":
        user_error = "Username field cannot be empty"
        user_name = ""

    elif len(user_name) > 20 or len(user_name) < 3:
        user_error = "Username must be between 3 and 20 characters"
        user_name = ""

    if password == "":
        pass_error = "Password is required"
        password= ""
        
    elif len(password) > 20 or len(password) < 3:
        pass_error = "Password must be between 3 and 20 characters"
        password = ""
        
   
    if ver_pass != password:
        ver_error = "Verify password did not match password"
        ver_pass =""
    
    if len(email) > 20 or len(email) < 3 or "@" not in email or "." not in email:
        email_error = "This is not a valid email"
        email = ""
    


    if not user_error and not pass_error and not ver_error:
        
         return redirect('/welcome?user={0}'.format(user_name))   

    else:
        return render_template('user.html', user_name=user_name,email=email,user_error = user_error, pass_error = pass_error, ver_error= ver_error,email_error=email_error)

@app.route('/welcome')
def welcome():
    user = request.args.get('user')
    return render_template("welcome.html", user= user)
  


app.run()