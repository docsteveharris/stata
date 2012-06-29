import os
import sublime_plugin
import sublime

class text_2_stataCommand(sublime_plugin.TextCommand):
	""" copy SELECTION to temp file and send to stata """

	def run(self, edit):
		#  get path to current directory
		filename = self.view.file_name()
		filepath = os.path.dirname(filename)

		#  grab the buffer
		#  if nothing selected then send the line
		all_text = ""
		sels = self.view.sel()
		for sel in sels:
			all_text = all_text + self.view.substr(sel)
		if len(all_text) == 0:
			all_text = self.view.substr(self.view.line(sel)) 
		all_text = all_text + "\n"

		#  write the buffer to file in pwd
		dofile_path = os.path.join(filepath, 'sublime2stata.do')
		print "%r" % dofile_path
		this_file = open(dofile_path,'w')
		this_file.write(all_text)
		this_file.close()

		#  now call the file using osascript
		cmd = """osascript<< END
		 tell application "stata" 
			activate
			open POSIX file "%s"
		 end tell
		 END""" % dofile_path
		print cmd
		os.system(cmd)