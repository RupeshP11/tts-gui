# tts-gui
I have created a GUI software for TTS ( Text to speech generation) where you can change the language and save the audio file or you can play it temporarily. It uses the modern GUI customtkinter which gives an elegant UI feel to the desktop.


# Rupesh Text to Speech App

This is a simple Text-to-Speech (TTS) application built using Python. The application uses the `gTTS` library for generating speech from text and `pygame` for audio playback. The graphical user interface (GUI) is built using `tkinter` and `customtkinter`.

## Features

- **Text to Speech Conversion**: Convert text input to speech in multiple languages.
- **Audio Playback**: Listen to the generated speech without saving it.
- **Save as MP3**: Save the generated speech as an MP3 file.
- **Theme Toggle**: Switch between light and dark themes.

## Prerequisites

- Python 3.x
- `gTTS` library
- `pygame` library
- `customtkinter` library

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/your-username/rupesh-tts-app.git
    cd rupesh-tts-app
    ```

2. **Install the required libraries**:

    ```bash
    pip install gtts pygame customtkinter
    ```

## Usage

1. **Run the application**:

    ```bash
    python tts_app.py
    ```

2. **Instructions**:

    - Enter the text you want to convert to speech in the text area.
    - Choose the language (default is English) by entering the language code (e.g., 'en' for English, 'es' for Spanish).
    - Enter a name for the MP3 file (without the `.mp3` extension) if you want to save the audio.
    - Click on "Listen Audio without saving the MP3 file" to play the audio.
    - Click on "Save the Audio" to save the audio as an MP3 file.
    - Use the "Toggle Theme" button to switch between light and dark themes.
