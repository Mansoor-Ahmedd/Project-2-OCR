from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import pytesseract
import joblib
import io
import re

# ====================== CONFIGURATION ======================
# Set Tesseract path for Windows (Change only if your path is different)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

app = FastAPI(
    title='Document Intelligence API',
    description='OCR + Classification + Extraction',
    version='1.0.0'
)

# Load models
try:
    vectorizer = joblib.load('../models/vectorizer.pkl')
    classifier = joblib.load('../models/classifier.pkl')
    print("✅ Models loaded successfully!")
except Exception as e:
    print(f"❌ Error loading models: {e}")

# ====================== EXTRACTION FUNCTIONS ======================
def extract_dates(text):
    return re.findall(r'\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b', text)

def extract_amounts(text):
    return re.findall(r'[\$₹€£]?\s*\d+[.,]?\d*', text)

def extract_entities(text):
    # Simple entity extraction
    return re.findall(r'[A-Z][a-z]+(?:\s[A-Z][a-z]+)*', text[:500])

# ====================== ROOT ENDPOINT ======================
@app.get('/')
def root():
    return {
        'message': 'Document Intelligence API is running!',
        'version': '1.0.0',
        'endpoints': ['/classify', '/process']
    }

# ====================== CLASSIFY ENDPOINT ======================
@app.post('/classify')
async def classify_document(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)
        
        print(f"📄 OCR extracted {len(text)} characters")

        if len(text.strip()) < 30:
            return JSONResponse(status_code=400, content={
                "error": "Very little text detected. Please upload a clearer document image."
            })

        # Classify
        text_vec = vectorizer.transform([text])
        prediction = classifier.predict(text_vec)[0]
        probabilities = classifier.predict_proba(text_vec)[0]
        confidence = float(max(probabilities))

        return {
            "document_type": prediction,
            "confidence": confidence,
            "all_probabilities": dict(zip(classifier.classes_, [float(p) for p in probabilities])),
            "text_length": len(text)
        }
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})

# ====================== PROCESS ENDPOINT ======================
@app.post('/process')
async def process_document(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))
        text = pytesseract.image_to_string(image)

        if len(text.strip()) < 30:
            return JSONResponse(status_code=400, content={
                "error": "Very little text detected. Please upload a clearer document."
            })

        # Classify
        text_vec = vectorizer.transform([text])
        doc_type = classifier.predict(text_vec)[0]
        confidence = float(max(classifier.predict_proba(text_vec)[0]))

        # Extract
        extracted = {
            "dates": extract_dates(text),
            "amounts": extract_amounts(text),
            "entities": extract_entities(text)
        }

        return {
            "document_type": doc_type,
            "confidence": confidence,
            "extracted_data": extracted,
            "text_length": len(text),
            "status": "success"
        }
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        return JSONResponse(status_code=500, content={"error": str(e)})

print("🚀 API code loaded successfully!")