from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

import dashscope
from rag import search  # 你的检索函数

# 👉 填你的API Key（或用环境变量更好）
dashscope.api_key = "sk-5b0adfd00d464404990b52ff2bf65997"

app = FastAPI()

# ✅ 解决跨域问题（前端必须）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👉 请求格式
class Question(BaseModel):
    question: str

# 👉 简单会话存储（内存版）
sessions = {}

@app.post("/ask")
def ask(q: Question):
    user_id = "default"  # 先用单用户

    # 1️⃣ 初始化历史
    if user_id not in sessions:
        sessions[user_id] = []

    history = sessions[user_id]

    # 2️⃣ RAG检索（关键）
    context = search(q.question)

    # 3️⃣ 构造 Prompt（重点！！！）
    prompt = f"""
请基于以下内容回答问题：

【参考内容】
{context}

【问题】
{q.question}
"""

    # 4️⃣ 加入用户问题（带上下文）
    history.append({"role": "user", "content": prompt})

    # 👉 防止历史过长（最多保留10轮）
    if len(history) > 20:
        history = history[-20:]
        sessions[user_id] = history

    # 5️⃣ 调用大模型
    response = dashscope.Generation.call(
        model="qwen-turbo",
        messages=history
    )

    answer = response.output.text

    # 6️⃣ 加入AI回答
    history.append({"role": "assistant", "content": answer})

    return {
        "answer": answer
    }