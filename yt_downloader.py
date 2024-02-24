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
        if '/watch?v=' in url:  # YouTube video URL
            return  pytube.YouTube(url).author
        elif '/playlist?list=' in url:  # Playlist URL
            return pytube.Playlist(url).owner
        elif '/channel/' in url:  # Channel URL
            # Extract channel name from a vid
            return pytube.Channel(url).channel_name
    except Exception as err:
        print(err)
    
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
  
def get_publishdate(url):
    try:
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, pytube.YouTube) :
            return yt_obj.publish_date

        elif isinstance(yt_obj, pytube.Playlist) or isinstance(yt_obj, pytube.Channel) :
            return {pytube.YouTube(video_url).title : f'{pytube.YouTube(video_url).publish_date.year}-{pytube.YouTube(video_url).publish_date.month}-{pytube.YouTube(video_url).publish_date.day} {pytube.YouTube(video_url).publish_date.hour}:{pytube.YouTube(video_url).publish_date.minute}:{pytube.YouTube(video_url).publish_date.second}'  for video_url in yt_obj.video_urls}
    except Exception as e:
        print("Error:", e)

    
def get_keywords(url):
    try:
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, pytube.YouTube) :
            return yt_obj.keywords
        
        elif isinstance(yt_obj, pytube.Playlist) or isinstance(yt_obj, pytube.Channel) :
                return {pytube.YouTube(video_url).title : get_keywords(video_url) for video_url in yt_obj.video_urls}
    except Exception as e:
        print("Error:", e)

def append_video_descriptions(url):
    try:
        yt_obj = get_youtube_object(url)
        with open("video_descriptions.txt", 'a', encoding='utf-8') as file:
            if isinstance(yt_obj, pytube.YouTube):
                file.write(f"Video Title: {yt_obj.title}\n")
                file.write(f"Video Description:\n{yt_obj.description}\n\n")
                print(yt_obj.description)

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
    
def get_channel_id(url):
    try:
        yt_obj = get_youtube_object(url)
                
        if isinstance(yt_obj, pytube.YouTube) or isinstance(yt_obj, pytube.Channel):
            return yt_obj.channel_id
        
        elif isinstance(yt_obj, pytube.Playlist) :
            return yt_obj.owner_id

    except Exception as e:
        print("Error:", e)

def get_video_urls(url):
    try:
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, (pytube.Playlist, pytube.Channel)):
            return yt_obj.video_urls
        else:
            return url
    except Exception as e:
        print("Error:", e)
        return []

def download_captions(url, lang_code='a.en'):
    try:
        yt_obj = get_youtube_object(url)
        
        if isinstance(yt_obj, pytube.Playlist):
            for video_url in yt_obj.video_urls:
                download_captions(video_url, lang_code)
        
        elif isinstance(yt_obj, pytube.YouTube):
            captions = yt_obj.captions
            caption_track = captions.get_by_language_code(lang_code)
                # Download captions in SRT format (default)
            caption_track.download(title=f'caption_{yt_obj.video_id}_{lang_code}', srt=True)
            print(f"Captions in '{lang_code}' downloaded successfully for video: {yt_obj.title}")

            
    except Exception as e:
        print("Error:", e)





def vid_download(url):
    try:
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, pytube.YouTube):
            yt_obj =  pytube.YouTube(url,on_progress_callback=down_prog)
            vid = yt_obj.streams.get_highest_resolution() 
            vid.download()
        
        elif isinstance(yt_obj, pytube.Playlist) or isinstance(yt_obj, pytube.Channel):
            for video_url in yt_obj.video_urls:
                yt = pytube.YouTube(video_url , on_progress_callback=down_prog)
                vid = yt.streams.get_highest_resolution() 
                vid.download()
    except Exception as e:
        print("Error:", e)
    
def down_prog(stream , chunk , bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_compeletion = int((bytes_downloaded / total_size) * 100)
    print(percentage_of_compeletion)
