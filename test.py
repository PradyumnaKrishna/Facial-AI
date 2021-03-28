import main
import unittest

get = {
    '/': 302,
    '/FER/': 200,
    '/anywhere/': 404
}

test = {
    'test/not_a_img.jpg': 400,
    'test/octocat.jpg': 200,
    'test/jon_snow.jpg': 200,
}

api_url = '/FER/api/v1/'


class Test(unittest.TestCase):

    def test_frontend(self):
        main.app.testing = True
        client = main.app.test_client()

        for link, response in get.items():
            self.assertEqual(client.get(link).status_code, response)

        # No test for post

    def test_api(self):
        main.app.testing = True
        client = main.app.test_client()

        self.assertEqual(client.post(api_url).status_code, 400)

        for file, response in test.items():
            r = client.post(api_url, data={'image': open(file, 'rb')})
            self.assertEqual(r.status_code, response)


if __name__ == "__main__":
    unittest.main()
