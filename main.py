"""
Imports.
"""
from fastapi import FastAPI
from fastapi import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI()  # initialize of server on http://127.0.0.1:80

# templates directory for Jinja2
templates = Jinja2Templates(directory='templates')
app.mount("/static", StaticFiles(directory="static"),
          name="static")  # the static

# returns an HTML page


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    """ Returns html """
    return templates.TemplateResponse('index.html', {'request': request})
