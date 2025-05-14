# Sedna Canvas App - Python & Chalice Quickstart Guide

This guide provides a step-by-step walkthrough for creating a simple Sedna Canvas App using Python and the Chalice framework, and deploying it to AWS Lambda with an API Gateway endpoint.

The goal is to create a basic panel app that displays "Hello World" within Sedna.

## Table of Contents

1.  [Introduction to Sedna Canvas Apps](#introduction-to-sedna-canvas-apps)
2.  [Prerequisites](#prerequisites)
3.  [Project Setup with Chalice](#project-setup-with-chalice)
4.  [Understanding the Schemas](#understanding-the-schemas)
    *   [Request Schema (`request.schema.json`)](#request-schema)
    *   [Response Schema (`response.schema.json`)](#response-schema)
5.  [Building the "Hello World" App](#building-the-hello-world-app)
6.  [Deploying to AWS Lambda](#deploying-to-aws-lambda)
7.  [Connecting to Sedna](#connecting-to-sedna)
8.  [Further Development](#further-development)

## Introduction to Sedna Canvas Apps

Sedna Canvas Apps allow developers to extend the Sedna interface with custom UI elements and functionality. These apps are essentially web services that receive a JSON request from Sedna and respond with a JSON object that defines the UI to be rendered. This enables a wide range of integrations and custom tools to be built directly into the Sedna user experience.

This guide focuses on building a "Panel" app, which typically appears on the side of the screen.

## Prerequisites

Before you begin, ensure you have the following installed and configured:

*   **Python (3.7+)**: [Download Python](https://www.python.org/downloads/)
*   **pip**: Python package installer (usually comes with Python).
*   **AWS CLI**: [Install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html)
    *   Ensure it's configured with your AWS credentials and a default region: `aws configure`
*   **Chalice**: `pip install chalice`
*   **An AWS Account**: To deploy the Lambda function and API Gateway.
*   **Access to a Sedna environment**: To register and test your app.

## Project Setup with Chalice

Chalice is a Python Serverless Microframework for AWS. It makes it easy to create and deploy applications using AWS Lambda and API Gateway.

1.  **Create a new Chalice project:**
    ```bash
    chalice new-project sedna-hello-world-app
    cd sedna-hello-world-app
    ```
    This will create a new directory `sedna-hello-world-app` with the following structure:
    *   `app.py`: Your application code.
    *   `requirements.txt`: Python package dependencies.
    *   `.chalice/config.json`: Configuration for your Chalice app.

2.  **Review `requirements.txt`:**
    Chalice automatically adds itself. For this simple app, no other dependencies are strictly needed initially.

## Understanding the Schemas

Sedna Canvas Apps communicate using a defined JSON schema. You should have `request.schema.json` and `response.schema.json`.

*   Place these files in a `schemas` directory within your project for reference:
    *   `sedna-hello-world-app/schemas/request.schema.json`
    *   `sedna-hello-world-app/schemas/response.schema.json`

### Request Schema (`request.schema.json`)

This schema defines the structure of the JSON object your app will receive from Sedna. Key properties include:

*   `appId`: The unique ID of your app.
*   `version`: The protocol version.
*   `user`: Information about the user interacting with the app.
*   `company`: Information about the company context.
*   `context`: Details about where the app is being displayed (e.g., `GLOBAL`, `MESSAGE_READ`) and the entity in context (e.g., a specific message ID).
*   `state`: The current state of interactive elements in your app's UI (if any).
*   `action`: If the request is due to a user interaction with an element (e.g., a button click), this will identify the element.

For our "Hello World" app, we won't need to deeply inspect the request, but it's good to be aware of its structure for more complex apps.

### Response Schema (`response.schema.json`)

This schema defines the structure of the JSON object your app must return to Sedna. This response tells Sedna how to render your app's UI. Key properties for our simple app:

*   `surfaces`: An array defining the UI surfaces to render (e.g., panels, modals).
    *   Each surface has a `type` (e.g., `"panel"`), `id`, and `blocks`.
    *   `blocks`: Define the layout and content within a surface. Common block types include `header`, `section`, `row`, `footer`.
        *   `elements`: Contained within blocks, these are the actual UI components like `text`, `button`, `table`, etc.

Our app will return a single `panel` surface containing a `section` block, which in turn holds a `text` element displaying "Hello World".

## Building the "Hello World" App

Modify your `app.py` file with the following code:

```python
from chalice import Chalice

app = Chalice(app_name='sedna-hello-world-app')

@app.route('/', methods=['POST'], content_types=['application/json'])
def handle_canvas_request():
    # request_data = app.current_request.json_body # Access request if needed
    return {
        "surfaces": [
            {
                "type": "panel",
                "id": "hello_world_panel",
                "blocks": [
                    {
                        "type": "section",
                        "elements": [
                            {
                                "type": "text",
                                "content": "Hello World"
                            }
                        ]
                    }
                ]
            }
        ]
    }
```

## Deploying to AWS Lambda

1.  **Deploy the app:**
    From within your `sedna-hello-world-app` directory, run:
    ```bash
    chalice deploy
    ```
    Chalice will package your application, create an IAM role, the Lambda function, and an API Gateway endpoint.
    After deployment, Chalice will output the **Rest API URL**. This is crucial for connecting to Sedna.

## Connecting to Sedna

1.  Contact Sedna team at support@sedna.com and deliver the following details:
    *   **Name:** "Hello World App"
    *   **URL:** The Rest API URL from `chalice deploy`.
    *   **Contexts:** MESSAGE_READ.

## Further Development

*   Process the `request_data`.
*   Add interactive elements.
*   Manage state.
*   Use `referenceData`.

Refer to `request.schema.json` and `response.schema.json` for details. 