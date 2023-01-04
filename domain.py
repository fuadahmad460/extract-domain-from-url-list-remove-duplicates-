from urllib.parse import urlparse

# Read the URLs from the input file
with open("input.txt", "r", encoding="utf-8") as f:
    urls = f.readlines()

# Extract the domains
domains = set()  # Use a set to store the domains
for url in urls:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    domains.add(domain)  # Add the domain to the set

# Write the domains to the output file
with open("output.txt", "w") as f:
    for domain in domains:
        f.write(domain + "\n")
