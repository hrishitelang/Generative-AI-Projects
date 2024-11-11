import streamlit as st
from dotenv import load_dotenv

load_dotenv() ##load all the environment variables
import os
import google.generativeai as genai

from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt= """You are YouTube video summarizer. You will be taking the transcript text and summarizing 
the entire video and providing the important summary in points within 250 words.
The transcript text will be appended here:"""

## getting the transcript data from yt videos
def extract_transcript_details(youtube_video_url):
    try:
        # Extract the video ID using a regex to be more flexible with the URL format
        video_id = re.search(r"(?<=v=)[^&]+", youtube_video_url).group(0)
        print(f"Video ID: {video_id}")
        
        # Attempt to retrieve the transcript
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)

        # Concatenate the transcript into a single string
        transcript_text = ""
        for entry in transcript_list:
            transcript_text += " " + entry["text"]

        return transcript_text
    
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"
    
## getting the summary based on prompt from Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model=genai.GenerativeModel("gemini-pro")
    response=model.generate_content(prompt+transcript_text)
    return response.text

st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        summary = generate_gemini_content(transcript_text, prompt)
        st.markdown("## Detailed notes:")
        st.write(summary)

