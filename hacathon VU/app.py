from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
import numpy as np

app = Flask(__name__)

model = tf.saved_model.load("C:\\Users\\piyus\\Code\\VIIT-Hackathon\\model\\saved_model")
class_names = ['adenocarcinoma', 'normal']

def predict_lung_cancer(image):
    img = tf.image.decode_image(image.read(), channels=3)
    img = tf.image.resize(img, [64, 64])
    img = tf.expand_dims(img, 0)
    img = img / 255.0
    
    predictions = model(img)
    predicted_class_index = tf.argmax(predictions, axis=1).numpy()[0]
    predicted_class = class_names[predicted_class_index]
    
    return predicted_class

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        if 'lung_scan' in request.files:
            image = request.files['lung_scan']
            if image.filename != '':
                prediction = predict_lung_cancer(image)
                if prediction == 'adenocarcinoma':
                    result = "Cancer Detected"
                else:
                    result = "No Lung Cancer Detected"
                return render_template('result.html', result=result)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
