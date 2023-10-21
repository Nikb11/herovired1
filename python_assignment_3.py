from flask import Flask, jsonify
import json
import configparser

app = Flask(__name__)

def configuration(file):
    config = configparser.ConfigParser()
    config.read(file)
    
    data = {}
    
    for part in config.sections():
        data[part] = {key: value for key, value in config.items(part)}
    
    return data
@app.route('/', methods=['GET'])
def fetch_data():
    try:
        data = configuration('config_details.ini')
        return jsonify(data)
    except FileNotFoundError:
        return "File not present"
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
