import requests

def IEc(project_idorslug):
    try:
        gets = requests.get("https://api.modrinth.com/v2/project/{0}/check".format(project_idorslug))
    except requests.exceptions.ConnectionError:
        return "Error"
    
    if gets.status_code==200:
        return True
    else:
        return False
    
def IEg(project_idorslug):
    try:
        gets = requests.get("https://api.modrinth.com/v2/project/{0}".format(project_idorslug))
    except requests.exceptions.ConnectionError:
        return False
    return gets.json()

def IGd(gets_json):
    info = [gets_json['title'], gets_json['description'], gets_json['project_type'], gets_json['client_side'],
            gets_json['server_side'], gets_json['downloads'], gets_json['followers'], gets_json['body'],
            gets_json['license']['id'], gets_json['game_versions'], gets_json['loaders'], gets_json['issues_url'],
            gets_json['source_url'], gets_json['wiki_url'], gets_json['discord_url'], gets_json['donation_urls']]
    return info
