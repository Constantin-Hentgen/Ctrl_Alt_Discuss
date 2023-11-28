# Podcast Generator Project

## Introduction

Welcome to the Podcast Generator project! This project combines the powerful capabilities of OpenAI, Eleven Labs AI, and RSS feed aggregation to automatically create podcasts. The core of this solution relies on the GPT-3.5-turbo language model from OpenAI to generate podcast scripts, complemented by Eleven Labs' Text-to-Speech (TTS) to bring these scripts to life.

## Objective

The goal of this project is to simplify podcast creation by automating the content generation process. By leveraging state-of-the-art natural language processing and speech technologies, we aim to provide an innovative and efficient podcasting experience.

## Features

### 1. RSS Feed Aggregation

The project starts by aggregating RSS feeds from predefined sources. These RSS feeds provide the foundational content for podcast episodes.

### 2. Script Generation with GPT-3.5-turbo

The OpenAI GPT-3.5-turbo model is used to generate podcast scripts from content extracted from the RSS feeds. This model can understand context and produce high-quality natural language.

### 3. Text-to-Speech with Eleven Labs

Generated scripts are then converted into audio files using Eleven Labs' Text-to-Speech (TTS) technology. This step gives a realistic and pleasant voice to the scripts, creating the final podcast audio.

## Configuration

### Installing Dependencies

Make sure to install the necessary dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Resources
- OpenAI GPT-3.5-turbo: https://beta.openai.com/
- Eleven Labs AI TTS: https://www.eleven-labs.ai/text-to-speech