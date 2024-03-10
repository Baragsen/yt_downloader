# VidVortex

VidVortex is a Python Desktop application designed to simplify the process of downloading YouTube videos, extracting captions, and metadata. It utilizes the tkinter library for the graphical user interface (GUI) and various other libraries for handling YouTube data.

## Features

- **YouTube Video Downloading** : Download YouTube videos directly within the application.
- **Caption Extraction** : Extract captions/subtitles from YouTube videos in different languages.
- **MetaData Extraction** : Extract the following Data : 
  -  Channel Name
  -  Channel ID
  -  Channel URL
  -  Video Title
  -  Video URL
  -  Video ID
  -  Number of Views
  -  Length of the Video/Playlist
  -  Publish Date
  -  Thumbnail URL
  -  Keywords
  -  Video Description .
- **Archiving**: Archive downloaded videos, captions, and metadata .
- **Customizable Interface**: Uses ttkbootstrap for themed styling, providing a visually pleasing interface.

## Prerequisites

- Python 3.x
- tkinter
- ttkbootstrap
- pytubefix


## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/Baragsen/VidVortex.git
    ```

2. Navigate to the project directory:

    ```bash
    cd VidVortex
    ```

3. Install the required dependencies:

    ```bash
    python -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    python app.py
    ```

2. Enter the YouTube video URL or the Playlist URL in the provided field.
3. Optionally, choose to include metadata extraction and click on "Start".
4. Monitor the progress of the download via the progress bar.
5. Once the download is complete, the data will be archived .

