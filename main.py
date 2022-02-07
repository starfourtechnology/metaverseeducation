from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/")
def example():
    return {"FastAPI":"The fastest modern web framework"}

@app.get("/greetings")
def greeting():
    return {"Good Morning Ashik!"}

if __name__ == "__main__":
    uvicorn.run("main:app")