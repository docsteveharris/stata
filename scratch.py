import subprocess
from appscript import app, mactypes

SCRIPT = """/usr/bin/osascript<<END
tell app "Stata"
activate
open POSIX file "~/code/stata/sublime2stata.do"
end tell
END"""

subprocess.Popen(SCRIPT,shell=True)