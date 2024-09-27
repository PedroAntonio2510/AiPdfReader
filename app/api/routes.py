from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import JSONResponse
from app.services.pdf_services import model, extract_text_from_pdf
import google.generativeai as genai
from app.config.database import save_on_db, db


router = APIRouter()

@router.post("/file/upload")
async def upload_file(file: UploadFile = File(...), question: str = Form(...) ):
        if file.content_type != "application/pdf":
            raise HTTPException(
                status_code=400,
                detail="O arquivo enviado não é um PDF. Por favor, envie um arquivo PDF."
            )
        
        try:
            content = await file.read()
            
            if not content:
                return JSONResponse(content={"error": "Uploaded file is empty"}, status_code=400)
            
            pdf_file = extract_text_from_pdf(content)
            
            response = model.generate_content([question, pdf_file])
            
            question_doc = {
                "name": file.filename,
                "question": question,
                "content": pdf_file,
                "answer": response.text if hasattr(response, 'text') else str(response)
            }
            
            save_on_db(question_doc)
            
            return {"content": pdf_file, "answer": response.text}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading PDF: {str(e)}")
        
