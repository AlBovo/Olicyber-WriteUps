from morse_audio_decoder.morse import MorseCode # non ho voglia di scrivere tutto io :)
morse_code = MorseCode.from_wavfile("comunicazione.wav") # metterla nella main dir (Olicyber-WritesUp/....)
out = morse_code.decode()
print("flag{" + out + "}")
