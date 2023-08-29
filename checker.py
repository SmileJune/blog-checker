import os
import sys
import requests
import re
from datetime import datetime, date

def zero_blog_checker():
    response = requests.get('https://velog.io/@hannatoo').text
    
    updated_at_regex = r'"updated_at":"(\d{4}-\d{2}-\d{2})'

    matches = re.findall(updated_at_regex, response)

    today = date.today()
    today = today.strftime("%Y-%m-%d")
    
    for match in matches:
        if match == today:
            return True

    return False
