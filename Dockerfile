# Use an official Python image as the base
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml file
COPY pyproject.toml poetry.lock* ./

# Install the dependencies
RUN poetry install --no-dev

# Copy the application code
COPY . .

# Set environment variables
ENV OPENAI_COMPAT_MODEL_NAME=${OPENAI_COMPAT_MODEL_NAME}
ENV OPENAI_COMPAT_API_BASE=${OPENAI_COMPAT_API_BASE}
ENV OPENAI_COMPAT_API_KEY=${OPENAI_COMPAT_API_KEY}

# Expose the port for Streamlit
EXPOSE 8501

# Run the command to start the Streamlit app
CMD ["poetry", "run", "streamlit", "run", "streamlit_app.py"]
