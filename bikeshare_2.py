import time
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
    print('Hello! Let\'s explore some US bikeshare data!')
    # gets user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        print("which city are you choosing to explore its data? Is it Chicago, New York City or Washington?")
        city = input().lower()
        if city not in ["chicago", "new york city", "washington"]:
            print("Sorry! but the input is invalid!")
        else:
            print("You chose to explore {}".format(city.capitalize()))
            break

    # gets user input for month,day or both or none at all
    while True:
        print("Would you like to filter the data by month, day, both, or not at all")
        choice = input().lower()
        if choice == "month":
            print("please choose a month January, February, March, April, May, June")
            month = input().lower()
            if month not in ["january", "february", "march", "april", "may", "june"]:
                print("invalid input")
            else:
                day = ""
                break
        elif choice == "day":
            print("please choose a day in the week")
            day = input().lower()
            if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                print("invalid input")
            else:
                month = ""
                break
        elif choice == "both":
            print("please choose a month January, February, March, April, May, June")
            month = input().lower()
            if month not in ["january", "february", "march", "april", "may", "june"]:
                print("invalid input")
            else:
                print("please choose a day in the week")
                day = input().lower()
                if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                    print("invalid input")
                else:
                    break
        elif choice == "not at all":
            month = ""
            day = ""
            break
        else:
            print("Sorry! the input was invalid")

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
    if month != "":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != "":
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    the_most_common_month = df['month'].mode()
    months = ['january', 'feburary', 'march', 'april', 'may', 'june']
    month = months[int(the_most_common_month) - 1]
    print("The most common month is {}".format(month.capitalize()))

    # display the most common day of week
    the_most_common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day is {}".format(the_most_common_day_of_week))

    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    the_most_common_start_hour = df['hour'].mode()[0]
    print("The most common hour to start is {}".format(the_most_common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common Start Station is {}".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common End Station is {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ", " + df['End Station']
    freq_trip = df['Trip'].mode()[0]
    print("The most frequent Trip: {}".format(freq_trip))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total = df['Trip Duration'].sum()
    print("The total time travel= {}".format(total))

    # display mean travel time
    mean = df['Trip Duration'].mean()
    print("The mean time travel= {}".format(mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def user_stats(df):
    print('\nCalculating User Stats...\n')
start_time = time.time()

# Display counts of user types
users= df['User Type'].value_counts()
print("The count of User Types: \n{}".format(users))

try:
# Display counts of gender

    gender = df['Gender'].value_counts()
    print("The count of gender: \n{}".format(gender))

# Display earliest, most recent, and most common year of birt

    earliest= df['Birth Year'].min()
    print("The earliest birth year: {}".format(earliest))
    most_recent= df['Birth Year'].max()
    print("The most recent birth year: {}".format(most_recent))
    most_common= df['Birth Year'].mode()[0]
    print("The most common birth year: {}".format(most_common))
    print("Done calculating!")

except KeyError:
    print("Done calculating!")

print("\nThis took %s seconds." % (time.time() - start_time))
print('-'*40)


def raw_data(df2):
    """Displays the raw data of the city for the user."""
    #gets raw data for the user depending on the number of rows that he/she asks

    index=0
    raw_data=input("\n Would you like to check the raw data? Enter yes or no.\n")
    if raw_data == "yes":
        print(df2.iloc[index:index+5])
        index=index+5
        while True:
            more_rows=input("\n Would you like to check more rows of data? Enter yes or no.\n")
            if more_rows == "yes":
                print(df2.iloc[index:index+5])
                index=index+5
            else:
                break
    else:
        print("Well! That is all !")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        df2 = load_data(city, "", "")
        raw_data(df2)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
