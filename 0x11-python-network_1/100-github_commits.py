#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge"""

if __name__ == "__main__":
    import requests
    import sys
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API URL for commits
    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    try:
        # Send GET request to the GitHub API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request fails

        # Parse the JSON response
        commits = response.json()

        # Iterate through the commits and print the sha and author name
        for commit in commits[:10]:  # Print the 10 most recent commits
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

