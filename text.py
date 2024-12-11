import streamlit as st
from transformers import pipeline

# Load the generative AI pipeline
@st.cache(allow_output_mutation=True)
def load_model():
    return pipeline("text-generation", model="gpt-2")

# Streamlit Interface
st.title("Generative AI for Report Making")

# Input Section
user_input = st.text_area("Enter your topic or data description:")

# Generate Text
if st.button("Generate Report"):
    if user_input:
        model = load_model()
        generated_text = model(user_input, max_length=300, num_return_sequences=1)[0]['generated_text']
        st.subheader("Generated Report:")
        st.write(generated_text)
    else:
        st.warning("Please enter some input to generate the report!")
