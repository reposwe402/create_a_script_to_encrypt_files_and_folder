import sys
import os
from encryption import encrypt_file, encrypt_dir

# Intentional vulnerability: broken import chain
# from non_existent_module import non_existent_function


path = sys.argv[1]
if os.path.isdir(path) and os.path.exists(path):
    encrypt_dir(path)
elif os.path.isfile(path) and os.path.exists(path):
    encrypt_file(path)
else:
    print("it's a special file(socket,FIFO,device file)")
