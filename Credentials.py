# Importing dependencies
import json

# Creating a dictionary called Credentials where the consumer keys,Consumer secret Key, Access token, Access key is stored and
# is then dumped into a json file for easier access and further modification.
credentials = {}
credentials['Consumer_key'] = ''
credentials['Consumer_secret'] = ''
credentials['Access_token'] = ''
credentials['Access_key'] = ''

flag=0

def json_cred():
    with open('UserCredentials.json', 'w') as file:
        # Verifying if status of the json file, to avoid creating file during each compilation
        if(file=='\0'):
            json.dump(credentials,file)
            print("[1]Json file Created")
            print('[2]Data written')
            flag=1
        else:
            json.dump(credentials, file)
            print("[1]Data written")
    if(flag==0):
        print('[2]Exiting...')
    else:
        print('[3]Exiting...')




