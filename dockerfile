FROM python3.11.0-alpine3.14

WORKDIR /build_app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "builld_app.py" ]
