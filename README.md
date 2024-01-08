
# Football Data Co Uk Scrapper

## Overview
This Python script allows users to download football match data for various leagues and seasons. The script fetches CSV files containing match details from a specified URL based on the league and year provided by the user.

## Prerequisites
- Python 3
- Required Python packages: `requests`, `yaml`, `os`
  - Install these packages using `pip install requests pyyaml`
- Just run command to install all packages needed
```sh
pip install -r requirements.txt
```
## Configuration
Before running the script, make sure to set up the `config.yaml` file with the correct URLs for each football league. A sample structure of the `config.yaml` file is as follows:

```yaml
football_data_urls:
  EPL: https://www.football-data.co.uk/mmz4281/2324/E0.csv
  LA_LIGA: https://www.football-data.co.uk/mmz4281/2324/SP1.csv
  ...
```

Replace the URLs with the appropriate ones for the leagues and seasons you are interested in.

## Usage
To use the script, run it from the command line with the required year and optional league argument. For example:

```sh
python3 foot.py --year 2023 --league EPL
```

This command will download the 2023 season data for the English Premier League.

If no league is specified, the script will attempt to download data for all leagues listed in the `config.yaml` file.

## Output
The script will create a directory named after the specified league (or the year, if no league is specified) and download the CSV file(s) containing the match data into this directory.

## License
This project is [MIT licensed](#).

