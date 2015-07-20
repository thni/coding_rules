#!/usr/bin/python

for sourceFileName in vera.getSourceFileNames():
  if( not sourceFileName.islower() ):
    print("Source filename must be lowercase")
