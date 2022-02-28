from ros import data_emitter
import json

async def emitter(socketio = None, dimensions = []):
    print(dimensions)
    data = data_emitter(dimensions)
    data_string = json.dumps(data, separators=(',', ':'))
    socketio.emit('data', data_string);