FROM python:3.4
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD gunicorn api:app --pythonpath app --reload -c config/gunicorn.py
