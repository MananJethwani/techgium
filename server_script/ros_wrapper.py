from ros import data_emitter
import json

async def emitter(sio = None, dimensions = []):
    print(dimensions)
    data = data_emitter(dimensions)
    data_string = json.dumps(data, separators=(',', ':'))
    await sio.emit('data', data_string);