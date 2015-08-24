import harbor
def print_tides_for_location(location, day_name):
    """prints a table for a given day"""
    row_template = "{0:>2}:00 {1:>4.2} m   {2:>6}"
    print(location.upper() + " " + day_name.upper() + " TIDES")
    headers = ("{0:<7}{1:<8}{2:<6}").format("Hour", "Height", "Launch")
    print(headers)
    day_heights = harbor.tide_list(location.lower(), day_name.lower())
    safe_height = harbor.safe_launch_height(location.lower())
 
    #hour list = a list of the numbers in the range of 0,24
    hour_list = list(range(1,25))
 
    #for each hour in hour list
    for time in (hour_list):
        #find the current tide height for the current time -1 because indexing starts from 0 not 1
        #compare the curren tide height with safe height
        b = " "
        if day_heights[time - 1] < safe_height:
            #if tide height lower than safe print unsafe...
            print(row_template.format(time, day_heights[time - 1], "Unsafe"))
        else:
            print(row_template.format(time, day_heights[time - 1], "Safe"))

    print(day_heights)
   
 
       
   
 
print_tides_for_location("Castlepoint", "Monday")