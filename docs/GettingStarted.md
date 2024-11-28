## Getting started with your project

First, create a repository on GitHub with the same name as this project, and then run the following commands:

```bash
git init -b main
git add .
git commit -m "init commit"
git remote add origin git@github.com:sreekants/cospy.git
git push -u origin main
```

Finally, install the environment and the pre-commit hooks with

```bash
make install
```

You are now ready to start development on your project!



## Setting up a runtime environment
You will need to set up a few runtime variables for the simulation to run properly.

## Getting started with your project

Assume that you have cloned this git repository into a folder at *PATH_TO_COS_REPOSITORY*. Follow the instructions below to setup the environment

### Linux & MacOS setup
Setup the following environment variables by adding the following lines to your ~/.bashrc file or ~/.zshrc (depending on the shell you prefer to use). 

```bash
export COS_ROOT="*PATH_TO_COS_REPOSITORY*"
export COS_CONFIG="${COS_ROOT}/config"
export PYTHONPATH="${PYTHONPATH}:${COS_ROOT}/src"
```

Note that on the MacOS, the default shell is zsh and on Linux it is bash. Either way, what you want is the directories to show up in your environment variables. You can verify the setup with the *printenv* command that will dump out the variables for you.  

### Quickstart installation of python packages
If you are only installing the prerequisite python packages and prefer not to develop software on the repository, you can install the prerequisite files form the requirements.txt with the following command. 

```bash
pip install -r requirements.txt
```

If you have trouble with the python package installation, it is most likely a version mismatch. You may have to install a packages manually by looking at the requirements.txt.

### Checking your setup.
If you have got all your dependeicies and environment variables setup you should be good to go already. You can verify if everything is running by booting up the kernel. To do that, you change directory to *apps/coslaunch* under your installation dierctory. When you are at this folder, start the kernel with the following command:

```bash
/home/jdoe/devel/cospy/apps/cosservice$ python main.py
```

If all goes well, you should see an output like the following..

```bash
COS Simulation Operating system
Version: 1.0 [07 Mar 2018]
22/04/24 12:55:56 (Kernel) Initializing...
22/04/24 12:55:56 (Loader) Loading Kernel: Subsystem
22/04/24 12:55:56 (Loader) Loading Subsystem
22/04/24 12:55:56 (Loader)   level-0: /home/jdoe/devel/cospy/config/subsystem.yaml.
22/04/24 12:55:56 (Loader)    + Module: cos.core.subsystem.RPCBroker 
22/04/24 12:55:56 (Loader)    + Module: cos.core.subsystem.NetworkManager 
22/04/24 12:55:56 (Loader)    + Module: cos.core.subsystem.DataManager 
22/04/24 12:55:56 (Loader)    + Module: cos.core.subsystem.World 
22/04/24 12:55:56 (Loader) Loading Faculties: Environment,Monitors,Signals,Actors,Rules
22/04/24 12:55:56 (Loader) Loading Environment
....
22/04/24 12:55:57 (Loader)    + Module: cos.core.service.Sea 
22/04/24 12:55:57 (Loader)    + Module: cos.core.service.Vessel 
22/04/24 12:55:57 (RPC) Listening for RPC on [tcp://*:5556]
22/04/24 12:55:57 (IPC) Posting IPC events on [tcp://*:5557]
Press Enter to exit...
```

Pressing a key at this prompt shuts down the kernel. But otherwise, the kernel is up and running. You can visualize the kernel by likewise, change directory to *apps/cviz* under your installation dierctory. When you are at this folder, start the visualization with the following command:


```bash
/home/jdoe/devel/cospy/apps/cviz$ python main.py
pygame 2.5.2 (SDL 2.28.3, Python 3.12.2)
Hello from the pygame community. https://www.pygame.org/contribute.html
Connecting to tcp://localhost:5556
Connecting to tcp://localhost:5556
Collecting updates from world server on tcp://localhost:5557...
Connecting to tcp://localhost:5556
```
