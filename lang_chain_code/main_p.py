from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from .vector import retriever, store

chat_history = []

def get_assistant_response(question: str) -> dict:
    if question.strip().lower() == 'q':
        return {
            "quit": True,
            "response": "Session ended. Have a safe journey!",
            "documents": []
        }

    # 🔥 Model initialization
    model = OllamaLLM(
        model="llama3:8b",
        temperature=0.5,
        num_predict=256,
    )

    # ✨ Richer template with document context
    template = """
    You are a friendly and intelligent AI travel assistant.
    Help users with short, helpful travel advice using general knowledge and, if relevant, retrieved information.
    Your given info should be in good looking way, may contain multiple paragraph or even some point(should be in separate lines)

    Chat History:
    {history}

    Retrieved Info:
    {knowledge}

    New Question: {question}
    """

    # 🧠 Keep recent conversation memory
    history_str = "\n".join(chat_history[-10:])  # last 10 turns only

    # 🔍 Try to retrieve relevant documents
    retrieved = retriever.invoke(question)
    docs = [doc.page_content for doc in retrieved] if retrieved else []
    knowledge = "\n".join(docs) if docs else "No extra info available."

    # 🛠️ Format prompt and run the chain
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    response = chain.invoke({
        "question": question,
        "history": history_str,
        "knowledge": knowledge
    })

    # 💾 Store new response and update chat history
    store(response, question)
    chat_history.append(f"User: {question}")
    chat_history.append(f"Assistant: {response}")

    # 🚀 Final structured return
    return {
        "response": response,
        "documents": docs,
        "quit": False
    }
