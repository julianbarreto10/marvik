from fastapi import FastAPI, Request
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Contadores para las llamadas a los endpoints
post_counter = 0
get_counter = 0

class DateRequest(BaseModel):
    detailed: bool

@app.post("/get-date/")
def get_date(request: DateRequest):
    global post_counter
    post_counter += 1

    current_date = datetime.now()
    if request.detailed:
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    else:
        formatted_date = current_date.strftime("%Y-%d-%m")
    
    return {"date": formatted_date}

@app.get("/counter/")
def get():
    global get_counter
    global post_counter
    get_counter += 1
    return {"get_date_calls": post_counter, "counter_calls": get_counter}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)