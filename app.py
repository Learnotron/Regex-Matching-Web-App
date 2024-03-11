from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def index():
    
    if request.method == "POST":
        pattern = request.form.get('regex_pattern')
        
        if pattern: 
            test_string = request.form.get('test_string')   
        
            matches = re.findall(pattern, test_string)
        else:
            matches = None
    else:
        matches = None
    return render_template('index.html', matches = matches)

def validate_email(email):
    
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if re.match(email_pattern, email):
        return True
    else:
        return False

@app.route('/email_validate.html', methods = ["GET", "POST"])
def email_validate():
    email = request.form.get("email")
    if email:
        if validate_email(email):
            text = f"{email} is a valid email."
        else:
            text = f"{email} is not a valid email."
    else:
        text = None
        
    return render_template('email_validate.html', text = text)

if __name__ == '__main__':
    app.run(debug = True, host = "0.0.0.0", port  = 5000)
        