import requests
import threading

# Target domain
domain = "youtube.com"

# Shared list and lock for thread-safe writes
discovered_subdomains = []
lock = threading.Lock()

# Function to check if a subdomain exists
def check_subdomain(subdomain):
    url = f"http://{subdomain}.{domain}"
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            with lock:
                discovered_subdomains.append(f"{subdomain}.{domain}")
                print(f"[+] Found: {subdomain}.{domain}")
    except requests.ConnectionError:
        pass
    except requests.Timeout:
        pass

# Load subdomains from file
with open("subdomains.txt") as file:
    subdomains = file.read().splitlines()

# Create and start threads
threads = []
for sub in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(sub,))
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Save results
with open("discovered_subdomains.txt", "w") as output_file:
    for sub in discovered_subdomains:
        output_file.write(sub + "\n")

print("\n✅ Scan complete. Results saved in 'discovered_subdomains.txt'")
