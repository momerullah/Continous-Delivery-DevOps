[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LmudWTpa)
# Assignment 2: Building, Testing, and Publishing Containers

## Objective

The objective of this assignment is to create a CI pipeline which creates, tests, and publishes a container. In this assignment you will become familiar with Docker, building containers, testing containers, publishing containers, and running containers.

## Steps

### 1. Prequisites
For this assignment, you will need to install Docker.

### 2. Accept the Assignment

Similar to Assignment 1, follow the typical steps to accept the assignment in GitHub.

Please perform all your work in a separate Git branch. The act of merging this branch to main will
trigger the submission of your assignment.

### 3. Create a Basic Application

Write a simple application (e.g. a calculator) in the language of your choice. However, *the language must have a separate compilation step*,
i.e. you must be able to run the source code through a compiler in order to generate some sort of binary artifact (executable, JAR file, etc.).
This implies that languages such as C, C++, Java, Golang, and C# are acceptable, whereas Python and other scripting languages are not.

Ensure you know how to compile and run the application from the command-line.

While a real application would almost always also have a set of unit tests, writing them is not necessary for this assignment.

You may reuse your application from HW1.

### 4. Write a Multi-Stage Dockerfile

In this section, we will create a container-image using a multi-stage build process.

Following instructions such as https://docs.docker.com/build/building/multi-stage/, create a
Dockerfile that uses a multi-stage build process. This Dockerfile should:

1. Have a first stage, named builder, that prepares and compiles the application (e.g. install dependen- cies, compiles the application)
2. Have a second stage which copies the necessary artifacts, and only the necessary artifacts, from the builder stage and prepare the final, lightweight runtime image.
3. The runtime image should follow container image best practices, such as:
    1. Running the container should execute the compiled application.
    2. The image should have the minimal necessary dependencies. For example, you should not require the language compiler inside the image, as the compiler is not necessary to execute the application.
    3. The image should use a minimal base image
    4. The image should have appropriate metadata assigned with LABEL
    5. The layers in the image should be ordered in a way to maximimze caching
    6. etc.

Useful references for container image best practices include:

- Class lecture notes
- https://docs.docker.com/develop/develop-images/instructions/
- https://docs.docker.com/develop/develop-images/guidelines/
- https://docs.docker.com/develop/security-best-practices/
- https://docs.docker.com/develop/dev-best-practices/

Ensure that you can build the container with `docker build` and execute the container with `docker run`.

### 5. Add Container Tests

Using the Google Container Structure Tests framework at https://github.com/GoogleContainerTools/ container-structure-test,
add a set of tests for your build container. This framework can either be installed locally, or you can run them from
Docker using the command:

```sh
docker run gcr.io/gcp-runtimes/container-structure-test:latest
```

These tests should test properties of the container, such as:
1. Do various essential files exists with appropriate permissions, owners, content, etc.?
2. Is metadata on the container set properly?
3. Do key executables in the container (like your application) execute properly?

Note that these tests are testing the container (e.g. that it is correctly constructed), not the complete application
functionality (which would have been tested by earlier application-level unit and integration tests after the application
was built but before the container was built).

### 6. Automate with GitHub Actions

Write a GitHub action workflow named ci.yml which automates the build, testing, and release of the container. This workflow should:
1. Triggers on push and pull request events to the main branch.
2. Executes a job that builds the container image using the multi-stage Dockerfile.
3. Runs the container image tests against the built container to validate application functionality.
6. Automatically assign a version to the release
7. Push the successfully built and tested image to GitHub Container Registry, tagging it with the release
version and latest.

Creation of a GitHub release in this pipeline is optional.

For information about working with the GitHub Container Registry, see https://docs.github.com/ en/packages/working-with-a-github-packages-registry/working-with-the-container-registry.

## Grading Rubric

1. Application (10%)
    - Is the application functional
    - Does it follow the requirements (e.g. uses a compiled language) • Is the code “clean”?
2. Container Image Build (50%)
    - Does the built container image work properly?
    - Is the build perform in a two-step process?
    - Does the runtime image have only the necessary files to execute the application? • Does the runtime image follow best practices?
    - Is the code “clean”?
3. Container Image Test (20%)
    - Are a set of meaningful tests written? • Do the tests execute properly?
    - Is the code “clean”?
4. GitHub Actions Workflow (20%)
    - Does the pipeline trigger correctly?
    - Does the pipeline execute the build and steps correctly?
    - Does the pipeline generate versions automatically?
    - Does the pipeline upload the image to the GitHub Container Registry with appropriate tags? • Is the code “clean”?
