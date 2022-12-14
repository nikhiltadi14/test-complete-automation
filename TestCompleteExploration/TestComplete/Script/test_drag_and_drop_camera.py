from drag_and_drop_camera_page import *
import test_delete_user

def TestExportMultiplex():
  a = test_delete_user.TestDeleteUser.username
  launch_application()
  verify_signin_page_is_displayed()
  login_into_application(Project.Variables.Username,Project.Variables.Password)
  verify_user_successfully_logged_into_account()
  wait_for_the_cameras_to_load()
  verify_2_camera_panel_is_displayed()
  click_on_2_camera_panel()
  verify_2_camera_panel_is_blank()
  drag_and_drop_camera()
  verify_videos_are_streaming_live()
  logout_from_application()
  close_application()
  

 
