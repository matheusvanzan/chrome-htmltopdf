#!/usr/bin/env python
from subprocess import Popen
from subprocess import PIPE

class ChromeHtmlToPdf():
    
    def __init__(self, url, output_path=None, verbose=False):
        ''' 
        Initialize class with google chrome parameters
        
        Params:
        
        Return:
        
        '''
        
        # Base command
        self.command = 'google-chrome --headless --disable-gpu'
            
        # Set output path
        self.command += ' --print-to-pdf'
        if output_path:
            self.command += '=' + output_path
        
        # Set url
        self.command += ' ' + url
        
        if verbose:
            print self.command
        
    def render(self):
        ''' Actually render html to pdf '''
        try:
            p = Popen(self.command, shell=True, stdout=PIPE, stderr=PIPE, close_fds=True)
            stdout, stderr = p.communicate()
            retcode = p.returncode
            
            if retcode == 0:
                # call was successful
                return
            elif retcode < 0:
                raise Exception("Terminated by signal: ", -retcode)
            else:
                raise Exception(stderr)
        except OSError, exc:
            raise exc