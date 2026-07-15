#!/usr/bin/env python3
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

# Global set to keep track of active connections
connected_clients = set()


async def connection_handler(websocket):
    # Register the new connection
    connected_clients.add(websocket)
    print(f"Client connected. Total clients: {len(connected_clients)}")

    try:
        # Receive messages continuously from this client
        async for message in websocket:
            # Format the broadcast payload
            broadcast_message = f"B:{message}"

            # Broadcast to all connected clients concurrently
            if connected_clients:
                tasks = [
                    client.send(broadcast_message)
                    for client in connected_clients
                ]
                await asyncio.gather(*tasks)

    except ConnectionClosed:
        print("Client disconnected gracefully")
    finally:
        # Unregister the client when they disconnect
        connected_clients.remove(websocket)
        print(f"Client disconnected. Total clients: {len(connected_clients)}")


async def main():
    # Start the WebSocket server on localhost, port 8765
    async with websockets.serve(connection_handler, "localhost", 8765):
        print("WebSocket Server running on ws://localhost:8765")
        await asyncio.Future()  # Keep the server running indefinitely


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped.")
