# StructureBlock
![GitHub repo size](https://img.shields.io/github/repo-size/BravestCheetah/StructureBlock)
![GitHub Issues Count](https://img.shields.io/github/issues/BravestCheetah/StructureBlock) 
![GitHub Repo stars](https://img.shields.io/github/stars/BravestCheetah/StructureBlock?style=flat&color=#fff700) 
![GitHub watchers](https://img.shields.io/github/watchers/BravestCheetah/StructureBlock?style=flat)


## Installation / Usage
As the project is still in so early developement any build or compiling scripts / ways have yet to be developed, if you are a developer please refer to the section below, if you are a user interested in using the project, remember that you can always come back later when an realease has been created :D


## Developing / Contributing
### Notice
The developement process relies on the [git](https://git-scm.com/) ecosystem and githubs integration with it, git is expected to be installed and linked to your github account during the developement process.
The enviorment is managed by the ![uv](https://github.com/astral-sh/uv) application which is also excpected to be installed before starting the developement process.

### Presetup
The first thing to do is cloning the repository, navigate to an appropriate directory and run the following command: 

``git clone https://github.com/BravestCheetah/StructureBlock``

and then proceed to navigate into the directory:

``cd StructureBlock``

the repository is now downloaded and you can begin the setup process!

### Dependencies
The project is made in Python and relies heavily on following libraries:
* Requests (Fetching data such as .jar files from the software sites)
* Pathlib (A wrapper for the os modules path functions, used all over the project to manage the different servers)
* NiceGUI (A library allowing you to easily create web based UI for the app)
* PyTest (The library used to run and create unit tests easily)

Note: All required dependencies will be installed automatically when following the next section (Enviorment), you do NOT have to install these dependencies manually or in any other way than the way listed below.

### Enviorment
The enviorment is managed by the ![uv](https://github.com/astral-sh/uv) application and all dependencies are managed by uv as well.
To set up the enviorment run the `uv sync`, this will let uv set up your local enviorment based on the lockfiles, it will install the .env python envoiormnet and required dependencies.
If any code you add or change require dependencies that are not already installed you can add them to the uv enviorment using `uv pip install <library>`. Do not install dependencies without using uv, this will not save to the uv enviorment and wont be installed by other developers which will end in errors and the libraries installed not being synced accross devices / users.

### Executing Code
To execute a script using the enviormennt uv manages run it via uv like this: `uv run <your_file>.py`, make sure the code works when being ran with the uv enviorment to ensure it works on others devices too.

### Unit Tests
Before pushing your code to github, please make sure it passes all unit tests, to run the unit tests start the [PyTest](https://docs.pytest.org/en/stable/) (it will be installed druing the uv enviorment setup) testing process by running `uv run pytest`. To create or edit unit tests, its quite simple, the unit tests are just python files located in the `/tests` directory. PyTest will automatically detect and run the files in the folder following [their documentation](https://docs.pytest.org/en/stable/)

### Pushing your code
yeah, just... push and create a pull request, the request will be reviewed and if it passes it will be merged :D

### Pulling code
make sure before pushing to pull (always, just to make sure) and resolve any merging conflicts BEFORE pushing and always rerun the sync command through uv to ensure your enviorment is always up to date to the latest developement enviorment to prevent errors when running newer code.


## Forking
You are allowed to fork the project and redistribute it if you credit the original project - this one :) - and the developers of this project. 
You are NOT allowed to fork and/or redistribute the project and claiming it as your own or redistributing it without changing it, we encourage you to make this project your own! This is supposed to be an amazing project, but if you try to make it your own, you can make it even better! Dont copy, thats not fun for anyone :(
