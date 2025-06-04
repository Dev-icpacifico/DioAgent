from langchain.tools.retriever import create_retriever_tool
from agent.knowledge_base import get_retriever

retriever_tool = create_retriever_tool(
    get_retriever(),
    name="info_departamentos",
    description="Responde preguntas sobre el condominio Altavista: ubicación, modelos, precios, etc."
)

tools = [retriever_tool]
