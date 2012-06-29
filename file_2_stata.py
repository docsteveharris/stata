import os
import sublime_plugin
import sublime

class file_2_stataCommand(sublime_plugin.TextCommand):
	""" copy buffer to temp file and send to stata """

	def run(self, edit):
		#  get path to current directory
		filename = self.view.file_name()
		filepath = os.path.dirname(filename)

		#  grab the buffer
		region = sublime.Region(0, self.view.size())
		# print "%r" % region
		all_text =  self.view.substr(region)

		#  write the buffer to file in pwd
		dofile_path = os.path.join(filepath, 'sublime2stata.do')
		print "%r" % dofile_path
		this_file = open(dofile_path,'w')
		this_file.write(all_text)
		this_file.close()

		# FIXME: 2012-06-29 - temp file while debugginf
		dofile_path = "~/data/aki/vcode/sublime2stata.do"

		#  now call the file using osascript
		cmd = """osascript<< END
		 tell application "stata" 
			activate
			open POSIX file "%s"
		 end tell
		 END""" % dofile_path
		print cmd
		os.system(cmd)