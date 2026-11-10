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
                    uploaded_file.type
                )

                st.subheader("Analysis Results")
                st.write(result)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
