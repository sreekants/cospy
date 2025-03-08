import asyncio
import websockets
import json

start_at = 0

def response(msgid, target):
    return { 
            "r": {
                 'id': 1, 
                 'guid': 'bedc897f-512b-45a2-aea4-bcfc248d2a8d', 
                 'name': 'True North', 
                 'identifier': {'imo': '9713076', 'mmsi': '6360214245LDW9'}, 
                 'length': [300.0, 50.0, -1.0], 
                 'weight': 8390.0, 
                 'pose': {
                     'position': [0,0,1,10,20,20], 
                     'X': [], 
                     'R': []
                    },

                'angle':f"{msgid+1000}",
                'angleSetpoint':f"{msgid+2000}", 
                'thrust':f"{msgid+3000}", 
                'thrustSetpoint':f"{msgid+4000}" 
            }
        }



async def notify(websocket):
    print("Client connected")
    target = websocket.request.path
    try:
        global start_at
        # Send messages to the client asynchronously
        for i in range(1, 1000):  
            resp    = response(start_at+i, target)
            message = json.dumps(resp)
            await websocket.send(message)
            await asyncio.sleep(2)  # Wait 2 seconds before sending the next message

        # Keep the connection alive to receive messages from the client
        async for message in websocket:
            req = json.loads(message)
            print(f"Received from client: {req['r']['start']}")

    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    finally:
        print("Client disconnected")


async def api(websocket):
    print("RPC:Client connected")
    try:
        global start_at
        async for message in websocket:
            req = json.loads(message)
            start_at = req['r']['start']
            print(f"Received from client: {start_at}")

    except websockets.exceptions.ConnectionClosed as e:
        print(f"Connection closed: {e}")
    finally:
        print("Client disconnected")


# Server loops to service clients
async def ipc():
    async with websockets.serve(notify, "localhost", 8756):
        await asyncio.Future()  # run forever

async def rpc():
    async with websockets.serve(api, "localhost", 8757):
        await asyncio.Future()  # run forever

def main():   
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.create_task(ipc())
    loop.create_task(rpc())
    loop.run_forever()


if __name__ == "__main__":
    main()