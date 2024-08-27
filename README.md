# Lotion Plus

This project involves creating a full-stack application, with the frontend built in React and the backend deployed on AWS. The application is a Notion-like note-taking tool called Lotion, which utilizes the Context API for state management.

## Project Overview

I developed and deployed both the frontend and backend for the Lotion app. The backend is hosted on AWS, with infrastructure managed using Terraform. The application integrates Google authentication and uses AWS DynamoDB for data storage.

## Key Components

- **Lotion Application**: A Notion-like note-taking app built in React, using the Context API for state management.
- **Full-Stack Development**: Created a full-stack application with a React frontend and an AWS backend.
- **Google Authentication**: Integrated Google login using the `@react-oauth/google` library.
- **AWS Infrastructure**: Managed with Terraform, including the setup of DynamoDB for storing user notes.
- **Backend Functions**: Created three AWS Lambda functions to handle note retrieval, creation/updating, and deletion.
- **Deployment**: Deployed the app using Netlify.

## Instructions

1. Clone the repository and run `npm install` in the root directory.
2. Add infrastructure code to the `main.tf` file.
3. Implement the necessary function code in the respective files:
   - `get-notes`
   - `save-note`
   - `delete-note`
4. Push changes to the `main` branch and a private GitHub repository.
5. Deploy the application on Netlify and include the URL in the project.
