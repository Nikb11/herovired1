import configparser
import json
from flask import Flask, jsonify

app = Flask(__name__)

def configuration(file):
    config = configparser.ConfigParser()
    config.read(file)
    
    data = {}
    
    for section in config.sections():
        data[section] = {key: value for key, value in config.items(section)}
    
    return data
@app.route('/', methods=['GET'])
def fetch_data():
    try:
        data = configuration('config_details.ini')
        return jsonify(data)
    except FileNotFoundError:
        return "Configuration file not found"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
