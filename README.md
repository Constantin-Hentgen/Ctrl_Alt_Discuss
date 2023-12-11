# Podcast Generator Project

## Introduction

Welcome to the ByteBeacon project! This project combines the powerful capabilities of OpenAI, Eleven Labs AI, and RSS feed aggregation to automatically create podcasts. The core of this solution relies on the GPT-3.5-turbo language model from OpenAI to generate podcast scripts, complemented by Eleven Labs' Text-to-Speech (TTS) to bring these scripts to life.

## Objective

The goal of this project is to simplify podcast creation by automating the content generation process. By leveraging state-of-the-art natural language processing and speech technologies, aim to provide relevant and accurate content on demand.

## Features

### 1. RSS Feed Aggregation

The project starts by aggregating RSS feeds from predefined sources. These RSS feeds provide the foundational content for podcast episodes.

### 2. Script Generation with GPT-3.5-turbo

The OpenAI GPT-3.5-turbo model is used to generate podcast scripts from content extracted from the RSS feeds. This model can understand context and produce high-quality natural language.

### 3. Text-to-Speech with Eleven Labs

Generated scripts are then converted into audio files using Eleven Labs' Text-to-Speech (TTS) technology. This step gives a realistic and pleasant voice to the scripts, creating the final podcast audio.

## Configuration

Make sure that you’re inside the virtual environement :
```bash
cd ByteBeacon
poetry env list
```
Which should return a result such as  :
`bytebeacon-Z2Ju98Sf-py3.11 (Activated)`

Otherwise try the following command :
```bash
poetry env use env_name||python||python3||python3.X
```

### Installing Dependencies

Make sure to install the necessary dependencies by running the following command:

```bash
cd ByteBeacon
poetry install --no-root
```

### Setting Environment Variables

```bash
export POETRY_OPENAI_API_KEY="your_openai_api_key_here"
export POETRY_XI_API_KEY="your_xi_api_key_here"
export POETRY_BYTEBEACON_ROOT_PATH="/path/to/ByteBeacon"
```

### Run the project

```bash
cd ByteBeacon
poetry run python -i src/main.py
```

## Resources
- OpenAI GPT-3.5-turbo: https://platform.openai.com/
- OpenAI TTS: https://platform.openai.com/docs/guides/text-to-speech
- Eleven Labs AI TTS: https://www.eleven-labs.ai/text-to-speech
- Poetry: https://python-poetry.org/docs/