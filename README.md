# AuraView

## Overview
AuraView is an augmented reality application that recognizes faces in real-time and fetches user information from social media profiles.

## Project Structure
AR-Social-Glasses/ ├── Android/
│ ├── app/ │ ├── ... ├── server/
│ ├── mock_server.py │ ├── social_media_api.py │ ├── face_recognition.py ├── .env
├── README.md
└── requirements.txt

## Setup Instructions

### Backend Server
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd AR-Social-Glasses/server
Install the required Python packages:
 '''bash

    pip install -r requirements.txt
    Set up environment variables in the .env file with your social media API keys.
 '''bash
  
       Run the mock server:
       python mock_server.py
 '''Android App
 
    Open the Android project in Android Studio.
    Make sure you have ARCore installed on your device/emulator.
    Build and run the application on an ARCore compatible device.
    
# Usage
    The application captures video from the camera and detects faces.
    It matches the detected faces against known faces and retrieves user info from the mock server.
    API Endpoints
    GET /get_user_info
    Parameters: name - Name of the user to retrieve info for.

Response: Returns user information including name, occupation, and social media links.

# License
    This project is licensed under the MIT License.


### Final Notes
     Please replace the placeholder values in `.env` and any other areas with your actual configurations. Ensure you test the application thoroughly to verify that everything works as intended.
