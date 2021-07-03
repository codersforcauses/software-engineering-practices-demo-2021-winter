# Software Engineering Practices Demo
This repository is about demonstrating the usual workflow of software engineers in the real-world.

There are usually a couple parts:

- Issues / tickets
- Kanban board (todo, in progress, review)
- Pull Requests
- Code Reviews

## Setup
Please run the following script (type the command in the terminal) before proceeding:

Clone the repository (if you have not already. Command: `git clone https://github.com/codersforcauses/software-engineering-practices-demo.git`)

**Note:** For windows git is not built-in. Install git from https://github.com/git-for-windows/git/releases/download/v2.32.0.windows.1/Git-2.32.0-64-bit.exe


### Windows Python Path Setup
```
env.bat
```

Install

### Linux/Mac Python Path Setup
```
env.sh
```

## Instruction
Do the following:

1. Look at the github issues
2. Assign yourself an issue
3. Create a branch with the following format `s{Issue Number}-{Issue Name}`. `git checkout -b s{Issue Number}-{Issue Name}`
4. Create the change to satisfy or complete the github issue
5. Commit (package) the change `git commit -m "{insert message here}"` and push `git push`.
6. Create a pull request and request for a reviewer from CFC peeps