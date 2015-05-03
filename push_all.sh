#!/bin/bash
(cd azumangaorg && make clean && make rsync_upload)
(cd azumangafitness && make clean && make rsync_upload)
