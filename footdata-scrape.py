import argparse
import requests
import yaml
import os

def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as file:
            file.write(response.content)
        print(f"File downloaded successfully: {filename}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")

def main(year, league=None):
    # Create or select the directory named after the league if provided, else year
    directory = league if league else str(year)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    
    if league:
        if league in config['football_data_urls']:
            base_url = config['football_data_urls'][league]
            modified_year = str(year[-2:]) + str(int(year[-2:])+1)
            modified_url = base_url.replace("2324", modified_year)
            filename = os.path.join(directory, f"{league}_{modified_year}.csv")
            download_file(modified_url, filename)
        else:
            print(f"League not found: {league}")
    else:
        for league_key in config['football_data_urls']:
            base_url = config['football_data_urls'][league_key]
            modified_year = str(year[-2:]) + str(int(year[-2:])+1)
            modified_url = base_url.replace("2324", modified_year)
            filename = os.path.join(str(year), f"{league_key}_{year}.csv")
            download_file(modified_url, filename)

if __name__ == "__main__":
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
    leagues = ', '.join(config['football_data_urls'].keys())

    parser = argparse.ArgumentParser(description='Download football data files for a specific year and league.')
    parser.add_argument('--year', type=str, required=True, help='Year in the format YYYY')
    parser.add_argument('--league', type=str, help=f'League code (optional). Available leagues: {leagues}')
    
    args = parser.parse_args()
    main(args.year, args.league)


