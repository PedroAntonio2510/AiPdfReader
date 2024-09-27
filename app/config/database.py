import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import PyMongoError


load_dotenv(".env")

username = os.getenv("DB_USERNAME")  # Substitua pelo seu nome de usuário
password = os.getenv("DB_PASSWORD")

client = MongoClient(f"mongodb+srv://{username}:{password}@cluster0.8mxqa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["AiPdf_db"]

def save_on_db(question_doc):
        try:
            db.questions.insert_one(question_doc)
            print("Saved sucessfully")
        except PyMongoError as e:
            raise Exception(f"Error on adding to database: {str(e)}")

