FROM python:3.4
WORKDIR /code
ADD requirements.txt /code/
ADD config/gunicorn.py /code/config/
RUN pip install -r requirements.txt
CMD gunicorn api:app -c config/gunicorn.py
ADD . /code
