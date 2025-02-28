# FROM quay.io/jupyter/base-notebook:latest
FROM quay.io/jupyter/tensorflow-notebook:latest

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["start-notebook.sh"]
