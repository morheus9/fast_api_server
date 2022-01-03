"""
Imports.
"""
from fastapi import FastAPI
from fastapi import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()  # initialize of server on http://127.0.0.1:8000

templates = Jinja2Templates(directory='templates')  # defines the "templates" directory for Jinja2
app.mount("/static", StaticFiles(directory="static"), name="static")  # defines the static

"""
returns an HTML page
"""
@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})
