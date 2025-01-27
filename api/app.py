# from fastapi import FastAPI
# from contextlib import asynccontextmanager
# import httpx  

# app = FastAPI()

# response_data = None  


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     global response_data
#     async with httpx.AsyncClient() as client:
#         response = await client.get(
#             "https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow"
#         )
#         if response.status_code == 200:
#             response_data = response.json() 
#             print(response_data)
#         else:
#             response_data = None
#     yield


# app = FastAPI(lifespan=lifespan) 


# @app.get("/")
# def greet():
#     return "Welcome to Rest API Tutorials"


# @app.get("/get_questions/{number_of_questions}")
# def get_questions(number_of_questions: int):
#     if not response_data or "items" not in response_data:
#         return {"error": "No data available"}
    
#     items = response_data["items"]
#     number_of_questions = min(number_of_questions, len(items))  
    
#     data = [items[i]["title"] for i in range(number_of_questions)]
#     return {"questions": data}


# @app.get("/get_unsolved_questions")
# def unsolved_questions():
#     if not response_data or "items" not in response_data:
#         return {"error": "No data available"}
    
#     unsolved = [
#         item["title"]
#         for item in response_data["items"]
#         if not item.get("is_answered", True)
#     ]
#     return {"unsolved_questions": unsolved}
