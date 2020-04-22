import requests
import bs4
from datetime import datetime, timedelta
import pandas as pd
import urllib
import json
import numpy as np


if '__circle_key_cache__' not in globals():
    __circle_key_cache__ = {}

if '__traffic_timeseries_cache__' not in globals():
    __traffic_timeseries_cache__ = {}


def get_ranking_html():

    resp = requests.get(
        'https://www.tomtom.com/en_gb/traffic-index/ranking/',
        headers={
            'authority': 'api.midway.tomtom.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'sec-fetch-dest': 'empty',
            'accept': '*/*',
            'origin': 'https://www.tomtom.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'referer': 'https://www.tomtom.com/en_gb/traffic-index/beijing-traffic',
            'accept-language': 'en-US,en;q=0.9',
            'if-none-match': 'W/"1455c-iy6dK27IeH567VdfOKaFqmV1XO4"',
        }
    )

    print(resp.status_code)
    return resp.content


def ranking_html_extract_data(html):
    
    country_scraped_timestamp = datetime.now()
    # country_scraped_timestamp = (datetime.now() - timedelta(days=1))

    # Use bs4 to extract fields
    bshtml = bs4.BeautifulSoup(html, 'html.parser')
    table = bshtml.find_all('table')
    
    rows = table[0].find_all('tr')
    fields = [[f for f in row.find_all('td')] for row in rows]
    df_countries = pd.DataFrame(fields).iloc[1:,]
    
    # clean dataframe of bs4 fields

    df_countries.columns = ['rank', 'bla0', 'city', 'country', 'bla1', 'bla2']
    
    df_countries['url'] = df_countries.loc[:, 'bla2'].apply(lambda r: 'https://www.tomtom.com'+r.find('a').get('href'))
    df_countries['rank'] = df_countries.loc[:, 'rank'].apply(lambda r: r.text).astype(int)
    df_countries['city'] = df_countries.loc[:, 'city'].apply(lambda r: r.text)
    df_countries['country'] = df_countries.loc[:, 'country'].apply(lambda r: r.text)

    df_countries = df_countries[['rank', 'country', 'city', 'url']].copy()
    df_countries.loc[:, 'country_scraped_timestamp'] = country_scraped_timestamp

    return df_countries


def get_congestion_ranking():
    html = get_ranking_html()
    df_countries = ranking_html_extract_data(html)
    return df_countries

def get_circle_key(page_url):
    
    # Find URL of the JSON API for getting the "circle key"
    parsed_page_url = urllib.parse.urlparse(page_url)
    parsed_page_url1 = parsed_page_url._replace(fragment='', )
    
    path_fragments = parsed_page_url1.path.split('/')
    path_fragments = [f for f in path_fragments if f]
    path_fragments = [
        path_fragments[0],
        path_fragments[1],
        'page-data',
        path_fragments[2],
        'page-data.json'
    ]
    
    parsed_page_url1 = parsed_page_url._replace(path='/'.join(path_fragments))
    json_url = parsed_page_url1.geturl()
    
    # Make a request and get the circle key
    response = requests.get(
        json_url,
        headers={
            'Referer': 'https://www.tomtom.com/en_gb/traffic-index/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'Sec-Fetch-Dest': 'empty'
        }
    )
    
    assert response.status_code == 200
    
    try:
        data = json.loads(response.content)
    except Exception as e:
        print("Dumping response data:")
        print(response.content)
        raise e

    key = data['result']['data']['citiesJson']['circleKey']
    return key, response.content


def get_circle_key_mappings_and_historic_data(df_ranking):
    exceptions = []

    for _, row in df_ranking.iterrows():
        cache_key = (row['country'], row['city'])
        print(cache_key)

        if cache_key in __circle_key_cache__:
            pass

        else:
            try:
                circle_key, extra_data = get_circle_key(row['url'])
                __circle_key_cache__[cache_key] = (circle_key, extra_data)
            except Exception as e:
                print("Failed retrieving circle key for %s (%s)" % (cache_key.__str__(), e.__str__()))
                exceptions.append(e)
                
    if exceptions:
        raise exceptions[0]
        
    return __circle_key_cache__


def get_live_traffic_time_series(circle_key):
    scraped_timestamp = datetime.now()

    encoded_circle_key = urllib.parse.quote(circle_key.encode('utf-8'), safe='')

    response = requests.get(
        'https://api.midway.tomtom.com/ranking/live/{}'.format(encoded_circle_key),
        headers={
            'authority': 'api.midway.tomtom.com',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
            'sec-fetch-dest': 'empty',
            'accept': '*/*',
            'origin': 'https://www.tomtom.com',
            'sec-fetch-site': 'same-site',
            'sec-fetch-mode': 'cors',
            'referer': 'https://www.tomtom.com/en_gb/traffic-index/beijing-traffic',
            'accept-language': 'en-US,en;q=0.9',
            'if-none-match': 'W/"1455c-iy6dK27IeH567VdfOKaFqmV1XO4"'
        }
    )
    
    assert response.status_code == 200
    
    response_data = json.loads(response.content)
    response_data_data = response_data['data']

    df = pd.DataFrame(response_data_data)
    df['scraped_timestamp'] = scraped_timestamp
    df['circle_key'] = circle_key
    
    return df


def get_all_live_traffic_time_series(df_city_data):
    exceptions = []

    for _, row in df_city_data.iterrows():
        circle_key = (row['circle_key'])
        print(circle_key)

        if circle_key in __traffic_timeseries_cache__:
            pass

        else:
            try:
                df = get_live_traffic_time_series(circle_key)
                __traffic_timeseries_cache__[circle_key] = df
            except Exception as e:
                print("Failed retrieving data for %s (%s)" % (circle_key))
                exceptions.append(e)
                
    if exceptions:
        raise exceptions[0]
        
    return pd.concat(__traffic_timeseries_cache__.values()).reset_index()


def extract_dict_column(df, col):
    df = df.copy()
    series = df.pop(col)
    series = series.fillna(pd.Series([{} for _ in series]))
    extracted_df = pd.DataFrame(series.tolist())
    
    extracted_df.columns = ['%s.%s' % (col, c) for c in extracted_df.columns]

    return pd.concat([
        df,
        extracted_df
    ], axis=1)


def de_yearify(df, non_year_columns=[]):
    year_column_regex = 'result.data.citiesJson.stats([0-9]{4})'
    is_year_column = df.columns.str.match(year_column_regex)
    year_columns = df.columns[is_year_column]
    year_column_years = df.columns.str.extract(year_column_regex).iloc[:, 0].astype(float).astype(pd.Int64Dtype())
    year_column_names_year_removed = df.columns.str.replace(year_column_regex+'.', '').tolist()
    
    years = year_column_years.drop_duplicates().dropna().tolist()

    year_dfs = []

    for year in years:

        column_rename_dict = dict(zip(df.columns, year_column_names_year_removed))
        columns_to_use = df.columns[(year_column_years == year).fillna(0).astype(bool)].tolist() + non_year_columns

        year_df = df[columns_to_use].rename(columns=column_rename_dict).assign(year=year)

        missing_columns = set(year_column_names_year_removed) - set(year_df.columns)

        for col in missing_columns:
            year_df[col] = np.nan

        year_dfs.append(year_df)
        
    return pd.concat(year_dfs, axis=0).reset_index(drop=True)


def explode_dict_column(df, col, keys_colname, values_colname):
    df = df.copy()
    df[col] = df[col].fillna(pd.Series([{} for _ in df[col]]))
    df[col] = df[col].apply(lambda d: list(d.items()))
    df = df.explode(col)
    series = df.pop(col)
    df[keys_colname] = series.str.get(0)
    df[values_colname] = series.str.get(1)

    return df


def extract_mappings_dict(mappings_dict):
    # This function extracts historic data from tomtom JSON response

    scraped_timestamp = datetime.now()

    circle_key_df = pd.DataFrame(mappings_dict.items(), columns=['key', 'value'])
    circle_key_df['country'] = circle_key_df['key'].str.get(0)
    circle_key_df['city'] = circle_key_df['key'].str.get(1)
    circle_key_df['circle_key'] = circle_key_df['value'].str.get(0)
    circle_key_df['extra_data'] = circle_key_df['value'].str.get(1)

    city_data = pd.DataFrame(circle_key_df['extra_data'].apply(json.loads).tolist())
                             #.str.get('result').str.get('data').str.get('citiesJson').tolist())

    city_data = extract_dict_column(city_data, 'result')
    city_data = extract_dict_column(city_data, 'result.data')
    city_data = extract_dict_column(city_data, 'result.data.citiesJson')
    city_data = extract_dict_column(city_data, 'result.pageContext')

    yearly_stats_columns = city_data.columns[city_data.columns.str.match('result.data.citiesJson.stats[0-9]{4}')].tolist()

    for col in ['result.data.citiesJson.position', 'result.data.citiesJson.circle', 'result.data.citiesJson.roadNetwork'] + yearly_stats_columns:
        city_data = extract_dict_column(city_data, col)

    for col in ['%s.results' % c for c in yearly_stats_columns]:
        city_data = extract_dict_column(city_data, col)

    stats_subfields = [
        'results.worstDay',
        'results.bestDay',
        'results.allDays',
        'results.allDays.fullDay',
        'results.allDays.highway',
        'results.allDays.nonHighway',
        'results.workingDays',
        'results.workingDays.amPeak',
        'results.workingDays.pmPeak',
        'results.workingDays.peakHours',
    ]

    for col in ['%s.%s' % (y, c) for y in yearly_stats_columns for c in stats_subfields]:
        city_data = extract_dict_column(city_data, col)

    #city_data.columns = ['result.data.citiesJson.%s' % c for c in city_data.columns]

    circle_key_df = circle_key_df.drop(columns=['key', 'value', 'extra_data'])
    city_data = pd.concat([circle_key_df, city_data], axis=1)

    yearly_stats_extracted_columns = city_data.columns[city_data.columns.str.match('result.data.citiesJson.stats[0-9]{4}')].tolist()

    working_days_columns = city_data.columns[city_data.columns.str.match('result.data.citiesJson.stats[0-9]{4}.results.workingDays')].tolist()
    week_hours_columns = city_data.columns[city_data.columns.str.match('result.data.citiesJson.stats[0-9]{4}.results.weekHours')].tolist()
    city_year_columns = list(set(yearly_stats_extracted_columns) - set(working_days_columns) - set(week_hours_columns))
    city_data_columns = list(set(city_data.columns) - set(working_days_columns) - set(week_hours_columns) - set(city_year_columns) - set(['circle_key']))

    working_days = city_data[['circle_key'] + working_days_columns]
    working_days = de_yearify(working_days, ['circle_key'])
    working_days = working_days.explode('results.workingDays.days').reset_index(drop=True)

    working_days = extract_dict_column(working_days, 'results.workingDays.days')
    working_days = extract_dict_column(working_days, 'results.workingDays.days.amPeak')
    working_days = extract_dict_column(working_days, 'results.workingDays.days.pmPeak')

    week_hours = city_data[['circle_key'] + week_hours_columns]
    week_hours = de_yearify(week_hours, ['circle_key'])

    week_hours = explode_dict_column(week_hours, 'results.weekHours', 'day', 'results.weekHours')
    week_hours = week_hours.explode('results.weekHours').reset_index(drop=True)
    week_hours['hour'] = week_hours.groupby(by=['circle_key', 'year', 'day']).cumcount()
    week_hours = extract_dict_column(week_hours, 'results.weekHours')

    city_year_data = de_yearify(city_data[['circle_key']+city_year_columns], ['circle_key'])
    city_data = city_data[['circle_key']+city_data_columns]
    
    working_days['scraped_timestamp'] = scraped_timestamp
    week_hours['scraped_timestamp'] = scraped_timestamp
    city_year_data['scraped_timestamp'] = scraped_timestamp
    city_data['scraped_timestamp'] = scraped_timestamp

    return working_days, week_hours, city_year_data, city_data


def scrape():

    df_ranking = get_congestion_ranking()
    mappings_dict = get_circle_key_mappings_and_historic_data(df_ranking)

    working_days, week_hours, city_year_data, city_data = extract_mappings_dict(mappings_dict)

    time_series_df = get_all_live_traffic_time_series(city_data)

    current_time = time_series_df['scraped_timestamp'][0]

    # Check for duplication
    assert working_days.groupby(by=['circle_key', 'year', 'results.workingDays.days.day']).count().max().max() == 1
    assert week_hours.groupby(by=['circle_key', 'year', 'day', 'hour']).count().max().max() == 1
    assert city_year_data.groupby(by=['circle_key', 'year']).count().max().max() == 1
    assert city_data.groupby(by=['circle_key']).count().max().max() == 1


    df_ranking.to_csv('tomtom_ranking.csv', index=False)
    working_days.to_csv('tomtom_working_days.csv', index=False)
    week_hours.to_csv('tomtom_week_hours.csv', index=False)
    city_year_data.to_csv('tomtom_city_year_data.csv', index=False)
    city_data.to_csv('tomtom_city_data.csv', index=False)
    time_series_df.to_csv('tomtom_live_traffic.csv', index=False)


def get_live_vs_hist_comparison(df_ranking, city_data, time_series_df, week_hours, city_year_data):
    """
    This compares live traffic vs historical traffic
    """
    df_live_vs_hist = pd.merge(
        df_ranking,
        city_data,
        on=['country', 'city']
    )

    df_live_vs_hist = pd.merge(
        df_live_vs_hist,
        time_series_df,
        on='circle_key'
    )

    def localize_group(df):
        tz = df['result.data.citiesJson.timezone'].iloc[0]
        df = df.copy()
        df['UpdateTime'] = df['UpdateTimeUTC'].dt.tz_convert(tz)
        df['day'] = df['UpdateTime'].dt.day_name().str[0:3]
        df['hour'] = df['UpdateTime'].dt.hour
        df['date'] = df['UpdateTime'].dt.date

        return df[['UpdateTime', 'day', 'hour', 'date']]

    df_live_vs_hist = df_live_vs_hist.reset_index(drop=True)
    df_live_vs_hist['UpdateTimeUTC'] = pd.to_datetime(df_live_vs_hist.pop('UpdateTime'), unit='ms').dt.tz_localize('UTC')
    df_live_vs_hist_datefields = df_live_vs_hist.groupby(by='result.data.citiesJson.timezone', as_index=False).apply(localize_group).reset_index(drop=True)

    df_live_vs_hist = pd.concat([df_live_vs_hist, df_live_vs_hist_datefields], axis=1)

    city_max_year = week_hours.groupby(by=['circle_key'])['year'].max()
    week_hours['city_max_year'] = week_hours['circle_key'].map(city_max_year)
    week_hours_most_recent_year = week_hours[week_hours['year'] == week_hours['city_max_year']]

    df_live_vs_hist = pd.merge(
        df_live_vs_hist,
        week_hours_most_recent_year,
        on=['circle_key', 'day', 'hour']
    )

    return df_live_vs_hist


if __name__ == "__main__":
    scrape()
