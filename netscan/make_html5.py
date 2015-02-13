#!/usr/bin/python


class WebPage:
	def __init__(self):
		self.page = []
		
	# Note: this auto refreshes every 300 seconds.
	def create(self,html_body,title='Web Page'):
		html_start = """
		<!DOCTYPE html>
		<html>
		  <head>
			<link href="http://maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css" rel="stylesheet">
			<title>title</title>
			<meta charset="utf-8">
			<meta http-equiv="refresh" content="300">
		  </head>
		  <body>
		"""
		
		html_end = """	
		  </body>
		</html>
		"""
		
		page = []
		page.append(html_start)
		page.append(html_body)
		page.append(html_end)
		
		self.page = page
	
	def savePage(self,filename):
		f = open(filename,'w')
		for i in self.page:
			f.write(i)
		f.close()
		
	# Expect a list containing lines of html which will create a Google Map	
	def printPage(self):
		for i in self.page:
			print i


def main():
	page = WebPage()
	page.create('hello world!','LAN Host Map')
	page.savePage('test.html')
	

if __name__ == "__main__":
	main()