from pages.base_page import BasePage
from components.navigation.sidebar_component import SidebarComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from playwright.sync_api import Page, expect

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sidebar = SidebarComponent(page)

        self.navbar = NavbarComponent(page)

        self.empty_view = EmptyViewComponent(page, identifier='courses-list')

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')

        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')

        self.course_menu_button = page.get_by_test_id('course-view-menu-button')
        self.course_edit_menu_button = page.get_by_test_id('course-view-edit-menu-item')
        self.course_delete_menu_button = page.get_by_test_id('course-view-delete-menu-item')

    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')

    def check_visible_empty_view(self):
        self.empty_view.check_visible(
            title='There is no results',
            description='Results from the load test pipeline will be displayed here'
        )

    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_course_card(
            self,
            index: int,
            text: str,
            max_score: str,
            min_score: str,
            estimated_time: str
    ):
        expect(self.course_image.nth(index)).to_be_visible()

        expect(self.course_title.nth(index)).to_be_visible()
        expect(self.course_title.nth(index)).to_have_text(text)

        expect(self.course_max_text.nth(index)).to_be_visible()
        expect(self.course_max_text.nth(index)).to_have_text(f'Max score: {max_score}')

        expect(self.course_min_text.nth(index)).to_be_visible()
        expect(self.course_min_text.nth(index)).to_have_text(f'Min score: {min_score}')

        expect(self.course_estimated_time_text.nth(index)).to_be_visible()
        expect(self.course_estimated_time_text.nth(index)).to_have_text(f'Estimated time: {estimated_time}')

    def click_edit_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_edit_menu_button.nth(index)).to_be_visible()
        self.course_edit_menu_button.nth(index).click()

    def click_delete_course(self, index: int):
        self.course_menu_button.nth(index).click()

        expect(self.course_delete_menu_button.nth(index)).to_be_visible()
        self.course_delete_menu_button.nth(index).click()