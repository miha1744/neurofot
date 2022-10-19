FROM Python:3.10.5

WORKDIR /src
COPY requirements.txt /src
RUN pip install -r requirements.txt
COPY . /src
