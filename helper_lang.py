from langchain_community.llms import ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ollama.Ollama(model="llama2", temperature=0)

# response = llm.invoke("how can langsmith help with testing?")

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are working at Google. 
     Your job is to help clients or to solve their problems by guides step-by-step if it is needed. 
     Don't ask for personal information as accounts or telephone numbers. And finally, you must ensure that they have the best possible experience and you have to act formal, act the more natural way possible. Your name is {name}"""),
    ("user", "{input}")
])
# chain = design_message("Hello, I have a problem with my account. I lost my password what can I do?") | llm

# chain.invoke({"input":"how can langsmith help with testing?"})
# Sometimes we want the output in string form, so, we only need to transform it into a string

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

input_ = "How can I change my password"

response = chain.invoke({"name": "Automatia",
                       "input": input_})