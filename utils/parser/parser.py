from bs4 import BeautifulSoup
from datetime import date,datetime
import pandas as pd
import cfscrape

from data.config import URL

url = URL
scraper = cfscrape.create_scraper()
generated_html = scraper.get(url,timeout=(3,30)).text

# parse page with BeautifulSoup
soup = BeautifulSoup(generated_html, 'html.parser')

# returns the start time of events
def get_event_start_time():
    current_date = date.today()         # get current date
    event_time = soup.find_all(class_='robobet__time')
    event_time = [(time.text + ' ' + str(current_date)) for time in event_time[1::]] # get common format time
    event_time = [datetime.strptime(time, '%H:%M %Y-%m-%d') for time in event_time] # convert str time to timestamp format
    return event_time


# returns the leagues of events
def get_event_league():
    event_league = soup.find_all(class_='robobet__teams')
    event_league = [str(league.get('title')) for league in event_league[1::]]
    return event_league


# returns the command names of events
def get_event_teams():
    event_teams = soup.find_all(class_='robobet__team')
    event_teams = [team.text for team in event_teams]
    team_1_name = []
    team_2_name = []
    for row_team_number in range(len(event_teams)):   # division of commands into lists
        if row_team_number % 2 == 0:
            team_1_name.append(event_teams[row_team_number])
        else:
            team_2_name.append(event_teams[row_team_number])  
    return team_1_name,team_2_name



# returns the percentage of the probability of an outcome
def get_events_percentage():
    teams_percentage = soup.find_all(class_='robobet__percent')
    teams_percentage = [percent.text  for percent in teams_percentage]
    first_team_percentage = teams_percentage[3::3]        # division of percentage into lists
    draw_percentage = teams_percentage[4::3]                       
    second_team_percentage = teams_percentage[5::3]     
    return first_team_percentage,draw_percentage,second_team_percentage


# returns the forecasts of events
def get_event_forecast():
    event_forecast = soup.find_all(class_='robobet__bet')
    return [event_bet.text for event_bet in event_forecast[1::]]



# returns the odds of events
def get_event_odds():
    event_odds = soup.find_all(class_='robobet__odd')
    event_odds = [float(odds.text) for odds in event_odds[3::]]
    first_team_odd = event_odds[0::3]        # division of odds into lists
    draw_odd = event_odds[1::3]                     
    second_team_odd = event_odds[2::3]  
    return first_team_odd,draw_odd,second_team_odd


# returns the results of events
def get_event_result():
    event_result = soup.find_all(class_='robobet__result')
    return [result.text for result in event_result[1::]]

def create_df_robobet():
    event_time = get_event_start_time()
    event_league = get_event_league()
    team_1_name,team_2_name = get_event_teams()
    first_team_percentage,draw_percentage,second_team_percentage = get_events_percentage()
    event_forecast = get_event_forecast()
    first_team_odd,draw_odd,second_team_odd = get_event_odds()
    event_result = get_event_result()
    # Create pandas dataframe for temp_table
    df_robobet = pd.DataFrame({'event_start_time':event_time, 'event_league':event_league, 'team_1_name':team_1_name, 
                        'team_2_name':team_2_name, 'first_team_percentage':first_team_percentage, 'draw_percentage':draw_percentage,
                        'second_team_percentage':second_team_percentage, 'event_forecast':event_forecast, 'first_team_odd':first_team_odd,
                        'draw_odd':draw_odd, 'second_team_odd':second_team_odd, 'event_result':event_result
                            })
    return df_robobet.values.tolist()

create_df_robobet()
