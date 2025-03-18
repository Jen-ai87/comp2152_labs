import os
import sys
import platform
import socket


# 3a.a. Get the machine type
print(platform.machine())

# 3a.b. Get the processor type (architecture)
print(platform.architecture())

# 3a.c. Set the default timeout for a socket (in seconds) to 50 seconds
socket.setdefaulttimeout(50)

# 3a.d. Get the default socket timeout
print(socket.getdefaulttimeout())

# 3a.e. Get the operating system name
print(os.name)
print(platform.system())  # More user-friendly OS name

# 3a.f. Get the current process ID
print(os.getpid())

# 3a.g. Fork a new process (Unix-based systems only)


# 3b.a. Open (or create) a file named fdpractice.txt
fd = os.open("../../fdpractise.txt", os.O_RDWR | os.O_CREAT)

# 3b.b. Print the current process id
print(f"Current process ID: {os.getpid()}")

# 3b.d. Write the following text to the file: "Some string to write to the file"
os.write(fd, b"Hello my name is Jen Henry")

# 3b.e. Fork a new process
pid = os.fork()

# Fork returns 0 if Child process
if pid == 0:
    # 3b.e.a.a Print the current process id
    print(f"Child process ID: {os.getpid()}")
    # 3b.e.a.b Move the file pointer back to the beginning of the file
    os.lseek(fd, 0, os.SEEK_SET)
    # 3b.e.a.c. Read 100 bytes maximum and print out the contents
    data = os.read(fd, 100)
    print(f"Child read: {data.decode()}")
    # 3b.e.a.d. Close the file
    os.close(fd)
    # 3b.e.a.e. Exit the process
    os._exit(0)
else:  # Parent process
    # 3b.e.b.a. Print the current process id
    print(f"Parent process ID: {os.getpid()}")
    # 3b.e.b.b. Wait for the child process to finish
    os.waitpid(pid, 0)
    # 3b.e.b.c. Close the file
    os.close(fd)
