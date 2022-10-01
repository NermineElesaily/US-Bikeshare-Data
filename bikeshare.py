# Links used to solve the project:
# https://www.includehelp.com/python/asking-the-user-for-input-until-a-valid-response-in-python.aspx
# https://stackoverflow.com/questions/10139866/calling-variable-defined-inside-one-function-from-another-function
# https://stackoverflow.com/questions/55719762/how-to-calculate-mode-over-two-columns-in-a-python-dataframe
# https://stackoverflow.com/questions/65480967/how-can-i-display-five-rows-of-data-based-on-user-in-python

import time
import numpy as np
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """ Asks user to specify a city, month and day to analyze.

        Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or 'all' to apply no month filter
        (str) day - name of the weekday to filter by, or 'all' to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city, month, day = '', '', ''
    # get city user_input
    while True:
        try:
            city = str(input('\nWhich city would you like to explore? Chicago, New York City or Washington?\n').lower())
            if city in CITY_DATA:
                break
            else:
                print('\nPlease choose a city from the following: Chicago, New York City, or Washington\n')
        except:
                print('Please insert a valid city name')
                continue
    # get month user_input
    while True:
        try:
            month = str(input('\nPlease enter a month from january to june if you would like to filter data by month or \'all\' to apply no filter.\n').lower())
            if month in MONTHS:
                break
            else:
                print('Please choose a month from january to june')
        except:
            print('Please insert a valid month')
            continue
    # get day user_input
    while True:
        try:
            day = str(input('\nPlease choose a weekday if you would like to filter data by days or \'all\' to apply no filter.\n').lower())
            if day in DAYS:
                break
            else:
                print('Please insert a weekday name')
        except:
            print('Please enter a valid weekday')
            continue

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city filtered by month and/or day if applicable

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    Returns:
         df - Pandas DataFrame containing city data filtered by month and day
    """
    # load file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use index of month to get the corresponding int
        month = MONTHS.index(month)
        df = df[df['month'] == month]

    # filter by day if applicable
    if day != 'all':
        # filter by day to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        return df
        print(df)

def time_stats(df, month, day):
    """
    Displays statistics on the most frequent travel times

    """
    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

    # display the most common month
    if month == 'all':
        popular_month = df['month'].mode()[0]
        print('The most common month is: {}. '.format(MONTHS[popular_month]))

    # display the most common weekday
    if day == 'all':
        popular_weekday = df['day_of_week'].mode()[0]
        print('The most common weekday is: {}. '.format(popular_weekday))

    # display the most common hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour is: {}.'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """
    Displays statistics on the most popular stations

    """
    print('\nCalculating The Mot Popular Stations and Trips ...\n')
    start_time = time.time()

    # display most common start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common Start Station used is {}.'.format(popular_start_station))

    # display most common end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common end station used is {}.'.format(popular_end_station))

    # display most frequent combination of start and end stations
    popular_combination = (df['Start Station'] + df['End Station']).mode()[0]
    print('The most frequent combination of start and end stations is {}.'.format(popular_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """
    Displays statistics on the total and mean trip duration.

    """
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('The total travel time is {}'.format(str(total_travel_time)))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('The mean travel time is equal to {}'.format(str(mean_travel_time)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df, city):
    """
    Displays statisics on US bikeshare users

    """
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # display counts of user types
    user_type = df['User Type'].value_counts()
    print('The counts of user types are: \n{}.'.format(str(user_type)))

    # check city input in order to display gender counts and Birth year stats
    if city == 'chicago' or city == 'new york city':

        # display gender counts
        gender = df['Gender'].value_counts()
        print('The count of user gender is \n{}.'.format(str(gender)))
        # display earliest, most recent and most common year of birth
        earliest_BY = df['Birth Year'].min()
        print('The earliest year of birth is {}.'.format(int(earliest_BY)))
        most_recent_BY = df['Birth Year'].max()
        print('The most recent year of birth is {}.'.format(int(most_recent_BY)))
        most_common_BY = df['Birth Year'].mode()[0]
        print('The most common year of birth is {}.'.format(int(most_common_BY)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Displays raw data upon user input.

    """
    # asks user if they would like to view raw data
    answer = ['yes', 'no']
    while True:
        try:
            view_data = input('\nWould you like to see the first 5 rows of raw data? Please enter yes or no\n').lower()
            if view_data in answer:
                break
            else:
                print('Please reply with yes or no')
        except:
            print('Please insert a valid answer')
            continue
        if view_data == 'yes':
            print('df.iloc[0:5]')
       
    start_loc = 5
    view_raw = True
    # keep displaying thee next 5 rows of raw data until the user says 'no'
    while (view_raw):
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        view_next = input('\nWould you like to see the next 5 rows? Please enter yes or no\n').lower()
        if view_next == 'no': 
            view_raw = False


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == '__main__':
    main()
