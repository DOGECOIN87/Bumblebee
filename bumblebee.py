import requests
import pyttsx3

API_KEY = "42c8c7d61710431f98cc8e3ceeb6f5c0"
ORGANIZATION_ID = "Matthew_Mobley-9cca47e9"
USER_ID = "Matthew_Mobley-9cca47e9"

def convert_text_to_audio(text):
    # Set up the API endpoint
    url = "https://api.audiostack.io/v1/speech"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "organizationId": ORGANIZATION_ID,
        "userId": USER_ID,
        "input": {
            "text": text
        }
    }

    try:
        # Send a POST request to the API endpoint
        response = requests.post(url, headers=headers, json=payload)

        # Save the audio response to a file
        with open("output.wav", "wb") as audio_file:
            audio_file.write(response.content)

        print("Audio file generated successfully.")
    except requests.exceptions.RequestException as e:
        print("Error occurred during the API request:", str(e))

def bumblebee(input_text):
    # Convert text to audio
    convert_text_to_audio(input_text)

# Example usage
text_input = "Hello, how are you?"
bumblebee(text_input)
