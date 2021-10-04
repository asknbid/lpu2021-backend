FROM python:3.8
RUN mkdir /server
WORKDIR /server
COPY requirements.txt /server/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]