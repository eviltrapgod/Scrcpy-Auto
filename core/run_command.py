import subprocess


def run(self, command):
    subprocess.run(command, shell=True)
