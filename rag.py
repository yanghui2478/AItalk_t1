import numpy as np

# 简单文本
with open("data.txt", "r", encoding="utf-8") as f:
    docs = f.readlines()

# 简单向量（长度）
def text_to_vec(text):
    return np.array([len(text)])

doc_vectors = [text_to_vec(doc) for doc in docs]

def search(query):
    q_vec = text_to_vec(query)

    scores = [np.dot(q_vec, d) for d in doc_vectors]

    best_idx = np.argmax(scores)

    return docs[best_idx]
