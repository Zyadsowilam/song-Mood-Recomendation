import librosa
import numpy as np
import os
import librosa
import numpy as np
import pandas as pd

def extract_audio_features(audio_file):
    # Load the audio file
    audio, sr = librosa.load(audio_file)

    # Extract features
    chroma_stft = np.mean(librosa.feature.chroma_stft(y=audio, sr=sr))
    spectral_centroid = np.mean(librosa.feature.spectral_centroid(y=audio, sr=sr))
    spectral_bandwidth = np.mean(librosa.feature.spectral_bandwidth(y=audio, sr=sr))
    spectral_contrast = np.mean(librosa.feature.spectral_contrast(y=audio, sr=sr))
    spectral_rolloff = np.mean(librosa.feature.spectral_rolloff(y=audio, sr=sr))
    mel_frequencies = np.mean(librosa.feature.mfcc(y=audio, sr=sr))
    rmse = np.mean(librosa.feature.rms(y=audio))
    zero_crossing_rate = np.mean(librosa.feature.zero_crossing_rate(y=audio))
    mfccs = np.mean(librosa.feature.mfcc(y=audio, sr=sr), axis=1)
    chroma_cqt = np.mean(librosa.feature.chroma_cqt(y=audio, sr=sr))
    chroma_cens = np.mean(librosa.feature.chroma_cens(y=audio, sr=sr))
    melspectrogram = np.mean(librosa.feature.melspectrogram(y=audio, sr=sr))
    spectral_contrast = np.mean(librosa.feature.spectral_contrast(y=audio, sr=sr))
    spectral_flatness = np.mean(librosa.feature.spectral_flatness(y=audio))
    spectral_rolloff = np.mean(librosa.feature.spectral_rolloff(y=audio, sr=sr))
    tonnetz = np.mean(librosa.feature.tonnetz(y=audio, sr=sr))
    poly_features = np.mean(librosa.feature.poly_features(y=audio, sr=sr))
    
    # Create a dictionary to store the feature names and values
    features = {
        'chroma_stft': chroma_stft,
        'spectral_centroid': spectral_centroid,
        'spectral_bandwidth': spectral_bandwidth,
        'spectral_contrast': spectral_contrast,
        'spectral_rolloff': spectral_rolloff,
        'mel_frequencies': mel_frequencies,
        'rmse': rmse,
        'zero_crossing_rate': zero_crossing_rate,
        'mfcc1': mfccs[0],
        'mfcc2': mfccs[1],
        'mfcc3': mfccs[2],
        'mfcc4': mfccs[3],
        'mfcc5': mfccs[4],
        'mfcc6': mfccs[5],
        'mfcc7': mfccs[6],
        'mfcc8': mfccs[7],
        'mfcc9': mfccs[8],
        'mfcc10': mfccs[9],
        'mfcc11': mfccs[10],
        'mfcc12': mfccs[11],
        'mfcc13': mfccs[12],
        'chroma_cqt': chroma_cqt,
        'chroma_cens': chroma_cens,
        'melspectrogram': melspectrogram,
        'spectral_contrast': spectral_contrast,
        'spectral_flatness': spectral_flatness,
        'tonnetz': tonnetz,
        'poly_features': poly_features
    }

    return features


# Example usageD:\Song\songar\accompaniment.wav

audio_file = 'D:\\songs\\John Legend - All of Me (minus).mp3'
song_features = extract_audio_features(audio_file)
print(song_features)
{'chroma_stft': 0.18411036, 'spectral_centroid': 829.8279940630372, 'spectral_bandwidth': 860.5051180217334,
  'spectral_contrast': 29.536556498596156, 'spectral_rolloff': 1476.901748646037, 'mel_frequencies': -8.247642,
    'rmse': 0.10286317, 'zero_crossing_rate': 0.044962654620406585, 'mfcc1': -272.66647, 'mfcc2': 169.58217,
      'mfcc3': -24.468819, 'mfcc4': 13.37361, 'mfcc5': -4.9846187, 'mfcc6': -12.000866, 'mfcc7': 0.47936085,
        'mfcc8': -10.582651, 'mfcc9': -12.728232, 'mfcc10': -7.13533, 'mfcc11': -7.0393815, 
        'mfcc12': -13.347118, 'mfcc13': -8.882324, 'chroma_cqt': 0.22664663, 'chroma_cens': 0.15978836, 
        'melspectrogram': 2.9806747, 'spectral_flatness': 0.029178182, 'tonnetz': -0.02973494112901434, 
        'poly_features': 0.832272234147957}