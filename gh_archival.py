import os
from gh_api import GitHubOrg
 
# Assign environment variable values
repo_name = os.environ['GH_REPO_NAME']
org_name = os.environ['GH_ORG']
token = os.environ['GH_TOKEN']
 
# Create an instance of the GitHubOrg class
github_org = GitHubOrg(org_name, token)
 
# Archive the repository
github_org.github_archival(repo_name)
 
print(f"Repository '{repo_name}' has been archived.")