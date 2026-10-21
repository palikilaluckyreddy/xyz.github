on:
  workflow_call:
    secrets:
      DOCKERHUB_USERNAME:
        required: true
      DOCKERHUB_TOKEN:
        required: true
    inputs:
      image_base_name:
        required: true
        type: string
