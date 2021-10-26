from flask import Flask, request
from mainFunction import headlineScrapper

app = Flask(__name__)
@app.route('/getHeadline',methods = ['POST'])
def getHeadline():
    try:
        url = request.json['url']
        return headlineScrapper(url)
    except:
        return 'Invalid Input Formatr'

if __name__ == "__main__":
    app.run(debug=True)