from chrome import ChromeHtmlToPdf

c = ChromeHtmlToPdf('https://google.com/', output_path='/home/ubuntu/workspace/out.pdf', verbose=True)
c.render()