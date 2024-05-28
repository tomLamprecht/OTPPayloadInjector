# OTPPayloadInjector

**OTPPayloadInjector** is a tool designed to encrypt shellcode payloads using a one-time pad and dynamically inject them into a C program during runtime for execution, aiming to bypass Windows Defender. The original payload will be split up in 2 parts one being hardcoded into the executeable and the other one being written to a .bin file which is getting read by the executeable during runtime.

## Features

- **One-Time Pad Encryption**: Securely encrypts shellcode payloads to prevent any static flagging.
- **Dynamic Injection**: Loads the original payload on the stack and executes it from the stack.
- **Automated Compilation**: Compiles the generated C file into an executable.
- **Windows Defender Evasion**: Enhances payload delivery by aiming to bypass security measures.

## Usage

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/tomLamprecht/OTPPayloadInjector.git
    cd OTPPayloadInjector
    ```

2. **Prepare the Payload**: Modify `encoder.py` to include your desired shellcode payload. (Default payload is calc.exe)

3. **Run the Encoder**:
    ```sh
    python encoder.py
    ```

4. **Compile and Execute**: The script generates and compiles the C file into an executable.

## Files

- `encoder.py`: Main script for payload encryption and compilation.
- `template.c`: C template with placeholders for the encrypted payload and key.
- `keyfile.bin`: Binary file storing the one-time pad key (excluded from version control).

## Disclaimer

This tool is intended for educational purposes and authorized testing only. Misuse of this tool may result in legal consequences. Ensure you have explicit permission before running shellcode on any system.

---

**OTPPayloadInjector** © 2024 by Tom Lamprecht. All rights reserved.
