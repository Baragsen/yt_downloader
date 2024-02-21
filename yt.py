import pytube

def get_youtube_object(url):
    try:
        if '/watch?v=' in url:  # YouTube video URL
            return pytube.YouTube(url)
        elif '/playlist?list=' in url:  # Playlist URL
            return pytube.Playlist(url)
        elif '/channel/' in url:  # Channel URL
            return pytube.Channel(url)
        else:
            raise ValueError("Unsupported URL")
    except Exception as e:
        print("Error:", e)
        return None

def get_channel_name(url):
    try :
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, pytube.YouTube):
            return yt_obj.author
        elif isinstance(yt_obj, pytube.Playlist):
            return yt_obj.owner
        elif isinstance(yt_obj, pytube.Channel):
            # Extract channel name from the URL
            return url.split('/channel/')[-1].split('/')[0]
    except Exception as err:
        print(err)
        return None
    
def get_channel_url(url):
    try :
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, pytube.YouTube):
            return yt_obj.channel_url
        elif isinstance(yt_obj, pytube.Playlist):
            return yt_obj.owner_url
        elif isinstance(yt_obj, pytube.Channel):
            return url
    except Exception as err:
        print(err)
        return None


def append_video_descriptions(url):
    try:
        yt_obj = get_youtube_object(url)
        with open("video_descriptions.txt", 'a', encoding='utf-8') as file:
            if isinstance(yt_obj, pytube.YouTube):
                file.write(f"Video Title: {yt_obj.title}\n")
                file.write(f"Video Description:\n{yt_obj.description}\n\n")

            elif isinstance(yt_obj, pytube.Playlist) or isinstance(yt_obj, pytube.Channel):
                for video in yt_obj.video_urls:
                    yt = pytube.YouTube(video)
                    file.write(f"Video Title: {yt.title}\n")
                    file.write(f"Video Description:\n{yt.description}\n\n")

    except Exception as e:
        print("Error:", e)

def get_length(url):
    try:
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, pytube.YouTube) or isinstance(yt_obj, pytube.Playlist) :
            return yt_obj.length
        else :
            return None  
             
    except Exception as e:
        print("Error:", e)
        return None
    
def get_metadata(url):
    try:
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, pytube.YouTube):
            return yt_obj.metadata
        
        elif isinstance(yt_obj, pytube.Playlist) or isinstance(yt_obj, pytube.Channel) :
            metadata = []
            for video_url in yt_obj.video_urls:
                yt = pytube.YouTube(video_url)
                metadata.append(yt.metadata)
            return metadata

    except Exception as e:
        print("Error:", e)
        return None

def get_views(url):
    try:
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, pytube.YouTube) or isinstance(yt_obj, pytube.Playlist):
            return yt_obj.views
        
        elif isinstance(yt_obj, pytube.Channel):
            return None
    except Exception as e:
        print("Error:", e)
        return None


def get_thumbnail_url(url):
    try:
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, pytube.YouTube):
            return yt_obj.thumbnail_url
        
        elif isinstance(yt_obj, pytube.Playlist):
            thumbnails = []
            for video_url in yt_obj.video_urls:
                yt = pytube.YouTube(video_url)
                thumbnails.append(yt.thumbnail_url)
            return thumbnails
        
        elif isinstance(yt_obj, pytube.Channel):
            return None
        
    except Exception as e:
        print("Error:", e)
        return None
    
def download_captions(url, lang_code='en'):
    try:
        yt_obj = get_youtube_object(url)
        
        if isinstance(yt_obj, pytube.Playlist):
            for video_url in yt_obj.video_urls:
                download_captions(video_url, lang_code)
        
        elif isinstance(yt_obj, pytube.YouTube):
            captions = yt_obj.captions
            if lang_code in captions:
                caption_track = captions[lang_code]
                # Download captions in SRT format (default)
                caption_track.download(output_path=f'caption_{pytube.extract.video_id(url)}_{lang_code}', srt=True)
                print(f"Captions in '{lang_code}' downloaded successfully for video: {yt_obj.title}")
            
    except Exception as e:
        print("Error:", e)

def get_video_urls(url):
    try:
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, (pytube.Playlist, pytube.Channel)):
            return yt_obj.video_urls
        else:
            return []
    except Exception as e:
        print("Error:", e)
        return []