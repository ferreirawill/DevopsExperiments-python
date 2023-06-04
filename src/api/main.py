from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from src.MathOperations import SimpleOperations as op
import uvicorn



app = FastAPI()

data = {
    "lastNumbersStored": {"a": 1, "b": 2},
    "sum": 3,
    "subtract": -1,
    "multiply": 2,
    "divide": 0.5,
    "power": 1,
}


class DataModel(BaseModel):
    a: float
    b: float


@app.get('/')
def get_data():
    return JSONResponse(content=data)


@app.post('/')
def post_data(new_data: DataModel):
    new_dict = {
        "lastNumbersStored": {"a": new_data.a, "b": new_data.b},
        "sum": op.simple_sum(new_data.a, new_data.b),
        "subtract": op.subtract(new_data.a, new_data.b),
        "multiply": op.multiply(new_data.a, new_data.b),
        "divide": op.divide(new_data.a, new_data.b),
        "power": op.power(new_data.a, new_data.b),
    }

    data.update(new_dict)

    return JSONResponse(content=data, status_code=201)


@app.put('/')
def put_data(updated_data: DataModel):
    new_dict = {
        "lastNumbersStored": {"a": updated_data.a, "b": updated_data.b},
        "sum": op.simple_sum(updated_data.a, updated_data.b),
        "subtract": op.subtract(updated_data.a, updated_data.b),
        "multiply": op.multiply(updated_data.a, updated_data.b),
        "divide": op.divide(updated_data.a, updated_data.b),
        "power": op.power(updated_data.a, updated_data.b),
    }

    data.clear()
    data.update(new_dict)

    return JSONResponse(content=data)


@app.delete('/',status_code=204)
def delete_data():
    data.clear()
    return


if __name__ == "__main__":
    uvicorn.run("src.api.main:app", host="0.0.0.0", port=7001, http="h11", workers=6, log_level="info")
