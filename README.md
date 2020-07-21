# Bash-Scripts
These are my Bash Scripts that I use. Some only work with Debian and Debian based distrobutions of Linux.
Some are half-finished. Some don't even work. I just took these strait out of my bin directory.

## Update info
With the first year of this github page being open, I decided to make a rule. I will concider updating
scripts garunteed for 1 calender year. If afterward when I change copyright dates I don't want those
scripts to be included, they will be removed from the release deb file and a script will run to remove
the scripts from your system. If you wish to continue to use these scripts there will be a link provided
to this page where you can download the files and put them in the /usr/local/bin folder.

## What's New?
In version 5.1, we have updates to the Update and Ainstall scripts. Update will now give you the option to
backup the updatelog right from the command line by using the 'update --choice=8' command.
Ainstall will now always store .lastcupout in the /tmp directory so that it will always
be deleted on reboot.


# Licensing
All of these scripts are under the MIT License.

Copyright 2019-2020 Jeremiah Haven

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
