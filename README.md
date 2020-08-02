# Application

Application : 
This directory consists of the following files and folders.

		 1)Producer and Consumer Application
		 2)docker-compose.yaml to use for dev 
		 3)deployment.yaml file in the folder "deployments" for minikube deployment
		 4)Makefile to build the image of producer and consumer application using docker-compose up
		 

For development environment:

	1)	use the cmd : make build
	[Make file helps in building the images for producer and consumer application using respective docker file
	which is in its directory]
	
	2)	use the cmd : make start
	[This command executes the docker-compose commands in makefile]
	
	3)	Hit the end points to push the message and to get the count of it .
	https://www.getpostman.com/collections/5035358c6754bd8e2619 [Use this link and import the collection to Postman]
	

Deployment :
prerequisites:

	1) Minikube installed and kubectl installed 
	[link to access :https://kubernetes.io/docs/tasks/tools/install-minikube/]
	
	or
	Use the https://kubernetes.io/docs/tutorials/hello-minikube/ to launch the terminal with kubernetes environment.
	

Steps:

	1) Git clone the project 
	2) Go to directory "deployments" which has deploy.sh 
	   and run the cmd : ./deploy.sh 
     [which applies the deployment files]
	3) Execute the curl command to hit the apis : 
	   producer endpoint :curl --location --request POST 'http://{cluster_ip}/message/push --header 'Content-Type: application/json' --data-raw '{"message": {"triggered":true}}'
	   consumer end point :curl --location --request GET 'http://{cluster_ip}/message/count'
	   
	
Image Info:
Images for producer and consumer application have been pushed to dockerhub:
https://hub.docker.com/repository/registry-1.docker.io/vishwithan/dockerhub/





			  

			  
