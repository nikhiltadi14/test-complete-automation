from drag_and_drop_camera_page import *
from delete_user_page import *

def TestDeleteUser():
  username = "suresh712"
  
  launch_application()
  verify_signin_page_is_displayed()
  login_into_application(Project.Variables.Username,Project.Variables.Password)
  ''''
  verify_user_successfully_logged_into_account()
  wait_for_the_cameras_to_load()
  switch_to_security_setup_group_section()
  verify_security_setup_is_displayed()
  delete_a_user(username)
  verify_user_removed_successfully(username)
  logout_from_application()
  close_application()
  '''