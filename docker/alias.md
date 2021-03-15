# Setting alias on Ubuntu


## Edit the .bashrc file
```
$ sudo gedit ~/.bashrc
```

## Add alias related to docker
```
alias drun='docker run -it \
                --name="ros2_foxy" \
                --env="DISPLAY" \
                --env="QT_X11_NO_MITSHM=1" \
                --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
                --volume="/home/robotv/mani_ws:/home/mani_ws" \
                foxy:tutorial'  
alias dexec='docker exec -it ros2_foxy /bin/bash'  
alias dcommit='docker commit ros2_foxy foxy:tutorial'
alias drm='docker rm $(docker ps -q -f status=exited)'
```
## Save and Restart
```
$ source ~/.bashrc
```

## Command for docker
```
$ docker run -it \
    --name="ros2_foxy" \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="/home/robotv/mani_ws:/home/mani_ws" \
    foxy:tutorial

$ xhost +local:root

$ docker exec -it ros2_foxy /bin/bash
$ source /opt/ros/foxy/setup.bash

$ docker commit ros2_foxy foxy:tutorial
```

## Add alias in docker
```
source /opt/ros/foxy/setup.bash
source /home/mani_ws/install/local_setup.bash
```

## Docker hub

https://hub.docker.com/_/Ros
