FROM python:3.8.6-buster

RUN mkdir -p /home/workspace

WORKDIR /home/

COPY . .

COPY terminado/_static/terminado.js /usr/local/lib/python3.8/site-packages/terminado/_static/terminado.js

WORKDIR /home/demos/

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["/bin/bash", "-c"]

CMD ["python /home/demos/single.py"]

WORKDIR /home/workspace