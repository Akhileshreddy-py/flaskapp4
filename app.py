from flask import Flask

app=Flask(__name__)

@app.route("/")
def ak():
    return " <h1> HEllo akhilesh reddy man </h1> "

app.run(debug=True,port=8000)