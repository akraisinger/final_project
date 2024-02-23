from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    output = "For the given statement, the system response is "
    for emotion in response.keys():
        if emotion != 'dominant emotion':
            print(list(response.keys()).index(emotion))
            output += f"'{emotion}': {response[emotion]}, "
            if list(response.keys()).index(emotion) == len(response)-2:
                print("success")
                output=output[:-2]
        else:
            output += f". The dominant emotion is <b>{response[emotion]}</b>."
    return output

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
