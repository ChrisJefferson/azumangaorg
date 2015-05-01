#!/bin/bash

rm -rf coverout
mkdir coverout

echo 'Read(Filename( DirectoriesLibrary( "tst" ), "testinstall.g" ) ); Read(Filename( DirectoriesLibrary( "tst" ), "testall.g" ) ); UnprofileLineByLine(); FORCE_QUIT_GAP(0);' | gap --cover cover.gz
