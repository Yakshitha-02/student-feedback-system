FROM python:3.9

WORKDIR /app

COPY app/ /app/
COPY templates/ /app/templates/
COPY static/ /app/static/

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]