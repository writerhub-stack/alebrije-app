def create_prompt(features):
    tempo = features['tempo']
    pitch = features['avg_pitch']
    energy = features['energy']

    traits = []

    if tempo > 120:
        traits.append("vibrant wings")
    else:
        traits.append("calm glowing eyes")

    if pitch > 180:
        traits.append("high-pitched bird voice")
    else:
        traits.append("deep lion roar")

    if energy > 0.1:
        traits.append("glowing patterns")
    else:
        traits.append("dark scales")

    return f"A magical alebrije with {', '.join(traits)}"