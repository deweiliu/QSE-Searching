# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.7.0-alpine

# If you prefer miniconda:
#FROM continuumio/miniconda3

LABEL Name=qse-searching Version=0.0.1
EXPOSE 80

WORKDIR /app
ADD . /app

# Using pip:
RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
RUN pytest

CMD ["python3", "server.py"]

# Using pipenv:
#RUN python3 -m pip install pipenv
#RUN pipenv install --ignore-pipfile
#CMD ["pipenv", "run", "python3", "-m", "qse-searching"]

# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m qse-searching"
