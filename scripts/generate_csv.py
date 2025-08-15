import json

# Star count
with open('./files/stargazerCount.json') as star_count_json:
    star_count_data = json.load(star_count_json)
    print(star_count_data)

# Watchers count
with open('./files/watchersCount.json') as watchers_count_json:
    watchers_count_data = json.load(watchers_count_json)
    print(watchers_count_data)

# Fork count
with open('./files/forkCount.json') as fork_count_json:
    fork_count_data = json.load(fork_count_json)
    print(fork_count_data)

# Last Release
with open('./files/lastReleaseData.json') as last_release_json:
    last_release_data = json.load(last_release_json)
    print(last_release_data)

# Contributors Count
with open('./files/contributorsCount.json') as contributors_count_json:
    contributors_count_data = json.load(contributors_count_json)
    print(contributors_count_data)

# Open Issues
with open ('./files/openIssuesCount.json') as open_issues_count_json:
    open_issues_count_data = json.load(open_issues_count_json)
    print(open_issues_count_data)

# Closed Issues
with open('./files/closedIssuesCount.json') as closed_issues_count_json:
    closed_issues_count_data = json.load(closed_issues_count_json)
    print(closed_issues_count_data)

# Open PRs Count
with open('./files/openPRsCount.json') as open_prs_count_json:
    open_prs_count_data = json.load(open_prs_count_json)
    print(open_prs_count_data)

# Closed PRs Count
with open('./files/closedPRsCount.json') as closed_prs_count_json:
    closed_prs_count_data = json.load(closed_prs_count_json)
    print(closed_prs_count_json)

# Community Standards
with open('./files/communityStandards.json') as community_standards_json:
    community_standards_data = json.load(community_standards_json)
    print(community_standards_data)
          
# Security Data
with open('./files/security.json', 'r') as security_json:
    secutiry_data = json.load(security_json)
    print(secutiry_data)