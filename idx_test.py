class CategoryTree:

    def __init__(self):
        """
        Initialize a CategoryTree with an empty dict.
        """
        self.categories = {}

    def add_category(self, category, parent):
        """
        Add a category if it satisfies the validity criteria.
        """
        if not self._valid_category(category, parent):
            raise KeyError
        self.categories[category] = parent 

    def get_children(self, parent):
        """
        Add the children of the query parent value.

        Runs in O(n) time where n is the number of categories.
        """
        children = []
        for category, category_parent in self.categories.items():
            if category_parent == parent:
                children.append(category)
        return children

    def _valid_category(self, category, parent):
        """
        Verify that categories are valid.

        Checks that categories are unique and verifies that they are
        either root categories or have an existing parent.
        """
        return (category not in self.categories)\
                and (parent in self.categories or parent is None)

c = CategoryTree()
c.add_category('A', None)
c.add_category('B', 'A')
c.add_category('C', 'A')
print(','.join(c.get_children('A') or []))

