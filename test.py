import subprocess
line = "iu.mp3"
input_path ="local_input"

subprocess.run(["echo", line, input_path], check=True)