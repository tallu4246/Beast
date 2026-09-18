import argparse
import subprocess


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run OWASP ZAP baseline scan via Docker (lab/authorized only)."
    )
    parser.add_argument("--url", required=True, help="Example: http://localhost:3000")
    args = parser.parse_args()

    cmd = [
        "docker",
        "run",
        "--rm",
        "ghcr.io/zaproxy/zaproxy:stable",
        "zap-baseline.py",
        "-t",
        args.url,
        "-r",
        "zap_report.html",
    ]

    print("Running:", " ".join(cmd))
    result = subprocess.run(cmd, check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
