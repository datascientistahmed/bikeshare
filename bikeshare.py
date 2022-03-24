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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("=> Choose A City Name ( chicago, new york city, washington ): ")
    while city not in CITY_DATA.keys():
        print(" Please Enter A Correct City.")
        city = input("=> Choose A City Name ( chicago, new york city, washington ): ")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june", "all"]
    while True:
        month = input("Please Choose A Month Of Below (all, january, february, march, april, may, june):  ")
        if month in months:
            break
        else:
            print("Wrong Input Please Try Again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "all"]
    while True:
        day = input(" Please Choose A Day Of The Week (sunday, monday, tuesday, wednesday, thursday, friday, saturday, all):  ")
        if day in days:
            break
        else:
            print("Wrong Input Please Try Again.")
            
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
    
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday
    df["start hour"] = df["Start Time"].dt.hour
    
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month) + 1
        df = df[df["month"] == month]
        
    if day != "all":
        df = df[df["day_of_week"] == day.title()]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The Most Common Month Is:  {}".format(df["month"].mode()[0]))
    # TO DO: display the most common day of week
    print(" The Most Common Day Of Week Is:  {}".format(df["day_of_week"].mode()[0]))
    # TO DO: display the most common start hour
    print(" The Most Common Start Hour Is:  {}".format(df["start hour"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The Most Commonly Used Start Station Is: {}".format(df["Start Station"].mode()[0]))
    # TO DO: display most commonly used end station
    print("The Most Commonly Used End Station Is: {}".format(df["End Station"].mode()[0]))
    # TO DO: display most frequent combination of start station and end station trip
    df["combine"] = df["Start Station"] + "," + df["End Station"]
    print("The Most Frequent Combination Of Start Station And End Station Trip Is: {}".format(df["combine"].mode()[0]))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total Travel Time Is: ", (df["Trip Duration"].sum())) 
    # TO DO: display mean travel time
    print("Mean Travel Time: ", (df["Trip Duration"].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df["User Type"].value_counts().to_frame())
    # TO DO: Display counts of gender
    if city != "washington":
        print(df["Gender"].value_counts().to_frame)
    
        # TO DO: Display earliest, most recent, and most common year of birth
        print("The Earliest Year Of Birth Is: ",(df["Birth Year"].min()))
        print("The Most Recent Year Of Birth Is: ",(df["Birth Year"].max()))
        print("The Most Common Year Of Birth Is: ",(df["Birth Year"].mode()[0]))
    else:
        print("Washington Did Not Have This Type Of Data." )
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_five_rows(df):
    print("\n Five Rows Of Data Is Available To Read => ")
    m = 0
    user_input = input("Do You Want To Display The Five Rows ? => Please Type yes OR no")
    if user_input not in ["yes", "no"]:
          print("That Is Wrong Choice Could You Please Type (yes Or no)") 
          user_input = input("Do You Want To Display The Five Rows ? => Please Type yes OR no")
          
    elif user_input != "yes":
          print("thanks Very Much")
    else:
        while m + 5 < df.shape[0]:
            print(df.iloc[m:m+5])
            m += 5
            user_input = input("Would You Like More Five Rows ? => ")
            if user_input != "yes":
                print("Thank You Very Much")
                break
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_five_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

