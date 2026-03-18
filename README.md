# 🤖 AI RAG 问答系统（支持多轮对话）

## 📌 项目简介

本项目是一个基于大模型的智能问答系统，采用 **RAG（Retrieval-Augmented Generation，检索增强生成）架构**，实现了从知识库检索信息并结合大模型生成回答的能力。

系统支持多轮对话与上下文记忆，具备完整的前后端结构，并已部署上线，可直接访问使用。

---

## 🌐 在线体验

* 前端页面：👉(https://yanghui2478.github.io/AItalk_t1/)
* 后端接口：👉（https://secure-strength-production-7c5f.up.railway.app/docs#/default/ask_ask_post）

---

## 🧠 核心功能

* ✅ 基于 RAG 架构的问答系统（检索 + 生成）
* ✅ 支持多轮对话（上下文记忆）
* ✅ 简单知识库接入（可扩展）
* ✅ 前后端分离架构
* ✅ 在线部署（可直接访问）

---

## 🏗️ 技术架构

前端：

* HTML + CSS + JavaScript（原生实现）

后端：

* FastAPI（接口服务）

AI能力：

* 通义千问（DashScope API）

核心能力：

* 向量检索（RAG思想实现）
* Prompt Engineering（提示词优化）
* 多轮对话管理（Session机制）

部署：

* 前端：GitHub Pages
* 后端：Railway

---

## ⚙️ 系统流程

1. 用户输入问题
2. 系统从知识库中检索相关内容（RAG）
3. 将“问题 + 上下文”组合成 Prompt
4. 调用大模型生成回答
5. 返回结果并记录对话历史

---

## 📂 项目结构

```
.
├── main.py          # FastAPI 后端服务
├── rag.py           # 简单检索模块
├── data.txt         # 知识库内容
├── index.html       # 前端页面
├── requirements.txt # 依赖文件
```

---

## 🚀 本地运行

```bash
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

打开浏览器访问：

```
http://127.0.0.1:8000/docs
```

---

## 🔑 环境变量配置

```bash
DASHSCOPE_API_KEY=你的API_KEY
```

---

## ✨ 项目亮点

* 🔥 从零实现 RAG 架构（检索 + 生成）
* 🔥 支持多轮对话（上下文记忆）
* 🔥 完整前后端项目（非单一脚本）
* 🔥 已部署上线（具备真实使用场景）
* 🔥 具备工程化能力（接口、部署、结构清晰）

---

## 📈 后续优化方向

* 支持 PDF / 文档上传（增强知识库能力）
* 引入向量数据库（如 FAISS / Milvus）
* 增强 UI（类 ChatGPT 界面）
* 用户登录与多用户会话管理
* 部署至生产环境（Docker / 云服务）

---

## 👨‍💻 作者
yanghui2478
软件工程专业 | AI应用方向求职者

---

## ⭐ 如果觉得不错

欢迎点个 Star ⭐
