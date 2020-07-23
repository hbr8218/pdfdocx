# pdf to docx Converter

## Table of Content
  * [Overview](#overview)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Directory Tree](#directory-tree)
  * [To Do](#to-do)
  * [Bug Request](#bug-request)
  * [Technologies Used](#technologies-used)
  * [License](#license)
  * [Credits](#credits)


## Overview
This is flask app that convert a pdf file into docx format using api. User has to upload a pdf file and on pressing the convert button the file will be converted into file with .docx format and will redirect to another page from where user can download converted file.

## Technical Aspect
This project has been divided into three parts:-
  1. Sign up account in the following website to get required keys to use the API.(breifly explained below)
    [Get your app_sid and app_key]( https://dashboard.groupdocs.cloud )
  2. Simple flask app has been developed with attractive UI/UX design.
  3. Made the localhost live on Internet(Optional). Steps:-
      - Sign up an account in [ngrok](https://www.ngrok.com/)
      - Download binary, compatible with the OS.
      - Unzip the binary
      - Running this command will add your authtoken to the default ngrok.yml configuration file. This will grant you access to more features and longer session times.
        Running tunnels will be listed on the status page of the dashboard. </br>
        `./ngrok authtoken 1eyhBFdmZkCpEGW8Eo6t6xteZtZ_3y6Z5j4TBMHf4tXy7ed2Q`


## Installation
The code is written in python3. So if you don't have python3 installed on your system then do the followings:-

### For Linux(Ubuntu) and macOS users
- `sudo apt-get install python3`
- `sudo apt-get install python3-pip`
- `pip3 install virtualenv`
- In your project directory, excecute `virtualenv venv` where 'venv' is the name of your virtual environment for the project.
- Activate your virtual environment using `path/bin/activate`, where path should be absolute path of the virtual environment.
- Update ~/.bashrc using:- </br>
`echo "source '`which activate.sh`' "` , remove single qoutes, and </br>
`source ~/.bashrc`
- create a .env file in the project's root directory and add the write the followings:- </br>
  `source path/bin/activate` </br>
  APP_SID="YOUR_APP_SID_KEY" </br>
  APP_KEY="YOUR_APP_KEY"
  

### For Windows users:-
Above steps(for linux and macOS users) may not work for windows user so they can do the following steps:-
- Install python3 (Refer any good video and blogs)
- Install virtualenv and activate it (Refer any good video and blogs)
- Add environment variables:- </br>
  APP_SID="YOUR_APP_SID_KEY" </br>
  APP_KEY="YOUR_APP_KEY"


## Run
Run the following command to install all required libraries/dependencies:- </br>
`pip install -r requirements.txt` </br>
Finally, Execute `python app.py` to run the app

## Directory Tree
```
.
├── app.py
├── config.py
├── downloads
│   └── download.txt
├── ngrok
├── package
│   ├── __init__.py
│   └── pdftoword.py
├── requirements.txt
├── static
├── templates
│   ├── api_exception.html
│   ├── download2.html
│   ├── index3.html
│   └── unhandlederror.html
└── uploads
    └── upload.txt
```

## Bug Request
If you find any bug, inform me at hbr8218@gmail.com

## To Do
- Add options for users to select files from cloud storages like Goolge Drive, Microsoft onedrive, etc.
- Deploy on AWS for production.

## Technologies used
![alt text](https://user-images.githubusercontent.com/42790586/88217854-ca48c880-cc7c-11ea-856c-103d74ce7b1c.jpeg)

## License
I worked in the development of this project asked by my college Md. Farhan for a client (@Seema Sharma Dubey)

## Credits
- This project wouldn't have been possible without Groupdocs API. It saved my enormous amount of time
- Md. Farhan who helped in Frontend part.

