import json, csv

# --- OPEN JSON FILES --- #
# Star count
with open('./files/stargazerCount.json') as star_count_json:
    star_count_data = json.load(star_count_json)
    # print('Star count: ', star_count_data,'\n')

# Watchers count
with open('./files/watchersCount.json') as watchers_count_json:
    watchers_count_data = json.load(watchers_count_json)
    # print('Watchers count: ', watchers_count_data,'\n')

# Fork count
with open('./files/forkCount.json') as fork_count_json:
    fork_count_data = json.load(fork_count_json)
    # print('Fork count: ', fork_count_data)

# Last Release
with open('./files/lastReleaseData.json') as last_release_json:
    last_release_data = json.load(last_release_json)
    # print('Last release: ', last_release_data)
''
# Contributors Count
with open('./files/contributorsCount.json') as contributors_count_json:
    contributors_count_data = json.load(contributors_count_json)
    # print('Conbributors count: ', contributors_count_data)

# Open Issues
with open ('./files/openIssuesCount.json') as open_issues_count_json:
    open_issues_count_data = json.load(open_issues_count_json)
    # print('Open ISSUES: ', open_issues_count_data)

# Closed Issues
with open('./files/closedIssuesCount.json') as closed_issues_count_json:
    closed_issues_count_data = json.load(closed_issues_count_json)
    # print('Closed ISSUES: ', closed_issues_count_data)

# Open PRs Count
with open('./files/openPRsCount.json') as open_prs_count_json:
    open_prs_count_data = json.load(open_prs_count_json)
    # print('Open PRs: ', open_prs_count_data)

# Closed PRs Count
with open('./files/closedPRsCount.json') as closed_prs_count_json:
    closed_prs_count_data = json.load(closed_prs_count_json)
    # print('Closed PRs: ', closed_prs_count_data)

# Community Standards
with open('./files/communityStandards.json') as community_standards_json:
    community_standards_data = json.load(community_standards_json)
    # print('Community Standards: ', community_standards_data)
          
# Security Data
with open('./files/security.json', 'r') as security_json:
    secutiry_data = json.load(security_json)
    # print('Secutiry enabled: ', secutiry_data)


print('TESTS: generating dicts')

repo_data_dict = {
    'stars_count': star_count_data['stargazerCount'],
    'watchers_count': watchers_count_data['watchers']['totalCount'],
    'fork_count': fork_count_data['forkCount'],
    'last_release_name': last_release_data['name'],
    'last_release_date': last_release_data['publishedAt'],
    'contributors_count': contributors_count_data,
    'open_issues_count': open_issues_count_data,
    'closed_issues_count': closed_issues_count_data,
    'open_prs_count': open_prs_count_data,
    'closed_prs_count': closed_prs_count_data,
    'community_stardards_description': True if community_standards_data.get('description') else False,
    'community_stardards_readme': True if community_standards_data.get('files', {}).get('readme') is not None else False ,
    'community_stardards_code_of_conduct': True if community_standards_data.get('files', {}).get('code_of_conduct') is not None else False,
    'community_stardards_contributing': True if community_standards_data.get('files', {}).get('contributing', {}).get('url') is not None else False,
    'community_stardards_license': True if community_standards_data.get('files', {}).get('license', {}.get('name')) is not None else False,
    'community_stardards_security_policy': secutiry_data['isSecurityPolicyEnabled'],
    'community_stardards_issues_templates': True if community_standards_data.get('files', {}).get('issue_template') is not None else False,
    'community_stardards_pr_template': True if community_standards_data.get('files', {}).get('pull_request_template') is not None else False,
    'community_stardards_content_reports_enabled': community_standards_data.get('content_reports_enabled')
}

with open("repo_health_data.csv", "w", newline="", encoding="utf-8") as repo_health_data:
    writer = csv.DictWriter(repo_health_data, fieldnames=repo_data_dict.keys())
    writer.writeheader()
    writer.writerow(repo_data_dict)

print(repo_data_dict)