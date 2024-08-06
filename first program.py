
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# end point
@app.get("/")
def read_root():
    # Return a message
    return {"message": "Hello, FastAPI!"}
if __name__ == "__fast_":
    import uvicorn
    uvicorn.run()
