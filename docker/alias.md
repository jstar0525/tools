# Setting alias on Ubuntu


## Edit the .bashrc file
```
$ sudo gedit ~/.bashrc
```

## Add alias related to docker
```
$ alias drm='docker rm $(docker ps -q -f status=exited)' 
$ alias dr='docker run -it --gpus all -v "/home/robotv/mani_ws/:/home/mani_ws/" ros:foxy-ros-base-focal'
```

## Save and Restart
```
$ source ~/.bashrc
```

## Docker hub

https://hub.docker.com/_/Ros
