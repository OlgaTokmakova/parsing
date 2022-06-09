import requests
import img2pdf


def get_data():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }

    img_list = []
    for i in range(1, 49):
        url = f'https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
        req = requests.get(url=url, headers=headers)
        response = req.content

        with open(f'media/{i}.jpg', 'wb') as file:
            file.write(response)
            img_list.append(f'media/{i}.jpg')
            print(f'Downloaded {i} of 48')

    with open('result.pdf', 'wb') as f:
        f.write(img2pdf.convert(img_list))

    print('PDF file created successfully!')


# def main():
#     get_data()
#
#
# if __name__ == '__main__':
#     main()
