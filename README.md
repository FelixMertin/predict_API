REST API Docker Compose Container with Flask-RESTplus, NGINX & SpaCy
=========

What is this for?
------------
This repository aims at providing an easy-to-deploy, secured and lightweight REST API for German NLP tasks. 
The scope is merely for personal usage and not aimed for a company case. To start with,
there is only an endpoint providing Named Entity Recognition via SpaCy and its pretrained model de_core_news_md. 

In future this repository will be expanded for my custom TensorFlow models. 


Installation Guide for Ubuntu
------------

Prerequisites is a server with docker and docker compose! You'll also need to adjust 
the API_Key and the API_URL in the /python_api/app/.env file.

Get your domain
------------

Get your domain at your favorited domain provider or go for a free one such as: https://dynv6.com/.


!IMPORTANT! the data/nginx/nginx.conf must be adjusted as well:
    
    4 $ server_name domain;
    .
    17 $ server_name domain;
    .
    21 $ ssl_certificate /etc/letsencrypt/live/domain/fullchain.pem;
    22 $ ssl_certificate_key /etc/letsencrypt/live/domain/privkey.pem;



Initialize the certificates
-------

As NGINX only can start when certificates are in place a script is needed to get 
dummy certificates and after the NGINX image is running legit certificates are pulled
through the certbot image.  
Firstly, source the environment variables - defining your domain:

     $ source /python_api/app/.env

Secondly, to get the certificates init-letsencrypt.sh:

     $ chmod +x init-letsencrypt.sh
     $ sudo ./init-letsencrypt.sh


Start the Docker Container
-------
After the dynamic DNS has been adjusted to the public IPv4 of the current machine 
and the init-letsencrypt.sh was successful:

     $ sudo docker-compose up
     
     
Test and do post request 
-------

In Python Shell with request and pickle package:

    $ import requests
    $ import json
    $
    $ # Define the endpoint and the payload
    $ REST_API_URL = "https://inference-endpoint.dynv6.net/predict"
    $
    $
    $ # Provide some text
    $ text = "Wer aufgrund seiner sozialen Herkunft benachteiligt wird, gilt heute schnell als Opfer von Klassismus.     Was steckt dahinter?"
    $
    $ # So far only Named Entity Recognition is supported
    $ prediction_task = "NER"
    $ 
    $ # construct the payload for the request
    $ payload = {'text': text, 'prediction_task': prediction_task}
    $ headers = {'api-key': 'YOURAPIKEY'}
    $
    $ # submit the request
    $ r = post(url, data=json.dumps(payload), headers = headers)
    $  response_json = json.loads(r.text)
    $ 
    $ # print the response
    $ print(response_json[0])
    
    


Sources
-------
The repository is based on the following article and especially the init-letsencrypt.sh: 
https://medium.com/@pentacent/nginx-and-lets-encrypt-with-docker-in-less-than-5-minutes-b4b8a60d3a71

The according repository behind it: https://github.com/wmnnd/nginx-certbot
