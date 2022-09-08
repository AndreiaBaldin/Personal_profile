from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/project")
def project():
	return render_template("project.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

#coloca o site no ar
if __name__ == "__main__":
	app.run(debug=True)

