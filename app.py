import streamlit as st
from image_analyzer import analyze_image

st.set_page_config(
    page_title="AI Image Analyzer",
    page_icon="🔍",
    layout="centered"
)

st.title("🔍 AI Image Analyzer")

st.write(
    "Upload an image to receive an AI-generated description."
)

st.warning(
    "This demonstration is for general, non-medical "
    "image analysis only. Do not upload medicine or "
    "medical images."
)

uploaded_file = st.file_uploader(
    "Upload your image",
    type=["jpg", "jpeg", "png", "webp"]
)

if uploaded_file:

    st.image(
        uploaded_file,
        caption="Uploaded image",
        use_container_width=True
    )

    if st.button("Analyze Image"):

        with st.spinner("Analyzing image..."):

            try:
                result = analyze_image(
                    uploaded_file.getvalue(),
                    uploaded_file.typeimport base64
import streamlit as st
from groq import Groq

def analyze_image(image_bytes, mime_type):

    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

    encoded_image = base64.b64encode(
        image_bytes
    ).decode("utf-8")

    response = client.chat.completions.create(
        model="qwen/qwen3.8-27b",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Describe this non-medical image. "
                            "Explain visible objects, colors, "
                            "text and relevant visual details. "
                            "Do not guess facts that cannot "
                            "be verified from the image."
                        )
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": (
                                f"data:{mime_type};base64,"
                                f"{encoded_image}"
                            )
                        }
                    }
                ]
            }
        ],
        temperature=0.3,
        max_completion_tokens=1024
    )

    return response.choices[0].message.content
                )

                st.subheader("Analysis Results")
                st.write(result)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
