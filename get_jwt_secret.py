RED = "\33[91m"
BLUE = "\33[94m"
GREEN = "\033[32m"
YELLOW = "\033[93m"
PURPLE = '\033[0;35m'
CYAN = "\033[36m"
END = "\033[0m"
banner=f"""{YELLOW}
#  ██████╗ ██████╗  █████╗  ██████╗██╗   ██╗██╗      █████╗ {CYAN}
#  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██║   ██║██║     ██╔══██╗
#  ██║  ██║██████╔╝███████║██║     ██║   ██║██║     ███████║ {GREEN}
#  ██║  ██║██╔══██╗██╔══██║██║     ██║   ██║██║     ██╔══██║    {YELLOW}
#  ██████╔╝██║  ██║██║  ██║╚██████╗╚██████╔╝███████╗██║  ██║
#  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ TOOLS {PURPLE}
#            Author:MAIMO HARRIS Contact:+237680226898        
{END}"""
print(banner)
import jwt
import argparse
import warnings
from jwt import InvalidTokenError
from concurrent.futures import ThreadPoolExecutor
from threading import Event

warnings.simplefilter("ignore")

stop_event = Event()


def get_algorithm(token):
    try:
        header = jwt.get_unverified_header(token)
        return header.get("alg", "HS256")
    except Exception:
        return "HS256"


def try_secret(token, secret, algorithm, verbose=False):
    if stop_event.is_set():
        return None

    try:
        payload = jwt.decode(token, secret, algorithms=[algorithm])

        stop_event.set()
        return secret, payload

    except InvalidTokenError:
        if verbose:
            print(f"[-] Failed: {secret}")
        return None
    except Exception:
        return None


def brute_force_jwt(token, wordlist_path, threads, verbose=False):
    try:
        with open(wordlist_path, 'r', errors='ignore') as f:
            secrets = f.read().splitlines()
    except IOError as e:
        print(f"[ERROR] Wordlist issue: {e}")
        return

    algorithm = get_algorithm(token)

    print(f"[+] Loaded {len(secrets)} secrets")
    print(f"[+] Algorithm: {algorithm}")
    print(f"[+] Threads: {threads}\n")

    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = []

        for secret in secrets:
            if stop_event.is_set():
                break

            futures.append(
                executor.submit(try_secret, token, secret, algorithm, verbose)
            )

        for future in futures:
            result = future.result()
            if result:
                secret, payload = result
                print(f"\n[SUCCESS] Secret found: '{secret}'")
                print(f"[PAYLOAD] {payload}")
                return secret

    print("\n[FAILURE] Secret not found.")
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="jwt_cracker",
        description="⚡ Advanced JWT Brute Force Tool",
        epilog="Example: python3 script.py <token> wordlist.txt -t 20"
    )

    parser.add_argument("token", help="JWT token")
    parser.add_argument("wordlist", help="Path to wordlist")

    parser.add_argument(
        "-t", "--threads",
        type=int,
        default=10,
        help="Number of threads (default: 10)"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Show failed attempts"
    )

    args = parser.parse_args()

    brute_force_jwt(
        args.token,
        args.wordlist,
        args.threads,
        args.verbose
    )