FROM python

MAINTAINER Alexander Lotz "alotz@eggs.de"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]