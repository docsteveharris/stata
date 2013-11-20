import os
import sublime_plugin
import sublime

class file_2_stataCommand(sublime_plugin.TextCommand):
    """ copy buffer to temp file and send to stata """

    def run(self, edit):
        #  get path to current directory
        filename = self.view.file_name()
        # print(filename)
        # print("So far, so good")
        filepath = os.path.dirname(filename)

        #  grab the buffer
        region = sublime.Region(0, self.view.size())
        # print "%r" % region
        all_text =  self.view.substr(region)
        # Now prepend the file path
        # so the first thing stata does is to change to the working directory
        all_text = '''qui cd "''' + filepath + '''"\n ''' + all_text
        print(all_text)


        #  write the buffer to file in pwd
        dofile_path = os.path.join(filepath, 'sublime2stata.do')
        # print "%r" % dofile_path
        this_file = open(dofile_path,'w')
        this_file.write(all_text)
        this_file.close()

        cmd = """osascript<< END
         tell application "Finder"
          open POSIX file "%s"
         end tell
        END""" % dofile_path
        os.system(cmd)

