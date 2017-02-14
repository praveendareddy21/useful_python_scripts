import subprocess
#subprocess.call("date")
print("bs=100 count=10M")
for i in range(5):
	subprocess.call("dd bs=100 count=10M if=/dev/zero of=test", shell=True)
print("===========================")

#subprocess.call("iozone -R -r 1M -s 100m", shell=True)


print("bs=100 count=1M")
for i in range(5):
	subprocess.call("dd bs=100 count=1M if=/dev/zero of=test", shell=True)
print("===========================")



print("bs=100 count=100K")
for i in range(5):
	subprocess.call("dd bs=100 count=100k if=/dev/zero of=test", shell=True)
print("===========================")


print("bs=100 count=10K")
for i in range(5):
	subprocess.call("dd bs=100 count=10k if=/dev/zero of=test", shell=True)
print("===========================")


print("bs=100 count=1k")
for i in range(5):
	subprocess.call("dd bs=100 count=1k if=/dev/zero of=test", shell=True)
print("===========================")


print("bs=100 count=100")
for i in range(5):
	subprocess.call("dd bs=100 count=100 if=/dev/zero of=test", shell=True)
print("===========================")
