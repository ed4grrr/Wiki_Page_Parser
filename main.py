# This is a sample Python script.
import bs4
import requests

from RS3_Wiki_Page_Parser import RS3_Wiki_Page_Parser
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test = RS3_Wiki_Page_Parser()
    test.get_page_info("https://runescape.wiki/w/Category:Grand_Exchange_items_that_can_be_bought_by_ironmen")
    test.get_elements_with_class("mw-category-generated")
    test.get_GE_prices(1000000)
    test.print_results()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
