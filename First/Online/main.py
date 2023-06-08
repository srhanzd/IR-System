import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, 'First_Data_Set_Search.py'))
from First_Data_Set_Search import search

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'example': 'This is an example', 'data' : 0}

@app.post('/SearchApi/{query_id}+{query_text}')
async def SearchApi(query_id : int, query_text : str):
    SearchResult = search(query_id, query_text)
    return SearchResult