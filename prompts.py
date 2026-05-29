from langchain_core.prompts import ChatPromptTemplate

from langchain_core.prompts import ChatPromptTemplate

character_prompt= ChatPromptTemplate.from_template(
    """
    You are an expert character designer.

    Create a detailed character for:

    {request}
    """
)

dialogue_prompt = ChatPromptTemplate.from_template(
    """
    You are an expert screenplay writer.

    Generate realistic dialogue for:

    {request}
    """
)

plot_prompt = ChatPromptTemplate.from_template(
    """
    You are an expert novelist.

    Generate a compelling plot for:

    {request}
    """
)