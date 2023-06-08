import sys

import os

current_dir = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.join(current_dir, 'Secound_Data_Set_Search.py'))
from Secound_Data_Set_Search import search

from fastapi import FastAPI

Secondapp = FastAPI()

@Secondapp.get('/')
async def root():
    return {'Second Api'}

@Secondapp.post('/SecondSearchApi/{query_id}+{query_text}')
async def SecondSearchApi(query_id : int, query_text : str):
    SearchResult = search(query_id,query_text)
    return SearchResult