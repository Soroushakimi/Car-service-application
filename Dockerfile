FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /dogane

# Required to install mysqlclient with Pip

# Install pipenv
COPY ./requirement.txt ./requirement.txt

RUN pip install -r requirement.txt
# Copy the application files into the image
COPY . /app/

# Expose port 8000 on the container 
EXPOSE 8000