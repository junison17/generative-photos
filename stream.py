import streamlit as st
import openai


openai.api_key = st.secrets["OPENAI_API_KEY"]
st.title("DALL-E CLONE-Chat-GPT OF SON JH")

with st.form("form"):
    user_input = st.text_input("Prompt")
    size = st.selectbox("Size", ["1024x1024", "512x512", "256x256"])
    submit = st.form_submit_button("submit")

if submit and user_input:
    gpt_prompt = [{
        "role": "system",
        "content": "Imagine the detail appearance of the input. Respond with around 20 words. Don't imagine negative prompts. For example, worst quality, low quality, blur, bad hands, extra fingers, missing fingers, long neck, and low quality."
    }]

    gpt_prompt.append({
        "role": "user",
        "content": user_input
    })

    with st.spinner("Waiting for correct prompt"):
        gpt_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=gpt_prompt
        )

    prompt = gpt_response["choices"][0]["message"]["content"]
    st.write(prompt)

    with st.spinner("Waiting for your imagination"):
        dalle_response = openai.Image.create(
            prompt=prompt,
            size=size
        )

    st.image(dalle_response["data"][0]["url"])