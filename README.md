A simple RAG project

This program gets the context from a downloaded file in folder. Allowing me to experiment on 
how chunking, embedding, and connecting to the ai model works.

how it works:
- chunk
- embed
- model

## What you need
- Python 3 and Ollama
- Models: run `ollama pull bge-m3` and `ollama pull qwen2.5:3b`
- Packages: `pip install langchain-ollama numpy`
- A text file named `sample.txt` in the same folder (not included, so add your own)

## Run it
(a code box with the command, `python3 simple_rag.py`)

## Notes
RAG is just feeding context to an AI model. 
