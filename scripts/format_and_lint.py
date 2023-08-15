import subprocess

# Run autopep8 on all Python files
subprocess.run(["autopep8", "--in-place", "--aggressive", "--aggressive", "--recursive", "."])

# Run isort on all Python files
subprocess.run(["isort", "--recursive", "."])

# Run flake8 on all Python files
subprocess.run(["flake8"])
