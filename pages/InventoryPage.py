

class InventoryPage:

    def __init__(self, page):
        self.page = page
        self._products_header = page.locator("[data-test=\"title\"]")


    @property
    def products_header(self):
        # I get a recursion error when I use this, skipping for now.
        return self.products_header
