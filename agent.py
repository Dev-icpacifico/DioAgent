from langgraph.graph import StateGraph
from langchain_core.runnables import RunnableLambda
from typing import TypedDict

# ✅ Definir correctamente el esquema del estado
class AgentState(TypedDict):
    input: str
    output: str

# 🔹 Nodo router
def router_node(state: AgentState):
    msg = state["input"].lower()
    if "precio" in msg or "cotización" in msg:
        return "cotizar"
    elif "humano" in msg or "hablar con alguien" in msg:
        return "humano"
    else:
        return "faq"

# 🔹 Nodos simulados
def faq_node(state: AgentState):
    return {"output": "Sí, tenemos stock del producto A 😊"}

def cotizar_node(state: AgentState):
    return {"output": "Para cotizar, por favor indícame el nombre del producto."}

def humano_node(state: AgentState):
    return {"output": "Un ejecutivo se contactará contigo en breve."}

def final_node(state: AgentState):
    return state["output"]

# 🔧 Crear grafo con clase TypedDict como esquema
graph = StateGraph(schema=AgentState)
graph.add_node("router", RunnableLambda(router_node))
graph.add_node("faq", RunnableLambda(faq_node))
graph.add_node("cotizar", RunnableLambda(cotizar_node))
graph.add_node("humano", RunnableLambda(humano_node))
graph.add_node("final", RunnableLambda(final_node))

graph.set_entry_point("router")
graph.add_edge("router", "faq", condition=lambda s: router_node(s) == "faq")
graph.add_edge("router", "cotizar", condition=lambda s: router_node(s) == "cotizar")
graph.add_edge("router", "humano", condition=lambda s: router_node(s) == "humano")
graph.add_edge("faq", "final")
graph.add_edge("cotizar", "final")
graph.add_edge("humano", "final")

# 🔁 Compilar y probar
app = graph.compile()

mensaje = "Hola, ¿me puedes dar una cotización?"
estado_inicial = {"input": mensaje}

resultado = app.invoke(estado_inicial)
print("🤖 Respuesta del agente:", resultado)
