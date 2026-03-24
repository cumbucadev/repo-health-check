from load_json import load_json
from build_repo_data import build_repo_data
from write_csv import write_csv

STAR_COUNT_FILE = './files/stargazerCount.json'
WATCHERS_COUNT_FILE = './files/watchersCount.json'
FORK_COUNT_FILE = './files/forkCount.json'
LAST_RELEASE_FILE = './files/lastReleaseData.json'
CONTRIBUTORS_COUNT_FILE = './files/contributorsCount.json'
OPEN_ISSUES_COUNT_FILE = './files/openIssuesCount.json'
CLOSED_ISSUES_COUNT_FILE = './files/closedIssuesCount.json'
OPEN_PRS_COUNT_FILE = './files/openPRsCount.json'
CLOSED_PRS_COUNT_FILE = './files/closedPRsCount.json'
COMMUNITY_STANDARDS_FILE = './files/communityStandards.json'
SECURITY_FILE = './files/security.json'

OUTPUT_FILE = "repo_health_data.csv"

data_from_json = load_json(
    STAR_COUNT_FILE,
    WATCHERS_COUNT_FILE,
    FORK_COUNT_FILE,
    LAST_RELEASE_FILE,
    CONTRIBUTORS_COUNT_FILE,
    OPEN_ISSUES_COUNT_FILE,
    CLOSED_ISSUES_COUNT_FILE,
    OPEN_PRS_COUNT_FILE,
    CLOSED_PRS_COUNT_FILE,
    COMMUNITY_STANDARDS_FILE,
    SECURITY_FILE,
)

data_into_dict = build_repo_data(data_from_json)

write_csv(data_into_dict, file_name=OUTPUT_FILE)
