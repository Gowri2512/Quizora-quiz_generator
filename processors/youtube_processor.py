from youtube_transcript_api import YouTubeTranscriptApi

def extract_id(url):
    if "v=" in url:
        return url.split("v=")[-1]
    return url.split("/")[-1]

def process_youtube(url):
    video_id = extract_id(url)
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    return " ".join([entry['text'] for entry in transcript_list])
