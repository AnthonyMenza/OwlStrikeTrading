# backend/main.py
# FastAPI backend skeleton for OwlStrikeTrading (moving averages + order flow analysis)
from fastapi import FastAPI
app = FastAPI()

@app.get('/ping')
def ping():
    return {'status':'ok'}
