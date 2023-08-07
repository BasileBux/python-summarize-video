# YouTube Video Summarizer

This is a small Python project that provides an AI-based summarization solution for YouTube videos.

I stumbled upon [mindgraspAI](https://mindgrasp.ai/), an AI-powered file summarization tool. However, it offers only a 4-day free trial and the pricing for my usage is too high. As a cost-effective alternative, I developed a Python script. The only problem is that the chatGPT prompt uses a considerable number of tokens, incurring some cost. Nonetheless, this expense is still lower than that of [mindgraspAI](https://mindgrasp.ai/). It's worth noting that the token consumption increases with the length of the video.

## Functionality

Upon execution, the script prompts the user for a YouTube URL. Then, it downloads the video in mp3 format, sends the file to [whisperAI](https://openai.com/research/whisper) for a complete speech-to-text transcription, and forwards the transcription to [chatGPT](https://openai.com/chatgpt) for summarization.

All generated data is stored in the output folder:
- Downloaded mp3 file: [audio.mp3](/output/audio.mp3)
- Video speech-to-text transcription: [data.json](/output/data.json)
- Video summary by chatGPT: [summary.md](/output/summary.md)

![Code Function](/assets/python-video-summarize.png)

## Setup Instructions

To run this program on your machine, ensure you have [Python 3.8](https://www.python.org/downloads/) or a higher version installed. Then execute the following command in your terminal to install the necessary Python modules:

```bash
pip install -r requirements.txt
```
Next, create a file named .env in the main folder and add the following line, replacing "your-api-key" with your personal [openAI api key](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/):
```
OPENAI_APIKEY='your-api-key'
```
