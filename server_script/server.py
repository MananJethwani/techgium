from aiohttp import web
from setInterval import setInterval
from ros_wrapper import emitter
import socketio
import json

sio = socketio.AsyncServer(cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

# setting the interval function
args = [sio]
interval = setInterval(emitter, 1, args, False)

async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.on('start')
async def start_transmission(sid, message):
    dimensions = json.loads(message)
    print(dimensions)
    interval.start(dimensions)

@sio.on('stop')
async def stop_transmission(sid, message):
    print(message)
    interval.stop()



app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)
