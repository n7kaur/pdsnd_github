import time
import pandas as pd


CITY_DATA = {'Chicago': pd.read_csv('C:/Users/n7kau/Desktop/Udacity/Python/Project2/chicago.csv'),
              'New York City': pd.read_csv('C:/Users/n7kau/Desktop/Udacity/Python/Project2/new_york_city.csv'),
              'Washington': pd.read_csv('C:/Users/n7kau/Desktop/Udacity/Python/Project2/washington.csv')}

      # Bulid lists for cities, months and days
 
cities = ['Chicago', 'New York City', 'Washington']
months = ['All', 'January', 'February', 'March', 'April','May', 'June']
days= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All'] 


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

    city = print('\nHello! Let\'s explore some US bikeshare data!\n')
    
    while True:
        city = input("\nWhich city data are you looking for? Chicago, New York City or Washington?\n").title()
        if city not in cities:
            print("Sorry, this is an invalid input. Please select one of the above mentioned cities.")
            continue
        else:
            break
        # get user input for month (all, january, february, ... , june)
    while True:
        month = input("\nWhich month's data are you seeking? Please enter name of the month (for e.g- January, February etc.? Type 'All' to see data for all months.\n").title()
        if month not in months:
            print("Sorry, this is an invalid input. Please enter valid month name.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("\nWhich day's data are you seeking? Please enter integer (for e.g- 1 for Sunday, 2 for Monday etc.? Type 0 to see data for all days.\n").title()
        if day not in days:
            print("Sorry, this is an invalid input. Please enter valid weekday name.")
            continue
        else:
            break
        
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

    df = CITY_DATA[city]

    # Convert variable 'Start Time' to datetime format

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create two new columns of month and day by extracting these values from 'Start Time' variable
    df['Month_in_data'] = df['Start Time'].dt.month
    df['Day_in_data'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 'All':
       
        month = months.index(month)
        
        df = df[df['Month_in_data'] == month]
        

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        
        day = days.index(day) 
        df = df[df['Day_in_data'] == day]
        
    return df
    


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    time_stat = input("\nDo you want to see most frequent times of travel? Press 'Yes' or 'No'\n").title()
    
    if time_stat == 'Yes':

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()
    
        # display the most common month
        
        Most_Common_Month = df['Month_in_data'].mode()[0]
        
        print("The most common month from given data is: " +months[Most_Common_Month].title())
    
        # display the most common day of week
    
        Common_Day_Of_Week = df['Day_in_data'].mode()[0]
        
        print("The most common day of week from given data is: " +days[Common_Day_Of_Week].title())
        
        # display the most common start hour
        
        df['hour'] = df['Start Time'].dt.hour
        Most_Common_Start_Hour = df['hour'].mode()[0]
        
        print("The most common start hour from given data is: " +str(Most_Common_Start_Hour))
        
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    
    station_stat = input("\nDo you want to see most popular stations and trip? Press 'Yes' or 'No'\n").title()
    
    if station_stat == 'Yes':

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()
    
        # display most commonly used start station
        
    
        Most_Common_Start_Station = df['Start Station'].value_counts().index[0]
        
        print("The most commonly used start station from given data is: " +Most_Common_Start_Station)
    
        # display most commonly used end station
        
        Most_Common_End_Station = df['End Station'].value_counts().index[0]
        
        print("The most commonly used end station from given data is: " +Most_Common_End_Station)
    
        # display most frequent combination of start station and end station trip
        
        Most_Frequent_Combination = (df['Start Station']+ "-" +df['End Station']).value_counts().index[0]
        
        print("The most frequent combination of start station and end station trip is: "+str(Most_Frequent_Combination))
    
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    
    trip_stat = input("\nDo you want to see statistics on the total and average trip duration? Press 'Yes' or 'No'\n").title()
    
    if trip_stat == 'Yes':

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()
    
        # display total travel time
        
        Total_Travel_time = df['Trip Duration'].sum()
        Total_Travel_time = round(Total_Travel_time/86400,2)
        
        print('Total travel time is {} days.'.format(Total_Travel_time))
    
    
        # display mean travel time
        
        Mean_Travel_Time = df['Trip Duration'].mean()
        Mean_Travel_Time = round(Mean_Travel_Time/ 60,2)
        
        print('Mean travel time is {} minutes.'.format(Mean_Travel_Time))
    
    
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    user_stat = input("\nDo you want to see users' stats? Press 'Yes' or 'No'\n").title()
    
    if user_stat == 'Yes':
    
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        
        user_types = df['User Type'].value_counts()
        print('Count of all user types in the data:\n', user_types)

        # Display counts of gender
        
        if city != 'Washington':
            Gender_count = df['Gender'].value_counts()
            print('Count of gender types in the data:\n', Gender_count)

        else:
            print("Gender Data - Requested data is not available for this city.")
            

        # Display earliest, most recent, and most common year of birth
             
        if city !='Washington':
            Earliest_Birth_Year = df['Birth Year'].min()
            Most_Recent_Birth_Year = df['Birth Year'].max()
            Most_Common_Birth_Year = df['Birth Year'].value_counts().index[0]
            print('Earliest birth year in the data is:\n',Earliest_Birth_Year)
            print('Most recent birth year in the data is:\n',Most_Recent_Birth_Year)
            print('Most Common birth year in the data is:\n',Most_Common_Birth_Year)
        else:
            print("Birth Year - Requested data is not available for this city.")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)

def display_data(df):
    """Displays five rows on user request."""
    print(df.head())
    next = 0
    while True:
        view_data = input('\nWould you like to view next five rows of the data? Enter yes or no.\n')
        if view_data.lower() != 'yes':
            return
        next = next + 5
        print(df.iloc[next:next+5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        while True:
            view_data = input('\nWould you like to view first five rows of the data? Enter yes or no.\n')
            if view_data.lower() != 'yes':
                break
            display_data(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()

