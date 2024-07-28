#!/usr/bin/env runhaskell

{-# OPTIONS -Wno-x-partial #-}

import Control.Monad
import qualified Control.Monad.Trans.State as State
import Data.Char
import Data.Functor
import Data.List
import Data.List.Split
import qualified Data.Set as Set
import Text.Printf


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


type UID = Int


parseForest :: String -> [[Int]]
parseForest = map (map (\c -> read [c])) . lines . trim


addLabel :: [[Int]] -> [[(UID, Int)]]
addLabel = snd . addLabel' 0
  where
    addLabel' :: UID -> [[Int]] -> (Int, [[(UID, Int)]])
    addLabel' k [] = (k, [])
    addLabel' k (r : rs) = (k'', (rLabeled : rsLabeled))
      where
        (k', rLabeled) = addLabelRow k r
        (k'', rsLabeled) = addLabel' k' rs
    addLabelRow :: UID -> [Int] -> (Int, [(UID, Int)])
    addLabelRow k [] = (k, [])
    addLabelRow k (x : xs) = (k', (k, x) : xsLabeled)
      where
        (k', xsLabeled) = addLabelRow (k + 1) xs


addLabelM :: [[Int]] -> [[(UID, Int)]]
addLabelM forest = State.evalState (addLabel' forest) 0
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


countVisible :: [[Int]] -> Int
countVisible forest = Set.size visible4
  where
    markVisible :: Set.Set UID -> [[(UID, Int)]] -> Set.Set UID
    markVisible s [] = s
    markVisible s (r : rs) = markVisible (markVisibleRow s r (-1)) rs

    markVisibleRow :: Set.Set UID -> [(UID, Int)] -> Int -> Set.Set UID
    markVisibleRow s [] _ = s
    markVisibleRow s ((label, x) : xs) prev = markVisibleRow (if x > prev then Set.insert label s else s) xs (max prev x)

    lForest = addLabel forest
    visible0 = Set.empty :: Set.Set UID
    visible1 = markVisible visible0 lForest
    visible2 = markVisible visible1 $ map reverse lForest
    visible3 = markVisible visible2 $ transpose lForest
    visible4 = markVisible visible3 $ transpose $ reverse lForest


type VisState = State.State (Set.Set UID)


countVisibleM :: [[Int]] -> Int
countVisibleM forest = State.evalState countVisibleM' Set.empty
  where
    countVisibleM' :: VisState Int
    countVisibleM' = do
        let lForest = addLabelM forest
        markVisible lForest
        markVisible $ map reverse lForest
        markVisible $ transpose lForest
        markVisible $ transpose $ reverse lForest
        Set.size <$> State.get

    markVisible :: [[(UID, Int)]] -> VisState ()
    markVisible = mapM_ (markVisibleRow (-1))

    markVisibleRow :: Int -> [(UID, Int)] -> VisState ()
    markVisibleRow _ [] = return ()
    markVisibleRow prev ((label, x) : xs) = do
        markVisibleRow (max prev x) xs
        if x > prev
            then State.modify $ Set.insert label
            else return ()


main = do
    content <- readFile "input"
    -- content <- readFile "input_test"
    let forest = parseForest content

    let s1 = countVisible forest
    let s1M = countVisibleM forest
    let s2 = 0 :: Int

    printf "%d %d\n%d\n" s1 s1M s2
