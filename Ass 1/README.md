[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/JzgqJ4dG)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=13484196)
# Assignment 1: Basic CI Pipeline

## Objective

The objective of this assignment is to create a basic CI pipeline in GitHub Actions.
While this assignment requires you to write a simple application and unit tests
for it, that is not the primary focus of this assignment.  Allocate your time
accordingly.

## Steps

### 1. Accept the Assignment

Similar to Assignemnt 0, follow the typical steps to accept the assignment in
GitHub.

Please perform all your work in a separate Git branch.  The act of merging this
branch to `main` will trigger the submission of your assignment.

### 2. Create a Basic Application

Write a simple application (e.g. a calculator) in the language of your choice (e.g. Python).
The application should have at least one functionality (e.g. add, subtract, etc.).  Ensure
you know how to compile and run the application.

### 3. Write Unit Tests for the Application

Write a set of unit tests for the application.  Use a testing framework compatible with the
chosen language (e.g., PyTest for Python).  Run the unit tests and make sure that they pass.

### 4. Create a GitHub Actions CI Pipeline

Create a GitHub Actions workflow to define the CI pipeline.  The pipeline should:
- Trigger on every push and pull request to the main branch.
- Set up the environment for the chosen language.
- Run the unit tests.

See https://docs.github.com/en/actions/quickstart for information on how to get started
with GitHub Actions.

### 5. Create a GitHub Actions Release Pipeline

Create a second GitHub Actions workflow to define the release pipeline.  This pipeline will
be used when you want to create an official, versioned release of the software.  The pipeline
should:
- Trigger on the push of a tag with the format `vx.y.z` to the remote repository
- Compile the software and run the unit tests
- Extract the version number from the tag.  For example, if the tag is named `v1.2.3`, the
  extracted version number is 1.2.3.
- Create a GitHub release with the appropriate version number.
- Attach the built artifacts (see below) to the GitHub release as assets so that customers
  can download it by clicking on the release.

After successful execution of this workflow, you should see a GitHub release in the
Releases section of your repository such as the following:
![image](https://github.com/depaul-se441-winter2024/assignment1/assets/482551/0bb1cc65-cf58-45fb-a60c-94b3765fb782)

When you click on the release, you should see your artifacts under "assets".

Tags must be explicitly pushed by Git.  To push a tag to a remote repository, use:
```sh
git tag -a v1.2.3       # creates an annotated release tag locally
git push origin v1.2.3 # pushes the tag named v1.2.3 to the remote named origin
```

To delete a remote tag, use:
`git push --delete origin v1.2.3`

You may find this GitHub action useful for creating releases: https://github.com/actions/create-release

By _built artifacts_, I mean whatever is necessary for a user to execute your application without
compiling it from source code.  For example:
- For a C program it would typically be the compiled binary.
- For a C# program, it would typically be the compiled binary and any additional necessary assemblies.
- For a Go program, it would typically be the compiled binary.
- For a Java program, it would typically be a JAR file.
- For Python, it would typically be the `.py` files.

### 6. Reflection

In your repository, add a file named `REFLECTION.md` with a brief reflection on the process and
learning experience.

Questions for Reflection:
1. What challenges did you encounter while setting up the CI pipeline?
2. How does CI benefit software development projects?

### 7. Submit your Assignment

Merge your work from your branch to `main`, which triggers the submission of the assignment.

## Grading Rubric

Application Functionality and Unit Tests (30%)
- Does the application function correctly?
- Do the unit tests cover both success and failure scenarios?
- Is the code "clean" (comments where appropriate; proper indentation; etc.)

CI Pipeline (30%)
- Does the pipeline trigger correctly?
- Does the pipeline build and run unit tests?
- Does the pipeline fail if the unit tests fail?
- Is the code "clean" (comments where appropriate; proper indentation; etc.)
 
Release Pipeline (30%)
- Does the pipeline trigger correctly?
- Does the pipeline create a GitHub release correctly?
- Does the pipeline attach the artifacts to the release?
- Can any user download and run the artifacts from the release?
- Is the code "clean" (comments where appropriate; proper indentation; etc.)

Reflection (10%)
