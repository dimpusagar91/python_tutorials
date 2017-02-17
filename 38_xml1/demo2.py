from lxml import etree

xml_snippet = '''<topology>
 <switch id="10">
     <port no="1">h1</port>
     <port no="2">h2</port>
 </switch>

 <tunnel dpid="91">
 <port no="1">s1</port>
 <port no="8">s8</port>
 <port no="2">s2</port>
 <port no="3">s3</port>
 </tunnel>
 </topology>'''

root = etree.fromstring(xml_snippet)

for element in root.iter("*"):
  print element.tag, element.items()
