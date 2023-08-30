import os
import sys
import requests
import re
from datetime import datetime, date, timedelta

def zero_blog_checker():
    response = requests.get('https://velog.io/@hannatoo').text
    
    updated_at_regex = r'"released_at":"(\d{4}-\d{2}-\d{2})'

    matches = re.findall(updated_at_regex, response)

    yesterday = date.today() - timedelta(days=1)
    yesterday = yesterday.strftime("%Y-%m-%d")
    
    for match in matches:
        if match == yesterday:
            return True

    return False
