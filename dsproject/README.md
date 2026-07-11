### MLFLOW On AWS

## MLflow on AWS Setup:

1. Login to AWS console.
2. Create IAM user with AdministratorAccess
3. Export the credentials in your AWS CLI by running "aws configure"
4. Create a s3 bucket
5. Create EC2 machine (Ubuntu) & add Security groups 5000 port

Use Ubuntu 24.04 LTS (noble) for the EC2 instance — newer Ubuntu releases (e.g. 26.04) ship Python 3.14, which crashes recent MLflow versions with
`ImportError: cannot import name 'Traversable' from 'importlib.abc'`. Ubuntu 24.04 ships Python 3.12 by default, which is compatible.

A ~1GB instance (t2.micro/t3.micro) can OOM-kill the MLflow server process under load — add swap (step below) if you see the server silently die with `Killed` or `Child process ... died` and no traceback.

Run the following commands on the EC2 machine
```bash
sudo apt update && sudo apt upgrade -y

python3 --version   # should be 3.12.x on Ubuntu 24.04

# Ubuntu 24.04 blocks system-wide `pip install` (PEP 668) — use pipx instead
sudo apt install -y pipx
pipx ensurepath
source ~/.bashrc
pipx install pipenv

mkdir mlflow
cd mlflow

pipenv install --python python3.12 mlflow awscli boto3

pipenv shell


## Then set aws credentials
aws configure


## Add swap if on a small instance (recommended for t2.micro/t3.micro, 1GB RAM)
# Skip if `free -h` already shows Swap > 0
sudo fallocate -l 2G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile swap swap defaults 0 0' | sudo tee -a /etc/fstab
free -h   # confirm Swap shows 2.0Gi


#Finally
# --allowed-hosts / --cors-allowed-origins are required on newer MLflow —
# without them the built-in security middleware rejects any Host header
# that isn't localhost, even with -h 0.0.0.0
mlflow server -h 0.0.0.0 --workers 1 \
  --default-artifact-root s3://mlflowtrackingtesting \
  --allowed-hosts "*" \
  --cors-allowed-origins "*"

#open Public IPv4 DNS to the port 5000 (must be http://, not https:// — this server has no TLS)


#set uri in your local terminal and in your code 
export MLFLOW_TRACKING_URI=http://ec2-13-60-30-82.eu-north-1.compute.amazonaws.com:5000/