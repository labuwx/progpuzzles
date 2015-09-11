module Main where

import Data.Array

divsum :: Int -> Int
divsum n = sum [k | k <- [1..n-1], 0 == (n `mod` k)]

isab :: Int -> Bool
isab n = n < divsum n

m=28124

abundsArray = listArray (1,m) $ map isab [1..m]
abunds = filter (abundsArray !) [1..m]

rests x = map (x-) $ takeWhile (<= x `div` 2) abunds
isSum = any (abundsArray !) . rests



-- | The main entry point.
main :: IO ()
main = print . sum . filter (not . isSum) $ [1..m]
