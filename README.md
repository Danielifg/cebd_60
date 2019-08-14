# Big Data Technologies cebd_60
Concordia Univ. Big Data Diploma Summer 2019

# Cointainers & Kubernates Essentials with IBM Cloud

![alt text](K8sDeploy.png "Logo Title Text 1")


The isolation on Linux is provided by a feature called namespaces. Each different kind of isolation, that is, user and cgroups, is provided by a different namespace.

This is a list of some of the namespaces that are commonly used and visible to the user:

	- PID: process IDs
	- USER: user and group IDs
	- UTS: host name and domain name
	- NS: mount pointsNET: network devices, stacks, and ports
	- CGROUPS: control limits and monitoring of resources

  
![alt text](K8s_terms.png "Logo Title Text 1")

# Push an image to IBM Cloud Container Registry

	- ibmcloud login
	- ibmcloud cr login "get region ng"
	- ibmcloud cr namespace-add <my_namespace>
	- Inside project wd run:
		  docker build --tag us.icr.io/<my_namespace>/hello-world . 
  - verify with `docker images`
## Push that image to IBM Cloud Container Registry:

docker push us.icr.io/<namespace>/hello-world

	- ibmcloud ks clusters
	- ibmcloud ks workers

# Deploy Application
### Get the command to set the environment variable and download the Kubernetes configuration files: 
`ibmcloud cs cluster-config <cluster_name_or_ID>`

Display Namespaces
`kubectl get ns`

Get k8s Deployments
`kubectl get deployments`

### SET KUBECONFIG env var
`export KUBECONFIG=/Users/flodan00/.bluemix/plugins/container-service/clusters/Broker_v1/kube-config-hou02-Broker_v1.yml`
### Run your image as a deployment:
`ibmcloud cr namespaces`

`kubectl run hello-world --image=us.icr.io/<namespace>/hello-world`

### get status of pods
`kubectl get pods`
### Troubleshoot status imagepullbackoff
`kubectl describe pod <pod Name/ID>`

### When the status reads Running, expose that deployment as a service, which is accessed through the IP of the worker nodes. The example for this lab listens on port 8080. Run this command:
 
`kubectl expose deployment/hello-world --type="NodePort" --port=8080`

## Describe deployment and get public ports
` kubectl describe service hello-world-app`

## Take cluster name with ibcloud K8s plug-in
`ibmcloud  ks clusters`

## Get cluster public IP
`ibmcloud cs workers <clusterName>`

# Update and roll back:
	- make changes to code
	- build image with --tag <region/namespace/image>



## Make a change to your code and build a new docker image with a 	new tag:

`docker build --tag us.icr.io/<namespace>/hello-world:2 .`

Push the image to the IBM Cloud Container Registry:

docker push us.icr.io/<namespace>/hello-world:2

Using kubectl, update your deployment to use the latest image. You can do this in two ways:
Edit the YAML file again by using kubectl edit deployment/<name-of-deployment>
## Specify a new image by using a single command. Using a single command is especially useful when writing deployment automation. To specify the new image, run this command:

`kubectl set image deployment/hello-world hello-world=us.icr.io/<namespace>/hello-world:2`

A deployment can have multiple containers in which case each container will have its own name. Multiple containers can be updated at the same time. For more information about setting images, see the kubectl reference documentation.

Check he status of the rollout by running one of these commands:
`kubectl rollout status deployment/<name-of-deployment>`

`kubectl get replicasets`
