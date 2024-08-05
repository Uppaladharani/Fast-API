# Import the FastAPI class
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define an endpoint using the @app.get decorator
@app.get("/")
def read_root():
    # Return a dictionary with a message
    return {"message": "Hello, FastAPI!"}
if __name__ == "__fast_":
    import uvicorn
    uvicorn.run()
