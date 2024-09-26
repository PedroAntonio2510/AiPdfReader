import os
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
from fastapi.responses import JSONResponse
import PyPDF2
import io


load_dotenv(".env")

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

generation_config = {
    "temperature": 0.6,
    "top_k": 0,
    "top_p": 0.95,
    "max_output_tokens": 1000
}

safety_settings={
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
}

model_name = 'gemini-1.5-flash'

model = genai.GenerativeModel(
    model_name = model_name,
    generation_config = generation_config,
    safety_settings = safety_settings
)

def extract_text_from_pdf(pdf_content: bytes) -> str:
    extracted_text = ""
    pdf_reader = PyPDF2.PdfReader(io.BytesIO(pdf_content))

    for page in pdf_reader.pages:
        text = page.extract_text()
        if text:
            extracted_text += text
            
    return extracted_text


