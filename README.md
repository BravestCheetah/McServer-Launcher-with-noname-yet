# StructureBlock

## Notice
The Project Is Still In Early Developement And is not Useable in its current state, if you wanna use StructureBlock to manage your servers you can add BravestCheetah on discord and request to get pinged when we are ready to release the first test release!

This README is incomplete and mostly only contains notes for developers at the moment as the project is not ready for releases yet.

## Installation
Sadly there arent any versions of StructureBlock yet but we are planning on releasing it using docker for ease of installation sometime in the near future.

## How To Use
This section will be written when we release the projects first release

## How To Contribute

### Setup
First of all clone the repository using git:
`git clone https://github.com/BravestCheetah/StructureBlock`

Then to contribute to the project you need some dependencies:
* Python
* uv

All other dependencies will be installed by uv automatically when needed to create a developement enviorment where all users will have the same enviorment to prevent different enviorment from breaking other.

Then to install dependencies with uv you will have to run:
`uv sync`
in the root of the repository.

### Tests
To run tests (to check functionality on backend) run
`uv run pytest`
and lastly to create tests just create them following the [pytest docs](https://docs.pytest.org/en/stable/) in `/tests` named well to not confuse other developers.

### Pushing
To push please put your commits in a pull request which will be reviewed by one of the head developers and merged if no conflicts emerge, if the changes are confirmed but has conflicts the contributor is requested to fix these conflicts before being merged into main.

## Forking
You are allowed to fork the project and redistribute it if you credit the original project - this one :) - and the developers of this project. 
You are NOT allowed to fork and/or redistribute the project and claiming it as your own or redistributing it without changing it, we encourage you to make this project your own! This is supposed to be an amazing project, but if you try to make it your own, you can make it even better! Dont copy, thats not fun for anyone :(
