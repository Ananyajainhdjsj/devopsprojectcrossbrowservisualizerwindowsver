# Cross-Browser Test Result Visualizer
---

Student Name: Ananya Jain  
Course: CSE3253 DevOps   
Project Type: Jenkins & CI + Selenium Automation  
Difficulty: Intermediate  

---
## Documentation

- [ ] README
- [ ] Technical documentation
- [ ] User guide
- [ ] API documentation 

---

### README
## Project Overview: 
This README provides an overview of the project, setup instructions, technology stack, and project structure. 

### Problem Statement

In real-world DevOps environments, Selenium tests are executed across multiple browsers (Chrome, Firefox, Edge). However, results are usually scattered across logs and XML files, making it difficult to:

- Compare browser performance
- Identify failures quickly
- Visualize execution trends
- Monitor CI test quality

This project builds a centralized dashboard to visualize cross-browser Selenium test results in real time.

---

##  Objectives

- Collect Selenium test results automatically
- Store test data in PostgreSQL
- Visualize pass/fail comparison across browsers
- Compare execution times
- Integrate with Jenkins CI pipeline
- Containerize using Docker

---

## Key Features

- Cross-browser Selenium testing (Chrome & Firefox)
- REST API to collect test results
- PostgreSQL database storage
- Interactive dashboard with Chart.js
- Docker multi-container setup
- Jenkins CI pipeline automation

---

##  Technology Stack

### Core Technologies
- Python 3.10+
- Flask
- SQLAlchemy
- PostgreSQL
- Selenium
- Chart.js

### DevOps Tools
- Git
- Docker
- Docker Compose
- Jenkins
- Pytest

---
##  Project Structure

```
devopsprojectcrossbrowservisualizer/
│
├── README.md
├── requirements.txt
├── docker-compose.yml
│
├── src/
│   └── main/
│       ├── app.py
│       ├── models.py
│       ├── routes.py
│       ├── config.py
│       ├── extensions.py
│       └── templates/
│           └── dashboard.html
│
├── tests/
│   └── selenium/
│       ├── chrome.py
│       └── firefox.py
│
├── infrastructure/
│   └── docker/
│       ├── Dockerfile
│       └── wait-for-db.sh
│
└── pipelines/
    └── Jenkinsfile
```
##  Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.10+
- Firefox or Chromium installed (for local Selenium execution)

---

##  Run With Docker

From the project root:

```bash
docker-compose up --build -d
---
Open the application in your browser:

http://localhost:8080

---

###  Activate Virtual Environment (if using one)

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

```bash
Chrome tests:
pytest tests/selenium/chrome.py
Firefox tests:
pytest tests/selenium/firefox.py
```
```bash
When tests run, they automatically send results to:
POST /api/results
```

 

### Technical Documentation
- **Architecture:**
    - Flask backend serves REST API and dashboard.
    - Selenium scripts run browser tests and POST results to backend.
    - PostgreSQL stores test results.
    - Jenkins pipeline automates test execution and deployment.
- **Key Files:**
    - `src/main/app.py`: Flask app entry point.
    - `src/main/routes.py`: API endpoints and dashboard routes.
    - `src/main/models.py`: SQLAlchemy models for test results.
    - `tests/selenium/`: Selenium test scripts for Chrome, Firefox, Edge.
    - `infrastructure/docker/Dockerfile`: Container build instructions.
    - `pipelines/Jenkinsfile`: CI pipeline definition.
- **Data Flow:**
    1. Selenium test runs →
    2. Result sent to Flask API →
    3. Stored in PostgreSQL →
    4. Dashboard visualizes results.

### User Guide
1. **Setup:**
     - Install Docker, Python, and browsers.
     - Clone repo and run `docker-compose up --build -d`.
2. **Run Tests:**
     - Activate virtualenv, install requirements.
     - Run `pytest tests/selenium/chrome.py` or `firefox.py`.
3. **View Dashboard:**
     - Open `http://localhost:8080` in browser.
4. **CI Pipeline:**
     - Jenkinsfile automates test and deploy steps.

### API Documentation
#### Submit Test Result
- **POST** `/api/results`
    - **Body:** `{ "browser": "chrome", "status": "pass", "duration": 2.5 }`
    - **Response:** `{ "success": true }`

#### Get All Results
- **GET** `/api/results`
    - **Response:** `[ { "browser": "chrome", "status": "pass", "duration": 2.5 }, ... ]`

#### Dashboard
- **GET** `/`
    - Renders dashboard.html with charts and statistics.


