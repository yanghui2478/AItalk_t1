from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# 加载模型
model = SentenceTransformer('all-MiniLM-L6-v2')

# 读取知识库
with open("data.txt", "r", encoding="utf-8") as f:
    docs = f.readlines()

# 向量化
embeddings = model.encode(docs)

# 建立索引
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# 查询函数
def search(query):
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k=1)
    return docs[I[0][0]]