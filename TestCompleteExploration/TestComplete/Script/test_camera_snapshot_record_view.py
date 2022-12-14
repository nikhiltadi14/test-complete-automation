from drag_and_drop_camera_page import *
import test_delete_user
from export_video_page import *
from play_pause_forward import *
from camera_snapshot_record_view import *
from utility_method import *

def SaveSnapshots():
  launch_application()
  verify_signin_page_is_displayed()
  login_to_application()
  verify_user_successfully_logged_into_account()
  wait_for_the_cameras_to_load()
  verify_2_camera_panel_is_displayed()
  click_on_2_camera_panel()
  verify_2_camera_panel_is_blank()
  drag_and_drop_camera()
  verify_videos_are_streaming_live()
  click_on_export_recorded_video_button()
  play_button_click()
  fast_backward_button_click()
  pause_button_click()
  click_on_save_snapshot_button()
  verify_snapshot_window_is_displayed()
  click_on_save_as_file_button()
  verify_browser_file_location_option_is_displayed()
  click_on_browser_file_location()
  click_on_file_destination_path()
  enter_file_destination_path()
  file_name = generate_random_file_name()
  enter_file_name(file_name)
  click_on_save()
  close_application()
  verify_that_the_file_got_saved()
  