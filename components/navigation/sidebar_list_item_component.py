from playwright.sync_api import Page, expect
from components.base_component import BaseComponent
from typing import Pattern
from elements.icon import Icon
from elements.text import Text
from elements.button import Button

class SidebarListItemComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str):
        super().__init__(page)

        self.icon = Icon(page, f'{identifier}-drawer-list-item-icon', 'Icon')
        self.title = Text(page, f'{identifier}-drawer-list-item-title-text', 'Title')
        self.button = Button(page, f'{identifier}-drawer-list-item-button', 'Button')

    def check_visible(self, title: str):
        self.icon.check_visible()

        self.title.check_visible()
        self.title.check_have_text(title)

        self.button.check_visible()

    def navigate(self, expected_url: Pattern[str]):
        self.button.click()
        self.check_current_url(expected_url)