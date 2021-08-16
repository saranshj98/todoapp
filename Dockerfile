FROM python:3.7
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip3 install python-dotenv
COPY . /app
EXPOSE 5000
CMD ["flask", "run"]