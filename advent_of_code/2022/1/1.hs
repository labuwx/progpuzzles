#!/usr/bin/env runhaskell

import Data.Char (isSpace)
import Data.List
import Text.Printf


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


splitList :: [a] -> ([a], [a])
splitList [] = ([], [])
splitList [x] = ([x], [])
splitList (x : y : xs) = (x : sxs, y : sys)
  where
    (sxs, sys) = splitList xs


merge :: (Ord a) => [a] -> [a] -> [a]
merge [] [] = []
merge xs [] = xs
merge [] ys = ys
merge (x : xs) (y : ys)
    | x > y = x : merge xs (y : ys)
    | otherwise = y : merge (x : xs) ys


mergeSort :: (Ord a) => [a] -> [a]
mergeSort xs
    | ys == [] = []
    | zs == [] = ys
    | otherwise = merge (mergeSort ys) (mergeSort zs)
  where
    (ys, zs) = splitList xs


calcGroups :: [String] -> [Integer]
calcGroups = calcGroupsInner 0
  where
    calcGroupsInner acc [] = [acc]
    calcGroupsInner acc ("" : xs) = acc : (calcGroupsInner 0 xs)
    calcGroupsInner acc (x : xs) = calcGroupsInner (acc + (read x)) xs


main = do
    content <- readFile "input"
    let lc = lines . trim $ content

    let (a : b : c : _) = mergeSort $ calcGroups lc
    let s1 = a
    let s2 = a + b + c

    printf "%d\n%d\n" s1 s2
