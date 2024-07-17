#!/usr/bin/env runhaskell

{-# OPTIONS -Wno-x-partial #-}

import Data.Char
import Data.List
import Data.List.Split
import qualified Data.Set as Set
import Text.Printf


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


getSOx :: Int -> String -> Int
getSOx n = getSOx' n
  where
    getSOx' offset cs = if nUnique == n then offset else getSOx' (offset + 1) (drop 1 cs)
      where
        window = take n cs
        nUnique = Set.size $ Set.fromList window


main = do
    content <- readFile "input"
    -- content <- readFile "input_test"
    let signal = trim content

    let s1 = getSOx 4 signal
    let s2 = getSOx 14 signal

    printf "%d\n%d\n" s1 s2
