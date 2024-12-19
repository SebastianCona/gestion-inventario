import json
import asyncio
import httpx

class SessionManager:
    def __init__(self, request_data):
        self.url = "http://localhost:8000/auth/register"
        self.request_data = request_data
        self.headers = {"Content-Type": "application/json"}

    def to_json(self) -> str:
        """
        Convert the dictionary to a JSON string.
        
        Returns:
            str: JSON-formatted string of the dictionary.
        """
        try:
            return json.dumps(self.data)
        except (TypeError, ValueError) as e:
            raise ValueError(f"Invalid data format: {e}")

    async def auth_register(self):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                self.url, json=self.request_data, headers=self.headers
            )
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response
    
