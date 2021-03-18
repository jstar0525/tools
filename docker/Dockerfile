FROM ros:kinetic

RUN apt update
RUN apt upgrade

# run as nonroot user
RUN groupadd -g 999 robotis
RUN useradd -rm -d /home/kinetic_user -s /bin/bash -g robotis -G sudo -p "$(openssl passwd -1 kinetic)" -u 999 kinetic_user
USER kinetic_user
WORKDIR /home/kinetic_user