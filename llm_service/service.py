
from llm_service.llm_abc import LLMABC


class LLMService:
    def __init__(self, llm: LLMABC):
        self.llm = llm
    
    async def generate_response(self, prompt: str):
        async for response in self.llm.generate_response(prompt):
            yield response
        