![](../images/artemis.png)
Chapter 0: Development Environment Setup
=====

## Content

[Why Linux?](#why-linux)
> Brief explanation on why you should consider learning how to use Linux
[Hypervisor Intallation](#hypervisor-installation)
> Choosing and installing a hypervisor
[Linux Installation](#linux-installation)
> Finding and installing linux
[Common Issues](#common-issues)
> Having trouble? Look here!
[Resources](#resources)
> List of resources for when things inevitably go wrong

-----

### Why Linux?

Linux has many open source and free distrobutions available. The command line interface and how tools are installed and maintained make Linux operating systems ideally suited for software development. Additionally, your project may require use of Linux. Additonally, if you set up your development environment following this guide, not only can I help troubleshoot issues you may be having, but you will also be able to follow along with the rest of this guide.

### Hypervisor Intallation

First, what is a hypervisor? A hypervisor is software that can create and run irtual machines. A virtual machine is a virtualized environment that emulates a computer's operating system. Think of it as a computer inception.

We must choose which hypervisor software we want to use. I recommend two differe hypervisors: VMware, and VirtualBox. For Windows, both VMWare and VirtualBox are free. For Mac, only VirtualBox is free. VMWare, however, does have a paid version that you can get for free through Florida Tech so long as you are enrolled in a CSE coded course. Here are my recommendations:

> For MacOS users:	[VMWare fusion](https://www.vmware.com/products/fusion.html)

> For Windows users: 	[VirtualBox](https://www.virtualbox.org/)

Please follow the installation guide for whichever hypervisor you choose. 

### Linux Installation

The linux distribution I am recommending you use is Ubuntu 18.04. There are many distributions of Linux. You can choose any disribution you'd like, but be warned, there may be unintended issues with the VM should you continue following this guide (i.e. things may not install or operate the same).

Download here: [Ubuntu 18.04](https://ubuntu.com/download/desktop)

After downloading Ubuntu, you need to create a virtual machine using the hypervisor you installed in the step above. Please follow the guides provided below:

> For VirtualBox users: 	[VirtualBox Guide](https://askubuntu.com/questions/142549/how-to-install-ubuntu-on-virtualbox)

> For Windows VMWare users:	[VMWare Guide Windows](https://theholmesoffice.com/installing-ubuntu-in-vmware-player-on-windows/)

> For MacOS VMWare users:	[VMWare Guide Mac](https://graspingtech.com/vmware-fusion-ubuntu-18.04/)

### Common Issues

These are some of the common issues I've run into over the years of creating virtual machines:

* Insufficient disk space while creating the VM
 
	> This one is relatively simple. Sometimes when you create a virtual machine, the hypervisor incorrectly sizes what the VM needs to install the OS. This results in a failure during VM creation. To fix this, go back through the installation and make sure you add more disk space for the VM.
	> 

* Virtualization disabled in the BIOS
	
	> This one is a more difficult problem to sort out, mainly because everyone's boot keys are different per motherboard. You may need to find out what kind of motherboard you have and look up a guide on how to boot to the BIOS. Once in the BIOS, you can change the virtualization settings to enable you to creake and run a virtual machine.
	> Here is a link to an example: [Enabling virtualization](https://graspingtech.com/vmware-fusion-ubuntu-18.04/)
### Resources

If you have problems during installation and the developer's website is unable to provide an answer, please join the discord channel for FITSEC, Florida Tech's competitive hacking team. Most of the members in the channel will be able to help you with setting up a virtual machine. Ain invite link to the discord channel is provided under "getting involved" on FITSEC's website.

[FITSEC's website](fitsec.github.io)

![](../images/floridatech.png)
