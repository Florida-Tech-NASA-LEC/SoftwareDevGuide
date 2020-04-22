![](../images/artemis.png)
Section 5: System Commands
=====

## Content

### [Subsection 0: System](#system)
> Brief description of the system commands
### [Subsection 1: System Commands](#system-commands)
> List of all of the system commands in this guide
### [Subsection 2: System Exercises](#system-exercises)
> Exercises to hone your skills

#### System

System commands help is discover information we need about the system, such as IP addresses and hostnames, find files or programs, and test connectivity.

#### System Commands

* [whoami](#whoami)	- Print the current username
* [hostname](#hostname)	- Print current hostname
* [ifconfig](#ifconfig)	- Print network connectivity information
* [ping](#ping)		- Test network connectivity
* [which](#which)	- Locate a program that is listed in the PATH variable

#### whoami

The whoami command is useful to determine which user you are currently logged into.

#### hostname

The hostname utility is useful for discovering the name of your computer. You may need to reference the name of a device in system configurations.

#### ipconfig

We have briefly covered ipconfig. This is a very useful network tool to discover a lot about how your current network configuration is set. I'll save more details for the network portion of this guide.

#### ping

Ping is a network connectivity tool that is useful for determining if you are able to communicate with another device over the network. In Linux, unlike Windows, ping continuously sends ICMP packets to the target host until you control-c out of the utility. One way to prevent this is with the -c flag. I will leave it up to you to determine how to use that flag with ping.

#### which

Which is useful when you're looking for the path to a program. For instance, perhaps you'd like to make a python script executable and would like to place a shebang at the top of the script, but you can't remember where python is located. If you run the following, you will find where python is in the file structure of the system.

> which python

#### System Exercises

* Find the path to python
* Find the name of your computer
* Find your IP address
	* Bonus points for if you can isolate your IP address with grep and cut
* Find you username

#### What you should have learned:

* ***How to find the path to a program***
* ***How to find the hostname of a device***
* ***How to find the IP Address of a device***
* ***How to test connectivity between two devices***

![](../images/floridatech.png)
