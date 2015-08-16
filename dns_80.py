from __future__ import print_function
import sys
from collections import deque

argv = sys.argv

dns_file = argv[1]
file = argv[2]
out_file = argv[3]

out_fh = open(out_file, 'w')

ip_dict = {}
latest_domains = deque(maxlen=10000)
with open(file) as fh:
	for line in fh:
		ip_dict[line.rstrip()] = True

	with open(dns_file) as dns_fh:
		i = 0 
		for line in dns_fh:
			s = line.split(",")
			domain, record, val = s[0], s[1], s[2]
			already_added = domain in latest_domains
			if record == "a" and not already_added:
				if val.strip() in ip_dict:
					out_string = val.strip() + " " + domain.strip() + "\n"
					out_fh.write(out_string)
				latest_domains.append(domain)
			
			if i % 1000 == 0 and i != 0:
				print(".", end="")

			i += 1
						
out_fh.close()
