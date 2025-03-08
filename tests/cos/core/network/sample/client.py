import asyncio, websockets, json
import random, time

async def test():
    host        = f'localhost:8757'
    vessel_id   = 'bedc897f-512b-45a2-aea4-bcfc248d2a87'
    async with websockets.connect(f"ws://{host}/World/Vehicle/Vessel/POWER_DRIVEN/{vessel_id}") as websocket:
        random.seed(time.time())
        message = json.dumps({
                "r": {
                    'start': random.randrange(10, 1000)
                }                
            }
        )
        await websocket.send(message)

asyncio.new_event_loop().run_until_complete(test())