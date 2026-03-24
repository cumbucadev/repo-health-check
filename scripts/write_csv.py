import csv

def write_csv(data_dict, file_name):

    repo_data_dict = {
        'stars_count': data_dict['stars_count'],
        'watchers_count': data_dict['watchers_count'],
        'fork_count': data_dict['fork_count'],
        'last_release_name': data_dict['last_release_name'],
        'last_release_date': data_dict['last_release_date'],
        'contributors_count': data_dict['contributors_count'],
        'open_issues_count': data_dict['open_issues_count'],
        'closed_issues_count': data_dict['closed_issues_count'],
        'open_prs_count': data_dict['open_prs_count'],
        'closed_prs_count': data_dict['closed_prs_count'],
        'community_standards_description': data_dict['has_description'],
        'community_standards_readme': data_dict['has_readme'],
        'community_standards_code_of_conduct': data_dict['has_code_of_conduct'],
        'community_standards_contributing': data_dict['has_contributing'],
        'community_standards_license': data_dict['has_license'],
        'community_standards_issues_templates': data_dict['has_issues_templates'],
        'community_standards_pr_template': data_dict['has_pr_template'],
        'community_standards_content_reports_enabled': data_dict['has_content_reports_enabled'],
        'community_standards_security_policy': data_dict['has_security_policy']
    }

    with open(file_name, "w", newline="", encoding="utf-8") as repo_health_data:
        writer = csv.DictWriter(repo_health_data, fieldnames=repo_data_dict.keys())
        writer.writeheader()
        writer.writerow(repo_data_dict)
