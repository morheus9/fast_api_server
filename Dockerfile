# install python in the container
FROM python:3.10-alpine3.15
# setup workdir
WORKDIR /usr/src/app
# copy the local requirements.txt file to the /app/requirements.txt in the container
COPY requirements.txt ./
# install the packages from the requirements.txt file in the container
RUN pip install --no-cache-dir --upgrade -r ./requirements.txt
# copy the local "./" folder to the "/app" fodler in the container
COPY . .
# execute the command python main.py (in the WORKDIR) to start the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
#docker build -t python:v1_alphine .
#docker run -d -p 80:80 python:v1_alphine
