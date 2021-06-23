import botocore.vendored.requests as requests

def negative1():
    response = requests.get('https://...')

def negative2(self, endpoint: str, message: str) -> dict:
    full_url = '{}/{}'.format(self.github_api_url, endpoint)
    LOGGER.info(
            "Posting message '{}' to GitHub endpoint '{}".format(
                message,
                full_url
            )
    )
    response = requests.post(
                full_url,
                json.dumps(github_message),
                headers=self.request_headers)

def negative3(self, endpoint: str, message: str) -> dict:
    full_url = '{}/{}'.format(self.github_api_url, endpoint)
    LOGGER.info(
        "Posting message '{}' to GitHub endpoint '{}".format(
            message,
            full_url
        )
    )
    response = requests.get('https://...')

    response = requests.post(
        full_url,
        json.dumps(github_message),
        headers=self.request_headers)
