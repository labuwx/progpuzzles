-- | Main entry point to the application.
module Main where

import Data.List

fact 0 = 1
fact x = x*fact(x-1)


perm _ [x] = [x]
perm k l = l !! m : perm (k' `rem` fact (n-1))  (delete (l !! m) l)
    where
        n = length l
        k' = k `rem` fact n
        m = k `div` fact (n-1)


-- | The main entry point.
main :: IO ()
main = print $ foldl (\acc x -> acc ++ show x) "" (perm 999999 [0..9])

