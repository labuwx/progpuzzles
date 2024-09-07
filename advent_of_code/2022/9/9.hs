#!/usr/bin/env runhaskell

{-# OPTIONS -Wno-x-partial #-}
{-# LANGUAGE LambdaCase #-}

import Control.Monad
import qualified Control.Monad.Trans.State as State
import Data.Char
import Data.Functor
import Data.List
import Data.List.Split
import qualified Data.Set as Set


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


data Dir = DLeft | DRight | DUp | DDown deriving (Show)
type Mot = (Dir, Int)
type Pos = (Int, Int)


parseInput :: String -> [(Dir, Int)]
parseInput inps =
    map
        (\l -> let [d, k] = words l in (case d of "U" -> DUp; "D" -> DDown; "L" -> DLeft; "R" -> DRight, read k))
        (lines $ trim inps)


pAdd :: Pos -> Pos -> Pos
pAdd (x, y) (dx, dy) = (x + dx, y + dy)


pSub :: Pos -> Pos -> Pos
pSub (x, y) (xx, yy) = (x - xx, y - yy)


dPd :: Dir -> Pos
dPd DUp = (0, 1)
dPd DDown = (0, -1)
dPd DLeft = (-1, 0)
dPd DRight = (1, 0)


type VisState = State.State (Pos, Pos, Set.Set Pos)


countVisited :: [Mot] -> Int
countVisited mots =
    flip State.evalState ((0, 0), (0, 0), Set.singleton (0, 0)) $
        ( do
            simulate mots
            (\(_, _, s) -> Set.size s) <$> State.get
        )
  where
    simulate :: [Mot] -> VisState ()
    simulate [] = return ()
    simulate ((dir, n) : mots) = do
        (hp, tp, tps) <- State.get
        let (hp', tp') = step dir (hp, tp)
        State.put (hp', tp', Set.insert tp' tps)
        simulate (if n > 1 then (dir, n - 1) : mots else mots)

    step :: Dir -> (Pos, Pos) -> (Pos, Pos)
    step dir (hp, tp) = (hp', tp')
      where
        hp' = pAdd hp $ dPd dir
        (dx, dy) = pSub hp' tp
        tp' =
            if abs (dx) <= 1 && abs (dy) <= 1
                then tp
                else pAdd tp (signum dx, signum dy)


main = do
    content <- readFile "input"
    -- content <- readFile "input_test"
    let dirs = parseInput content

    let s1 = countVisited dirs
    let s2 = 0

    print s1
    print s2
