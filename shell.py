import subprocess

def run(command):
    process = subprocess.Popen(
        [command],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        shell=True
    )

    output, _ = process.communicate()
    return output.decode('utf-8').strip()
