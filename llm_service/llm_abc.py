from abc import ABC, abstractmethod
from typing import AsyncGenerator

class LLMABC(ABC):
    @abstractmethod
    async def  generate_response(self, prompt: str) -> AsyncGenerator[str, None]:
        pass