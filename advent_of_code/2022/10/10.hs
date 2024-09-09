#!/usr/bin/env runhaskell

{-# OPTIONS -Wno-x-partial #-}

import Data.Char
import Data.List
import Data.List.Split
import qualified Data.Map as Map
import Text.Printf


data Op = NoOp | AddX Int


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


parseOp :: String -> Op
parseOp s = if op == "addx" then AddX (read (args !! 0)) else NoOp
  where
    (op : args) = splitOn " " s


doOps :: [Op] -> [Int]
doOps ops = 1 : doOps' 1 ops
  where
    doOps' _ [] = []
    doOps' x (NoOp : ops) = x : doOps' x ops
    doOps' x (AddX dx : ops) = let x' = x + dx in ([x, x'] ++ doOps' x' ops)


main = do
    content <- readFile "input"
    -- content <- readFile "input_test"
    let ops = map parseOp $ lines $ trim content

    let res = doOps ops
    let s1 = sum [k * x | (k, x) <- zip [1 ..] res, k `elem` [20, 60, 100, 140, 180, 220]]
    let s2 = 0

    print s1
    print s2
