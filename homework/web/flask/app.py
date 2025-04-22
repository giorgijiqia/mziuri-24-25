from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    welcome_message = "Welcome to my website!"
    return render_template("home.html", message=welcome_message)

@app.route('/about')
def about():
    about_info = {
        "name": "John Doe",
        "bio": "I'm a web developer passionate about creating cool web applications."
    }
    return render_template("about.html", info=about_info)

@app.route('/hobbies')
def hobbies():
    hobbies_list = [
        {"name": "Photography", "description": "Capturing moments through the lens."},
        {"name": "Programming", "description": "Building amazing things with code."},
        {"name": "Music", "description": "Exploring new genres and sounds."},
        {"name": "Reading", "description": "Losing myself in sci-fi and fantasy books."}
    ]
    return render_template("hobbies.html", hobbies=hobbies_list)

if __name__ == '__main__':
    app.run(debug=True)