from flask import Flask,render_template
app = Flask(__name__,template_folder="templates")

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/payments')
def payment():
	return render_template("payments.html")

@app.route('/contact')
def contact():
	return render_template("contact.html")

@app.route('/login')
def login():
	return render_template("login.html")



if __name__ == '__main__':
    app.run(debug=True)
