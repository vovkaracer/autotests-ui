from components.base_component import BaseComponent
from playwright.sync_api import Page, expect

class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = page.get_by_test_id('create-course-toolbar-title-text')
        self.button = page.get_by_test_id('create-course-toolbar-create-course-button')

    def check_visible(self, is_create_course_disabled: bool = True):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Create course')

        expect(self.button).to_be_visible()
        if is_create_course_disabled:
            expect(self.button).to_be_disabled()

        if not is_create_course_disabled:
            expect(self.button).to_be_enabled()

    def click_create_course_button(self):
        self.button.click()

    def check_disabled_create_course_button(self):
        expect(self.button).to_be_disabled()
