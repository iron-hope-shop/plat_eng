FROM python:3.7-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
CMD ["gunicorn", "-w 2", "-k uvicorn.workers.UvicornWorker", "example:app"]