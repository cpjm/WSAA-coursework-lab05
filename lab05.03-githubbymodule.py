#
# Ciaran Moran
# G00426050@atu.ie
# Assignment: Lab for topic 05 - Authentication
#
from github import Github
from config import config as cfg
apikey = cfg["githubkey"]
# use your own key
g = Github(apikey)
for repo in g.get_user() :
 print(repo.name)

