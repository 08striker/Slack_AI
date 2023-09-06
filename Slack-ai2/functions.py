from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

import os
os.environ['OPENAI_API_KEY'] = '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'


load_dotenv(find_dotenv())


def draft_email(user_input, name="Austen"):
    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=1)

    template = """
    
    You are a Rude chat bot that roasts people.
    
    Your goal is to reply back with angry  and clever responses that makes them speechless.
    
    Keep your reply short and to the point. try to make them angry by teasing them
    
    
    """

    # signature = f"Kind regards, \n\{name}"
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = "remeber you're goal is to make people angry: {user_input}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    response = chain.run(user_input=user_input, name=name)

    return response