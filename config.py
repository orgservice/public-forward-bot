import os
import logging
class Config:                                                                   
    API_ID = int(os.environ.get("API_ID", "24715632"))
    API_HASH = os.environ.get("API_HASH", "dc1320bd5c50d6834a5abe2e343b0bee")       
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7269198396:AAFKKvA7u_oTIWYZwvqYCBAAZLKnM49tRwM")
    BOT_SESSION = os.environ.get("BOT_SESSION", "1BVtsOK0Buwy7c67JW6blDTy_vIDa32v5naSTxAPFB8RM-m93mlbmSmDhNPCeyF7UIsZKW--COSAdo_-yOf4C0c8mILby0EpESwLWCoOD9njKIl9-cu-A_39i_HMCC8Nc2Vub9DRoo8E0rcg1WHOgBxh9Kc8zCovZPoO0NPxnmXl9d-ZHaybje1q4fHeorpD6Os4F-GReK-howfzdngU5_K5zOW9ITFtZAHddEkEiSMTr92QNqPPaGewt-8ZKrhZBbi8bhBKVgAYmDgbaZuACqN_Nv0JHOYItSPdmfJN_oFaW1Uv0OHvEDx9jpOPRXggmDqFnO4B0DCY8EhKgOi7uBt-Hb9GqMFE=")
    OWNER_ID = os.environ.get("OWNER_ID", "6648168722")                             
    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://uhdprime:uhdprime@cluster0.ry5y4yk.mongodb.net/?retryWrites=true&w=majority")  
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluste0")
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'Data')
    SESSION = os.environ.get("SESSION", "1BVtsOK0Buwy7c67JW6blDTy_vIDa32v5naSTxAPFB8RM-m93mlbmSmDhNPCeyF7UIsZKW--COSAdo_-yOf4C0c8mILby0EpESwLWCoOD9njKIl9-cu-A_39i_HMCC8Nc2Vub9DRoo8E0rcg1WHOgBxh9Kc8zCovZPoO0NPxnmXl9d-ZHaybje1q4fHeorpD6Os4F-GReK-howfzdngU5_K5zOW9ITFtZAHddEkEiSMTr92QNqPPaGewt-8ZKrhZBbi8bhBKVgAYmDgbaZuACqN_Nv0JHOYItSPdmfJN_oFaW1Uv0OHvEDx9jpOPRXggmDqFnO4B0DCY8EhKgOi7uBt-Hb9GqMFE=")   
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", "-1002055068009"))
    BOT_USERNAME= os.environ.get("BOT_USERNAME", "orgpostforwardbot")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
