FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt --no-cache-dir

COPY ./auth_server /app/auth_server

EXPOSE 3000
CMD ["uvicorn","auth_server.main:app","--host","0.0.0.0","--port","3000"]
