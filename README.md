# Introduction

In [this GitHub repository](https://github.com/arod40/swe-k8s.git) you will find:

1. A folder `k8s/` containing several Kubernetes configuration files, corresponding to the components of the system shown in the presentation demo.
2. The file `people-api.json` that contains a Postman collection that you can use to interact with the system once it is set up. You can import this collection into Postman following this [instructions](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-postman-data). 
<!-- 3. A 'README.md' file containing a description of the server API that you need to consume; instructions to set up the prerequisites for the assignment; and a non-comprehensive list of minikube and kubectl commands that you may need in the assignment. You can use --help option in either tool if you need further explanation for those or other commands. Also, you can revisit the resources provided in the presentation slides. -->


I tested the instructions and environment provided in Windows 10 OS, but the setup should be almost identical in UNIX-based operative systems. Please, reach out to me if you have any issues setting everything up.

# Pre-requisites

1. Install Minikube: [https://minikube.sigs.k8s.io/docs/start/](https://minikube.sigs.k8s.io/docs/start/)
2. Install a virtualization driver for minikube. I used Docker. See [here](https://minikube.sigs.k8s.io/docs/drivers/) for available options in each OS. Either Docker or VirtualBox must be fine in any OS
   - Docker [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
   - VirtualBox [https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)  
3. Start a Minikube local cluster: `minikube start`


# API description

The API exposes a single resource `/people`, and all the CRUD operations for an entity Person that contains attributes `id` and `name`.

Here is a publicly available description: [https://documenter.getpostman.com/view/20589489/2s8YK6NSaZ](https://documenter.getpostman.com/view/20589489/2s8YK6NSaZ)

# Cheat-sheet: minikube

1. `minikube start`: Starts a local cluster and links minikube to it.
2. `minikube stop`: Stops the local cluster
3. `minikube status`: Checks the status of the local cluster

# Cheat-sheet: kubectl

1. `kubectl apply -f [filepath]`: Applies the configuration file `'filepath'`  to the local cluster. This is used to create components from configuration files.
2. `kubectl get all`: Gets a description of the components created in the cluster.
3. `kubectl get [pod|service|deployment|...]`: Gets a list of the components of the specified type.
4. `kubectl describe [component-name]`: Shows a detailed description of a component.
5. `kubectl logs [pod-name] -f`: Connects to a pod and stream the logs of the container(s) running inside.
6. `kubectl port-forward [component-name]`: Exposes the port of a component to be accessed by an application in your local computer (e.g. Postman).
7. `kubectl delete [component-name]`: Delete a component.

# Assignment

Make a video of your screen showing your execution of the following tasks. For each task, it is described what needs to be shown in the video. I suggest to rehearse these tasks before recording the video, so that you can make sure what to expect in a success scenario. You can always delete the components created during practice using the `kubectl delete` command.

1. Show the output of the command  
   ```console
   kubectl get all
   ```
   to make sure you deleted everything you created while practicing. Your output should look like this:  
   ```console
   NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
   service/kubernetes         ClusterIP   10.96.0.1        <none>        443/TCP          2d20h
   ```  
   Note there is a service `service/kubernetes` created by default. Do not delete this service!😱

1. Reproduce the system presented in the class demo. You should use the configuration files provided. This entails creating all the components in the APPROPRIATE ORDER 😉. Show your terminal while you setup the system. (Hint: Recall the `kubectl apply` command)

2. Expose the port 8080 of the service `service/flaskapp-service` in order to connect to it from your local computer. To do that, you run:  
   ```console
   kubectl port-forward service/flaskapp-service 8080:8080
   ```  
   Interact with the server API (call a couple of CRUD operations from Postman) and show which pod received each API call via their logs. The flask server is configured to log each API call. (Hint: Recall the `kubectl logs` command)

3. Without killing the cluster and starting everything over, make the cluster scale the `flaskapp-server` deployment to three replicas instead of the existing two. Show the output of the command  
   ```console
   kubectl get pods
   ``` 
   It must show the three replicas.

Reach out if you have any issues or questions. Hope you enjoy it. 😀