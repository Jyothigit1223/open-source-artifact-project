import subprocess

package="requests"

print("Downloading package:",package)

subprocess.run(["pip","download",package])

print("Download completed")
