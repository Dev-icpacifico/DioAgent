from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "Eres un asistente virtual que responde exclusivamente en base al documento del condominio Altavista. Usa herramientas si es necesario para encontrar información relevante."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
])
