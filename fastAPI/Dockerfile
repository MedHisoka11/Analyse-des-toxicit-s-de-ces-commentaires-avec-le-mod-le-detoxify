FROM python:3.11.6

WORKDIR /fastAPI

COPY requirements.txt /fastAPI/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /fastAPI

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
