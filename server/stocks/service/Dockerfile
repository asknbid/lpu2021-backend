FROM python: 3
ENV PYTHONUNBUFFERD 1
RUN MKDIR /app
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/

