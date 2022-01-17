import time
import pandas as pd
import numpy as np
import statistics

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    city_lst1 = ['chicago','new york city','washington']
    month_lst1 = ['january','february','march','april','may','june']
    day_lst1 = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    try:
        while True:
            city = city_lst1.index(input("\nWould Like to see the data for (chicago, new york city, washington) ?\n ").title().lower())
            print(" you've choosen %s  interesting!! " %(city_lst1[city]))
            time_frame = input(" \nhow would you like to filter the data? by (month, day, both), in case you do not want filter type 'none'\n ").title().lower()
            month = "none"
            day = 'none'
            if time_frame =='both':
                month = month_lst1.index(input("\nplease give me the month(january, february, march, april, may, june) you want to learn about\n").title().lower())
                day = day_lst1.index(input("\nplease give me the day(monday, tuesday, wednesday, thursday, friday, saturday, sunday) you want to learn about\n ").title().lower())
                print(month,day)
                break
            elif time_frame == 'month':
                month = month_lst1.index(input("\nplease give me the month(january, february, march, april, may, june) you want to learn about\n").title().lower())
                day ='none'
                print(month)
                break
            elif time_frame == 'day':
                day = day_lst1.index(input("\nplease give me the day(monday, tuesday, wednesday, thursday, friday, saturday, sunday) you want to learn about\n ").title().lower())
                month ='none'
                print(day)
                break
            break


        return city_lst1[city], month, day
    except ValueError:
            print(" there is something wrong!! please make sure that you have given the correct answer from the above mentioned options")





    # get user input for month (all, january, february, ... , june)


    # get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)



def load_data(city, month, day):


    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "none" to apply no month filter
        (str) day - name of the day of week to filter by, or "none" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    print(df)
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    print(df['month'])
    df['day_of_week'] = df['Start Time'].dt.day
    if month !='none' and day !='none':
        df = df[df['month']==(month+1)]
        df = df[df['day_of_week']==(day+1)]
        return df
    if month != 'none':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        df = df[df['month']==(month+1)]
        print('right!!')
        print(df)
    if day != 'none':
        df = df[df['day_of_week']==(day+1)]
        print('right!!!')
        return df



    print(df['Start Time'])
    return df


def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    print("can u see me")
    if month != 'none':
        print(df['day_of_week'][df['month']==(month+1)].mode())
    else:
        pass
    if day != 'none':
        print(df['day_of_week'].mode())
    else:
        pass
    print(df['Start Time'].mode())



    # display the most common day in a given month




    # display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    # display most commonly used start station
    most_common_start_Station = df['Start Station'].mode()
    print(most_common_start_Station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].mode()
    print(most_common_end_station)


    # display most frequent combination of start station and end station trip
    most_common_combination_stations = df["Start Station"] +df['End Station']
    print(most_common_combination_stations.mode())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    Start = pd.to_datetime(df['End Time'])
    End  = pd.to_datetime(df['Start Time'])
    print("\ntotal travel time\n ",Start.subtract(End))


    # display mean travel time
    print("\nmean travel time\n",Start.subtract(End).mean())



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()
    print(counts_of_user_types)


    # Display counts of gender
    if city !='washington':
        counts_of_gender = df["Gender"].value_counts()
        print(counts_of_gender)
    else:
        print('you have choosen washington, which has no gender count for the user ')


    # Display earliest, most recent, and most common year of birth
    if city !='washington':
        earliest = df['Birth Year'].min()
        print("\nthe oldest users\n",earliest)
        most_recent = df['Birth Year'].max()
        print("\nthe youngest users\n",most_recent)
        most_common_birth_year = df['Birth Year'].mode()
    else:
        print("you've choosen washington, which has no birth years within its data")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(city):
    df = pd.read_csv(CITY_DATA[city])
    head = 5
    print(df.head(head))

    while True:
        respond= input("\nwould you like to see the raw data? type 'yes' or 'no'\n ")
        if respond == 'yes':
            head +=5
            print(df.head(head))
        else:
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        display_raw_data(city)




        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
