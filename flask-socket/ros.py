import random

def data_emitter(dimensions):
    # frame = {
    #     "a1": 1,   #0-2 0-->green 1--> yellow 2-->red
    #     "b1": 1,
    #     "c1": 1,
    #     "d1": 1,
    #     "e1": 1,
    #     "f1": 1,
    #     "g1": 1,
    #     "h1": 1,
    #     "a2": 1,
    #     "b2": 1,
    #     "c2": 1,
    #     "d2": 1,
    #     "e2": 1,
    #     "f2": 1,
    #     "g2": 1,
    #     "h2": 1,
    #     "building_height": 20.5, # 0-100 in meter
    #     "active_height": 10.3,   #1-100 in meter
    #     "speed":10,              #0-50 in cm/sec
    #     "distance":20,           #0-40 in meter
    #     "iteration":100,         #0-100
    #     "longitude": 743,        
    #     "latitude": 475,
    #     "acceleration": 1.5,     #0-50
    #     "jerk": 7
    # }
    randFrame = {
        "a1": random.randint(0, 2),   #0-2 0-->green 1--> yellow 2-->red
        "b1": random.randint(0, 2),
        "c1": random.randint(0, 2),
        "d1": random.randint(0, 2),
        "e1": random.randint(0, 2),
        "f1": random.randint(0, 2),
        "g1": random.randint(0, 2),
        "h1": random.randint(0, 2),
        "quad": random.randint(0, 7),  # quadrant from 0 to 7
        "building_height": random.uniform(0, 100), # 0-100 in meter
        "active_height": random.uniform(1, 100),   #1-100 in meter
        "speed":random.uniform(0, 50),              #0-50 in cm/sec
        "distance":random.uniform(0, 40),           #0-40 in meter
        "iteration":random.randint(0, 100),         #0-100
        "longitude": random.randint(0, 800),        
        "latitude": random.randint(0, 800),
        "acceleration": random.uniform(0, 50),     #0-50
        "jerk": random.randint(0, 20)
    }
    return {"data": randFrame};