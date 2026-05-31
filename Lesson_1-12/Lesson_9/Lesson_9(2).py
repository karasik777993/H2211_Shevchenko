import requests

parse_list = []

resource = requests.get("https://coinmarketcap.com/")

print(resource.text)
resource_text = resource.text
resource_perse = resource_text.split("<span>")
print(resource_perse)
for pars_elem_1 in resource_perse:
    if pars_elem_1.startswith("$"):
        for pars_elem_2 in pars_elem_1.split("</span>"):
            if pars_elem_2.startswith("$") and pars_elem_2[1].isdigit():
                parse_list.append(pars_elem_2)


bitcoin_er = parse_list[1]
print(bitcoin_er)