Install Nvidia-driver on ubuntu 18.04
=====================================

## List hardware display info.
Check graphics card recognition
```
$ sudo lshw -C display
```
```
*-display
       description: VGA compatible controller
       product: NVIDIA Corporation
       vendor: NVIDIA Corporation
       physical id: 0
       bus info: pci@0000:01:00.0
       version: a1
       width: 64 bits
       clock: 33MHz
       capabilities: pm msi pciexpress vga_controller bus_master 
                     cap_list rom
       configuration: driver=nouveau latency=0
       resources: iomemory:600-5ff iomemory:600-5ff irq:144 
                  memory:80000000-80ffffff 
                  memory:6000000000-600fffffff 
                  memory:6010000000-6011ffffff 
                  ioport:4000(size=128) 
                  memory:81000000-8107ffff
```
----
## Determine the latest version of Nvidia driver available for your graphics card

1. Visit the graphics drivers PPA homepage [here](https://launchpad.net/~graphics-drivers/+archive/ubuntu/ppa) and 
determine the latest versions of Nvidia drivers

2. Verify that your graphics card is capable of running the latest drivers.

If your graphic is supported, you can go ahead and remove all previously installed Nvidia drivers on your system. Enter the following command in terminal.

```
sudo apt-get purge nvidia*
```

## Add the graphics drivers PPA

Let us go ahead and add the graphics-driver PPA

```
$ sudo add-apt-repository ppa:graphics-drivers
$ sudo apt-get update
```

## 1. Auto install

```
$ sudo ubuntu-drivers autoinstall
```

## 2. Optional install

Search Nvidia drivers
```
$ sudo apt-cache search NVIDIA driver metapackage
```
```
vdpau-driver-all - Video Decode and Presentation API for Unix (driver metapackage)
nvidia-driver-390 - NVIDIA driver metapackage
nvidia-headless-390 - NVIDIA headless metapackage
nvidia-headless-no-dkms-390 - NVIDIA headless metapackage - no DKMS
bumblebee-nvidia - NVIDIA Optimus support using the proprietary NVIDIA driver
nvidia-driver-450 - NVIDIA driver metapackage
nvidia-driver-460 - NVIDIA driver metapackage
nvidia-headless-450 - NVIDIA headless metapackage
nvidia-headless-460 - NVIDIA headless metapackage
nvidia-headless-no-dkms-450 - NVIDIA headless metapackage - no DKMS
nvidia-headless-no-dkms-460 - NVIDIA headless metapackage - no DKMS
nvidia-driver-418-server - NVIDIA Server Driver metapackage
nvidia-driver-450-server - NVIDIA Server Driver metapackage
nvidia-headless-418-server - NVIDIA headless metapackage
nvidia-headless-450-server - NVIDIA headless metapackage
nvidia-headless-no-dkms-418-server - NVIDIA headless metapackage - no DKMS
nvidia-headless-no-dkms-450-server - NVIDIA headless metapackage - no DKMS
nvidia-driver-410 - NVIDIA driver metapackage
nvidia-driver-415 - NVIDIA driver metapackage
nvidia-headless-410 - NVIDIA headless metapackage
nvidia-headless-415 - NVIDIA headless metapackage
nvidia-headless-no-dkms-410 - NVIDIA headless metapackage - no DKMS
nvidia-headless-no-dkms-415 - NVIDIA headless metapackage - no DKMS
```
Select and install Nvidia graphics drivers.    
Enter the following command to install the version of Nvidia graphics supported by your graphics card 
**(xxxx - is the Supported Version for your Nvidia driver)**
```
$ sudo apt-get install nvidia-driver-xxxxx 
```

## Reboot

```
$ sudo reboot
```
-----
## Check install
```
$ nvidia-smi
```
```
Thu Feb  4 19:01:34 2021       
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.39       Driver Version: 460.39       CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  GeForce GTX 165...  Off  | 00000000:01:00.0 Off |                  N/A |
| N/A   42C    P8     2W /  N/A |    164MiB /  3911MiB |      5%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1314      G   /usr/lib/xorg/Xorg                 95MiB |
|    0   N/A  N/A      1499      G   /usr/bin/gnome-shell               66MiB |
+-----------------------------------------------------------------------------+

```
-----
## Reference
* https://askubuntu.com/questions/1054954/how-to-install-nvidia-driver-in-ubuntu-18-04
* https://codechacha.com/ko/install-nvidia-driver-ubuntu/   
* https://oofbird.tistory.com/55