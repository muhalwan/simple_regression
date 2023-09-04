---

# ML DevOps: Simple Regression Model

This repository contains a machine learning project that integrates a simple regression model with DevOps practices. The model is served as an API using Flask and can be containerized using Docker.

## Table of Contents

- [Overview](#overview)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Testing with Postman](#testing-with-postman)
- [Docker Deployment](#docker-deployment)
- [Contributing](#contributing)
- [License](#license)

## Overview

The purpose of this project is to showcase how Machine Learning can be integrated with DevOps. It consists of:

- A simple regression model trained on a generic dataset.
- A Flask API that serves the trained model.
- Docker support for containerizing the application.

## Setup and Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/muhalwan/simple_regression.git
   cd simple_regression
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Flask app with:

```bash
python app.py
```

This will start the server on `http://127.0.0.1:5000/`.

## Testing with Postman

1. Launch Postman.
2. Create a new `POST` request to `http://127.0.0.1:5000/predict`.
3. Set the header `Content-Type` to `application/json`.
4. Provide sample data in the request body and send.

## Docker Deployment

1. **Build the Docker image**:

   ```bash
   docker build -t simple_regression .
   ```

2. **Run the Docker container**:

   ```bash
   docker run -p 5000:5000 simple_regression
   ```