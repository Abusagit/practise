from xml.etree import ElementTree

colours = {'red': 0, 'green': 0, 'blue': 0}
# tree = ElementTree.parse('cubes.xml')
# root = tree.getroot()
# for child in root:
#     print(child.attrib['color'])

"""
class MaxDepth:                     # The target object of the parser
    def __init__(self):
        self.maxDepth = 0
        self.depth = 0

    def start(self, tag, attrib):   # Called for each opening tag.
        self.depth += 1
        if self.depth > self.maxDepth:
            self.maxDepth = self.depth

    def end(self, tag):             # Called for each closing tag.
        self.depth -= 1

    def data(self, data):
        pass    # We do not need to do anything with data.

    def close(self):    # Called when all data has been parsed.
        return self.maxDepth


root = ElementTree.fromstring(input())
print(root)
print(type(root))
# exampleXml = 
# <a>
#     <b>
#     </b>
#     <b>
#         <c>
#             <d>
#             </d>
#         </c>
#     </b>
# </a>
target = MaxDepth()
parser = ElementTree.XMLParser(target=target)
parser.feed(root)
print(parser.close())"""


def finding_depth(branch, x, number=0):
    number += 1
    try:
        for item in branch.findall(x)


# root = ElementTree.fromstring(input())
tree = ElementTree.parse('cubes.xml')
root = tree.getroot()
