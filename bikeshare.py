import time
import os
import sys
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let\'s explore some US bikeshare data!")
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city = ''

    print("\n" * os.get_terminal_size().lines)
    while city not in CITY_DATA.keys():
        print("\nPlease, enter the name of chosen city: Chicago, New York City or Washington.")
        print("What do you prefer:")
        city = input().lower()

        if city not in CITY_DATA.keys():
            print("\n",city," is an invalid city. You have to choose chicago, new york city or washington")
            print("Please, check spelling and enter the city gain...")

    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'all':0, 'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    month = ''

    print("\n" * os.get_terminal_size().lines)
    while month not in MONTH_DATA.keys():
        print("\nPlease, now chosen a month - january to june or all")
        print("Which month do you prefer:")
        month = input().lower()

        if month not in MONTH_DATA.keys():
            print("\nYou have written",month," that is not on the list of months options.")
            print("Please, check spelling and if the month is on the list bellow:")
            print("months: January, February,Mmarch, April, May, June or All for total months")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''

    print("\n" * os.get_terminal_size().lines)
    while day not in DAY_DATA:
        print("\nPlease, finally, select a day of week - Monday to Sunday or All for whole week")
        day = input().lower()

        if day not in DAY_DATA:
            print("\nYou have written",day," that is not on the list of week days.")
            print("Please, check spelling and if the week day is on the list bellow:")
            print("days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All for whole week")

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

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    """filter by month"""
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    """filter by day"""
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mostcom_month = df['month'].mode()[0]
    print("\nMost common month:", mostcom_month)

    # TO DO: display the most common day of week
    mostcom_day = df['day_of_week'].mode()[0]
    print("\nMost common day:", mostcom_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    mostcom_hour = df['hour'].mode()[0]
    print("\nMost common start hour: ", mostcom_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    input("Press Enter to continue...")


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    mostcom_startstation = df['Start Station'].mode()[0]
    print("\nMost commonly used start station is ",mostcom_startstation)

    # TO DO: display most commonly used end station
    mostcom_endstation = df['End Station'].mode()[0]
    print("\nMost commonly used end station is ",mostcom_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start and End Station trip'] = df['Start Station'] + ' to ' + df['End Station']
    mostfreq_StartEnd = df['Start and End Station trip'].mode()[0]
    print("\nMost frequent combination of start station and end station trip", mostfreq_StartEnd)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    input("Press Enter to continue...")

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totaltravel_time = df['Trip Duration'].sum()
    print("\nTotal travel time: ", totaltravel_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("\nMean travel time: ", mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    input("Press Enter to continue...")

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        user_type = df['User Type'].value_counts()
        print("\nCounts of user types:\n", user_type)
    except:
        print("\nSorry, but there is no user type registered for this city!")

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nCounts of gender:\n", gender)
    except:
        print("\nSorry, but there is no gender data registered for this city!")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        print("\nEarliest birthday: ", earliest)
        recent = int(df['Birth Year'].max())
        print("\nMost recent birthday: ", recent)
        mostcom_year = int(df['Birth Year'].mode()[0])
        print("\nMost common year of birthday: ", mostcom_year)
    except:
        print("\nSorry, but there is no birthday data registered for this city!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    input("Press Enter to continue...")


def rawdata_print(df):
    PRT_RAWDATA = {'header','raw','no'}
    prt_rd_opt = {'yes','no'}

    prt_rd = ''
    prt_rd5 = ''

    while prt_rd not in PRT_RAWDATA:
            print("\n" * os.get_terminal_size().lines)
            prt_rd = input("\nWould you like to print the header or the raw data? Enter header, raw or no.\n")
            if prt_rd.lower() == 'header':
                print(df.head())
                prt_rd = ''
            if prt_rd.lower() == 'raw':
                    lfrom = 0
                    lto = 4
                    prt_rd = ''
                    print(df.iloc[lfrom:lto,:])
                    while prt_rd5 not in prt_rd_opt:
                            print("\n" * os.get_terminal_size().lines)
                            prt_rd5 = input("\nWould you like to print additional 5 lines? Enter yes or no.\n")
                            if prt_rd5.lower() == "yes":
                                 print(df.iloc[lfrom:lto,:])
                                 lfrom = lto
                                 lto = lto+5
                                 prt_rd5 = ''
                            elif prt_rd5.lower() == "no":
                                 break
                            else: print ("\nSorry, I couldn't understand! Please, can try again...")
            elif prt_rd.lower() == 'no':
                 break
            else: print("\nSorry, I couldn\'t understand! The option",prt_rd,"is not available.")

def main():
    RESTART_OPT = {'yes','no'}

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        rawdata_print(df)

        restart = ''

        while restart not in RESTART_OPT:
            restart = input("\nPlease, would you like to restart? Enter yes or no.\n")
            if restart not in RESTART_OPT:
                 print("\nSorry, I couldn\'t understand! The option",restart,"is not available.")
            elif restart.lower() == "no":
                 print("\n" * os.get_terminal_size().lines)
                 print("Thank you! Obrigado! Gracias! Grazie! Merci! xiè xiè!")
                 sys.exit()

if __name__ == "__main__":
	main()
