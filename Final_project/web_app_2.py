from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

with open('my_pipeline_2.pkl', 'rb') as pkl_file: 
    model = pickle.load(pkl_file)

app = Flask(__name__)
app.config['DEBUG'] = True
@app.route('/predict', methods=['POST'])
def predict():
    
    features = request.json.get('features')
    features = np.array(features)
    features = features.reshape(1, 18)
    prediction = model.predict(features)
    return  jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    
    app.run('localhost', 4000)

    