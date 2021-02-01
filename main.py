import pandas as pd
import numpy as np

df = pd.read_csv("stats.csv")

df_fantasy = df
#Values for different stats
# "3P" , "2P", "FT", "TOV", "ORB", "AST", "BLK", "STL"
##threepointer = 3
##twopointer = 2
##freethrow = 1
##rebound = 1.2
##assist = 1.5
##block = 2
##steal = 2
##turnover = -1

df_fantasy["3P"] = 3*df_fantasy["3P"]
df_fantasy["2P"] = 2*df_fantasy["2P"]
df_fantasy["FT"] = 1*df_fantasy["FT"]
df_fantasy["ORB"] = 1.2*df_fantasy["ORB"]
df_fantasy["AST"] = 1.5*df_fantasy["AST"]
df_fantasy["BLK"] = 2*df_fantasy["BLK"]
df_fantasy["STL"] = 2*df_fantasy["STL"]
df_fantasy["TOV"] = -1*df_fantasy["TOV"]

score = df_fantasy["3P"] + df_fantasy["2P"] + df_fantasy["FT"] + df_fantasy["ORB"] + df_fantasy["AST"] + df_fantasy["BLK"] + df_fantasy["STL"] + df_fantasy["TOV"]

df_fantasy["Score"] = score
df_fantasy = df_fantasy[["Player", "Pos","3P" , "2P", "FT", "TOV", "ORB", "AST", "BLK", "STL","Score"]]
#print(df_fantasy.iloc[2])



#print(df_fantasy.iloc[1])
centers = df_fantasy[(df_fantasy["Pos"] == "C")]
small_forwards = df_fantasy[(df_fantasy["Pos"] == "SF")]
power_forwards = df_fantasy[(df_fantasy["Pos"] == "PF")]
shooting_guards = df_fantasy[(df_fantasy["Pos"] == "SG")]
point_guards = df_fantasy[(df_fantasy["Pos"] == "PG")]

center_max = centers["Score"].idxmax()
small_forwards_max = small_forwards["Score"].idxmax()
power_forward_max = power_forwards["Score"].idxmax()
shooting_guards_max = shooting_guards["Score"].idxmax()
point_guards_max = point_guards["Score"].idxmax()



best_five = []
best_five.append(small_forwards.loc[small_forwards_max])
best_five.append(centers.loc[center_max])
best_five.append(power_forwards.loc[power_forward_max])
best_five.append(shooting_guards.loc[shooting_guards_max])
best_five.append(point_guards.loc[point_guards_max])


print(best_five)






