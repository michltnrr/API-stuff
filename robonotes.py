from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI

url = input("Enter the youtube video url: ")
video = url[url.index('=')+1:]

# to get transcript of yt video
transcript = YouTubeTranscriptApi.get_transcript(video)
video_text = ''
for i in range(len(transcript)):
    video_text += transcript[i]['text']
    video_text += ' '

# access chatgpt 
key = 'YOURAPIKEY'
client = OpenAI(api_key=key)

prompt = "Given the transcript of this math video, summarize the main ideas in 2-3 pargraphs, and walkthrough some example problems \
solving them as explained in the video, then explain how u solved them using 3-5 bullet points,\
make the explanation  applicable to all problems relating to the discussed topic"

response = client.chat.completions.create(
  model = "gpt-3.5-turbo",
  messages = [
    {"role": "system", "content": prompt},
    {"role": "user", "content": video_text}
  ]
)

print()
print(response.choices[0].message)
