FROM python

MAINTAINER Alexander Lotz "alexlotz@posteo.de"

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["main.py"]