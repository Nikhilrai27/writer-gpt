from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import (
    GOOGLE_API_KEY,
    LLM_MODEL,
    LLM_TEMPERATURE,
    LLM_MAX_TOKENS,
)
from src.prompts import (
    character_prompt,
    dialogue_prompt,
    plot_prompt,
    memory_prompt,
)
from src.schemas import CharacterMemory


llm = ChatGoogleGenerativeAI(
    model=LLM_MODEL,
    google_api_key=GOOGLE_API_KEY,
    temperature=LLM_TEMPERATURE,
    max_tokens=LLM_MAX_TOKENS,
)

character_chain = character_prompt | llm
dialogue_chain = dialogue_prompt | llm
plot_chain = plot_prompt | llm
structured_llm = llm.with_structured_output(CharacterMemory)
memory_chain = memory_prompt | structured_llm
