AI Grammar Checker
Project Overview
AI Grammar Checker is a web-based application developed with Python and Flask. It is designed to identify and correct common grammatical errors in user-provided sentences.

The project also demonstrates the use of Continuous Integration and Continuous Deployment (CI/CD) practices in software development.

Features
Accepts text from users through a web interface.
Checks submitted sentences for supported grammatical errors.
Provides a corrected version when a matching error is identified.
Automated testing through GitHub Actions.
Deployed online using Render.
Technologies Used
Python
Flask
HTML
Git and GitHub
GitHub Actions
Gunicorn
Render
CI/CD Pipeline
The project uses GitHub Actions for Continuous Integration (CI).

Whenever changes are pushed to the GitHub repository, the workflow runs automated checks and tests to help ensure that the application continues to work correctly.

The application is deployed as a Flask web service using Render.

Project Structure
AI-Grammar-Checker/
├── .github/
│   └── workflows/
│       └── ci.yml
├── templates/
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
How to Run Locally
Clone the repository.
Create and activate a Python virtual environment.
Install the required packages:
pip install -r requirements.txt
Run the application:
python app.py
Open the local address displayed by Flask in your web browser.
Deployment
The application is deployed as a web service on Render.

Live Application: Add the Render URL here after retrieving it.

Project Purpose
The purpose of this project is to demonstrate how a Python web application can be developed, tested, version-controlled, integrated with a CI pipeline, and deployed using modern software development practices.