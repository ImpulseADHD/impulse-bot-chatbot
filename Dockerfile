# Use the official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy your code into the container
COPY . /app

# Install any necessary packages
RUN pip install -r requirements.txt

ARG DISCORD_TOKEN
ARG OPENAI_API_KEY

# Set environment variables inside the Docker container
ENV DISCORD_TOKEN=$DISCORD_TOKEN
ENV OPENAI_API_KEY=$OPENAI_API_KEY

# Make port 80 available to the world outside this container
EXPOSE 80

# Run your Python script
CMD ["python", "impulseBotv1.py"]
