FROM python:3.7
COPY . ./app
WORKDIR app
RUN pip install pipenv
RUN pipenv install --dev --deploy --system
RUN bash test.sh
