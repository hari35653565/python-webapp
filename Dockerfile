FROM python:3.8

WORKDIR /app

COPY home/ubuntu/python/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY home/ubuntu/python/ .

EXPOSE 8080

CMD ["streamlit", "run", "app.py"]
