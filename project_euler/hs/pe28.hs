-- | Main entry point to the application.
module Main where

-- | The main entry point.
main :: IO ()
main = print ((-1502999) + 4*sum ( map (^2) [3,5..1001]))

