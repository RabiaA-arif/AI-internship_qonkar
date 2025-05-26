import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
load_dotenv()

class Chain:
    def __init__(self):
        
        self.llm = ChatGroq(temperature=0, model_name="gemma2-9b-it")

    def write_mail(self, job_description, portfolio_links, job_role):
        prompt = f"""write a cold email{job_description}
        """
        return self.llm.invoke(prompt)

if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))