from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data_processing import process_data
import uvicorn
from fastapi import FastAPI
from data_processing import process_data
import uvicorn
from loading import connect,load_data_to_mongodb

collection = connect()

app = FastAPI()

@app.post("/process_data")
async def process_data_endpoint():
    data_json  = process_data()
    load_data_to_mongodb(data_json,collection)
    
    return JSONResponse(content={"message": "Data processed and stored in MongoDB successfully."})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
#async def process_data_endpoint():
 #   process_data()
  #  return {"message": "Data processed successfully."}