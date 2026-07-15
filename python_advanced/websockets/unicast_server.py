import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

# Global set to keep track of active connections
connected_clients = set()

async def handle_client(websocket):
    # Register the new connection
    connected_clients.add(websocket)
    print(f"Client connected. Total clients: {len(connected_clients)}")
    
    try:
        # Keep connection open and receive messages from this specific client
        async for message in websocket:
            # Unicast: Send the response ONLY to this specific connection
            await websocket.send(f"U:{message}")
            
    except ConnectionClosed:
        print("Client disconnected gracefully")
    finally:
        # Unregister the client when they disconnect
        connected_clients.remove(websocket)
        print(f"Client disconnected. Total clients: {len(connected_clients)}")

async def main():
    # Start the WebSocket server on localhost, port 8765
    async with websockets.serve(handle_client, "localhost", 8765):
        print("WebSocket Server running on ws://localhost:8765")
        await asyncio.Future()  # Keep the server running indefinitely

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nServer stopped.")
