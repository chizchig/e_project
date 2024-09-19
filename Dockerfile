# Build stage
FROM python:3.8 AS builder

WORKDIR /app

COPY requirements.txt .
RUN python -m pip install --upgrade pip && \
    python -m pip install virtualenv

RUN python -m virtualenv /venv

ENV PATH="/venv/bin:$PATH"

RUN . /venv/bin/activate && pip install -r requirements.txt

# Final stage
FROM python:3.8-slim

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /venv /venv

# Copy application files
COPY applications/ .
COPY tests/ ./tests/
COPY templates/ ./templates/

ENV PATH="/venv/bin:$PATH"

# Set environment variable for Flask
ENV FLASK_APP=app.py

# Command to run tests (can be overridden)
CMD ["/venv/bin/pytest", "tests/"]