FROM tiangolo/uwsgi-nginx-flask:python3.8

WORKDIR /app/

COPY ./requirements.txt /app/
COPY /static/ /app/static
COPY /templates/ /app/templates

RUN pip install --upgrade pip && pip install -r ./requirements.txt

COPY ./__init__.py ./main.py /app/

EXPOSE 5000/tcp
CMD ["python", "main.py"]

