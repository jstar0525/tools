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
```
xauth nlist $DISPALY | sed -e 's/^..../ffff/' | xauth -f /tmp/.docker.xauth nmerge -

docker build -t robotis:kinetic .

docker run -it \
    --name="kinetic" \
    -e NVIDIA_VISIBLE_DEVICES=all \
    -e NVIDIA_DRIVER_CAPABILITIES=all \
    -e unix$DISPLAY \
    --env="QT_X11_NO_MITSHM=1" \
    --env="XAUTHORITY=/tmp/.docker.xauth" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="/tmp/.docker.xauth:/tmp/.docker.xauth:rw" \
    --device=/dev/ttyUSB0 \
    robotis:kinetic

docker commit kinetic robotis:kinetic

docker exec -it kinetic /bin/bash
```

## ROBOTIS OpenMANIPULATOR-X U2D2
```
# If you are using docker, then install both container and host

sudo cp /99-open-manipulator-cdc.rules /etc/udev/rules.d/

# sudo apt install udev

sudo udevadm control --reload-rules
sudo udevadm trigger

# TIP: This entered command set USB latency timer to 1 ms. 
# If you would like to see the setting, run the following command in a terminal.
cat /sys/bus/usb-serial/devices/ttyUSB0/latency_timer
```

## Add alias in docker
```
source /opt/ros/foxy/setup.bash
source /home/mani_ws/install/local_setup.bash
```

## Docker hub

https://hub.docker.com/_/Ros
