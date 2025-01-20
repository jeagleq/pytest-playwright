from pages.loginPage import LoginPage
from utilities.readConfig import ReadConfig
from logs.customLogger import CustomLogger
import pytest # type: ignore
import allure # type: ignore
from utilities.readConfig import ReadConfig

logger = CustomLogger().get_logger("test_logger")


@pytest.mark.ui
@allure.feature("Login")
@allure.story("Check that state is saved")
def test_login_and_save_state(logged_in_context, record_property):
    logger.info("Starting test 'test_login_and_save_state'")
  
    record_property("Description", "This test checks the save state functionality.") # type: ignore
    assert logged_in_context is not None
    logger.info("Test 'test_login_and_save_state' passed")
    
@pytest.mark.ui
@pytest.mark.regression
@allure.feature("Login")
@allure.story("Successful login using saved state")
def test_login_with_saved_state(page_from_state, record_property):
    record_property("Description", "This test checks the login functionality.") # type: ignore
    logger.info("Starting test 'test_login_with_saved_state'")
    
    page = page_from_state.new_page()
    login_page= LoginPage(page)
    login_page.goto()
    #print(page.context.cookies())
    login_page.wait_for_user()
    actual_title = page.locator("#nameofuser").text_content()
    if actual_title == f"Welcome {ReadConfig.getUsername()}":
        logger.info("Test 'test_login_with_saved_state' passed")
        assert True
    else:
        logger.error('Test "test_login_with_saved_state" failed')
        page.screenshot(path="./Screenshots/test_login_with_saved_state.png", full_page=True)
        assert False
    page.close()


    