import openai
import pathlib
import math
import datetime
import streamlit as st
from pydub import AudioSegment


st.title("Transcribe Audio with OpenAI")

# APIキーを設定します
openai.api_key = st.text_input("openAIのAPIキーを入力してください。", value="")

# Upload the audio file
audio_file = st.file_uploader("Upload an audio file", type=["mp3", "mp4 ", "m4a", "wav"])
if audio_file is None:
    st.warning("Please upload an audio file.")

if audio_file is not None:
    current_time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # Convert the audio file to the required format
    original_file = pathlib.Path(audio_file.name)
    audio_file_path = pathlib.Path("./audio").with_suffix(original_file.suffix)
    audio_segment = AudioSegment.from_file(str(audio_file_path))
    converted_file = audio_segment.export(pathlib.Path("./converted"+'_'+current_time_str).with_suffix(".wav"), format='wav')

    # Write the transcription prompt
    system_template = """
    A transcript of the meeting is passed.

    Please write a summary of this meeting in Markdown format. Write your summary in the following format:

    - Purpose of the meeting
    - Content of the meeting
    - Meeting result"""

    # Transcribe the audio using OpenAI API
    with open(converted_file.name, "rb") as f:
        response = openai.Audio.transcribe(
            "whisper-1", f, prompt=system_template, language="en"
        )
    transcription = str(response["text"])

    st.header("Transcription")
    st.write(transcription)

    # Generate a response using GPT-3
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{system_template}\n\n{transcription}\n",
        max_tokens=1024,
    )
    response_text = completion.choices[0].text.strip()

    st.header("GPT-3 Response")
    st.write(response_text)

    # Save the transcription to a file
    current_time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_file = f"transcription_{current_time_str}.txt"

    with open(output_file, "wt", encoding="utf-8") as f:
        f.writelines([transcription])

    st.success(f"Transcription saved to {output_file}")
