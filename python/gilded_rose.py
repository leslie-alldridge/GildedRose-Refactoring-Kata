# -*- coding: utf-8 -*-

class GildedRose(object):

    backstage_passes = "Backstage passes to a TAFKAL80ETC concert"
    aged_brie = "Aged Brie"

    def __init__(self, items):
        self.items = items

    def adjust_quality(self, item, rate):
        """
        Adjust the quality of an item, defaults to -1
        Quality cannot be less than 0 or bumped beyond 50
        """
        item.quality += rate
        # Clamp method - not available in Python
        item.quality = max(min(item.quality, 50), 0)

    def update_quality(self):
        for item in self.items:
            
            item.sell_in -= 1
            rate = -1 if item.sell_in >= 0 else -2

            match item.name:
                case self.aged_brie:
                    rate = abs(rate)
                case item.name if "Conjured" in item.name:
                    rate *= 2
                case self.backstage_passes:
                    if 5 <= item.sell_in <= 10:
                        rate = 2
                    elif 0 <= item.sell_in <= 5:
                        rate = 3
                    else:
                        rate = 1 if item.sell_in >= 0 else -item.quality
                case item.name if "Sulfuras" in item.name:
                    return
                case _:
                    return self.adjust_quality(item, rate)

            return self.adjust_quality(item, rate)
            

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
