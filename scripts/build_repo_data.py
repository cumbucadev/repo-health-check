def build_repo_data(data_list):

    """ Extract the wanted values from a list into a dict """

    stars_count = data_list[0]['stargazerCount']              #00 Stars Count
    watchers_count = data_list[1]['watchers']['totalCount']   #01 Watchers Count
    fork_count = data_list[2]['forkCount']                    #02 Fork Count  
    last_release_name = data_list[3]['name']                  #03 Last Release: NAME 
    last_release_date = data_list[3]['publishedAt']           #04 Last Release: DATE  
    contributors_count = data_list[4]                         #05 Contributors Count
    open_issues_count = data_list[5]                          #06 Open Issues Count
    closed_issues_count = data_list[6]                        #07 Closed Issues Count
    open_prs_count = data_list[7]                             #08 Open PRs Count
    closed_prs_count = data_list[8]                           #09 Closed PRs Count
    
    has_description = bool (                                  #10 Returns 'True' if the repo has description
        data_list[9].get('description') 
    )

    has_readme = bool (                                  #11 Returns 'True' if the repo has description
        (data_list[9].get('files') or {}).get('readme') 
    )

    has_code_of_conduct = bool(                               #12 Returns 'True' if the repo has code of conduct
        (data_list[9].get('files' or {})).get('code_of_conduct')
    )

    has_contributing = bool(                                  #13 Returns 'True' if the repo has contributing file
        (data_list[9].get('files') or {}).get('contributing', {}). get('url')
    )

    has_license = bool(                                       #14 Returns 'True' if the repo has license
        (data_list[9].get('files') or {}).get('license', {}).get('name')
    )

    has_issues_templates = bool(                              #15 Returns 'True' if the repo has issues templates
        (data_list[9].get('files') or {}).get('issue_template')
    )

    has_pr_template = bool(                                   #16 Returns 'True' if the repo has PR template
        (data_list[9].get('files') or {}).get('pull_request_template')
    )

    has_content_reports_enabled = bool(                       #17 Returns 'True' if the repo had content reports enabled
        data_list[9].get('content_reports_enabled')
    )

    has_security_policy = data_list[10].get('isSecurityPolicyEnabled') #18 Returns the value in 'isSecurityPolicyEnabled'

    return {
        'stars_count': stars_count,
        'watchers_count': watchers_count,
        'fork_count': fork_count,
        'last_release_name': last_release_name,
        'last_release_date': last_release_date,
        'contributors_count': contributors_count,
        'open_issues_count': open_issues_count,
        'closed_issues_count': closed_issues_count,
        'open_prs_count': open_prs_count,
        'closed_prs_count': closed_prs_count,
        'has_description': has_description,
        'has_readme': has_readme,
        'has_code_of_conduct': has_code_of_conduct,
        'has_contributing': has_contributing,
        'has_license': has_license,
        'has_issues_templates': has_issues_templates,
        'has_pr_template': has_pr_template,
        'has_content_reports_enabled': has_content_reports_enabled,
        'has_security_policy': has_security_policy
    }
