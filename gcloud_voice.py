import speech_recognition as sr
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Load the service account key file
credentials = Credentials.from_service_account_file('service-account.json')

# Create a client for the Google Cloud Speech API
speech_client = build('speech', 'v1', credentials=credentials)

# Create a Recognizer object
r = sr.Recognizer()

# Create a microphone object
mic = sr.Microphone()

while True:
    # Start listening for audio
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Try to recognize the speech
    try:
        # Use the Google Cloud Speech API to recognize the speech
        response = speech_client.recognize(
            audio={"content": audio.get_raw_data()},
            config={"languageCode": "en-US"}
        )

        # Print the transcript
        transcript = response['results'][0]['alternatives'][0]['transcript']
        print(transcript)

        # Implement the logic for your voice recognition application here, using the transcript
        if 'play cricket match' in transcript:
            # Turn on the lights
            pass
        elif 'play arijit sngh songs' in transcript:
            # Play music
            pass
        # ... more

    except sr.UnknownValueError:
        print("sorry, couldn't understand what you said. Please check your voice.....")
    except sr.RequestError as e:
        print(f'Error calling the API: {e}')
