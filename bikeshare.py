import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city_choices = CITY_DATA.keys()
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York or Washington?\n').lower()
    while city not in city_choices:
        city = input('Would you like to see data for Chicago, New York or Washington?\n').lower()
    print('City ', city)

    filter_choices = ['month', 'day', 'both', 'none']
    filter = input('Would you like to filter the data by month, day, both or not at all?  Type "none" for no time filter.\n').lower()
    while filter not in filter_choices:
        filter = input('Would you like to filter the data by month, day, both or not at all?  Type "none" for no time filter.\n').lower()

    month = 'all'
    day = 'all'

    if filter in ('month', 'both'):
    # get user input for month (all, january, february, ... , june)
        month_choices = ['january', 'february', 'march', 'april', 'may', 'june', 'none']
        month = input('Which month?  January, February, March, April, May or June?  Please type out the month name.\n')
        while month.lower() not in month_choices:
            month = input('Which month?  January, February, March, April, May or June?  Please type out the month name.\n')

    if filter in ('day', 'both'):
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day_choices = ['M', 'Tu', 'W', 'Th', 'F', 'Sa', 'Su']
        day = input('Which day?  Please type a day M, Tu, W, Th, F, Sa, Su\n')
        while day.title() not in day_choices:
            day = input('Which day?  Please type a day M, Tu, W, Th, F, Sa, Su\n\n')

    print('Month ', month)
    print('Day ', day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == dayIntFromWeekdayName(day.title())]

    print('day of week ', day.title())
    return df

def dayIntFromWeekdayName(day_name):
    """
    Converts day of the week to day in int

    Args:
        (str) day_name - name of the day
    Returns:
        int - dt Series day of the week
    """
    if day_name == 'M':
        return 0
    if day_name == 'Tu':
        return 1
    if day_name == 'W':
        return 2
    if day_name == 'Th':
        return 3
    if day_name == 'F':
        return 4
    if day_name == 'Sa':
        return 5
    if day_name == 'Su':
        return 6

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df["month"].mode()[0]
    print('\nMost Common Month:', popular_month)

    # display the most common day of week
    popular_day = df["day_of_week"].mode()[0]
    print('\nMost Common Day of Week:', popular_day)

    # display the most common start hour
    popular_start_hour = df["hour"].mode()[0]
    print('\nMost Common Start Hour:', popular_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    most_common_start_station = df["Start Station"].mode()[0]
    print("\nDataFrame: \n", df["Start Station"].mode())
    #start_counts = df["Start Station"].mode()[1]
    print("\nMost Frequent Start Station: ", most_common_start_station)
    #print("\nMost Frequent Start Station: {} Count: {}".format(most_common_start_station, start_counts))

    # display most commonly used end station
    most_common_end_station = df["End Station"].mode()[0]
    #end_counts = df["End Station"].mode()[1]
    print("\nMost Frequent End Station: ", most_common_end_station)
    #print("\nMost Frequent End Station: {} Count: {}".format(most_common_end_station, end_counts))

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df['Start Station'] + ' to ' + df['End Station']
    print('\nMost Frequent Combination of Start and End Station Trip:\n', most_common_start_end_station.mode()[0])

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_trip_duration = df["Trip Duration"].sum()
    print('\nTotal Travel Time:', total_trip_duration)

    # display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print('\nMean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_type_count = df["User Type"].value_counts()
    print('\nCounts of User Types:\n', user_type_count)

    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df["Gender"].value_counts()
        print('\nCounts of Gender:\n', gender_count)


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df["Birth Year"].dropna()

        earliest_birth_year = birth_year.min()
        print('\nEarliest Year of Birth:', int(earliest_birth_year))

        latest_birth_year = df["Birth Year"].max()
        print('\nMost Recent Year of Birth:', int(latest_birth_year))

        common_birth_year = df["Birth Year"].mode()
        print('\nMost Common Year of Birth:', int(common_birth_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 0
        while True:
            # get user input if they want to display raw data
           raw_data = input('\nDo you like to display 5 records of raw data (yes or no)\n')
            if raw_data.lower() == 'yes':
                print(df.iloc[i:i+5])
                i +=5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
