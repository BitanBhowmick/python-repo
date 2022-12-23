import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome to Ansible Test Web Project"


@app.route("/test")
def test():
    return "Deployed through Ansible"



if __name__ == "__main__":
    app.run()