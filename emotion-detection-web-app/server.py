from flask import Flask, request, render_template
from EmotionDetection.emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        text = request.form.get('text')
        if text:
            result = emotion_predictor(text)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)