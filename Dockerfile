# Base image
FROM python:3.10-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project code to container
COPY . .

# Expose the port where Django application runs
EXPOSE 8000

# Entrypoint script
COPY entrypoint.sh .

RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]

# Command to run the Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
