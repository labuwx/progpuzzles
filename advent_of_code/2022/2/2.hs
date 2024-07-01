#!/usr/bin/env runhaskell

import Data.Char (isSpace)
import Data.List
import Text.Printf


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


data Outcome = Lose | Draw | Win
data RPS = Rock | Paper | Scissors deriving (Eq)


instance Ord RPS where
    (<=) Rock Rock = True
    (<=) Paper Paper = True
    (<=) Scissors Scissors = True
    (<=) Rock Paper = True
    (<=) Paper Scissors = True
    (<=) Scissors Rock = True
    (<=) _ _ = False


string2RPS :: String -> RPS
string2RPS "A" = Rock
string2RPS "B" = Paper
string2RPS "C" = Scissors
string2RPS "X" = Rock
string2RPS "Y" = Paper
string2RPS "Z" = Scissors


string2Outcome :: String -> Outcome
string2Outcome "X" = Lose
string2Outcome "Y" = Draw
string2Outcome "Z" = Win


scoreOutcome :: RPS -> RPS -> Integer
scoreOutcome opponent own
    | own < opponent = 0
    | opponent < own = 6
    | otherwise = 3


scoreShape :: RPS -> Integer
scoreShape Rock = 1
scoreShape Paper = 2
scoreShape Scissors = 3


scoreAll :: RPS -> RPS -> Integer
scoreAll opponent own = scoreShape own + scoreOutcome opponent own


findOwn :: RPS -> Outcome -> RPS
findOwn Rock Lose = Scissors
findOwn Rock Draw = Rock
findOwn Rock Win = Paper
findOwn Paper Lose = Rock
findOwn Paper Draw = Paper
findOwn Paper Win = Scissors
findOwn Scissors Lose = Paper
findOwn Scissors Draw = Scissors
findOwn Scissors Win = Rock


main = do
    content <- readFile "input"
    let lc = lines . trim $ content

    let s1 = sum [scoreAll opponent own | [opponent, own] <- map (map string2RPS . words) lc]
    let s2 =
            sum
                [ scoreAll opponent (findOwn opponent outcome)
                | (opponent, outcome) <-
                    [ (string2RPS opponentS, string2Outcome outcomeS)
                    | [opponentS, outcomeS] <- map words lc
                    ]
                ]

    printf "%d\n%d\n" s1 s2
