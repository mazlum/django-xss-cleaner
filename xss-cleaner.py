import re


class XssCleaner:

	#for HTML Context
    def htmlContextCleaner(self, input):
        chars = {
            '<': '&lt;',
            '>': '&gt;'
        }
        for k, v in chars.iteritems():
            input = input.replace(k, v)
        return input

    #for Script Context
    def scriptContextCleaner(self, input):
        chars = {
            "\"" : "&quot;",
            "<": "&lt;",
            "'": "&apos;",
            "\\\\": "&bsol;",
            "%": "&percnt;",
            "&": "&amp;",
        }
        for k, v in chars.iteritems():
            input = input.replace(k, v)
        return input

    #for Attribute Context
    def attributeContextCleaner(self, input):
        chars = {
            "\"": "&quot;",
            "'": "&apos;",
            "`": "&grave;",
        }
        for k, v in chars.iteritems():
            input = input.replace(k, v)
        return input

    #for Style Context
    def styleContextCleaner(self, input):
        chars = {
            "\"": "&quot;",
            "'": "&apos;",
            "``": "&grave;",
            "(": "&lpar;",
            "\\\\": "&bsol;",
            "<": "&lt;",
            "&": "&amp;",
        }
        for k, v in chars.iteritems():
            input = input.replace(k, v)
        return input

    #for URL Context
    def urlContextCleaner(self, url):
        response = re.match("(?:(?:https?|ftp):{1})\/\/[^\"\s\\\\]*.[^\"\s\\\\]*$", url)
        if response != None:
            return response.group()
        else:
            noxss='javascript:void(0)'
            return noxss
