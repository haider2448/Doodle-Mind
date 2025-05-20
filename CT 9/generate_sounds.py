import pyttsx3
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Set voice properties
# Get available voices
voices = engine.getProperty('voices')
# Explicitly set Microsoft Zira female voice
for voice in voices:
    if "Microsoft Zira" in voice.name:
        engine.setProperty('voice', voice.id)
        break
# Set slower speech rate for better clarity
engine.setProperty('rate', 120)  # Normal rate is around 200
# Set volume to maximum
engine.setProperty('volume', 1.0)

# List of characters and their descriptions
characters = {
    'A': "Let's draw A",
    'B': "Let's draw B",
    'C': "Let's draw C",
    'D': "Let's draw D",
    'E': "Let's draw E",
    '1': "Let's draw one",
    '2': "Let's draw two",
    '3': "Let's draw three",
    '4': "Let's draw four",
    '5': "Let's draw five"
}

# Create sounds directory if it doesn't exist
if not os.path.exists('sounds'):
    os.makedirs('sounds')

# Generate sounds for each character
for char, text in characters.items():
    # Save the initial sound (with "Let's draw")
    engine.save_to_file(text, f'sounds/{char}_initial.mp3')
    
    # Save the character-only sound for speaker button
    engine.save_to_file(char, f'sounds/{char}_charonly.mp3')
    
    # Save the correct sound
    engine.save_to_file(f"Right! It's {char}", f'sounds/{char}_correct.mp3')
    
    # Save the wrong sound
    engine.save_to_file("Wrong", f'sounds/{char}_wrong.mp3')
    
    engine.runAndWait()
    print(f'Generated sounds for {char}')
