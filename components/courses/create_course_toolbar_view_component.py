from components.base_component import BaseComponent
from playwright.sync_api import Page, expect
from elements.text import Text
from elements.button import Button

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'create-course-toolbar-title-text', 'Title')
        self.create_course_button = Button(
            page, 'create-course-toolbar-create-course-button', 'Create course'
        )

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Create course')

        self.create_course_button.check_visible()

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_disabled_create_course_button(self):
        self.create_course_button.check_disabled()
