# Use an official Python runtime as a parent image
FROM python:3.10-slim
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set the working directory in the container 

RUN apt-get update && apt-get install -y \
sudo \
&& rm -rf /var/lib/apt/lists/* 

RUN groupadd -r faizan && useradd -r -g faizan -m -d /home/faizan -s /bin/bash faizan  

RUN echo 'faizan:password' | chpasswd

# Add the new user to sudoers (optional)
RUN echo 'faizan ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Switch to the new user
USER faizan
RUN echo "Running as $(whoami)"


WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Command to run the Django application
CMD ["sh", "-c", "python ecommerce/manage.py migrate && python ecommerce/manage.py runserver 0.0.0.0:8000"]