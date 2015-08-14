import sys

dns_file = 'dns_records/20150606_dnsrecords_all'
ip_files = ['port_scan/port_scan_1.txt', 'port_scan/port_scan_2.txt']

out_file = 'dns_open_80.txt'
out_fh = open(out_file, 'w')

for file in ip_files:
	ip_dict = {}
	with open(file) as fh:
		for line in fh:
			ip_dict[line.rstrip()] = True

		with open(dns_file) as dns_fh:
			i = 0 
			for line in dns_fh:
				s = line.split(",")
				domain, record, val = s[0], s[1], s[2]
				if record == "a":
					if val.strip() in ip_dict:
						out_fh.write(line)
				
				if i % 1000 == 0 and i != 0:
					print(".",)

				i += 1
						
out_fh.close()
