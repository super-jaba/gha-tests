import os

import dotenv
import requests


def print_issue(
    gh_token: str,
    repo_full_name: str,
    issue_number: int | str,
) -> None:
    url = f'https://api.github.com/repos/{repo_full_name}/issues/{issue_number}'

    headers = {
        'Authorization': f'Bearer {gh_token}',
    }
    res = requests.get(url, headers=headers)

    if res.status_code != 200:
        print(f'Error: {res.status_code}')

    print(res.json())


def main() -> None:
    dotenv.load_dotenv()

    gh_token = os.getenv('GITHUB_TOKEN')
    repo_full_name = os.getenv('REPO_FULL_NAME')
    issue_number = os.getenv('ISSUE_NUMBER')

    print_issue(gh_token, repo_full_name, issue_number)


if __name__ == '__main__':
    main()
