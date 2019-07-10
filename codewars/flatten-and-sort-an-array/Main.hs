module Main where
-- Tests can be written using Hspec http://hspec.github.io/
-- Replace this with your own tests.

import Test.Hspec
import FlatSort
import Test.QuickCheck
import Data.List (sort,concat)

-- `spec` of type `Spec` must exist
spec :: Spec
spec = do
    describe "flattens and sorts" $ do
        it "some specs" $ do
        flatSort [[], []] `shouldBe`  []
        flatSort [[], [1]] `shouldBe` [1]
        flatSort [[], [], [], [2], [], [1]] `shouldBe` [1, 2]
    describe "and randoms as well" $ do  
        it "randoms " $ property $
          \x -> flatSort x == (sort.concat) x

-- the following line is optional for 8.2
main = hspec spec
--main = do
    --let res = flatSort [[0, 0]]
    --(putStrLn.show) res
