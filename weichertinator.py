from flask import Flask, render_template, url_for, request, redirect
app = Flask("weichertinator")

@app.route('/',methods=["GET"])
def index():
    return render_template('hello.html')

@app.route('/',methods=["POST"])
def generate():
    if request.form['name']:
        name = request.form["name"]
    else:
        redirect(url_for("index"))
    return render_template('greeting.html',name=name, quote="DER UNTERGANG!")


if __name__ == '__main__':
    app.run()
