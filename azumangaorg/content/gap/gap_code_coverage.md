Title: Line by Line Code Coverage in GAP By Example
Date: 01-05-2015
Modified: 01-05-2015
Category: GAP
Tags: GAP, Profiling, Testing

_This article is not yet finished_

The purpose of this article is to show how to use GAP's new line-by-line profiler / code coverage. We will do this with by looking at looking at how running GAP's test suite, finding some untested code and adding a test. Working through this tutorial would be an excellent way for you to also help extend GAP's test coverage!


Installing
=================

Hopefully in the near future there will be a new release of GAP with line by line profiling built-in (I will hopefully update this page when that happens). For now, you need the latested development version of GAP.

* A working copy of the [latest development version of GAP](https://github.com/gap-system/gap). Be sure to read the documentation to get the packages you will need to get a working basic copy of GAP!

* The [profile package](https://github.com/ChrisJefferson/profiling). To install the package run the following commands from inside GAP's pkg directory.

        :::bash
        git clone https://github.com/ChrisJefferson/profiling
        cd profiling && ./configure && make

  You can check everything is working by starting gap and typing ```LoadPackage("profiling");```.


Now we are ready to do some code coverage and profiling! We do these profiling and code coverage in almost exactly the same way, the difference is (as you might expect) code coverage does not store any information about how long code took to execute, only that it executed at all.


Quickstart Guide
===============

We will start with a quick guide to code coverage, with some brief comments. We will explain later how to do these things in greater depth!

    :::bash
    mkdir outdir # Somewhere to put our output
    gap.sh --cover testcover.gz # Replace gap.sh with however you run gap
    ...
    gap> Read(Filename( DirectoriesLibrary( "tst" ), "testinstall.g" ) ); $ Run GAP's quick test suite, put your own code here
    gap> UnprofileLineByLine(); $ End profiling. At this point we could quit GAP, if we wanted.
    gap> LoadPackage("profiling"); $ We only need the package for reading profiles
    gap> x := ReadLineByLineProfile("testcover.gz");; $ Read profile data back in
    gap> OutputAnnotatedCodeCoverageFiles(x, "outdir"); $ lots of files are put in outdir!


After running this, open ```index.html``` from ```outdir```. Alternatively, you can see a copy of the coverage for all of GAP's tests [here](//gap-test-coverage/latest).

Extended Guide
==============

There is a GAP function, 
