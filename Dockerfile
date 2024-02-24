FROM --platform=linux/x86-64 python:3.8.1-slim 

ENV *PYTHONUNBUFFERED *1 
EXPOSE 8000 
WORKDIR /todo_list # Make /app as a working directory in the container

COPY ./requirements.txt .
COPY ./src/* ./src/
COPY ./todo_list.py .

RUN pip install -r requirements.txt # Install the dependencies

CMD ["python", "todo_list.py"]