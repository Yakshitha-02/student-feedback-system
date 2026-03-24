FROM python:3.9

WORKDIR /app

# copy backend code
COPY app/ /app/

# copy templates
COPY templates/ /app/templates/

# install dependencies
RUN pip install flask

# expose port
EXPOSE 5000

# run app
CMD ["python", "app.py"]