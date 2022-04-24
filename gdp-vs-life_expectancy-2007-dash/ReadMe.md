_______________________________________________________________
Creating a conda environment and installing dash
===============================================================
### 1.	Create a project directory
`mkdir my-dash-project && cd my-dash-project`

### 2.	Create a virtual environment within the project directory 
`conda create --prefix .\env	 <package>`	_creates a new environment in a sub-directory of the project directory called env. Packages can also be installed as well_ `conda create -–prefix .\env dash pandas`
  
### 3.	Activate the  conda environment 
`conda activate .\env`
  
### 4.	Check to see if the conda environment is created and currently active
`conda env list`	_Lists all existing conda environments and their locations_
  
### 5.	Check to see that all the packages needed for your project are currently installed in the current active environment.
`conda list`	_Lists name of all packages in current active directory_
  
### 6.	To prefix the command prompt with active environment’s generic name (env) on the prompt instead of the active environment’s absolute path which might become very lengthy and problematic
`conda config --set env_prompt ({name})`
  
### 7.	To deactivate an active environment
`conda deactivate`
