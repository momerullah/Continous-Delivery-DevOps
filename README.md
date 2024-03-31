# SEE 441 Course Assignments Repository

This repository hosts the assignments for SEE 441 at DePaul University, focusing on software engineering practices, Continuous Integration (CI), and Continuous Deployment (CD) using modern tools and platforms.

## Assignments Overview

### Assignment 1: Basic CI Pipeline

**Objective:** The goal is to create a basic CI pipeline using GitHub Actions, involving a simple application and its unit tests. The primary learning outcome is understanding and implementing CI practices rather than application development.

**Highlights:**
- Writing a simple application in a language of your choice.
- Writing unit tests for the application.
- Creating a CI pipeline that triggers on every push and pull request to the main branch.
- Creating a release pipeline that triggers on version tag pushes, compiles the software, runs unit tests, and creates a GitHub release with attached artifacts.

### Assignment 2: Building, Testing, and Publishing Containers

**Objective:** This assignment focuses on Docker containers, encompassing their creation, testing, and publishing to GitHub Container Registry. It aims to familiarize students with Docker, container testing, and publishing practices.

**Highlights:**
- Writing a simple compiled application.
- Creating a multi-stage Dockerfile for building a minimal and secure container.
- Testing the container using Google Container Structure Tests.
- Automating the container's build, test, and publish process using a GitHub Actions workflow.

### Assignment 3: Web Application Deployment to Azure Using Terraform and GitHub Actions

**Objective:** The objective is to deploy a simple Node.js web application to Azure, utilizing Terraform for infrastructure provisioning and GitHub Actions for continuous deployment.

**Highlights:**
- Automated CI/CD pipeline setup with GitHub Actions for deploying to Azure.
- Terraform configuration for provisioning Azure resources like Resource Group, App Service Plan, and App Service.
- Managing challenges such as Azure service limits, secrets management, and deployment package configurations.

## Getting Started

To utilize these assignments, clone this repository and explore each assignment in its respective folder (`Ass 1`, `Ass 2`, `Ass 3`). Each folder contains detailed instructions, code, and CI/CD configurations related to the assignment.

## Prerequisites

- Familiarity with Git and GitHub.
- For Assignment 2: Docker installed on your machine.
- For Assignment 3: Access to an Azure account and basic knowledge of Terraform.

## Installation and Usage

Refer to each assignment's specific instructions for details on how to compile/run applications, configure CI/CD pipelines, and deploy to cloud platforms.

## Reflections

Each assignment includes a `REFLECTION.md` file, where I share challenges encountered, lessons learned, and the impact of CI/CD practices on software development.

## License

This project is licensed under the [ISC License](LICENSE).

## Contact

For more information, contact me at [omarullahk@gmail.com].
