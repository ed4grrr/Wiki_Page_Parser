
import bs4
import requests

from RS3_Wiki_Page_Parser import RS3_Wiki_Page_Parser




if __name__ == '__main__':
    test = RS3_Wiki_Page_Parser()
    test.get_page_info("https://runescape.wiki/w/Category:Grand_Exchange_items_that_can_be_bought_by_ironmen")
    test.get_elements_with_class("mw-category-generated")
    test.get_GE_prices(1000000)
    test.print_and_save_results()

