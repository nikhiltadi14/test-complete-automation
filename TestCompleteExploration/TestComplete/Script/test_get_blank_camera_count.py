from drag_and_drop_camera_page import *
from get_blank_camera_count_page import *

def TestCameraCount():
  launch_application()
  verify_signin_page_is_displayed()
  login_into_application(Project.Variables.Username,Project.Variables.Password)
  verify_user_successfully_logged_into_account()
  ''''
  wait_for_the_cameras_to_load()
  verify_25_camera_panel_is_displayed()
  click_on_25_camera_panel()
  get_total_blank_camera_count()
  logout_from_application()
  close_application()
  '''
  