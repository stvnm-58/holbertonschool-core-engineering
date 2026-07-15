from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect

# Simple HTML page to serve at http://localhost:8000
HTML_CONTENT = """
<!DOCTYPE html>
<html>
    <head>
        <title>Starlette WebSocket Echo</title>
    </head>
    <body>
        <h1>Starlette WebSocket App</h1>
        <p>Use a WebSocket client to connect to <code>ws://localhost:8000/ws</code></p>
    </body>
</html>
"""

async def homepage(request):
    """Handles standard HTTP GET requests to '/'."""
    return HTMLResponse(HTML_CONTENT)

async def websocket_endpoint(websocket):
    """Handles stateful WebSocket connections at '/ws'."""
    # Complete the WebSocket handshake
    await websocket.accept()
    
    try:
        # Loop continuously to receive and echo messages
        while True:
            # Receive text data from the client
            message = await websocket.receive_text()
            # Echo the exact message back to the sender
            await websocket.send_text(message)
            
    except WebSocketDisconnect:
        print("WebSocket client disconnected gracefully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define Starlette application with both HTTP and WebSocket routing
app = Starlette(routes=[
    Route("/", homepage, methods=["GET"]),
    WebSocketRoute("/ws", websocket_endpoint),
])
