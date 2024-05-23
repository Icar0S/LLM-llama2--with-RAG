# LLM-llama2--with-RAG
Cloud Migratin article for ICAI_2024

project for studying llms with strategy RAG 

## running
### configure
`python3 -m venv .venv`

``source /bim/activate``

### adding ollama in docker
``docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama``

``ollama pull nomic-embed-text``

``ollama pull llama2``

### run
``python populate_database.py``
``python query_data.py "make question here"``
