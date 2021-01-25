# Welcome to DTBcreate

Contact: lm@contestsoftware.com

DTBcreate is to convert different types of database files such as
 - FCC databases (list of U.S. radio amateurs)
 - CRTC databases (list of Canadian radio amateurs)
 - any space delimited ASCII text file
to a binary Win-Test database file (DTB).

## Input files
Please note: These information may change fast. Please take it with care.

### FCC database
 - Upon 2020, FCC database files were available at _http://wireless.fcc.gov/uls/data/complete/l_amat.zip_
 - Since 2021: _ftp://wirelessftp.fcc.gov/pub/uls/complete/l_amat.zip_

By default, the only file of interest is the _EN.dat_. The columns of this file are separated by '|' characters. The columns of interest are
 - Call sign between 4th and 5th "|" and
 - State between 17th und 18th "|"

This file ist structured like this (first two lines of EN.dat as example):
<pre>
EN|215000|||AA0A|L|L00209566|MC CARTHY, DENNIS J|DENNIS|J|MC CARTHY|||||5022 LANSDOWNE AVE|SAINT LOUIS|MO|63109|||000|0002274249|I|||
EN|215001|||AA0AA|L|L00196154|MONKS, WILLIAM S|WILLIAM|S|MONKS|||||3258 TAMU|College Station|TX|77843||c/o Gil Rosenthal, Dept of Biology|000|0002268431|I|||
</pre>

### CRTC database
Upon 2010, the default database file was called amateur.rpt, it could be loaded as a ZIP file using _wget_ from here:
_wget -c --no-passive-ftp ftp://ftp.rac.ca/pub/cdncaldb.zip_

From 2011 on, the database name is amateur.txt as part of a ZIP file:
 - 2011 the way to get it was with the following link: _http://205.236.99.41/%7Eindicatif/download/amateur.zip_
 - From 2012 on (at least upon 2021) the following link worked: _http://apc-cap.ic.gc.ca/datafiles/amateur.zip_

It's a plain ASCI text file, too. Each record (= line) is in the following format:
<pre>
 FIELD                    STARTING COLUMN   LENGTH
 ~~~~~                    ~~~~~~~~~~~~~~~   ~~~~~~
 Callsign                               1        6
 Given Names                            8       35
 Surname                               44       35
 Street Address                        80       70
 City                                 151       35
 Province                             187        2
 Postal/ZIP Code                      190       10
 BASIC Qualification (A)              201        1
 5WPM Qualification (B)               203        1
 12WPM Qualification (C)              205        1
 ADVANCED Qualification (D)           207        1
 Club Name (field 1)                  211       70
 Club Name (field 2)                  282       70
 Club Address                         353       70
 Club City                            424       35
 Club Province                        460        2
 Club Postal/ZIP Code                 463        7
</pre>
DTBcreate reads only callsign from column 1 (length 6) and province column 187 (length 2). If there's no province avaliable at column 187, the tool has another try at column 460.

There's a special treatment of stations from NL (VO1/VO2):
 - Treat VO1 in NL as NF
 - Treat VO2 in NL as LB

Example record from amateur.rpt:
<pre>
VA1AA  Bill                                McFadden                            188 MILLWOOD DRIVE                                                     LOWER SACKVILLE                     NS B4E 2X8    A B   D
</pre>
### Space delimited text file
Any tabular text file with the format "Call Number" can be converted to a Win-Test DTB.
Examples:
 - A line "DK9VZ F27" will create a DTB entry with callsign=DK9VZ and number=F27.
 - A line "DL2ARD X28 Z88" will create a DTB entry with callsign=DL2ARD and number=X28.
