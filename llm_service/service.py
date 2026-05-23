
from llm_service.llm_abc import LLMABC


class LLMService:
    def __init__(self, llm: LLMABC):
        self.llm = llm
        