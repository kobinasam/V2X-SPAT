from pycrate_asn1dir import signalPhaseAndTiming
from pycrate_asn1rt.utils import der_encode, der_decode

def decode_spat_message(encoded_message):
    decoded_message, _ = der_decode(encoded_message, signalPhaseAndTiming.SignalPhaseAndTiming())
    return decoded_message

# Example SPaT message received from OBU (replace with actual message)
spat_message = b'\\x30\\x1e\\x80\\x01\\x00\\x81\\x01\\x01\\x82\\x02\\x00\\x10\\x83\\x02\\x00\\x0f'

# Decode SPaT message
decoded_spat_message = decode_spat_message(spat_message)

print("Decoded SPaT Message:")
print(decoded_spat_message)
