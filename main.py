import os
import glob
from pytube import YouTube
import openai
from dotenv import load_dotenv
import json

load_dotenv()
OPENAI_APIKEY = os.getenv('OPENAI_APIKEY')

openai.api_key = OPENAI_APIKEY
systemPrompt = "You are an ai summarization tool. You recieive the raw transcribed text of a youtube video. You must summarize it with the main points (you can get technical). Your answer will be in markdown format with sections and subsections if needed so that your answer is easily readable by anyone."

def removeFiles():
    files = glob.glob('/output/*')
    for f in files:
        os.remove(f)

def DownloadAudio(url):
    yt = YouTube(url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    output_path = "output"
    filename = "audio.mp3"
    audio_stream.download(output_path=output_path, filename=filename)
    print(f"Audio downloaded to {output_path}/{filename}")

def TranscriptAudio(filePath):
    f = open(filePath, "rb")
    transcript = openai.Audio.transcribe("whisper-1", f)
    with open('output/data.json', 'w', encoding='utf-8') as j:
        json.dump(transcript, j, ensure_ascii=False, indent=4)
    print("File transcription done!")
    return transcript

def summarize(text):
    answer = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
       	{"role": "system", "content": f"{systemPrompt}"}, 
       	{"role": "user", "content": f"{text}"}
       ],
       max_tokens=200,
       temperature=0.5,
       stop=None
    )
    print("Summary finished and available in output folder !")
    return answer

if __name__ == "__main__":
    removeFiles()
    videoURL = input('Enter a youtube video URL: ')
    DownloadAudio(videoURL)
    audioTranscription = TranscriptAudio("output/audio.mp3")
    summary = summarize(audioTranscription['text']).choices[0].message.content
    s = open("output/summary.md", "w")
    s.write(summary)
    s.close()
    print("Program finished. Find all your files in the output folder in the script's workspace. ")
