module Main where

import Data.List
import Data.Ord



isprime :: Int -> Bool
isprime n = (not $ any  (\k -> n `rem` k == 0) [2..n-1]) && not ( n<=1 )

count :: (Int, Int) -> Int -> Int
count (a,b) n
    | isprime (n*n+a*n+b) = 1 + count (a,b) (n+1)
    | otherwise = 0


-- | The main entry point.
main :: IO ()
main = print (maximumBy (comparing snd) [(a*b, count (a,b) 0) | a <- [-999..999], b <- [-999..999] ])
