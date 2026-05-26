class ChatService:
    def __init__(self, llm_service):
        self.llm = llm_service
    
    async def get_response(self, query:str, metadata: dict):
        response = await self.llm.generate_response(query, **metadata)
        return response