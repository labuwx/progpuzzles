#!/usr/bin/env runhaskell

{-# OPTIONS -Wno-x-partial #-}

import Data.Char
import Data.List
import Data.List.Split
import qualified Data.Map as Map
import Text.Printf


type Label = Char
type Op = (Integer, Label, Label)
type Stacks = Map.Map Label [Char]


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


parseShip :: String -> ([Label], Stacks)
parseShip ship_raw = (map fst sss, Map.fromList sss)
  where
    isStackLine "" = False
    isStackLine (c : _) = isDigit c
    ucons (x : xs) = (x, xs)
    ss = map ucons $ filter isStackLine $ map trim $ transpose $ reverse $ lines ship_raw
    sss = [(k, reverse v) | (k, v) <- ss]


parseOp :: String -> Op
parseOp s = (read x, head y, head z)
  where
    [_, x, _, y, _, z] = splitOn " " s


doOps :: [Op] -> Bool -> Stacks -> Stacks
doOps [] _ stacks = stacks
doOps ((n, from, to) : ops) revStack stacks = doOps ops revStack stacks''
  where
    (cs, cs_from) = splitAt (fromIntegral n) (stacks Map.! from)
    stacks' = Map.adjust (\_ -> cs_from) from stacks
    stacks'' = Map.adjust (\cs_to -> (if revStack then cs else reverse cs) ++ cs_to) to stacks'


stackTops :: [Label] -> Stacks -> [Char]
stackTops labels stacks = [head (stacks Map.! k) | k <- labels]


main = do
    content <- readFile "input"
    --content <- readFile "input_test"
    let [ship, ops'] = splitOn "\n\n" $ content
    let ops = map parseOp $ lines ops'
    let (labels, stacks) = (parseShip ship)

    let s1 = stackTops labels $ doOps ops False stacks
    let s2 = stackTops labels $ doOps ops True stacks

    printf "%s\n%s\n" s1 s2
