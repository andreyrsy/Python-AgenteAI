from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_tools_agent
from langchain import hub
from langchain.agents import Tool
import os
from estudante import DadosDeEstudante

class AgenteOpenAIFunctions:
    def __init__(self):
        llm = ChatOpenAI(model="gpt-4o",
                         api_key=os.getenv("OPENAI_API_KEY"))

        dados_de_estudante = DadosDeEstudante()
        self.tools = [
            Tool(name = dados_de_estudante.name,
                func = dados_de_estudante.run,
                description = dados_de_estudante.description)
        ]

        prompt = hub.pull("hwchase17/openai-functions-agent")
        self.agente = create_openai_tools_agent(llm, self.tools, prompt)
