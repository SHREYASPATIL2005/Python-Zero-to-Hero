# 7. Explore the 'Flask' module and create a web server using Flask & Python.
# Install Flask: pip install flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# app.run(debug=True)  # Run the Flask web server in debug mode
# app.run(host='0.0.0.0', port=5000)  # Run the Flask web server on all available network interfaces and port 5000

app.run()


