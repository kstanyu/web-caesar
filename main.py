from flask import Flask, request

from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method = "POST">
            <label for = "key"><strong>Rotate by:</strong></label>
            <input name = "rot" type = "text" id = "key" value = 0 />
            <br />
            <textarea name = "text">{ciphertext}</textarea>
            <br />
            <input type = "submit" value = "SUBMIT"/>
        </form>
    </body>
</html>
       """



@app.route("/")
def index():
    
    return form.format(ciphertext = "")


#recieves, process plaintext and renders ciphertext
  
@app.route("/", methods = ["POST"])
def encrypt():
    rot_key = int(request.form["rot"])
    plaintext = request.form["text"]
    
    cipher = rotate_string(plaintext,rot_key)
    
    return form.format(ciphertext = cipher)

app.run()
