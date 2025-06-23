import librosa

def analyze_audio(path):
    y, sr = librosa.load(path)

    tempo, _ = librosa.beat.beat_track(y=y,sr=sr)
    pitch =librosa.yin(y, fmin=50, fmax=300, sr=sr)
    avg_pitch = pitch.mean()

    energy = sum(abs(y)) / len(y)

    return {
        "tempo": tempo, #Beats per minute
        "avg_pitch": avg_pitch, #average pitch frequency
        "energy": energy #how "loud" the track feels
    }