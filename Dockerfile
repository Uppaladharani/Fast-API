# base image to use container
FROM python:3.11-slim
#directory in the container
WORKDIR /app
# Copy the current directory contents into the container
COPY . /app
# Install FastAPI and Uvicorn
RUN pip install --no-cache-dir fastapi uvicorn
#port
EXPOSE 8000
#specifies the command to run when conatiner starts
CMD ["uvicorn", "first_program:app", "--host", "0.0.0.0", "--port", "8000"]

