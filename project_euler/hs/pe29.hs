-- | Main entry point to the application.
module Main where

import Data.List

-- | The main entry point.
main :: IO ()
main = print (length . nub $ [a^b | a <- [2..100], b <- [2..100]])

