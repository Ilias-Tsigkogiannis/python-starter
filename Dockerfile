FROM python:2.7

# Cache Dependency Install
RUN mkdir -p /app
ADD requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt

# Add Repository
ADD . /app

EXPOSE 5000
CMD python main.py
