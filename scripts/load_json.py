import json

def load_json(*filepathes):
    """ This function returns a dict list with data collected from the github repository """
    data = []

    # Star count
    with open(filepathes[0], 'r') as star_count_json:
        star_count_data = json.load(star_count_json)
        # print(type(star_count_data))
        # print('Star count: ', star_count_data,'\n')
    data.append(star_count_data)

    # Watchers count
    with open(filepathes[1], 'r') as watchers_count_json:
        watchers_count_data = json.load(watchers_count_json)
        # print('Watchers count: ', watchers_count_data,'\n')
    data.append(watchers_count_data)

    # Fork count
    with open(filepathes[2], 'r') as fork_count_json:
        fork_count_data = json.load(fork_count_json)
        # print('Fork count: ', fork_count_data)
    data.append(fork_count_data)

    # Last Release
    with open(filepathes[3], 'r') as last_release_json:
        last_release_data = json.load(last_release_json)
        # print('Last release: ', last_release_data)
    data.append(last_release_data)

    # Contributors Count
    with open(filepathes[4], 'r') as contributors_count_json:
        contributors_count = json.load(contributors_count_json)
        # print('Conbributors count: ', contributors_count)
    data.append(contributors_count)

    # Open Issues
    with open (filepathes[5], 'r') as open_issues_count_json:
        open_issues_count = json.load(open_issues_count_json)
        # print('Open ISSUES: ', open_issues_count)
    data.append(open_issues_count)

    # Closed Issues
    with open(filepathes[6], 'r') as closed_issues_count_json:
        closed_issues_count = json.load(closed_issues_count_json)
        # print('Closed ISSUES: ', closed_issues_count)
    data.append(closed_issues_count)

    # Open PRs Count
    with open(filepathes[7], 'r') as open_prs_count_json:
        open_prs_count = json.load(open_prs_count_json)
        # print('Open PRs: ', open_prs_count)
    data.append(open_prs_count)

    # Closed PRs Count
    with open(filepathes[8], 'r') as closed_prs_count_json:
        closed_prs_count = json.load(closed_prs_count_json)
        # print('Closed PRs: ', closed_prs_count)
    data.append(closed_prs_count)

    # Community Standards
    with open(filepathes[9], 'r') as community_standards_json:
        community_standards_data = json.load(community_standards_json)
        # print('Community Standards: ', community_standards_data)
    data.append(community_standards_data)

    # Security Data
    with open(filepathes[10], 'r') as security_json:
        security_data = json.load(security_json)
        # print('Security enabled: ', security_data)
    data.append(security_data)

    return data
