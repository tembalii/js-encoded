import os

import paramiko
from fastapi import FastAPI

app = FastAPI()

@app.get("/direct/{input}")
def direct_response(input: str):

    tainted = input
    rand = os.urandom()

    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.WarningPolicy())
    client.connect('localhost', port, username, password)

    # proruleid: tainted-os-command-paramiko-fastapi
    stdin, stdout, stderr = client.exec_command(f"git clone {tainted}")

    # ok: tainted-os-command-paramiko-fastapi
    stdin, stdout, stderr = client.exec_command(f"git clone {rand}")

    # ok: tainted-os-command-paramiko-fastapi
    stdin, stdout, stderr = client.exec_command(f"git clone my-repo")


    client.close()
