from pyasn1.codec.ber import decoder
from pyasn1_modules import rfc1155
from pyasn1.type import univ

# Read the ASN.1 definitions from the provided file
with open('V2X_ASN.1_Module_Collection/J2735-ITIS.asn', 'r', encoding='latin-1') as file:
    asn1_definition = file.read()

# Parse the input data (assuming it's already in ASN.1 BER format)
with open('payloads.txt', 'r') as file:
    data = file.read()

# Decode the messages using the ASN.1 definitions
ber_data = bytes.fromhex(data)  # Assuming data is in hexadecimal format
decoded_messages, _ = decoder.decode(ber_data, asn1Spec=rfc1155.Message())

# Handle the decoded output
for msg in decoded_messages:
    print(msg.prettyPrint())
