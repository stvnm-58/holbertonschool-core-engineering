#!/usr/bin/env python3
"""Echo server using the asyncio API."""
import asyncio
from websockets.asyncio.server import serve


async def connection_handler(websocket):
    """Handle the websocket connection and echo back messages."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the websocket server."""
    async with serve(connection_handler, "localhost", 8765) as server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
