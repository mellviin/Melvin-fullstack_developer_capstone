FROM python:3.12.0-slim-bookworm

ENV PYTHONBUFFERED=1
ENV PYTHONWRITEBYTECODE=1
ENV APP=/app

# Change the workdir
WORKDIR $APP

# Install dependencies
COPY requirements.txt $APP
RUN pip3 install --upgrade pip && pip3 install -r requirements.txt

# Copy project files
COPY . $APP

# Expose Django port
EXPOSE 8000

# Entrypoint permissions
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/bin/bash","/app/entrypoint.sh"]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "djangoproj.wsgi"]
