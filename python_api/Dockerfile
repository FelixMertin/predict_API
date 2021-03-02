# A dockerfile must always start by importing the base image.
# Slim buster lowers image size by 700 mb
FROM python:3.7

# Set the working directory to /app for the docker container
WORKDIR /app

# Copy the current directoy content into container at /app
COPY . /app

# Copy requirements
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install -r requirements.txt
RUN python -m spacy download de_core_news_md



# Possibility to cache models ?
CMD ["uwsgi", "app.ini"]
