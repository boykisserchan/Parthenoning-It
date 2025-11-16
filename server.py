import asyncio
import websockets
import subprocess

async def handler(websocket):
    async for message in websocket:
        result = subprocess.run(
            ["python3", "idk.py"], capture_output=True, text=True
        )
        await websocket.send(result.stdout)

asyncio.run(websockets.serve(handler, "localhost", 6967))