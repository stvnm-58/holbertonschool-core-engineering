import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

async def handle_client(websocket):
    print("Client connected")
    try:
        # Keep the connection open and continuously receive messages
        async for message in websocket:
            # Check if the message is empty after stripping whitespace
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                # Send OK: followed by the original, unaltered message
                await websocket.send(f"OK:{message}")
                
    except ConnectionClosed:
        print("Client disconnected gracefully")
    except Exception as e:
        print(f"An error occurred: {e}")

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
