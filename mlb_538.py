#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 13:51:41 2020

@author: jaibansal
"""
#%%
import pandas as pd
import numpy as np
import math
#%%
def computeOverallCorrect(dataframe,CorrectPrediction):
    return dataframe[CorrectPrediction].sum() / len(dataframe.index)
#%%
def computeBrierScore(dataframe,SquareError):
    return dataframe[SquareError].sum() / len(dataframe.index)
#%%
def analyzeCorrect_Reference(dataframe,Prediction,team1Projection,team2Projection,Winner,Correct):
    dataframe[Prediction] = np.where(dataframe[team1Projection] > dataframe[team2Projection],1,0)
    dataframe[Correct] = np.where(dataframe[Prediction] == dataframe[Winner],1,0)
#%%
def analyzeCorrect_538(dataframe,Prediction,Rating,Correct,Winner):
     dataframe[Prediction] = np.where(dataframe[Rating]>=0.5,1,0)
     dataframe[Correct] = np.where(dataframe[Winner]==dataframe[Prediction],1,0)
#%%
def analyzeError(dataframe,Error,Rating,Winner):
    dataframe[Error] = (dataframe[Winner] - dataframe[Rating]) **2
#%%
def printResults(correct_538,correct_Reference,brier_538,brier_Reference,BSS):
    print("538 Correct Winner: " + str(round(correct_538 * 100,2))+"%")
    print("538 Brier Score: " + str(round(brier_538,2)))
    print("Reference Correct Winner: "+ str(round(correct_Reference*100,2))+"%")
    print("Reference Brier Score: " + str(round(brier_Reference,2)))
    print("538 Brier Skilled Score: " + str(round(BSS,2)))
#%%
mlb2020 = pd.read_csv("mlb_elo_latest.csv")
#%%
mlb2020 ['Team 1 Winner'] =  np.where(mlb2020['score1'] > mlb2020['score2'],1,0)
#%%
analyzeCorrect_538(mlb2020, '538 Predicted Winner','rating_prob1','538 Correct', 'Team 1 Winner')
analyzeError(mlb2020, '538 Squared Error','rating_prob1','Team 1 Winner')
#%%
overallCorrect_538 = computeOverallCorrect(mlb2020,'538 Correct')
brierScore_538 = computeBrierScore(mlb2020,'538 Squared Error')
#%%
analyzeCorrect_Reference(mlb2020,'Reference Predicted Winner','team1_Avg_Proj','team2_Avg_Proj','Team 1 Winner', 'Reference Correct')
#%%
analyzeError(mlb2020,'Reference Squared Error','Reference Predicted Winner','Team 1 Winner')
#%%
overallCorrect_Reference = computeOverallCorrect(mlb2020,'Reference Correct')
brierScore_Reference = computeBrierScore(mlb2020,'Reference Squared Error')
#%%
brierSkillScore = 1 - brierScore_538/brierScore_Reference
#%%
printResults(overallCorrect_538, overallCorrect_Reference, brierScore_538, brierScore_Reference, brierSkillScore)
#%%

   