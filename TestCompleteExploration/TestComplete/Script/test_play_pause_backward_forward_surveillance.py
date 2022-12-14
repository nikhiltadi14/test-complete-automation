from drag_and_drop_camera_page import *
import test_delete_user
from export_video_page import *
from play_pause_forward import *

def TestExportMultiplex():
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
  click_on_export_recorded_video_button()
  current_time = get_display_time()
  play_button_click()
  #backward_button_click()
  fast_backward_button_click()
  pause_button_click()
  backward_time = get_display_time()
  compare_time(current_time,backward_time)