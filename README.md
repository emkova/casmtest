![AI Badge](https://img.shields.io/badge/Chat_GPT_3.5-purple)
![SQL Badge](https://img.shields.io/badge/SQLite-purple)

# Content and Social Manager (C.A.S.M)
This web application is intended to help members of an organization brainstorm and organize content, primarily for online and social media. The current model is a single- page web application that allows users to interact with the AI assistant, asking questions and receiving a generated response.


## Table of Contents
- [Motivation](#motivation)
- [Build Status](#build-status)
- [Installation and Usage](#installation-and-usage)
- [Files](#files)
- [Contributing](#contributing)
- [Credits and Acknowledgements](#credits-and-acknowledgements)
- [License](#license)
- [Updated](#updated)

## Motivation
This project is being pursued in order to explore ways to utilize GenAI in the creative process and how it can be used to foster human-technology collaboration. The primary objective is to support team members in their creative projects through redistributing some of the workload and allowing them to use their time more effectively.

## Build Status
![Build Status Badge](https://img.shields.io/badge/build%20-%20in_progress-orange)


## Installation and Usage
There are various ways you can get access to a repository from GitHub. For more insight, refer to: [Get Started](https://docs.github.com/en/get-started/start-your-journey).

### Option 1
Due to the nature of the project, you likely will want to **download** the repository files to your local computer. This will allow you to view the files (and edit and customize them for your own purposes).

1. **Ready, set, go!**
Before you begin, ensure that you have *git* installed, as this is necessary for downloading casmtest from the project leader's GitHub.
```
sudo apt-get -y install git
```

2. **Download a copy of the files from GitHub.**
For a step-by-step guide, refer to: [Downloading Files](https://docs.github.com/en/get-started/start-your-journey/downloading-files-from-github).

3. **Configure your environment.**
Once you have unzipped the files, you are ready to configure your environment. Refer to the requirements.txt file to make sure you have the appropriate software installed.

For an in-depth overview of navigating Flask in a Python environment, refer to: [Visual Studio Code Flask Guide](https://code.visualstudio.com/docs/python/tutorial-flask).

Don't forget to configure your OpenAPI Keys! You can find a step-by-step guide at: [OpenAI website](https://platform.openai.com/docs/quickstart?context=python).

4. **Run the app.**
In terminal, change into the correct directory:
```
cd casmtest-main
```
If this returns an error, try copy and pasting the folder location link instead.

Use the Flask command or python -m flask to run the application. In order to do this, you need to specify to Flask where you application is, using the --app option.
```
python3 -m flask --app app run
```

If successful, terminal will provide a link, which you can then paste into your web browser. This is how you can interact with the front-facing end of the web application when you download the repository.

### Option 2
Another option you have is to **clone** the repository. This allows you to work from your local computer remotely, but gives you the ability to easily sync files to the GitHub-hosted repository.

1. **Create a folder.**
You can use your terminal to execute the following to create a new folder *git-final*. 

Make a directory:
```
mkdir git-final
```

Change to the correct directory:
```
cd git-final
```
2. **Clone the repository.**
Now, you can navigate to the desired repository.
```
git clone https://github.com/emkova/casmtest
```

This will now allow you to edit the folder from your local computer.
```
cd casmtest
```

For more in-depth information, refer to [Cloning A Repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository).

## Files
### README
This files contains an introduction to the project, an overview of the repository, and guidelines and tips for interacting with the web application. 
### LICENSE
Contains licensing information about the software.
### requirements.txt
Contains information about how the environment has to be set up in order to successfully run the software, including libraries, certificates, and packages. If you run into errors when trying to run the application, this is a good place to start for troubleshooting.
### pycache
These files were automatically generated when the program was first run, and act to improve the performance of subsequent executions. **You do not need to interact with these files.**
### static
Contains assets (images/logos) and specifics (main.css) for the user-facing interface of the application. **To change the design of the user-facing interface, edit the main.css file.**
### templates
Contains the file(s) which define the structure of and generates the Flask web application. As it is currently a single-page web application, the index.html file defines the static elements and design patterns (layout, structure, etc) of the user-facing interface.
### database.db
Stores the data (user queries) entered into the application, as well as the generated responses.
### schemas.sql
Defines the structure of the database tables, including column and data types.
### init_db.py
Contains the code to initialize the database, establishing a connection to database.db and schemas.sql. **Only to be run if you want to initialize the database.**
### db_test.py
Execute to check the contents of the database:
### app.py
This is the main Flask application, connecting with GPT-3.5 and the SQLite database (through database.db) to create the functioning user-facing interface and web application.

## Contributing
Please contact the project lead (em382884@dal.ca) with proposals. They will be reviewed and taken under consideration.

## Credits and Acknowledgements
Thank you to Dr. Colin Conrad for acting as the project supervisor and mentor, and finding the time to provide feedback ahead of schedule during a busy time.
I would also like to acknowledge the contributions of my previous work (*Hallie* and *REB-CT*), as this project builds upon them greatly.

## License
![License Badge](https://img.shields.io/badge/License-MIT-blue)


### Updated
April 2024
Emma Hak-Kovacs
![Department Badge](https://img.shields.io/badge/Dalhousie_University-MI-yellow)
![Workplace Badge](https://img.shields.io/badge/St_Mary's-PPL-red)
