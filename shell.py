import subprocess

def execute(cmd):
  """
  Execute command in a subprocess.
  
  :param cmd: Command to execute.
  :return result: Tuple with return code, stdout and stderr.
  """

  process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  stdout, stderr = process.communicate()
  returncode = process.returncode

  return (returncode, stdout, stderr)

if __name__ == "__main__":
  output = execute("whoami")
  print(output[1])
