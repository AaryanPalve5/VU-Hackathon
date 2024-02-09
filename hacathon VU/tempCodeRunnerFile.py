from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'


#model here


def predict_lung_cancer(image):
    pass

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        image = request.files['lung_scan']
        prediction = predict_lung_cancer(image)

        if prediction == 'cancerous':
            result = "Lung Cancer Detected"
        else:
            result = "No Lung Cancer Detected"

        return redirect(url_for('show_result', result=result))

    return redirect(url_for('index'))

@app.route('/show_result/<result>')
def show_result(result):
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
