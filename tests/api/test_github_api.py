import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user('defunkt')
    assert user['login'] == 'defunkt'


@pytest.mark.api
def test_user_non_exists(github_api):
    r = github_api.get_user('butenkosergii')
    assert r['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo('become-qa-auto')
    assert r['total_count'] == 54
    assert 'become-qa-auto' in r['items'] [0] ['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert r['total_count'] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo('s')
    assert r['total_count'] != 0


@pytest.mark.api
def test_branch_can_be_found(github_api):
    branch_name = 'main'
    r = github_api.search_branch_in_repo('nadzvychayna', 'QA-auto-2023', branch_name)
    assert r['name'] == branch_name


@pytest.mark.api
def test_branch_cannot_be_found(github_api):
    branch_name = 'apple'
    r = github_api.search_branch_in_repo('nadzvychayna', 'QA-auto-2023', branch_name)
    assert r['message'] == 'Branch not found'


@pytest.mark.api
def test_no_open_issues(github_api):
    r = github_api.get_issues('nadzvychayna', 'QA-auto-2023', 'open')
    assert len(r) == 0