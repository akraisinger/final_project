''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the emotions and their
        scores for the provided text, as well as the dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    output = "For the given statement, the system response is "
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    for emotion in response.keys():
        if emotion != 'dominant_emotion':
            output += f"'{emotion}': {response[emotion]}, "
            if list(response.keys()).index(emotion) == len(response)-2:
                output=output[:-2]
        else:
            output += f". The dominant emotion is <b>{response[emotion]}</b>."
    return output

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
