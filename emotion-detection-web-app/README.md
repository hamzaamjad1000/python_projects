# Emotion Detection Web App

Welcome! This is a simple web application that uses IBM Watson Natural Language Processing (NLP) services to detect emotions from user-input text. It’s built with Python and Flask, and designed to be easy to use, understand, and extend.

## Demo

Just enter any sentence or paragraph, and the app will analyze it to tell you the emotions expressed—such as joy, anger, sadness, fear, or disgust.

## Features

- **Emotion Analysis:** Uses IBM Watson NLP to detect emotions in text.
- **User-Friendly Web Interface:** Built with Flask for easy interaction.
- **Fast & Lightweight:** Quick responses and minimal requirements.
- **Easy to Deploy:** Can run locally or on cloud platforms.

## How to Run

1. **Clone this repository:**
   ```bash
   git clone https://github.com/hamzaamjad1000/emotion-detection-web-app.git
   cd emotion-detection-web-app
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your IBM Watson API credentials:**
   - Create a `.env` file or edit `config.py` with your Watson API key and URL.

4. **Run the app:**
   ```bash
   python server.py
   ```
   The app will be accessible at [http://localhost:5000](http://localhost:5000).

## Folder Structure

```
emotion-detection-web-app/
├── EmotionDetection/
│   └── emotion_detector.py
├── templates/
│   └── index.html
├── server.py
├── requirements.txt
├── README.md
```

## Example Usage

- Enter: `I am so happy with my results!`
- Output:  
  ```
  Emotion: Joy
  Score: 0.92
  ```
  
## Screenshots

![Web App Screenshot](screenshots/web_app.png)

## Author

**Hamza Amjad**  
[GitHub Profile](https://github.com/hamzaamjad1000)
