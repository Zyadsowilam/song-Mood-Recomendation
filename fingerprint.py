import librosa
import numpy as np
import soundfile as sf

def compute_spectrogram(audio_file):
    audio, sr = librosa.load(audio_file)
    spectrogram = librosa.feature.melspectrogram(audio, sr=sr)
    return audio, sr, spectrogram

# List of audio files
audio_files = [
    'E:\\songR\\Song-Mood-Recommendation\\happ\\accompaniment.wav',
    'E:\\songR\\Song-Mood-Recommendation\\sonngg\\accompaniment.wav',
    'E:\\songR\\Song-Mood-Recommendation\\song2\\accompaniment.wav'
]

# Compute spectrograms for each audio file
spectrograms = []
for file in audio_files:
    audio, sr, spectrogram = compute_spectrogram(file)
    spectrograms.append(spectrogram)

# Compare spectrograms
common_features = set(spectrograms[0].flatten())
for spectrogram in spectrograms[1:]:
    common_features = common_features.intersection(spectrogram.flatten())

# Convert common features to audio
common_audio = np.zeros_like(audio)
for feature in common_features:
    common_audio += np.sin(2 * np.pi * feature * np.arange(len(audio)) / sr)

# Save common features as text file
with open('common_features.txt', 'w') as f:
    for feature in common_features:
        f.write(str(feature) + '\n')

# Save common audio as WAV file
sf.write('common_audio.wav', common_audio, sr)

# Play common audio
import IPython.display as ipd
ipd.Audio('common_audio.wav')
