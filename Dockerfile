FROM public.ecr.aws/lambda/python:3.11

# Copy requirements file
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install dependencies
RUN pip install -r requirements.txt

# Copy function code
COPY app ${LAMBDA_TASK_ROOT}/app

# Run the seed script to populate the database
RUN python -m app.seed

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.main.handler" ]
