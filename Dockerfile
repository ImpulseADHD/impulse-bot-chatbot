# Use the official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy your code into the container
COPY . /app

# Install any necessary packages
RUN pip install -r requirements.txt

# Define environment variables if needed
ENV DISCORD_TOKEN = 'MTE2NjgzMjcxMTE2NDQ5NzkyMA.G65O_T.A1s6A4FAIhWN9N74EFlNY08FMkrGHbrrjBBhgA'
ENV openai.api_key = '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'

# Make port 80 available to the world outside this container
EXPOSE 80

# Run your Python script
CMD ["python", "impulseBotv1.py"]
