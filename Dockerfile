FROM python:3.8
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY requirements.txt /requirements.txt
ADD . /code
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt
ENV PATH="/py/bin:$PATH"
USER app
CMD ["python", "Project.py"]
EXPOSE 5000

