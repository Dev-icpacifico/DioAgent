from langchain.agents import create_tool_calling_agent, AgentExecutor
from agent.config import llm
from agent.tools import tools
from agent.agent_prompt import prompt

agent = create_tool_calling_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

if __name__ == "__main__":
    pregunta = input("👤 Usuario: ")
    respuesta = executor.invoke({"input": pregunta})
    print("🤖 Agente:", respuesta["output"])
