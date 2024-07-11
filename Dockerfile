# pull official base image for getting requirements.txt file from poetry
FROM python:3.12-alpine as requirements-from-poetry

# set working directory
WORKDIR /tmp

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expected versions
ARG EXPECTED_PYTHON_VERSION="3.12"

# install system dependencies
# RUN apt-get update \
#   && apt-get -y install \
#     --no-install-recommends \
#     netcat gcc g++ libpq-dev \
#   && apt-get clean

# Let's do some safety checks
RUN python3 --version | grep -q "Python $EXPECTED_PYTHON_VERSION" \
    || (echo "###### FAILED CHECK FOR PYTHON ${EXPECTED_PYTHON_VERSION} (got $(python3 --version)) ######"; false)

    
# install python dependencies
RUN pip install --upgrade pip
RUN pip install poetry
COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

# pull official base image 
FROM python:3.12-alpine
LABEL maintainer="Connor Yu"
LABEL description="Shopping Cart App Backend"
# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
# RUN apt-get update \
#   && apt-get -y install \
#     --no-install-recommends \
#     netcat gcc g++ libpq-dev \
#   && apt-get clean

# install python dependencies
RUN pip install --upgrade pip
COPY --from=requirements-from-poetry /tmp/requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# Entrypoint waits until database is ready
RUN chmod +x /usr/src/app/bin/entrypoint.sh
ENTRYPOINT ["sh", "/usr/src/app/bin/entrypoint.sh"]