import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer

# Load the data from the Excel file

input_excel = 'D:\\songs\\output_features.xlsx'
df = pd.read_excel(input_excel, engine='openpyxl')

# Randomize the data except for the first row (header)
df = df.sample(frac=1, random_state=42)

# Select input features and label
X = df.iloc[:, 0:26].values  # Features: chroma_stft, spectral_centroid, spectral_bandwidth, spectral_contrast, spectral_rolloff, mel_frequencies
y = df.iloc[:, 28].values    # Label: mood (assuming mood is at column index 7, which is the 8th column in Excel)

# Encode the target variable as numeric labels
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

# Print unique values in the target variable after encoding
print("Unique values in target variable (after encoding):", set(y))

# Handle missing values in the input data
imputer = SimpleImputer(strategy='mean')

# Get the number of samples in the dataset
total_samples = len(df)

# Split the data into training and testing sets (80% for training, 20% for testing)
test_size = 0.2
train_size = int(total_samples * (1 - test_size))
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)

print(f"Number of samples in the dataset: {total_samples}")
print(f"Number of samples in the training set: {len(X_train)}")
print(f"Number of samples in the testing set: {len(X_test)}")

# Fit the imputer only on the training data and then transform both the testing data and input data
X_train = imputer.fit_transform(X_train)
X_test = imputer.transform(X_test)

# Create and train a Random Forest Classifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print("Confusion Matrix:")
print(conf_matrix)
# Get input data from the user
input_data = [float(input(f"Enter {feature}: ")) for feature in df.columns[0:26]]
input_data = imputer.transform([input_data])  # Handle missing values in input data

# Make prediction on the input data
predicted_mood = model.predict(input_data)[0]
predicted_mood_label = label_encoder.inverse_transform([predicted_mood])[0]

print(f"Predicted Mood: {predicted_mood} (0: Sad, 1: Happy)")
print(f"Predicted Mood Label: {predicted_mood_label}")