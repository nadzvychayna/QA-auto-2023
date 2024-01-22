import requests


class GitHub:

    def get_user(self, username):
        r =  requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body 
    
    def search_repo(self, name):
        r = requests.get(
            "https://api.github.com/search/repositories", 
            params={"q": name}
        )
        body = r.json()
        
        return body
    
    def search_branch_in_repo(self, username, repo, branch):
        r = requests.get(f'https://api.github.com/repos/{username}/{repo}/branches/{branch}')
        body = r.json()

        return body
    

    def get_issues(self, username, repo, state):
        r = requests.get(
            f'https://api.github.com/repos/{username}/{repo}/issues',
            params={"state": state})
        body = r.json()

        return body