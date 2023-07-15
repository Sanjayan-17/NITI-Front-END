import requests
import os
for i in range(28,31):
    url = 'https://api.themoviedb.org/3/movie/' + str(i)
    params = {
        'api_key': '7b450ff63e34766a040e75582c89444c'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        poster_path = data['poster_path']
        print(data)
    else:
        print(f"Error: {response.status_code}")
    output_folder = "images"
    data = [data]
    os.makedirs(output_folder, exist_ok=True)
    for item in data:
        print(item['poster_path'])
        image_url = f"https://image.tmdb.org/t/p/w500{item['poster_path']}"
        image_filename = os.path.join(output_folder, os.path.basename(item['poster_path']))


        response = requests.get(image_url)
        if response.status_code == 200:
            with open(image_filename, 'wb') as image_file:
                image_file.write(response.content)
            print(f"Image downloaded: {image_filename}")
        else:
            print(f"Failed to download image: {image_url}")
path = 'images'
contents = os.listdir(path)
for i in contents:
    print(i)

