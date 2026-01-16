

def map_voice_params(emotion, intensity):
    if emotion == "happy":
        return {
            "rate": 1.1 + intensity * 0.3,
            "pitch": 1.2 + intensity * 0.4,
            "volume": 1.0
        }

    elif emotion == "frustrated":
        return {
            "rate": 0.9 - intensity * 0.2,
            "pitch": 0.8 - intensity * 0.3,
            "volume": 0.9
        }

    else:  # neutral
        return {
            "rate": 1.0,
            "pitch": 1.0,
            "volume": 1.0
        }

