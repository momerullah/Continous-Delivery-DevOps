# Use an official Java development image to compile the code
FROM openjdk:17-slim AS builder
WORKDIR /app

# Copy the source code into the image
COPY BMICalculator.java /app

# Compile the application
RUN javac BMICalculator.java

# Use a minimal base image for the runtime
FROM openjdk:17-slim
WORKDIR /app

# Copy only the compiled artifact and any other necessary files from the builder stage
COPY --from=builder /app/BMICalculator.class /app

# Set the command to run the application
CMD ["java", "BMICalculator"]

# Set metadata labels
LABEL maintainer="Omerullah <omarullahk@gmail.com>" \
      description="A simple BMI Calculator Java application"
