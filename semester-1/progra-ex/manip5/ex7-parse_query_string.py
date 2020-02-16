def parse_query_string(url: str) -> dict:
    url_param = url.split('?')[1]
    url_param = url_param.split('&')
    url_param_dict = {}
    for param in url_param:
        param_split = param.split('=')
        url_param_dict[param_split[0]] = param_split[1]
    return url_param_dict

url = "http://example.com/show_item.php?item=car&color=red"
print(parse_query_string(url ))

