FROM python:3.4
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
CMD gunicorn api:app --reload -c config/gunicorn.py
ADD . /code
