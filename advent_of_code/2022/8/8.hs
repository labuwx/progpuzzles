#!/usr/bin/env runhaskell

{-# OPTIONS -Wno-x-partial #-}
{-# LANGUAGE LambdaCase #-}

import Control.Monad
import qualified Control.Monad.Trans.State as State
import Data.Char
import Data.Functor
import Data.List
import Data.List.Split
import qualified Data.Map as Map
import qualified Data.Set as Set
import Text.Printf


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


takeWhile1 :: (a -> Bool) -> [a] -> [a]
takeWhile1 _ [] = []
takeWhile1 p (x : xs) = if p x then x : takeWhile1 p xs else [x]


type UID = Int


parseForest :: String -> [[Int]]
parseForest = map (map (\c -> read [c])) . lines . trim


forest2Grid :: [[Int]] -> (Int, Int, Map.Map (Int, Int) Int)
forest2Grid fl = (w, h, pGrid Map.empty 1 1 fl)
  where
    h = length fl
    w = length $ head fl
    pGrid :: Map.Map (Int, Int) Int -> Int -> Int -> [[Int]] -> Map.Map (Int, Int) Int
    pGrid m _ _ [] = m
    pGrid m _ y ([] : rs) = pGrid m 1 (y + 1) rs
    pGrid m x y ((c : cs) : rs) = pGrid (Map.insert (x, y) c m) (x + 1) y (cs : rs)


addLabel :: [[Int]] -> [[(UID, Int)]]
addLabel forest = State.evalState (addLabel' forest) 0
  where
    freshLabel :: State.State UID UID
    freshLabel = do
        k <- State.get
        State.put (k + 1)
        return k

    addLabel' :: [[Int]] -> State.State UID [[(UID, Int)]]
    addLabel' =
        mapM
            ( mapM
                ( \x -> do
                    k <- freshLabel
                    return (k, x)
                )
            )


type VisState = State.State (Set.Set UID)


countVisible :: [[Int]] -> Int
countVisible forest =
    flip State.evalState Set.empty $
        ( do
            let lForest = addLabel forest

            markVisible lForest
            markVisible $ map reverse lForest
            markVisible $ transpose lForest
            markVisible $ transpose $ reverse lForest

            Set.size <$> State.get
        )
  where
    markVisible :: [[(UID, Int)]] -> VisState ()
    markVisible = mapM_ (markVisibleRow (-1))

    markVisibleRow :: Int -> [(UID, Int)] -> VisState ()
    markVisibleRow _ [] = return ()
    markVisibleRow prev ((label, x) : xs) = do
        markVisibleRow (max prev x) xs
        if x > prev
            then State.modify $ Set.insert label
            else return ()


scoreForest :: (Int, Int, Map.Map (Int, Int) Int) -> Int
scoreForest (w, h, fGrid) = maximum [scoreTree x y | x <- [1 .. w], y <- [1 .. h]]
  where
    scoreTree x y = product $ map (length . takeWhile1 (< Map.lookup (x, y) fGrid)) nbrl
      where
        nbrl =
            [ [Map.lookup (xx, y) fGrid | xx <- [x + 1 .. w]]
            , [Map.lookup (xx, y) fGrid | xx <- [x - 1, x - 2 .. 1]]
            , [Map.lookup (x, yy) fGrid | yy <- [y + 1 .. h]]
            , [Map.lookup (x, yy) fGrid | yy <- [y - 1, y - 2 .. 1]]
            ]


main = do
    content <- readFile "input"
    -- content <- readFile "input_test"
    let forest = parseForest content
    let fGrid = forest2Grid forest

    let s1 = countVisible forest
    let s2 = scoreForest fGrid

    print s1
    print s2
