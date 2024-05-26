# LLM-llama2-with-RAG
Cloud Migratin article for ICAI_2024

project for studying llms with strategy RAG 

## Running llm

### First step up container
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

### Second step prepare models
```
ollama pull nomic-embed-text
ollama pull llama2
```

## Get Started

### Create env
```python -m venv venv```
`source venv/Scripts/activate`

### Create install libs
```pip install -r ./backend/requirements.txt```

## CLI commands

### Populate database
```python ./backend/populate_chomadb.py```

### Make a question
```python ./backend/query_data.py "make question here"```

## Execute API

### Local
```python ./backend/src\app.py```

### Like a server
```python ./backend/server.py```
