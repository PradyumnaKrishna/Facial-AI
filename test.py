import main
import unittest

get = {
    '/': 302,
    '/FER/': 200,
    '/anywhere/': 404
}

test = {
    'test/octocat.jpg': 302,
    'test/jon_snow.jpg': 200,
}


class Test(unittest.TestCase):

    def test_index(self):
        main.app.testing = True
        client = main.app.test_client()

        for link, response in get.items():
            self.assertEqual(client.get(link).status_code, response)

        for file, response in test.items():
            with open(file, 'rb') as img:
                r = client.post('/FER/', data={'image': img})
                self.assertEqual(r.status_code, response)

        r = client.post('/FER/')
        print(r.status_code)


if __name__ == "__main__":
    unittest.main()
