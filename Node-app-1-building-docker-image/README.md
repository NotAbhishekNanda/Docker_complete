# Docker_complete


Steps followed so far:

1. Created a dockerfile

2. Build a docker image using command - docker build .

3. It will build a docker image based on the Dockerfile and give an Id.(It wraps the node environment which already exists(downloads from docker-hub) and then it will set up an image for an contatiner to be launched; for which all the setup steps to be executed inside of the image. It gives us an image which is prepared to be started in a container)

4. We will use the id and then run a container based on the image using - docker run command.
Command = docker run -p (port-number-if there is):(port-number-if there is) <id>

=> Now app is up and running in the given port in dockerfile

5. For stopping the file
-> open-up a new terminal
-> docker ps = to see the name of the container and grab the name of the container
-> docker stop <container-name>

=> Now the app is stopped.


