import requests
response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('man.jpg', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': '9Gcy1TbZ9GusEfV1ogMuEb31'},
)
if response.status_code == requests.codes.ok:
    with open('removed-background.png', 'wb') as out:
        out.write(response.content)
else:
    print("Error:", response.status_code, response.text)