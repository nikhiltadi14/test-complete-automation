from drag_and_drop_camera_page import *
from main_window_search_page import *

def TestSearchResults():
  server_name = "POC_View1"
  
  launch_application()
  verify_signin_page_is_displayed()
  login_into_application(Project.Variables.Username,Project.Variables.Password)
  verify_user_successfully_logged_into_account()
  wait_for_the_cameras_to_load()
  click_on_filter_option()
  verify_filter_option_is_displayed()
  search_for_server(server_name)
  verify_search_server_name_is_displayed(server_name)
  logout_from_application()
  close_application()
  