import librosa
import soundfile as sf

# Load the audio file
input_file = 'input_audio.wav'  # Replace with your audio file path
output_file = 'resampled_audio.wav'  # Output file path
target_sample_rate = 32000  # Target sample rate in Hz

# Load audio with librosa
audio, original_sample_rate = librosa.load(input_file, sr=None)

# Resample the audio to 32kHz
resampled_audio = librosa.resample(audio, orig_sr=original_sample_rate, target_sr=target_sample_rate)

# Save the resampled audio
sf.write(output_file, resampled_audio, target_sample_rate)

print(f"Audio resampled to {target_sample_rate} Hz and saved to {output_file}")