import main

get = {
    '/': 302,
    '/FER/': 200,
    '/anywhere/': 404
}


def test_index():
    main.app.testing = True
    client = main.app.test_client()

    for link, response in get.items():
        assert client.get(link).status_code == response

    with open('test/octocat.jpg', 'rb') as img1:
        r = client.post('/FER/', data={'image': img1})
        assert r.status_code == 302

    with open('test/jon_snow.jpg', 'rb') as img2:
        r = client.post('/FER/', data={'image': img2})
        assert r.status_code == 200


if __name__ == "__main__":
    test_index()
