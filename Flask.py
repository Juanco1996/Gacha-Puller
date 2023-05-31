from flask import Flask, jsonify, request
from Puller import *

app = Flask(__name__)

@app.route('/api/pulls/regular banner', methods=['POST'])
def pull():
    data = request.json #get JSON data from POST request
    num_pulls = int(data['num_pulls']) #extract 'num_pulls' param from JSON and convert to integer

    return jsonify(run_simulation("Regular", num_pulls)) #return JSONified results from run_simulation function

@app.route('/api/pulls/leo banner', methods=['POST'])
def pull():
    data = request.json
    num_pulls = int(data['num_pulls'])

    return jsonify(run_simulation("Leo Banner", num_pulls))

@app.route('/api/pulls/icarus banner', methods=['POST'])
def pull():
    data = request.json
    num_pulls = int(data['num_pulls'])

    return jsonify(run_simulation("Icarus Banner", num_pulls))

@app.route('/api/pulls/astraeus banner', methods=['POST'])
def pull():
    data = request.json
    num_pulls = int(data['num_pulls'])

    return jsonify(run_simulation("Astraeus Banner", num_pulls))

@app.route('/api/pulls/helios banner', methods=['POST'])
def pull():
    data = request.json
    num_pulls = int(data['num_pulls'])

    return jsonify(run_simulation("Helios Banner", num_pulls))

@app.route('/api/pulls/aphrodite banner', methods=['POST'])
def pull():
    data = request.json
    num_pulls = int(data['num_pulls'])

    return jsonify(run_simulation("Aphrodite Banner", num_pulls))

@app.route('/api/pulls/hades banner', methods=['POST'])
def pull():
    data = request.json
    num_pulls = int(data['num_pulls'])

    return jsonify(run_simulation("Hades Banner", num_pulls))

@app.route('/api/pulls/weapon', methods=['POST'])
def pull():
    data = request.json
    num_pulls = int(data['num_pulls'])

    return jsonify(run_simulation("Weapon", num_pulls))

if __name__ == '__main__':
    app.run(debug=True)