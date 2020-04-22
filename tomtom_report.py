import pandas as pd
import tomtom_scrape_traffic


DEFAULT_ABS_YOY_ALERT_THRESHOLD = 0.2


def load_tomtom_dump():

    ranking = pd.read_csv('tomtom_ranking.csv')
    city_data = pd.read_csv('tomtom_city_data.csv')
    city_year_data = pd.read_csv('tomtom_city_year_data.csv')
    week_hours = pd.read_csv('tomtom_week_hours.csv')
    live_traffic = pd.read_csv('tomtom_live_traffic.csv')
    working_days = pd.read_csv('tomtom_working_days.csv')

    city_data['city'] = city_data['city'].str.strip()
    city_data['country'] = city_data['country'].str.strip()
    #city_year_data['city'] = city_year_data['city'].str.strip()
    #city_year_data['country'] = city_year_data['country'].str.strip()
    ranking['city'] = ranking['city'].str.strip()
    ranking['country'] = ranking['country'].str.strip()

    return ranking, city_data, city_year_data, week_hours, live_traffic, working_days


def load_report_settings():
    
    return pd.read_csv('tomtom_report_settings.csv')

def get_city_date_level_stats(df_live_vs_hist, min_readings_per_day):
# def get_city_date_level_stats(df_live_vs_hist, min_readings_per_day, max_hr = 23):
    # import pdb;
    # pdb.set_trace()

    city_date_level_stats = df_live_vs_hist.groupby(by=['country', 'city', 'date']).aggregate(
        {
            'results.weekHours.congestion': 'mean',
            'TrafficIndexLive': 'mean',
            'UpdateTime': 'count'
        }
    )
    city_date_level_stats.columns = ['TrafficIndexLastYear', 'TrafficIndex', 'num_readings']
    
    city_date_level_stats['change_yoy'] = (
        city_date_level_stats['TrafficIndex'] - city_date_level_stats['TrafficIndexLastYear']
    )/city_date_level_stats['TrafficIndexLastYear']
    
    max_date_df = (
            city_date_level_stats[
                city_date_level_stats['num_readings'] >= min_readings_per_day
            ]
            .reset_index()
            .groupby(by=['country', 'city'], as_index=False)
            ['date']
            .max()
            .rename(columns={'date': 'latest_full_date'})
        )

    city_date_level_stats = pd.merge(
        max_date_df,
        city_date_level_stats.reset_index(),
        how='left'
    ).set_index(['country', 'city', 'date'])
    
    return city_date_level_stats


def get_city_most_recent_stats(city_date_level_stats):
    
    city_date_level_stats = city_date_level_stats.copy()
    
    df_prev_prev_day = city_date_level_stats[
        city_date_level_stats.index.get_level_values(-1) == (city_date_level_stats['latest_full_date'] - pd.to_timedelta('1d'))
    ]
    
    df_prev_day = city_date_level_stats[
        city_date_level_stats.index.get_level_values(-1) == city_date_level_stats['latest_full_date']
    ]

    df_city_most_recent_stats = pd.concat([
        df_prev_prev_day.droplevel('date').rename(columns={'TrafficIndex': 'TrafficIndexPrevPrevDay'})[['TrafficIndexPrevPrevDay']],
        df_prev_day.reset_index(level='date')
    ], axis=1)
    
    return df_city_most_recent_stats


def city_stats_merge_report_settings(city_date_level_stats, report_city_settings):

    df = pd.merge(
        city_date_level_stats.reset_index(),
        report_city_settings,
        on=['country', 'city'],
        how='left'
    ).set_index(['country', 'city', 'date'])
    
    df['included'] = df['included'].fillna(False)
    df['alert_yoy'] = df['alert_yoy'].fillna(True)
    df['alert_yoy'] = df['alert_yoy'].fillna(DEFAULT_ABS_YOY_ALERT_THRESHOLD)
    
    return df


def style_change(v):
    if pd.isnull(v) or v == 0:
        c = 'black'
    elif v > 0:
        c = 'green'
    else:
        c = 'red'
    return "color: %s" % c


def format_percent(val):
    
    if pd.isnull(val):
        return val

    else:
        return "%.1f" % (val*100)

    
def style_time_series_tab(df):

    df_style = df.style.applymap(style_change)
    df_style = df_style.format(format_percent)
    
    return df_style


def get_yoy_time_series(city_date_level_stats):
    yoy_time_series = city_date_level_stats.reset_index()

    yoy_time_series = yoy_time_series[yoy_time_series['date'] <= yoy_time_series['latest_full_date']]
    
    yoy_time_series['date'] = yoy_time_series['date'].dt.date
    
    yoy_time_series = yoy_time_series.set_index(['country', 'city', 'date'])['change_yoy'].unstack()

    # Change the columns to be date strings
    yoy_time_series.columns = pd.Series(yoy_time_series.columns).dt.date.astype(str).tolist()
    
    return yoy_time_series


def alert_table(df_changes, suffix, filter=True):
    
    df_changes = df_changes.copy()

    df_changes['abs_%s' % suffix] = df_changes['change_%s' % suffix].abs()
    alert_condition = df_changes['abs_%s' % suffix] > df_changes['abs_yoy_alert_threshold']

    df_changes['alert'] = alert_condition
    
    if filter:
        df_changes = df_changes[
            df_changes['alert_%s' % suffix] &
            alert_condition
        ]
        
    df_changes = df_changes.sort_values('abs_%s' % suffix, ascending=False)
                                             
    return df_changes[['latest_full_date', 'abs_yoy_alert_threshold', 'TrafficIndexLastYear', 'TrafficIndexPrevPrevDay', 'TrafficIndex', 'change_yoy', 'alert']]


def color_alert(val):
    
    if val:
        return "background-color: red"
    else:
        #return "background-color: green"
        return ""

    
def generate_report_data(city_date_level_stats, df_city_most_recent_stats, report_city_settings):

    df_city_most_recent_stats_settings = city_stats_merge_report_settings(
        df_city_most_recent_stats, report_city_settings)
    city_date_level_stats_settings = city_stats_merge_report_settings(
        city_date_level_stats, report_city_settings)

    yoy_time_series_unfiltered = get_yoy_time_series(city_date_level_stats_settings)
    yoy_time_series_filtered = get_yoy_time_series(city_date_level_stats_settings[city_date_level_stats_settings['included']])

    alerts_filtered = alert_table(df_city_most_recent_stats_settings, 'yoy', filter=True)
    alerts_unfiltered = alert_table(df_city_most_recent_stats_settings, 'yoy', filter=False)

    return alerts_filtered, alerts_unfiltered, yoy_time_series_filtered, yoy_time_series_unfiltered


def style_report(alerts_filtered, alerts_unfiltered, yoy_time_series_filtered, yoy_time_series_unfiltered):

    yoy_time_series_filtered_tab = style_time_series_tab(yoy_time_series_filtered)
    yoy_time_series_unfiltered_tab = style_time_series_tab(yoy_time_series_unfiltered)

    alerts_filtered_tab = (
        alerts_filtered
        .style
        .applymap(style_change, subset=['change_yoy'])
        .applymap(color_alert, subset=['alert'])
        .format(format_percent)
    )

    alerts_unfiltered_tab = (
        alerts_unfiltered
        .style
        .applymap(style_change, subset=['change_yoy'])
        .applymap(color_alert, subset=['alert'])
        .format(format_percent)
    )
    
    return alerts_filtered_tab, alerts_unfiltered_tab, yoy_time_series_filtered_tab, yoy_time_series_unfiltered_tab


def output_report(
        report_city_settings,
        alerts_filtered_tab,
        alerts_unfiltered_tab,
        yoy_time_series_filtered_tab,
        yoy_time_series_unfiltered_tab,
        worst_hrs_alerts_filtered_tab,
        worst_hrs_alerts_unfiltered_tab,
        worst_hrs_yoy_time_series_filtered_tab,
        worst_hrs_yoy_time_series_unfiltered_tab):

    with pd.ExcelWriter('tomtom_report.xlsx') as writer:

        report_city_settings.to_excel(writer, sheet_name='City Settings')
        alerts_filtered_tab.to_excel(writer, sheet_name='Alerts')
        yoy_time_series_filtered_tab.to_excel(writer, sheet_name='YoY time series')
        alerts_unfiltered_tab.to_excel(writer, sheet_name='Alerts (All cities)')
        yoy_time_series_unfiltered_tab.to_excel(writer, sheet_name='YoY time series (All cities)')
        worst_hrs_alerts_filtered_tab.to_excel(writer, sheet_name='worst_hrs_Alerts')
        worst_hrs_yoy_time_series_filtered_tab.to_excel(writer, sheet_name='worst_hrs_YoY time series')
        worst_hrs_alerts_unfiltered_tab.to_excel(writer, sheet_name='worst_hrs_Alerts (All cities)')
        worst_hrs_yoy_time_series_unfiltered_tab.to_excel(writer, sheet_name='worst_hrs_YoY time series (All cities)')

def worst_hrs(working_days, df_live_vs_hist):
    df_worst_pm_hours = working_days[['circle_key', 'year', 'results.workingDays.days.day', 'results.workingDays.days.pmPeak.worstHour']]
    df_worst_am_hours = working_days[['circle_key', 'year', 'results.workingDays.days.day', 'results.workingDays.days.amPeak.worstHour']]
    df_worst_am_hours.columns = ['circle_key', 'year', 'day', 'worstHour']
    df_worst_pm_hours.columns = ['circle_key', 'year', 'day', 'worstHour']
    # df_worst_am_hours['am_or_pm'] = 'am'
    # df_worst_pm_hours['am_or_pm'] = 'pm'
    df_worst_hrs = pd.concat([df_worst_am_hours,df_worst_pm_hours])
    df_worst_hrs['day'] = df_worst_hrs['day'].str[0:3]
    df_wrst_hrs_vs_live_hist_hrs = pd.merge(
        df_live_vs_hist, 
        df_worst_hrs,
        left_on = ['circle_key', 'year', 'day', 'hour'],
        right_on = ['circle_key', 'year', 'day', 'worstHour']
    )
    # df_wrst_hrs_vs_live_hist_hrs = pd.merge(
    #     df_wrst_hrs_vs_live_hist_hrs,
    #     df_worst_pm_hours.rename(columns = {'worstHour':'worstPMHour'}),
    #     left_on = ['circle_key', 'year', 'day'],
    #     right_on = ['circle_key', 'year', 'day']
    # )
    return df_wrst_hrs_vs_live_hist_hrs

def run_report():
    report_city_settings = load_report_settings()
    ranking, city_data, city_year_data, week_hours, live_traffic, working_days = load_tomtom_dump()

    df_live_vs_hist = tomtom_scrape_traffic.get_live_vs_hist_comparison(
        ranking, city_data, live_traffic, week_hours, city_year_data
    )
    df_wrst_hrs_vs_live_hist_hrs = worst_hrs(working_days, df_live_vs_hist)
    df_live_vs_hist['date'] = df_live_vs_hist['UpdateTime'].apply(lambda d: d.date())
    city_date_level_stats = get_city_date_level_stats(df_live_vs_hist, 80)
    df_city_most_recent_stats = get_city_most_recent_stats(city_date_level_stats)

    alerts_filtered, alerts_unfiltered, yoy_time_series_filtered, yoy_time_series_unfiltered = generate_report_data(city_date_level_stats, df_city_most_recent_stats, report_city_settings)
    alerts_filtered_tab, alerts_unfiltered_tab, yoy_time_series_filtered_tab, yoy_time_series_unfiltered_tab = style_report(alerts_filtered, alerts_unfiltered, yoy_time_series_filtered, yoy_time_series_unfiltered)

    df_wrst_hrs_vs_live_hist_hrs['date'] = df_wrst_hrs_vs_live_hist_hrs['UpdateTime'].apply(lambda d: d.date())

    # wrst_hrs_city_date_level_stats = get_city_date_level_stats(df_wrst_hrs_vs_live_hist_hrs, 5, df_wrst_hrs_vs_live_hist_hrs['worstPMHour'])
    wrst_hrs_city_date_level_stats = get_city_date_level_stats(df_wrst_hrs_vs_live_hist_hrs, 5)
    wrst_hrs_df_city_most_recent_stats = get_city_most_recent_stats(wrst_hrs_city_date_level_stats)

    wrst_hrs_alerts_filtered, wrst_hrs_alerts_unfiltered, wrst_hrs_yoy_time_series_filtered, wrst_hrs_yoy_time_series_unfiltered = generate_report_data(wrst_hrs_city_date_level_stats, wrst_hrs_df_city_most_recent_stats, report_city_settings)
    wrst_hrs_alerts_filtered_tab, wrst_hrs_alerts_unfiltered_tab, wrst_hrs_yoy_time_series_filtered_tab, wrst_hrs_yoy_time_series_unfiltered_tab = style_report(wrst_hrs_alerts_filtered, wrst_hrs_alerts_unfiltered, wrst_hrs_yoy_time_series_filtered, wrst_hrs_yoy_time_series_unfiltered)

    output_report(report_city_settings, alerts_filtered_tab, alerts_unfiltered_tab, yoy_time_series_filtered_tab, yoy_time_series_unfiltered_tab, wrst_hrs_alerts_filtered_tab, wrst_hrs_alerts_unfiltered_tab, wrst_hrs_yoy_time_series_filtered_tab, wrst_hrs_yoy_time_series_unfiltered_tab)


if __name__ == "__main__":
    run_report()
