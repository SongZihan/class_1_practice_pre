# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask
from hello import hello

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run(host="localhost", port=5001)
    # hello('there is truely main  function')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
