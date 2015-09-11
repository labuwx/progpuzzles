-- | Main entry point to the application.
module Main where

t = 10^999

fib :: Integer -> Integer -> Integer -> Integer
fib a b n
    | b >= t = n
    | otherwise = fib b (a+b) n+1

-- | The main entry point.
main :: IO ()
main = print $ fib 0 1 1

