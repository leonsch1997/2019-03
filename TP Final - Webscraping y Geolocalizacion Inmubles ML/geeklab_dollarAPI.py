import pandas
import requests
import json

def get_dollar():
    try:
        gl_url_get_dollar = ' '
        dollar = float(pandas.read_json(gl_url_get_dollar, orient='index').loc['blue'][0])
    except:
        dollar = 60.0
    return dollar

if __name__ == "__main__":
    print(type(get_dollar()))