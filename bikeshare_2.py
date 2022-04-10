import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
month_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 'all'}
day_list = ['All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
   """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA:
        city = input('Which city would you like to analyse (Chicago, New York City or Washington): ').lower()
        if city not in CITY_DATA:
            print('Please enter one of the three available cities')



    # get user input for month (all, january, february, ... , june)
    month =''
    while month not in month_dict:
        month = input('Which month would you like to analyse(all, january, february, ... , june): ').lower()
        if month not in month_dict:
            print('Please enter a valid month')



    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day not in day_list:
        day = input('Which day would you like to analyse(all, monday, tuesday, ... sunday): ').title()
    if day not in day_list:
        print('Please enter a valid day')



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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['start_day_of_week'] = df['Start Time'].dt.day_name()
    df['start_month'] = df['Start Time'].dt.month
    df['start_hour'] = df['Start Time'].dt.hour
    df['route'] = df['Start Station'] + ' to ' + df['End Station']
    if month_dict[month] != 'all':
        df = df[df['start_month'] == month_dict[month]]
    if day != 'All':
        df = df[df['start_day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month = df['start_month'].value_counts().index.tolist()[0]
    most_common_month_count = df['start_month'].value_counts().tolist()[0]

    print('The most popular month to hire a bike is {} with {:,} rentals'.format(most_common_month, most_common_month_count))


    # display the most common day of week
    most_common_day = df['start_day_of_week'].value_counts().index.tolist()[0]
    most_common_day_count = df['start_day_of_week'].value_counts().tolist()[0]
    print('The most popular day to hire a bike is {} with {:,} rentals'.format(most_common_day, most_common_day_count))


    # display the most common start hour
    most_common_hour = df['start_hour'].value_counts().index.tolist()[0]
    most_common_hour_count = df['start_hour'].value_counts().tolist()[0]
    print('The most popular hour to hire a bike is {} with {:,} rentals'.format(most_common_hour, most_common_hour_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most popular start station is '+ str(df['Start Station'].value_counts().index.tolist()[0]) + ' with ' + str("{:,}".format(df['Start Station'].value_counts().tolist()[0]))+' rentals')


    # display most commonly used end station
    print('The most popular end station is '+ str(df['End Station'].value_counts().index.tolist()[0]) + ' with ' + str("{:,}".format(df['End Station'].value_counts().tolist()[0]))+' rentals')


    # display most frequent combination of start station and end station trip
    print('The most popular route station is '+ str(df['route'].value_counts().index.tolist()[0]) + ' with ' + str("{:,}".format(df['route'].value_counts().tolist()[0]))+' rentals')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is ' + str("{:,.2f}".format(df['Trip Duration'].sum()/360)) + ' hours')


    # display mean travel time
    print('Average travel time is ' + str("{:,.2f}".format(df['Trip Duration'].mean()/360)) + ' hours')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    print('\nBelow is the number of rentals per user type\n')
    print(df.groupby(['User Type'])['Start Time'].count())


    # Display counts of gender
    if city == 'washington':
        print('\nThere is no gender data for you selected city')
    else:
        print('\nBelow is the number of rentals per user gender\n')
        print(df.groupby(['Gender'])['Start Time'].count())


    # Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('\nThere is no birth year data for you selected city')
    else:
        print('\nThe oldest birth year is ' + str(int(df['Birth Year'].min())))
        print('\nThe youngest birth year is ' + str(int(df['Birth Year'].max())))
        print('\nThe most common birth year '+ str(int(df['Birth Year'].value_counts().index.tolist()[0])) + ' with ' + str("{:,}".format(df['Birth Year'].value_counts().tolist()[0]))+' rentals')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    size = 5
    start = 0
    end = size
    max_length = len(df.index)
    sample_data = input('Would you like to see some raw data? (yes/no)?').lower()

    while sample_data == 'yes':
        print(df.iloc[start:end])
        start += size
        if (end + size) < max_length:
            end += size
            sample_data = input('More raw data (yes/no)?')
        else:
            sample_data = input('More rample data (yes/no)?')
            if sample_data == 'yes':
                end = max_length
                print(df.iloc[start:end])
                print('This is the end of the data')
                sample_data = 'no'
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
