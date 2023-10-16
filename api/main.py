from flask import Flask, send_from_directory, render_template, jsonify, request
from flask_cors import cross_origin, CORS
from db import search_db

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/videos')
def list_videos():
    query = request.args.get('query','')
    result = search_db(query)
    print(result)
    return jsonify(result)


def main():
    app.run(host='0.0.0.0',debug=True,port=81)


if __name__ == '__main__':
    main()