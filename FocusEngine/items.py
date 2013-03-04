from scrapy.item import Item, Field

class FocusItem(Item):
    """Basic way to memorize field
    """
    title = Field()
    link = Field()
    text = Field()
    image = Field()
    worlds = Field()
    
