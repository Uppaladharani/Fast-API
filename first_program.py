app = FastAPI()

@app.get("/")
def first():
    return {"hello": "here iam creating a docker file"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)



