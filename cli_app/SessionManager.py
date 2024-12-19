import json
import asyncio
import httpx

class SessionManager:
    def __init__(self, request_data):
        self.base_url = "http://localhost:8000"
        self.request_data = request_data
        self.headers = {"Content-Type": "application/json"}
        self.refresh_token = ""
        self.access_token = ""

    async def auth_register(self):
        endpoint = self.base_url + "/auth/register"
        async with httpx.AsyncClient() as client:
            response = await client.post(
                endpoint, json=self.request_data, headers=self.headers
            )
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response

    async def auth_login(self):
        endpoint = self.base_url + "/auth/login"
        async with httpx.AsyncClient() as client:
            response = await client.post(
                endpoint, json=self.request_data, headers=self.headers
            )
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            jwt_tokens = response.json()  # Store the JSON response that contains access and refresh tokens
            
            access_token = jwt_tokens.get("access")
            refresh_token = jwt_tokens.get("refresh")
            
            return response 
    
