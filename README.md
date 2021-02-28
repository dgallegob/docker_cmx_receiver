# docker_cmx_receiver

This is a Python/Docker/Docker-Compose implementation of a [Meraki Scanning API receiver](https://developer.cisco.com/meraki/scanning-api/#!introduction/scanning-api). 

- cmxreceiver.py This is the flask cmx receiver. It's necessary to define  SECRET, VALIDATOR, PORT environment variables before running the script. The content of the HTTP POSTs is just printed as a part of the output of the script. 
- Dockerfile. File to build cmxreceiver docker image. The [image](https://hub.docker.com/r/dangalle/cmx-receiver) can also be found on dockerhub. 
- docker-compose.yml. Docker compose file to have a cmx receiver with HTTPs. It uses ngrok image in order to support HTTPS. If you need another solution/docker-image to support HTTPS, modfiy ngrok_cmx section.
