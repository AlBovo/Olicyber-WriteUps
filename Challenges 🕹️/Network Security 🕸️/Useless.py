import pyshark # libreria per usare i file di wireshark su python 
cap = pyshark.FileCapture("capture.pcapng") # il file come al solito deve essere nella main dir di questo progetto
print(cap[0])