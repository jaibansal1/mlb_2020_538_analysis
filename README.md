## Summary
This project does a brief analysis of [538's MLB Predictions](https://projects.fivethirtyeight.com/2020-mlb-predictions/games/) for the shortened 2020 season. 538 very generously provides a spreadsheet with all of their game-level predictions, so no complex scraping was required to analyze the accuracy of their predictions. Instead, all I had to do was download the csv file and load it in as a data frame using Pandas. 

538 uses an ELO system to project the winner of a particular game. For those unfamiliar with ELO, 538 assigns every team with a rating dependent on the level of skill on that team (hitters, pitchers). 538 adjusts their baseline ELO for MLB teams with other information such as home field advantage and the relative skill of the team's starting pitcher. Once they have both teams' ELO for a particular matchup, they use the difference between the two teams' ratings to assign each team a probability that they will win the matchup. After a game is played and the result is finalized, both teams' ELO ratings change (the winning team gains some points, and the losing team loses some points). The amount each teams' ELO changes depends on the original ELO difference between the two teams. This sort of rating system is very prominent in chess. 

I analyzed 538's raw ability to predict the correct winner of the game by just comparing the number of times they gave a team a greater than 50% chance of winning, and when that team actually won. However, just looking at the raw accuracy is not a fully accurate way of assessing the model. For instance, if in one game 538 predicted a 90% chance win for the Yankees, and the Yankees ended, they should be rewarded by my analysis more than if they gave the Yankees a 51% chance of winning. 

Because of this, I also calculated the Brier score of 538's MLB Predictions. Brier score, which is really just the mean squared error, measures the accuracy of predictions by summing the squares of the differences between the projected chance of winning and the actual result (whether or not the team won). A lower Brier score is better (closer to 0), because that means the difference between the expected and actual values was low, or in other words, the predictions were accurate. 

However, a raw Brier score itself is also limited in how much it reveals about the model's efficacy, so I compared 538's model with a reference model I created on my own. My reference model was extremely rudimentary: all I did was average each team's 2019 win totals with their expected 2020 win totals (courtesy of bettingpros). I added both of these columns to 538's Prediction CSV (last two columns), which is included in this repository. The reference model's prediction was to just give the team with the higher number of average wins (based on that formula) the win every single time. The reason I created this reference model was to see how much better 538's complex math and ELO system was compared to this extremely basic model.

## Results
538's MLB Predictions correctly forecasted the result of 57.73% of MLB games in 2020. The model's Brier score is 0.24. 

These numbers are a little difficult to interpret on their own, but they seem pretty good. However, my arbitrary reference model was able to correctly predict the result of games 57.1% of the time, which is just 0.63% worse than 538. My reference model's Brier score is 0.44, which means the Brier Skill Score for 538, which ranges from -infinity to 1, is 0.44. A value close to 1 represents a strong predictive model.

## Shortcomings & Future Steps 
I am in no way criticizing 538's MLB Predictions. I am an amateur data scientist trying to get my feet wet in the field, and I stuck to data analysis techniques I learned in my econometrics class from my sophomore year at Vanderbilt University. It is very possible that baseball is just a really difficult game to predict, with high levels of uncertainty at the micro-level. 

I want to continue this project and add a few more aspects to my analysis. First, I think using some more data (e.g., 2019 Season) could be beneficial, especially because 2020 was such an unusual MLB Season. I also want to compare 538's results with other websites that predict MLB games, including ESPN, Fangraphs, and potentially some Vegas oddsmakers. These other websites do not present their predictions in as convenient a way as 538, so I will have to sharpen my scraping skills during this winter break. If you are experienced at web scraping using Python and would be willing to answer some questions I encounter along the way, please shoot me an email (author section). 

Eventually, my goal is to integrate all of these different prediction websites into a single tool that can use machine learning to take all of the predictions in a given day and spit out a well-tested prediction of what is going to happen that day. I could then compare this prediction with the implied odds of betting markets, and potentially make some solid returns investing in differences. Then again, sports wagering markets are empirically pretty efficient, but it's less about the money and more about the process.  

## Author
As of November 2020, Jai Bansal is a junior at Vanderbilt University triple majoring in Economics, Computer Science, and Applied Mathematics. Jai is interested in pursuing a career related to mathematic finance, algorithmic trading, or baseball analytics upon graduation. Originally from Short Hills, New Jersey, Jai is a die-hard Yankee fan #ChaseFor28. You can find more information about Jai's experiences on his [Linkedin](https://www.linkedin.com/in/jai-bansal-ba1b79178/). If you want to chat about anything, including opportunities, this project, or just baseball, please feel free to reach out at jai.k.bansal@vanderbilt.edu. 

## Citations
https://www.bettingpros.com/mlb/futures-picks/over-under/

https://fivethirtyeight.com/

https://www.statisticshowto.com/brier-score/

https://en.wikipedia.org/wiki/Elo_rating_system

