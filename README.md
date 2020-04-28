# Deploy a flask app to OpenShift and connect to db2 using an OpenShift secret

Applications nowadays are built in many different source codes and in many components hence comes the concept of microservices 
where you build your application in different small pieces (containers) and use some orchestration tool hat can orchestrate 
your processes simply and ensure that all tasks happen in the proper order.

RedHat's Openshift has emerged as a leading hybrid cloud, enterprise Kubernetes application platform that can help with containerizing, deploying, and monitoring your application. It delivers a cloud-like experience as a self-managing
platform with automatic software updates and lifecycle management across hybrid cloud environments.

In today's tutorial, we will see how easy it is to deploy an app and connect it securely to a database elsewhere using Openshift
secret to ensure credentials are encrypted yet accessible to our application, Openshift will automatically detect our framework
containerize, deploy, and manage our application in a span of minutes.

# Prerequisites
In order to follow the tutorial you should have.

- Active IBM cloud account, please create one if you don't have one on [IBM Cloud](https://cloud.ibm.com/registration)
- provisioned OpenShift 4.2, you can provision yours [here](https://cloud.ibm.com/kubernetes/landing?platformType=openshift)

# Estimated Time
This tutorial should take about 45 min to complete.

# Steps

1- create a db2 database on IBM cloud

- Go to Catalog -> choose services from the left pane -> tick the database checkbox -> choose db2




- 
