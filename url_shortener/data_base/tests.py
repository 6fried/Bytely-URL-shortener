import requests

def exists(url):
    try:
        response = requests.get(url)
        return True
    except requests.ConnectionError:
        return False
    except requests.exceptions.MissingSchema:
        pass
    
def begins_with_http(url):
    if len(url) < 7:
        return False
    if (( (url[0], url[1], url[2], url[3], url[4], url[5], url[6]  ) == ('h', 't', 't', 'p', ':', '/', '/')) or 
        ((url[0], url[1], url[2], url[3], url[4], url[5], url[6], url[7]  ) == ('h', 't', 't', 'p', 's', ':', '/', '/'))):
        return True
    else:
        return False