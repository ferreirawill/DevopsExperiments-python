from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn
app = FastAPI()

# Placeholder data - replace with your actual JSON file or database integration
data = {
    "responsibility": "Placeholder"
}

class DataModel(BaseModel):
    responsibility: str

@app.get('/')
def get_data():
    return JSONResponse(content=data)

@app.post('/')
def post_data(new_data: DataModel):
    data.update(new_data.dict())
    return JSONResponse(content=data, status_code=201)

@app.put('/')
def put_data(updated_data: DataModel):
    data.clear()
    data.update(updated_data.dict())
    return JSONResponse(content=data)

@app.delete('/')
def delete_data():
    data.clear()
    return JSONResponse(status_code=204)




if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=7001, http="h11", workers=6,log_level="info")