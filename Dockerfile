# Use the official Python base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the Python code to the working directory
COPY . .

# Expose the port to access the Streamlit app
EXPOSE 8501

# Set the command to run the Streamlit app
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]

