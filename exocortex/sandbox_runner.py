import subprocess
import tempfile
from pathlib import Path
import datetime

def run_code_in_sandbox(code: str, timeout: int = 5):
    """
    Runs Python code in a temporary isolated file.
    Returns:
      - stdout (string)
      - stderr (string)
      - success (True/False)
    """

    start_time = datetime.datetime.utcnow()

    with tempfile.TemporaryDirectory() as tmpdir:
        script_path = Path(tmpdir) / "script.py"
        script_path.write_text(code)

        try:
            process = subprocess.Popen(
                ["python3", str(script_path)],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            stdout, stderr = process.communicate(timeout=timeout)
            success = (process.returncode == 0)

        except subprocess.TimeoutExpired:
            process.kill()
            stdout, stderr = "", "Timeout: Code took too long to execute."
            success = False

    end_time = datetime.datetime.utcnow()

    return {
        "stdout": stdout,
        "stderr": stderr,
        "success": success,
        "started": start_time,
        "finished": end_time
    }
