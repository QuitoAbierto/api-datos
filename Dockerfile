FROM python:3.4
WORKDIR /code
COPY requirements.txt /code/
COPY config/gunicorn.py /code/config/
RUN pip install -r requirements.txt
CMD gunicorn api:app -c config/gunicorn.py
COPY . /code
