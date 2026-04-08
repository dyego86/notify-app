from fastapi import FastAPI

app = FastAPI(title="notify-app backend")


@app.get("/")
def root():
    return {"message": "Backend funcionando 🚀"}