import re
import json
import requests
 
GH_BASE_URL = 'https://api.github.com'
 
class GitHubAuthorization:
 
    def __init__(self, token: str):
        self.token = token
        self.token_auth = f'Bearer {self.token}'
 
class GitHubOrg:
    '''
        GitHub ORG Apis
    '''
    def __init__(self, org_name: str, token: str):
        self.org_name = org_name
        self.auth = GitHubAuthorization(token)
        self.default_header = {
            'Content-Type': 'application/json',
            'Authorization': self.auth.token_auth
        }
 
    def github_archival(self, repo_name):
        '''
            Archive GitHub Repository
        '''
        url = f"{GH_BASE_URL}/repos/{self.org_name}/{repo_name}"
        payload = json.dumps({"archived": True})
        response = requests.request('PATCH', url, headers=self.default_header, data=payload)
        if response.status_code not in [200, 204]:
            raise RuntimeError(response.text)
        print(f"GitHub Repository '{repo_name}' has been archived.")