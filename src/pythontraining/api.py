from fastapi import FastAPI

app = FastAPI()

db = {1: "John Doe",
      2: "Sally Jones",
      }


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):
    return db[customer_id]
