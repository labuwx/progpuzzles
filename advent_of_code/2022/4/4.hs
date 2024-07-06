#!/usr/bin/env runhaskell

import Data.Char
import Data.List
import Data.List.Split
import Text.Printf


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


parseInp :: String -> ((Integer, Integer), (Integer, Integer))
parseInp s = ((s11, s12), (s21, s22))
  where
    [[s11, s12], [s21, s22]] = (map read . splitOn "-") <$> (splitOn "," s)


checkFullOverlap :: ((Integer, Integer), (Integer, Integer)) -> Bool
checkFullOverlap ((a1, a2), (b1, b2)) = (a1 <= b1 && b2 <= a2) || (b1 <= a1 && a2 <= b2)


checkOverlap :: ((Integer, Integer), (Integer, Integer)) -> Bool
checkOverlap ((a1, a2), (b1, b2)) = (a1 <= b1 && b1 <= a2) || (b1 <= a1 && a1 <= b2)


main = do
    content <- readFile "input"
    -- content <- readFile "input_test"
    let lc = lines . trim $ content
    let lp = map parseInp lc

    let s1 = sum $ map (fromEnum . checkFullOverlap) lp
    let s2 = sum $ map (fromEnum . checkOverlap) lp

    printf "%d\n%d\n" s1 s2
