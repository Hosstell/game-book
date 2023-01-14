FROM python:3.7-alpine

WORKDIR /gamebook
ENV TG_GROUP_TOKEN TG_GROUP_TOKEN
ENV BOOK_NAME BOOK_NAME

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python", "main.py"]