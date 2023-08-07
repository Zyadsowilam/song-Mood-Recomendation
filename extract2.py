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

# Example usage

input_folder = 'E:\\Music\\sad\\'
output_excel = 'D:\\songs\\output_features.xlsx'

# If the output Excel file exists and is a valid Excel file, load it
if os.path.exists(output_excel) and output_excel.endswith('.xlsx'):
    try:
        df = pd.read_excel(output_excel, engine='openpyxl')
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        df = pd.DataFrame()
else:
    df = pd.DataFrame()

# Walk through all subdirectories in the input folder
for root, _, files in os.walk(input_folder):
    for file in files:
        if file.endswith('.wav') and file.lower() == 'accompaniment.wav':
            full_audio_file_path = os.path.join(root, file)
            print(f"Processing: {full_audio_file_path}")

            # Check if the audio file exists and is being loaded correctly
            if not os.path.exists(full_audio_file_path):
                print(f"Audio file not found: {full_audio_file_path}")
                continue

            song_features = extract_audio_features(full_audio_file_path)

            # Get the folder name from the subdirectory
            folder_name = os.path.basename(root)
            song_features['folder_name'] = folder_name

            df = df._append(song_features, ignore_index=True)

# Save the DataFrame to the Excel file with xlsx format
df.to_excel(output_excel, index=False, engine='openpyxl')
