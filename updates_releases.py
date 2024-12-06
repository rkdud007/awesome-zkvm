import re
import requests
from typing import Dict, List, Tuple

def extract_repo_from_url(url: str) -> str:
    """Extract repository name from GitHub URL."""
    match = re.search(r'github\.com/([^/\s]+/[^/\s]+?)(?:\.git|/.*)?(?=[\s)\'"<]|$)', url)
    return match.group(1) if match else None

def get_latest_release(repo: str) -> str:
    """Get the latest release version for a GitHub repository."""
    api_url = f'https://api.github.com/repos/{repo}/releases/latest'
    headers = {
        'Accept': 'application/vnd.github.v3+json',
        # 'Authorization': 'token YOUR_GITHUB_TOKEN'
    }
    
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return response.json()['tag_name']
        return ""  # Keep empty if no release found
    except:
        return ""

def parse_markdown_table(table: str) -> List[Dict[str, str]]:
    """Parse markdown table into list of dictionaries."""
    lines = table.strip().split('\n')
    headers = re.findall(r'\|(.*?)\|', lines[0])
    headers = [h.strip() for h in headers]
    
    rows = []
    for line in lines[2:]:  # Skip header and separator lines
        if not line.strip(): continue
        values = re.findall(r'\|(.*?)\|', line)
        values = [v.strip() for v in values]
        rows.append(dict(zip(headers, values)))
    return rows

def update_table_with_releases(table: str) -> str:
    """Update markdown table with latest release versions."""
    rows = parse_markdown_table(table)
    
    # Extract and update releases
    for row in rows:
        url = re.search(r'\[.*?\]\((.*?)\)', row['zkVM'])
        if url:
            repo = extract_repo_from_url(url.group(1))
            if repo:
                release = get_latest_release(repo)
                row['Release'] = release

    # Rebuild table
    headers = ['zkVM', 'Release', 'ISA', 'Continuations']
    header_row = '|' + '|'.join(f'{h:^{max(len(h), 10)}}' for h in headers) + '|'
    separator = '|' + '|'.join(':' + '-'*(max(len(h), 10)-2) + ':' for h in headers) + '|'
    
    data_rows = []
    for row in rows:
        formatted_row = '|' + '|'.join(f'{row[h]:^{max(len(h), 10)}}' for h in headers) + '|'
        data_rows.append(formatted_row)
    
    return '\n'.join([header_row, separator] + data_rows)

# Example usage
if __name__ == "__main__":
    with open("readme.md", "r") as f:
        table = f.read()
    updated_table = update_table_with_releases(table)
    print(updated_table)