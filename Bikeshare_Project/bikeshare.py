# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 20:39:21 2021

@author: hazem
"""

import time
import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta


CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York': 'new_york_city.csv',
              'Washington': 'washington.csv' }
Months = ['All', 'January', 'February', 'March', 'April', 'May', 'June']
Days = ['All', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
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
    while True:
        city=str(input(" What City You Want To Check ? Chicago , New york or Washington \n Enter the city Name : "))
        city=city.title()
        if city in CITY_DATA.keys():
            break
        elif city.lower()=="newyork":
            city="New York"
            break
        else:
            print("Please Enter A Valid City Name !! ")
    # TO DO: get user input for month (all, january, february, ... , june)
    
    while True:
        month=str(input(" What Month You Want To Filter ? (January, February,March, April, May or June) \n Enter \"""All\""" If You Want All Months :\n "))
        month=month.title()
        if month in Months:
            break
        else:
            print("Oops ! That Is Not a Month Try  Again.\n")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=str(input("Now What Day Exactly ? Enter \"""All\""" If You Want All Days :\n "))
        day=day.title()
        if day in Days:
            break
        else:
            print("Not A Valid Day Please Try Again !!")
    print('-'*40)
    return city, month, day





def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    INPUTS:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df["Start Time"])
    df['month']=df['Start Time'].dt.month_name()
    df['week_day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != "All":
        #Creat the new Data Frame
        df=df[df['month']==month]
    if day !='All':
        df=df[df['week_day']==day]
    
    return df


def time_stats(df):
    """
        Displays statistics on the most frequent times of travel.
        INPUTS: df is a pandas DataFrame containing city data filtered by month and day
        Returns: None
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    MostCommonMonth=df["month"].mode()[0]
    print("The Most Common Month Is :",MostCommonMonth)
    # TO DO: display the most common day of week
    MostCommonDay=df["week_day"].mode()[0]
    print("The Most Common Day Is : ",MostCommonDay)

    # TO DO: display the most common start hour
    MostCommonHour=datetime.strptime(str(df["hour"].mode()[0]), "%H")
    #datetime.strptime(str(MostCommonHour), "%H")
    print("The Most Common Hour Is :",MostCommonHour.strftime("%I:%M %p"))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    """
        Displays statistics on the most popular stations and trip.
        INPUTS: df is a pandas DataFrame containing city data filtered by month and day
        Returns: None
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    MostCommonSstation=df['Start Station'].mode()[0]
    print("The Most Common Start Station is : ",MostCommonSstation)
    # TO DO: display most commonly used end station
    MostCommonEstation=df['End Station'].mode()[0]
    print("The Most Common End Station is : ",MostCommonEstation)

    # TO DO: display most frequent combination of start station and end station trip
    df["Combined Stations"]=df['Start Station']+" to "+df['End Station']
    MostStationsCombination=df["Combined Stations"].mode()[0]
    print("Most Common Station Of All Is :",MostStationsCombination )

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    TotalTime=df["Trip Duration"].sum()
    print("The Total Travel Time Is : ", timedelta(hours=int(TotalTime)))
    
    # TO DO: display mean travel time
    MeanTravelTime=df["Trip Duration"].mean()
    print("The Mean Travel Time Is : ", timedelta(hours=int(MeanTravelTime)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    SubUsersCount=df["User Type"].value_counts()[0]
    CusUserCount=df["User Type"].value_counts()[1]
    print("The Counts Of User Types Is :\nSubscriber={}\nCustomer={}".format(SubUsersCount, CusUserCount))

    # TO DO: Display counts of gender
    try:
        MaleGnderCount=df["Gender"].value_counts()[0]
        FemalGenderCount=df["Gender"].value_counts()[1]
        print("The Counts Of The Gender Is :\nMales={} \nFemales={}".format(MaleGnderCount,FemalGenderCount))
    except:
        print("Oops !! The File Has No Gender Data.")
    # TO DO: Display earliest, most recent, and most common year of birth
   ##if df['Birth Year'] in df[]:
    try: 
         print("The Earliest Year Is : ",df["Birth Year"].min())
         print("The Most Recent Year Is : ",df["Birth Year"].max())
         print("The Most Common Year of Birth Is : ",df["Birth Year"].mode()[0])
    except:
        print("Oops !! The File Has No Birth Year Data.")
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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
 	main()
