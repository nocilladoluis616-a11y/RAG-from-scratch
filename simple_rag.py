from langchain_ollama import OllamaEmbeddings, ChatOllama
import numpy as np

with open("sample.txt") as f:
    data = f.read()
    data = data.split()
    length = len(data)

    print(length)

chunks = []
chunks_size = 200
overlap = 50
#the loop tp create the chunks of data with the specified overlap
for start in range(0, length, chunks_size - overlap):
    chunks.append(data[start:start+chunks_size])

    #So the shunks won't reiterate the last end of the sample.txt file
    if start + chunks_size >= length:
        break


#Embedder


texts = []
for chunk in chunks: 
    texts.append(" ".join(chunk))

embedder = OllamaEmbeddings(model="bge-m3:latest")
vectors = embedder.embed_documents(texts)

print(len(vectors), len(vectors[0]))

print(len(texts), texts[0][:100])

#embed_query one string to one vector
question = "What happened to Fukushima?"
q_vector = embedder.embed_query(question)

def closenss(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

scores = []

for i in range(len(vectors)):
    score = closenss(vectors[i],q_vector)
    print(i, score)
    scores.append(score)

best = max(scores)
position = scores.index(best)
print(best, position)

min_score = 0.5
if best < min_score:
    print("too low")
else:
    print("good enough")


context = texts[position]

prompt = f"""Answer the question using ONLY the text below.
If the answer is not in the text, say "I don't know."

Text:
{context}

Question: {question}
Answer:"""

print(prompt)

llm = ChatOllama(model="qwen2.5:3b", temperature=0)
response = llm.invoke(prompt)
print(response.content)

