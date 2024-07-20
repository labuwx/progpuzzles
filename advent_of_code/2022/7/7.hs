#!/usr/bin/env runhaskell

{-# OPTIONS -Wno-x-partial #-}

import Data.Char
import Data.List
import Data.List.Split
import Text.Printf


data Token = T_CD String | T_CDBack | T_LS | T_LSODir String | T_LSOFile String Int
    deriving (Eq, Show)
data LSO = LSODir String | LSOFile String Int
    deriving (Eq, Show)
data Command = CD String | CDBack | LS [LSO]
    deriving (Eq, Show)
data FSO = File String Int | Dir String [FSO]
    deriving (Eq, Show)


trim :: String -> String
trim = dropWhileEnd isSpace . dropWhile isSpace


spanJust :: [a] -> (a -> Maybe b) -> ([b], [a])
spanJust [] _ = ([], [])
spanJust (x : xs) f = case f x of
    Nothing -> ([], x : xs)
    Just y -> let (ys, xss) = spanJust xs f in (y : ys, xss)


tokenize :: String -> [Token]
tokenize s = map (tokLine . words) (lines . trim $ s)
  where
    tokLine ["$", "cd", ".."] = T_CDBack
    tokLine ["$", "cd", name] = T_CD name
    tokLine ["$", "ls"] = T_LS
    tokLine ["dir", name] = T_LSODir name
    tokLine [size, name] = T_LSOFile name (read size)


parse :: [Token] -> [Command]
parse [] = []
parse (T_CDBack : ts) = CDBack : parse ts
parse (T_CD name : ts) = CD name : parse ts
parse (T_LS : ts) = LS ts_ls : parse ts_rest
  where
    parseLS (T_LSODir name) = Just (LSODir name)
    parseLS (T_LSOFile name size) = Just (LSOFile name size)
    parseLS _ = Nothing
    (ts_ls, ts_rest) = spanJust ts parseLS


buildFS :: [Command] -> FSO
buildFS = fst . buildFS'
  where
    consumeDirCmds :: [Command] -> ([FSO], [Command])
    consumeDirCmds [] = ([], [])
    consumeDirCmds (CDBack : cmds) = ([], cmds)
    consumeDirCmds cmds = (subdir : subdirs, cmds'')
      where
        (subdir, cmds') = buildFS' cmds
        (subdirs, cmds'') = consumeDirCmds cmds'

    buildFS' :: [Command] -> (FSO, [Command])
    buildFS' ((CD dirname) : (LS content) : cmds) = (Dir dirname (cntFiles ++ cntDirs), cmdRest)
      where
        cntFiles = [File filename size | (LSOFile filename size) <- content]
        (cntDirs, cmdRest) = consumeDirCmds cmds


calcSize :: FSO -> (Int, Int, [Int])
calcSize (File _ size) = (size, 0, [])
calcSize (Dir _ content) = (size, csize + if size <= 100000 then size else 0, size : sizeL)
  where
    contSize = map calcSize content
    size = sum [size | (size, _, _) <- contSize]
    csize = sum [csize | (_, csize, _) <- contSize]
    sizeL = concat [subSizeL | (_, _, subSizeL) <- contSize]


main = do
    content <- readFile "input"
    -- content <- readFile "input_test"

    let tokens = tokenize content
    let commands = parse tokens
    let fs = buildFS commands
    let (totalSize, underLimitSum, sizes) = calcSize fs

    let s1 = underLimitSum

    let spaceNeeded = 30000000 - (70000000 - totalSize)
    let s2 = minimum [size | size <- sizes, size >= spaceNeeded]

    printf "%d\n%d\n" s1 s2
