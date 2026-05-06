import os
import subprocess


def define_env(env):
    if os.environ.get("version", "0.0000000") != "0.0000000":
        v = os.environ["version"]
    else:
        isodate = (
            subprocess.check_output("git show --format=format:%cI", shell=True)
            .decode()
            .splitlines()[0]
            .strip()
        )
        v = isodate[:10]
    env.variables["version"] = v
    env.variables["release"] = v
