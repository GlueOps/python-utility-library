from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import UnsupportedAlgorithm, InvalidSignature


def extract_serial_number_from_cert_string(cert_string):
    try:
        certificate = x509.load_pem_x509_certificate(cert_string.encode(), default_backend())
        decimal_serial = certificate.serial_number
        
        # Convert to hexadecimal
        hex_serial = format(decimal_serial, 'X')
        
        # Ensure an even number of digits for correct byte representation
        if len(hex_serial) % 2 != 0:
            hex_serial = '0' + hex_serial
        
        # Insert colons between every 2 characters
        colon_separated_serial = ":".join(hex_serial[i:i+2] for i in range(0, len(hex_serial), 2))
        return colon_separated_serial

    except (ValueError, UnsupportedAlgorithm, InvalidSignature) as e:
        # You can specify more exceptions as needed based on the specific errors you're encountering.
        raise ValueError("Provided certificate string is not parsable: " + str(e))
