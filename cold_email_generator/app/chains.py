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
        prompt = f"""
        You are a professional job seeker applying for a **{job_role}** position.

        Below is the job description:
        --------------------
        {job_description}
        --------------------

        Here are your portfolio links: {portfolio_links}

        Write a professional and personalized cold email **following the structure below exactly**.
        Your tone should be confident and enthusiastic, without mentioning AI.

        Respond in plain text using this format (do not add markdown or special characters like ** or ##):

        Subject: [Write a compelling subject line]

        Dear [Hiring Manager/Team Name],

        [Body: Briefly express your excitement and explain why you're a good fit based on skills, experience, and the job description.]

        [Mention your portfolio and express interest in connecting or discussing further.]

        Best regards,  
        [Your Name]  
        [Your Contact Info (email/LinkedIn)]  
        [Your Location (optional)]
        """
        return self.llm.invoke(prompt)



if __name__ == "__main__":
    print(os.getenv("GROQ_API_KEY"))