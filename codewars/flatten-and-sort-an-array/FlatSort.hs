module FlatSort where

import Data.List

flat :: [[Int]] -> [Int]
flat [] = []
flat (x:xs) = x ++ flat xs

msort :: [Int] -> [Int]
msort [] = []
msort (x:xs) = (msort lesser) ++ [x] ++ (msort greater)
    where
        lesser = filter (< x) xs
        greater = filter (>= x) xs

unique :: (Eq a) => [a] -> [a]
unique [] = []
unique [x] = [x]
unique (x:y:xs) = (if x == y then [] else [x]) ++ (unique (y:xs))

flatSort l = (unique . msort . flat) l
