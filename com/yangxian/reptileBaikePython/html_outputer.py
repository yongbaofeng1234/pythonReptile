class HtmlOutputer():
    def __init__(self):
        self.datas=[]
    
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    
    def output_html(self):
        fileout=open('output.html','w')
        fileout.write("<html>")
        fileout.write("<body>")
        fileout.write("<table>")
        fileout.write("<tr>")
        fileout.write("<td>URL</td>")
        fileout.write("<td>Title</td>")
        fileout.write("<td>Summary</td>")
        fileout.write("<tr>")
        # code:ascii
        for data in self.datas:
            fileout.write("<tr>")
            fileout.write("<td>%s</td>" %data['url'])
            fileout.write("<td>%s</td>" %data['title'].encode('utf-8'))
            fileout.write("<td>%s</td>" %data['summary'].encode('utf-8'))
            fileout.write("<tr>")
        fileout.write("</table>")
        fileout.write("</body>")
        fileout.write("</html>") 
        fileout.close()