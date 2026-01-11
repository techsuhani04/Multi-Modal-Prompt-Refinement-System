import streamlit as st

st.title("Multi-Modal Prompt Refinement System (UI Demo)")

# Inform user about the purpose of this file
st.info(
    "Note: This UI is for demonstration purposes only. "
    "No LLM or AI model is used to generate real refined prompt outputs. "
    "For actual Input/Output examples, please check the accompanying documentation."
)

# Upload text input
uploaded_text = st.text_area("Enter text input here (optional)")

# Upload images
uploaded_images = st.file_uploader("Upload image(s)", type=["png", "jpg"], accept_multiple_files=True)

# Upload documents
uploaded_docs = st.file_uploader("Upload document(s)", type=["pdf", "docx"], accept_multiple_files=True)

if st.button("Process Input"):
    # Check which modalities have been ingested
    modalities_ingested = []
    if uploaded_text:
        modalities_ingested.append("Text")
    if uploaded_images:
        modalities_ingested.append("Images")
    if uploaded_docs:
        modalities_ingested.append("Documents")

    # Display ingested modalities
    if modalities_ingested:
        st.success(f"Ingested modalities: {', '.join(modalities_ingested)}")
    else:
        st.warning("No inputs uploaded!")

    # Final message simulating refinement
    st.info("Refined prompt successfully generated (simulation only).")
