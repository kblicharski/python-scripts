#
# Generate a valid xml file at /tmp/vulnerable-countries.xml.
# It should contain a list of country nodes attached to a root node
# that have name attributes, the third node should be Panama.
#


from xml.etree import import ElementTree, cElementTree
from xml.dom import import minidom

root = ElementTree.Element('root')

child1 = ElementTree.SubElement(root, 'country', {'name': 'Poland'})
child2 = ElementTree.SubElement(root, 'country', {'name': 'Canada'})
child3 = ElementTree.SubElement(root, 'country', {'name': 'Panama'})

print ElementTree.tostring(root)
tree = cElementTree.ElementTree(root) # wrap it in an ElementTree instance, and save as XML

t = minidom.parseString(ElementTree.tostring(root)).toprettyxml() # Since ElementTree write() has no pretty printing support, used minidom to beautify the xml.
tree1 = ElementTree.ElementTree(ElementTree.fromstring(t))

tree1.write("/tmp/vulnerable-countries.xml",encoding='utf-8', xml_declaration=True)
