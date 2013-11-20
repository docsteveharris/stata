## Revision Log

- 131120: there is a package by Andrew Heiss at https://github.com/andrewheiss/SublimeStata13 which works for Stata 13
- 131120: updated: now works with Stata 12: Note you *must* go to Preferences>Do-file editor>Advanced and uncheck the box which says "Edit do-files opened from the Finder in Do-file Editor" 

##   Syntax highlighting for Stata in Sublime text

This is a hacked version of the textmate bundle from http://bylr.net/3/2010/10/stata-bundle-for-textmate/.

There are a few modifications
- compound quotes are supported
- digits are highlighted

## Commands

There are also two commands to send code to stata from sublime text. Both work by creating a temporary file in your current working directory (otherwise references within the code that depend on relative paths would fail).

- do file (bound to ctrl-command-r)
- do selected text (bound to ctrl-shift-r) - and if there is no text selected then it will send the current line

## Known issues

- the commands are mac specific (they depend on osascript)
- double forward slash doesn't work as a comment marker at the beginning of a line

Hope it might be useful.
