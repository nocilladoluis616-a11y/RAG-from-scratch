with open("sample.txt") as f:
    data = f.read()
    data = data.split()
    length = len(data)

    print(length)

chunks = []
chunks_size = 200
overlap = 50
for start in range(0, len(data), chunks_size - overlap):
    chunks.append(data[start:start+chunks_size])
    
    if start + chunks_size >= length:
        break

for chunk in chunks[0:3]:
    print(" ".join(chunk))
    print("-------")


print(chunks[0][-50:] == chunks[1][:50])
print([len(c) for c in chunks])