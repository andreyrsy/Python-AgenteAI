# LangChain - Desenvolva agentes de inteligência artificial

Bem-vindo ao projeto! Aqui você encontra um exemplo prático e didático de como usar a biblioteca **LangChain** para criar agentes inteligentes capazes de interagir com dados reais de estudantes e universidades.

---

## 🚀 Sobre o Projeto

Este projeto demonstra como construir um agente de IA que responde perguntas sobre estudantes, suas preferências acadêmicas e possíveis universidades, utilizando dados reais e processamento de linguagem natural.

Você pode perguntar, por exemplo:
- "Quais os dados da Ana?"
- "Quais os dados de Ana e da Bianca?"

O agente entende, busca as informações nos arquivos CSV e retorna um resumo personalizado.

---

## 🧠 Aprendizados e Tecnologias

- **LangChain**: Aprendi como estruturar agentes inteligentes que conectam modelos de linguagem (LLMs) a ferramentas e dados externos. O LangChain facilita a criação de fluxos de decisão, integração com APIs e manipulação de prompts.
- **Integração com OpenAI**: O projeto utiliza o modelo GPT-4o para interpretar perguntas e gerar respostas precisas.
- **Manipulação de Dados com Pandas**: Os dados dos estudantes e universidades são lidos e processados a partir de arquivos CSV, mostrando como conectar IA a bases de dados reais.
- **Criação de Ferramentas Customizadas**: Desenvolvi ferramentas específicas para extrair e processar informações dos estudantes, integrando-as ao agente.
- **.env e Segurança**: Aprendi a proteger chaves de API usando variáveis de ambiente.

---

## 📁 Estrutura dos Dados

- `documentos/estudantes.csv`: Informações dos estudantes (notas, preferências, idiomas, etc.)
- `documentos/universidades.csv`: Dados sobre universidades (país, critérios de seleção, cursos de destaque, perfil desejado)

---

## 🛠️ Como rodar o projeto

1. **Clone o repositório** e instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. **Configure sua chave da OpenAI** em um arquivo `.env`:
   ```env
   OPENAI_API_KEY=sua-chave-aqui
   ```
3. **Execute o projeto**:
   ```bash
   python main.py
   ```
---

## 📚 Referências

- [LangChain Documentation](https://python.langchain.com/)
- [OpenAI API](https://platform.openai.com/docs/)
- [Pandas Documentation](https://pandas.pydata.org/)

---

Sinta-se à vontade para contribuir, adaptar ou usar como inspiração para seus próprios projetos! ✨ 
