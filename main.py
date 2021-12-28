from fastapi import FastAPI
from fastapi import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory='templates')  # defines the "templates" directory for Jinja2
app.mount("/static", StaticFiles(directory="static"), name="static")  # defines the "static" directory


@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})  # returns an HTML page
