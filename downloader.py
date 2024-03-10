from pytubefix import YouTube, Playlist
import shutil
import os
import zipfile

def get_youtube_object(url): 
    try:
        if '/watch?v=' in url:  # YouTube video URL
            return YouTube(url)
        elif '/playlist?list=' in url:  # Playlist URL
            return Playlist(url)
        else:
            raise ValueError("Unsupported URL")
    except Exception as e:
        print("Error:", e)
        return None


def write_to_file(url):
    obj = get_youtube_object(url)
    with open("data.txt", 'w', encoding='utf-8') as file:
        if isinstance(obj , YouTube) : 
    
            file.write(f"Channel Name : {obj.author}\n")
            file.write(f"Channel id : {obj.channel_id}\n")
            file.write(f"Channel URL : {obj.channel_url}\n")

            file.write("\n")
            
            file.write(f"{obj.title} : {{ \n")
            file.write("\n")
            file.write(f"\tVideo URL: {url}\n")

            file.write(f"\tVideo id: {obj.video_id}\n")
            file.write(f"\tNumber of Views: {obj.views}\n")
            file.write(f"\tLength of the video: {obj.length / 60}\n")
            file.write(f"\tPublish date: {obj.publish_date }\n")
            file.write(f"\tThumbnail link: {obj.thumbnail_url }\n")
            file.write(f"\tKeywords : {obj.keywords }\n")
            file.write(f"\tVideo description: {obj.description }\n}}")
        if isinstance(obj , Playlist) :  

            file.write(f"Channel Name : {obj.owner}\n")
            file.write(f"Channel id : {obj.owner_id}\n")
            file.write(f"Channel URL : {obj.owner_url}\n")

            for vid in obj.video_urls :
                video = YouTube(vid)

                
                file.write(f"{video.title} : {{ \n")
                file.write("\n")
                file.write(f"\tVideo URL: {vid}\n")

                file.write(f"\tVideo id: {video.video_id}\n")
                file.write(f"\tNumber of Views: {video.views}\n")
                file.write(f"\tLength of the video: {video.length / 60}\n")
                file.write(f"\tPublish date: {video.publish_date }\n")
                file.write(f"\tThumbnail link: {video.thumbnail_url }\n")
                file.write("\n")

                file.write(f"\tKeywords : {video.keywords }\n")
                file.write(f"\tVideo description: {video.description }\n}}\n\n")

def download_captions(url, lang_code='a.en'):
    try:
        captions_folder = 'captions'
        os.makedirs(captions_folder, exist_ok=True)
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, Playlist):
            for video_url in yt_obj.video_urls:
                download_captions(video_url, lang_code)
        
        elif isinstance(yt_obj, YouTube):
            captions = yt_obj.captions
            caption_track = captions[lang_code]
                # Download captions in SRT format (default)
            caption_track.download(title=f'{yt_obj.title}_caption_{lang_code}', srt=True , output_path=captions_folder)
      
    except Exception as e:
        print("Error:", e)

def vid_download(url , progress_bar):
    try:
        videos_folder = 'videos'
        os.makedirs(videos_folder, exist_ok=True)
        yt_obj = get_youtube_object(url)
        if isinstance(yt_obj, YouTube):
            progress_bar['value']=0
            yt_obj =  YouTube(url,on_progress_callback=lambda stream, chunk, bytes_remaining: down_prog(stream, chunk, bytes_remaining, progress_bar))
            vid = yt_obj.streams.get_highest_resolution() 
            vid.download(output_path=videos_folder)

        
        elif isinstance(yt_obj, Playlist) :
            for video_url in yt_obj.video_urls:
                progress_bar['value']=0
                yt = YouTube(video_url , on_progress_callback=lambda stream, chunk, bytes_remaining: down_prog(stream, chunk, bytes_remaining, progress_bar))
                vid = yt.streams.get_highest_resolution() 
                vid.download(output_path=videos_folder)

    except Exception as e:
        print("Error:", e)
    
def down_prog(stream , chunk , bytes_remaining,progress_bar):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = int((bytes_downloaded / total_size) * 100)
    progress_bar['value'] = percentage_of_completion
    progress_bar.update_idletasks()  

def archive_data():
    try:
        # Creating a zip file for archiving
        with zipfile.ZipFile('archive.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Archiving data.txt
            zipf.write('data.txt')

            # Archiving videos folder
            videos_folder = 'videos'
            for root, dirs, files in os.walk(videos_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, videos_folder)
                    zipf.write(file_path, os.path.join('videos', arcname))

            # Archiving captions folder
            captions_folder = 'captions'
            for root, dirs, files in os.walk(captions_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, captions_folder)
                    zipf.write(file_path, os.path.join('captions', arcname))

        # Removing original folders after archiving
        shutil.rmtree(videos_folder)
        shutil.rmtree(captions_folder)
        os.remove('data.txt')

    except Exception as e:
        print("Error:", e)
