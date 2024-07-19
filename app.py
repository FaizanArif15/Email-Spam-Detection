# app.py
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import joblib
from fastapi.templating import Jinja2Templates

# Load the model and vectorizer
model = joblib.load('spam_ham_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

app = FastAPI()
templates = Jinja2Templates(directory="templates")

class Message(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/predict")
async def predict(request: Request, message: str = Form(...)):
    # Transform the message using the loaded vectorizer
    message_vec = vectorizer.transform([message])
    # Predict using the loaded model
    prediction = model.predict(message_vec)
    if prediction[0] == 0:
        prediction = 'Ham'
    else:
        prediction = 'spam'
    return templates.TemplateResponse("result.html", {"request": request, "prediction": prediction, "message": message})
