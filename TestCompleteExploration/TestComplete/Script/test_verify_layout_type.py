from drag_and_drop_camera_page import *
from get_blank_camera_count_page import *
from verify_layout_type_page import *


def TestLayoutType():
  launch_application()
  verify_signin_page_is_displayed()
  #login_into_application(Project.Variables.Username,Project.Variables.Password)
  #verify_user_successfully_logged_into_account()
  #wait_for_the_cameras_to_load()
  #select_stack_pane_camera_panel()
  #sub_string = select_stack_pane_camera_panel_v2()
  #verify_layout_count_matches_with_blank_camera_count(sub_string)
  
  
  ''''
  verify_1_camera_panel_is_displayed()
  click_on_1_camera_panel_button()
  select_camera_view_layout()
  sub_string = get_layout_type_header_text()
  verify_layout_count_matches_with_blank_camera_count(sub_string)
  '''