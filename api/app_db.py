from fastapi import FastAPI
from contextlib import asynccontextmanager
import httpx
from motor.motor_asyncio import AsyncIOMotorClient
import os

app = FastAPI()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DATABASE_NAME = "Test"
COLLECTION_NAME = "questions"

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with httpx.AsyncClient() as http_client:
        response = await http_client.get(
            "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
        )
        if response.status_code == 200:
            data = response.json()
            if "items" in data:
                # Insert data into MongoDB
                await collection.insert_many(data["items"])
                print("Data inserted into MongoDB")
        else:
            print("Failed to fetch data from Stack Exchange API")
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/")
def greet():
    return "Welcome to Rest API Tutorials"

@app.get("/get_questions/{number_of_questions}")
async def get_questions(number_of_questions: int):
    cursor = collection.find({}, {"_id": 0, "title": 1}).limit(number_of_questions)
    questions = [doc["title"] async for doc in cursor]
    if not questions:
        return {"error": "No data available"}
    return {"questions": questions}
