from langchain_core.prompts import ChatPromptTemplate


character_prompt = ChatPromptTemplate.from_template(
    """
You are an expert character designer. Create a detailed character for:

{request}

Include their background, personality, motivations, flaws, and appearance.
"""
)

dialogue_prompt = ChatPromptTemplate.from_template(
    """
You are an expert screenplay writer. Generate realistic dialogue for:

{request}

Context from previous memory:
{context}
"""
)

plot_prompt = ChatPromptTemplate.from_template(
    """
You are an expert novelist. Generate a compelling plot for:

{request}

Context from previous memory:
{context}
"""
)

memory_prompt = ChatPromptTemplate.from_template(
    """
Extract important long-term character facts from the following character description:

{character}

Return structured memory with name, role, summary, and key facts.
"""
)
