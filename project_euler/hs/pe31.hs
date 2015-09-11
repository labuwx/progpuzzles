-- | Main entry point to the application.
module Main where

import Data.List


pay :: [Int] -> Int -> Int
pay [x] c
    | c `rem` x == 0 = 1
    | otherwise = 0
pay (x:xs) c = sum $ map (\a -> (pay xs (c-a*x))) (takeWhile (\a -> c-a*x >= 0) [0..])

-- | The main entry point.
main :: IO ()
main = print (pay [1,2,5,10,20,50,100,200] 200)
