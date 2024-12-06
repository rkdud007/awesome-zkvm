import re
import requests
from datetime import datetime, UTC
from typing import Dict, List, Optional

def get_latest_release(repo: str) -> str:
    """Get latest release version for a GitHub repository."""
    api_url = f'https://api.github.com/repos/{repo}/releases/latest'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    
    try:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            return response.json()['tag_name']
        return ""
    except:
        return ""

def update_readme(content: str) -> str:
    """Update README with latest releases and add timestamp."""
    # Find the table section
    table_pattern = r'\| zkVM.*?\|(.*?\|.*?\n)*'
    table_match = re.search(table_pattern, content, re.MULTILINE | re.DOTALL)
    
    if not table_match:
        return content
        
    table = table_match.group(0)
    lines = table.split('\n')
    updated_lines = []
    updated_lines.extend(lines[:2])  # Keep header and separator

    for line in lines[2:]:
        if not line.strip() or '|' not in line:
            continue
            
        url_match = re.search(r'\((https://github\.com/[^)]+)\)', line)
        if url_match:
            url = url_match.group(1)
            repo = re.sub(r'https://github.com/', '', url)
            repo = re.sub(r'/tree/master/.*$', '', repo)
            release = get_latest_release(repo)
            
            # Split the line into parts and update the Release column
            parts = line.split('|')
            if len(parts) >= 3:  # Make sure we have enough columns
                parts[2] = f" {release} "
                line = '|'.join(parts)
        
        updated_lines.append(line)
    
    updated_table = '\n'.join(updated_lines)
    timestamp = datetime.now(UTC).strftime("%Y-%m-%d %H:%M UTC")
    timestamp_note = f"\n\n*Release versions last updated: {timestamp}*\n"
    
    return content.replace(table_match.group(0), updated_table + timestamp_note)

def main():
    with open('README.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated_content = update_readme(content)
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(updated_content)

if __name__ == '__main__':
    main()