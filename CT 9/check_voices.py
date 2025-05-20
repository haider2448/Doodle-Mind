import pyttsx3

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Get available voices
voices = engine.getProperty('voices')

print('Available voices:')
for i, voice in enumerate(voices):
    print(f'Voice {i}: {voice.name} (ID: {voice.id})')
