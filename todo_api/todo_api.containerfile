###############################################################################
# Put Source together
###############################################################################
FROM python:3 as base

RUN mkdir /install
WORKDIR /install
COPY requirements.txt /install
RUN python3 -m pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY src /app

###############################################################################
# Test
###############################################################################
FROM base as test

WORKDIR /install
COPY requirements_test.txt /install
RUN python3 -m pip install -r requirements_test.txt

WORKDIR /app
COPY .pylintrc /app
RUN python3 -m pytest
RUN python3 -m pytest --pylint

###############################################################################
# Final Version
###############################################################################
FROM base as final

ENV MONGO_DB_URL="mongo"
ENV MONGO_DB_PORT="27017"
ENV MONGO_DB_NAME="todo_dev_database"

EXPOSE 80

CMD ["python3", "main.py"]