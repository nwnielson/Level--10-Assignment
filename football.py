import pandas as pd

football_stats = pd.read_csv("cfb.csv")
keep_analyzing = True

#Loops until user wants to stop analyzing
while keep_analyzing :
    
    #Makes sure that input is valid (is a number and is a valid season in the CSV)
    try:
        season_num = int(input("\nWhich season would you like to analyze?\n"))
        
        #If number isn't found in data, inform user, then continue to next iteration to pick again
        if season_num not in football_stats["Season"].values:
            print(f"\nSeason {season_num} was not found in the data. Please try again")
            continue
            
    
    #If input isn't a number, this prompts user to pick a number in number form
    except ValueError:
        print("Please enter a season as a number (ex. 2020)\n")
        continue
    
    #If we get a rando error, exits program.
    except:
        print("Unknown Error. Terminating Program.")
        break
    
    #Runs if no error
    else:
        print(f"\nCollege Football Results for {season_num}:")
        
        #Sets season_stats to the stats of the selected season by the user
        season_stats = football_stats.query(f"Season == {season_num}")
        
        #Organizes teams in picked season into win categories
        team_info = {
        "10 or More Wins": season_stats.query("Win >= 10")["Team"],
        "8-9 Wins": season_stats.query("8 <= Win <= 9")["Team"],
        "6-7 Wins": season_stats.query("6 <= Win <= 7")["Team"],
        "Less Than 6 Wins": season_stats.query("Win < 6")["Team"]
        }
        
        #Display results
        for win_category in team_info:
            print(f"\n{win_category}:")
            for team in team_info[win_category]:
                print(team)
        
        #Loops until user gives valid answer of whether they want to analyze more seasons.
        while True:
            
            #Makes sure input is valid
            try: 
                keep_looping = input("\nWould you like to analyze another year? (Yes or No)\n").upper()
                if keep_looping not in ["YES", "NO"]:
                    raise Exception
            
            #If there is any error, prompts user to give valid input (yes or no)  
            except:
                print("Invalid response. Please answer with yes or no.\n")
            
            #If no error, checks if user wants to analyze more and repeats if yes, quits program if no
            else:
                if keep_looping == "NO" :
                    keep_analyzing = False
                    print("Thanks! Come back soon to do more analyzing!")
                    break
                print("\n------------------------------------------------")
                break