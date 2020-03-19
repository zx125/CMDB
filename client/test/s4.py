
s = '''
SMBIOS 2.7 present.

Handle 0x0001, DMI type 1, 27 bytes
System Information
	Manufacturer: Parallels Software International Inc.
	Product Name: Parallels Virtual Platform
	Version: None
	Serial Number: Parallels-1A 1B CB 3B 64 66 4B 13 86 B0 86 FF 7E 2B 20 30
	UUID: 3BCB1B1A-6664-134B-86B0-86FF7E2B2030
	Wake-up Type: Power Switch
	SKU Number: Undefined
	Family: Parallels VM
'''

key_map = {
            'Manufacturer': 'manufacturer', #key_map[row_data[0]]
            'Product Name': 'model',
            'Serial Number': 'sn',
        }

result = {}

for item in s.split('\n'):
    # print(item)
    row_data = item.strip().split(':')
    # print(row_data)

    if len(row_data) == 2:
        # print(row_data)
        if row_data[0] in key_map:
            # print(row_data)
            result[key_map[row_data[0]]] = row_data[1].strip()

print(result)