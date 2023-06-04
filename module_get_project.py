import requests
import module_task_processing

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
    if gets_json is None:
        return None
    
    info = [gets_json['title'], gets_json['description'], gets_json['project_type'], gets_json['client_side'],
            gets_json['server_side'], gets_json['downloads'], gets_json['followers'], gets_json['body'],
            gets_json['license']['id'], gets_json['game_versions'], gets_json['loaders'], gets_json['issues_url'],
            gets_json['source_url'], gets_json['wiki_url'], gets_json['discord_url'], gets_json['donation_urls'],
            gets_json['slug']]
    return info

def IEs(query, facets, index):
    gurl = "https://api.modrinth.com/v2/search?query={0}&limit=30".format(query)
    if len(facets)!=0:
        gurl = gurl + "&{0}".format(module_task_processing.cURL(facets))
        
    try:
        gets = requests.get(gurl)
    except requests.exceptions.ConnectionError:
        return None
    
    a = gets.json()
    
    return gets.json()
def IEs_Gfl(f_list, f_name):
    if len(f_list)==1:
        return "empty"
    ver_f = list()
    for i in f_list:
        if i!="q":
            ver_f.append("{0}:{1}".format(f_name, i))
    return ver_f
