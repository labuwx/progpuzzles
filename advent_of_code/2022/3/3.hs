#!/usr/bin/env runhaskell

import Data.Char (isSpace, ord)
import Data.List
import Data.List.Split
import qualified Data.Set as Set
import Text.Printf


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


itemPrio :: Char -> Integer
itemPrio c
    | va <= vc && vc <= vz = toInteger (vc - va + 1)
    | vA <= vc && vc <= vZ = toInteger (vc - vA + 27)
  where
    vc = ord c
    va = ord 'a'
    vz = ord 'z'
    vA = ord 'A'
    vZ = ord 'Z'


splitBackpack :: String -> [String]
splitBackpack bp = [part1, part2]
  where
    (part1, part2) = splitAt ((length bp + 1) `div` 2) bp


findCommon :: [String] -> Char
findCommon sl = Set.elemAt 0 $ foldl Set.intersection allChars $ map (Set.fromList) sl
  where
    allChars = Set.fromList "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"


main = do
    content <- readFile "input"
    let lc = lines . trim $ content

    let s1 = sum $ map (itemPrio . findCommon . splitBackpack) lc
    let s2 = sum $ map (itemPrio . findCommon) $ chunksOf 3 lc

    printf "%d\n%d\n" s1 s2
