FROM python:3.7-alpine

ENV TG_GROUP_TOKEN TG_GROUP_TOKEN
ENV BOOK_NAME BOOK_NAME

WORKDIR /gamebook
COPY requirements.txt .
COPY src .

RUN pip install -r requirements.txt

WORKDIR /gamebook/src

CMD ["sleep", "1000000"]
#CMD ["python", "/gamebook/src/main.py"]