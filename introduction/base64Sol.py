import base64

encoded_flag_hex = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'
encoded_flag_bytes = bytes.fromhex(encoded_flag_hex)
encoded_flag_base64 = base64.b64encode(encoded_flag_bytes)

print(encoded_flag_base64.decode('utf-8'))