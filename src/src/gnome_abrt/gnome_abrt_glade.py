# coding=utf-8
GNOME_ABRT_GLADE_CONTENTS ="\
<?xml version=\"1.0\" encoding=\"UTF-8\"?>\
<interface>\
  <!-- interface-requires gtk+ 3.0 -->\
  <object class=\"GtkAccelGroup\" id=\"ag_accelerators\"/>\
  <object class=\"GtkActionGroup\" id=\"gag_problem_actions\">\
    <property name=\"name\">problems</property>\
    <property name=\"accel_group\">ag_accelerators</property>\
    <child>\
      <object class=\"GtkAction\" id=\"gac_delete\">\
        <property name=\"label\" translatable=\"yes\">_Delete</property>\
        <property name=\"tooltip\" translatable=\"yes\">Delete selected problems</property>\
        <signal name=\"activate\" handler=\"on_gac_delete_activate\" swapped=\"no\"/>\
      </object>\
      <accelerator key=\"Delete\"/>\
    </child>\
    <child>\
      <object class=\"GtkAction\" id=\"gac_report\">\
        <property name=\"label\" translatable=\"yes\">_Report</property>\
        <property name=\"tooltip\" translatable=\"yes\">Submits selected problem</property>\
        <signal name=\"activate\" handler=\"on_gac_report_activate\" swapped=\"no\"/>\
      </object>\
      <accelerator key=\"Return\"/>\
    </child>\
    <child>\
      <object class=\"GtkAction\" id=\"gac_detail\">\
        <property name=\"label\" translatable=\"yes\">Analy_ze</property>\
        <property name=\"tooltip\" translatable=\"yes\">Open selected problem for analysis</property>\
        <signal name=\"activate\" handler=\"on_gac_detail_activate\" swapped=\"no\"/>\
      </object>\
      <accelerator key=\"Return\" modifiers=\"GDK_CONTROL_MASK | GDK_MOD1_MASK\"/>\
    </child>\
    <child>\
      <object class=\"GtkAction\" id=\"gac_opt_all_problems\">\
        <property name=\"label\" translatable=\"yes\">_All problems</property>\
        <property name=\"tooltip\" translatable=\"yes\">Show all known problems from all system users</property>\
        <signal name=\"activate\" handler=\"on_gac_opt_all_problems_activate\" swapped=\"no\"/>\
      </object>\
    </child>\
    <child>\
      <object class=\"GtkAction\" id=\"gac_open_directory\">\
        <property name=\"label\" translatable=\"yes\">_Open problem's data directory</property>\
        <property name=\"tooltip\" translatable=\"yes\">Opens the selected problem's data directory in the default file system browser</property>\
        <signal name=\"activate\" handler=\"on_gac_open_directory_activate\" swapped=\"no\"/>\
      </object>\
      <accelerator key=\"o\" modifiers=\"GDK_CONTROL_MASK\"/>\
    </child>\
    <child>\
      <object class=\"GtkAction\" id=\"gac_copy_id\">\
        <property name=\"label\" translatable=\"yes\">_Copy problem's ID to Clipboard</property>\
        <property name=\"tooltip\" translatable=\"yes\">Stores the selected problem's ID in Clibpoard</property>\
        <signal name=\"activate\" handler=\"on_gac_copy_id_activate\" swapped=\"no\"/>\
      </object>\
      <accelerator key=\"c\" modifiers=\"GDK_CONTROL_MASK\"/>\
    </child>\
  </object>\
  <object class=\"GtkListStore\" id=\"ls_problems\">\
    <columns>\
      <!-- column-name application-type -->\
      <column type=\"gchararray\"/>\
      <!-- column-name date-count -->\
      <column type=\"gchararray\"/>\
      <!-- column-name problem -->\
      <column type=\"PyObject\"/>\
    </columns>\
  </object>\
  <object class=\"GtkMenu\" id=\"menu_problem_item\">\
    <property name=\"visible\">True</property>\
    <property name=\"can_focus\">False</property>\
    <property name=\"accel_group\">ag_accelerators</property>\
    <child>\
      <object class=\"GtkMenuItem\" id=\"mi_report\">\
        <property name=\"related_action\">gac_report</property>\
        <property name=\"visible\">True</property>\
        <property name=\"can_focus\">False</property>\
      </object>\
    </child>\
    <child>\
      <object class=\"GtkMenuItem\" id=\"mi_delete\">\
        <property name=\"related_action\">gac_delete</property>\
        <property name=\"visible\">True</property>\
        <property name=\"can_focus\">False</property>\
      </object>\
    </child>\
    <child>\
      <object class=\"GtkMenuItem\" id=\"mi_detail\">\
        <property name=\"related_action\">gac_detail</property>\
        <property name=\"visible\">True</property>\
        <property name=\"can_focus\">False</property>\
      </object>\
    </child>\
    <child>\
      <object class=\"GtkMenuItem\" id=\"mi_open_directory\">\
        <property name=\"related_action\">gac_open_directory</property>\
        <property name=\"visible\">True</property>\
        <property name=\"can_focus\">False</property>\
      </object>\
    </child>\
    <child>\
      <object class=\"GtkMenuItem\" id=\"mi_copy_id\">\
        <property name=\"related_action\">gac_copy_id</property>\
        <property name=\"visible\">True</property>\
        <property name=\"can_focus\">False</property>\
      </object>\
    </child>\
  </object>\
  <object class=\"GtkWindow\" id=\"wnd_main\">\
    <property name=\"width_request\">800</property>\
    <property name=\"height_request\">600</property>\
    <property name=\"can_focus\">False</property>\
    <property name=\"icon_name\">gnome-abrt</property>\
    <accel-groups>\
      <group name=\"ag_accelerators\"/>\
    </accel-groups>\
    <child>\
      <object class=\"GtkGrid\" id=\"gr_main_layout\">\
        <property name=\"visible\">True</property>\
        <property name=\"can_focus\">False</property>\
        <property name=\"margin_left\">10</property>\
        <property name=\"margin_right\">10</property>\
        <property name=\"margin_top\">10</property>\
        <property name=\"margin_bottom\">10</property>\
        <property name=\"hexpand\">True</property>\
        <property name=\"vexpand\">True</property>\
        <child>\
          <object class=\"GtkEntry\" id=\"te_search\">\
            <property name=\"visible\">True</property>\
            <property name=\"can_focus\">True</property>\
            <property name=\"invisible_char\">●</property>\
            <property name=\"caps_lock_warning\">False</property>\
            <property name=\"secondary_icon_name\">edit-find</property>\
            <property name=\"placeholder_text\">Search</property>\
            <signal name=\"changed\" handler=\"on_te_search_changed\" swapped=\"no\"/>\
          </object>\
          <packing>\
            <property name=\"left_attach\">0</property>\
            <property name=\"top_attach\">0</property>\
            <property name=\"width\">1</property>\
            <property name=\"height\">1</property>\
          </packing>\
        </child>\
        <child>\
          <object class=\"GtkNotebook\" id=\"nb_problem_layout\">\
            <property name=\"visible\">True</property>\
            <property name=\"can_focus\">True</property>\
            <property name=\"hexpand\">True</property>\
            <property name=\"vexpand\">True</property>\
            <property name=\"show_tabs\">False</property>\
            <property name=\"show_border\">False</property>\
            <child>\
              <object class=\"GtkGrid\" id=\"gd_problem_info\">\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">False</property>\
                <property name=\"hexpand\">True</property>\
                <child>\
                  <object class=\"GtkImage\" id=\"img_app_icon\">\
                    <property name=\"width_request\">156</property>\
                    <property name=\"height_request\">156</property>\
                    <property name=\"visible\">True</property>\
                    <property name=\"can_focus\">False</property>\
                    <property name=\"halign\">center</property>\
                    <property name=\"valign\">start</property>\
                    <property name=\"icon_name\">image-missing</property>\
                    <property name=\"icon-size\">3</property>\
                  </object>\
                  <packing>\
                    <property name=\"left_attach\">0</property>\
                    <property name=\"top_attach\">0</property>\
                    <property name=\"width\">1</property>\
                    <property name=\"height\">1</property>\
                  </packing>\
                </child>\
                <child>\
                  <object class=\"GtkBox\" id=\"vbx_problem_header\">\
                    <property name=\"visible\">True</property>\
                    <property name=\"can_focus\">False</property>\
                    <property name=\"hexpand\">True</property>\
                    <property name=\"orientation\">vertical</property>\
                    <child>\
                      <object class=\"GtkLabel\" id=\"lbl_reason\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"hexpand\">True</property>\
                        <property name=\"xalign\">0</property>\
                        <property name=\"yalign\">2.2351741291171123e-10</property>\
                        <property name=\"ypad\">11</property>\
                        <property name=\"label\">Application killed by signal</property>\
                        <property name=\"wrap\">True</property>\
                        <property name=\"ellipsize\">end</property>\
                        <attributes>\
                          <attribute name=\"font-desc\" value=\"Sans Bold 11\"/>\
                        </attributes>\
                      </object>\
                      <packing>\
                        <property name=\"expand\">False</property>\
                        <property name=\"fill\">True</property>\
                        <property name=\"position\">1</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <object class=\"GtkLabel\" id=\"lbl_summary\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"hexpand\">True</property>\
                        <property name=\"xalign\">0</property>\
                        <property name=\"yalign\">0</property>\
                        <property name=\"label\">Application can't continue becuase of received signal</property>\
                        <property name=\"wrap\">True</property>\
                        <property name=\"ellipsize\">end</property>\
                      </object>\
                      <packing>\
                        <property name=\"expand\">False</property>\
                        <property name=\"fill\">True</property>\
                        <property name=\"position\">3</property>\
                      </packing>\
                    </child>\
                  </object>\
                  <packing>\
                    <property name=\"left_attach\">1</property>\
                    <property name=\"top_attach\">0</property>\
                    <property name=\"width\">1</property>\
                    <property name=\"height\">1</property>\
                  </packing>\
                </child>\
                <child>\
                  <object class=\"GtkGrid\" id=\"gd_problem_data\">\
                    <property name=\"visible\">True</property>\
                    <property name=\"can_focus\">False</property>\
                    <child>\
                      <object class=\"GtkLabel\" id=\"lbl_app_name\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"halign\">end</property>\
                        <property name=\"xpad\">10</property>\
                        <property name=\"ypad\">5</property>\
                        <property name=\"label\" translatable=\"yes\">Name</property>\
                        <attributes>\
                          <attribute name=\"foreground\" value=\"#87877e7e8080\"/>\
                        </attributes>\
                      </object>\
                      <packing>\
                        <property name=\"left_attach\">0</property>\
                        <property name=\"top_attach\">0</property>\
                        <property name=\"width\">1</property>\
                        <property name=\"height\">1</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <object class=\"GtkLabel\" id=\"lbl_app_version\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"halign\">end</property>\
                        <property name=\"xpad\">10</property>\
                        <property name=\"ypad\">5</property>\
                        <property name=\"label\" translatable=\"yes\">Version</property>\
                        <attributes>\
                          <attribute name=\"foreground\" value=\"#87877e7e8080\"/>\
                        </attributes>\
                      </object>\
                      <packing>\
                        <property name=\"left_attach\">0</property>\
                        <property name=\"top_attach\">1</property>\
                        <property name=\"width\">1</property>\
                        <property name=\"height\">1</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <object class=\"GtkLabel\" id=\"lbl_detected\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"halign\">end</property>\
                        <property name=\"xpad\">10</property>\
                        <property name=\"ypad\">5</property>\
                        <property name=\"label\" translatable=\"yes\">Detected</property>\
                        <attributes>\
                          <attribute name=\"foreground\" value=\"#87877e7e8080\"/>\
                        </attributes>\
                      </object>\
                      <packing>\
                        <property name=\"left_attach\">0</property>\
                        <property name=\"top_attach\">2</property>\
                        <property name=\"width\">1</property>\
                        <property name=\"height\">1</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <object class=\"GtkLabel\" id=\"lbl_app_name_value\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"halign\">start</property>\
                        <property name=\"xpad\">5</property>\
                        <property name=\"label\">app</property>\
                        <property name=\"ellipsize\">end</property>\
                      </object>\
                      <packing>\
                        <property name=\"left_attach\">1</property>\
                        <property name=\"top_attach\">0</property>\
                        <property name=\"width\">1</property>\
                        <property name=\"height\">1</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <object class=\"GtkLabel\" id=\"lbl_app_version_value\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"halign\">start</property>\
                        <property name=\"xpad\">5</property>\
                        <property name=\"label\">2.0.13-2</property>\
                        <property name=\"ellipsize\">end</property>\
                      </object>\
                      <packing>\
                        <property name=\"left_attach\">1</property>\
                        <property name=\"top_attach\">1</property>\
                        <property name=\"width\">1</property>\
                        <property name=\"height\">1</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <object class=\"GtkLabel\" id=\"lbl_detected_value\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"halign\">start</property>\
                        <property name=\"xpad\">5</property>\
                        <property name=\"label\">2013-04-09 18:55</property>\
                      </object>\
                      <packing>\
                        <property name=\"left_attach\">1</property>\
                        <property name=\"top_attach\">2</property>\
                        <property name=\"width\">1</property>\
                        <property name=\"height\">1</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <object class=\"GtkScrolledWindow\" id=\"gsw_links\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">True</property>\
                        <property name=\"margin_top\">20</property>\
                        <property name=\"hexpand\">True</property>\
                        <child>\
                          <object class=\"GtkViewport\" id=\"gv_links\">\
                            <property name=\"visible\">True</property>\
                            <property name=\"can_focus\">False</property>\
                            <property name=\"hexpand\">True</property>\
                            <property name=\"shadow_type\">none</property>\
                            <child>\
                              <object class=\"GtkBox\" id=\"vbx_links\">\
                                <property name=\"visible\">True</property>\
                                <property name=\"can_focus\">False</property>\
                                <property name=\"hexpand\">True</property>\
                                <property name=\"orientation\">vertical</property>\
                                <child>\
                                  <object class=\"GtkLinkButton\" id=\"linkbutton1\">\
                                    <property name=\"label\">Very long button name\
</property>\
                                    <property name=\"visible\">True</property>\
                                    <property name=\"can_focus\">True</property>\
                                    <property name=\"receives_default\">True</property>\
                                    <property name=\"has_tooltip\">True</property>\
                                    <property name=\"halign\">start</property>\
                                    <property name=\"hexpand\">True</property>\
                                    <property name=\"border_width\">1</property>\
                                    <property name=\"relief\">none</property>\
                                    <property name=\"focus_on_click\">False</property>\
                                    <property name=\"uri\">http://glade.gnome.org</property>\
                                  </object>\
                                  <packing>\
                                    <property name=\"expand\">False</property>\
                                    <property name=\"fill\">True</property>\
                                    <property name=\"position\">0</property>\
                                  </packing>\
                                </child>\
                                <child>\
                                  <object class=\"GtkLinkButton\" id=\"linkbutton2\">\
                                    <property name=\"label\">button</property>\
                                    <property name=\"visible\">True</property>\
                                    <property name=\"can_focus\">True</property>\
                                    <property name=\"receives_default\">True</property>\
                                    <property name=\"has_tooltip\">True</property>\
                                    <property name=\"halign\">start</property>\
                                    <property name=\"relief\">none</property>\
                                    <property name=\"uri\">http://glade.gnome.org</property>\
                                  </object>\
                                  <packing>\
                                    <property name=\"expand\">False</property>\
                                    <property name=\"fill\">True</property>\
                                    <property name=\"position\">1</property>\
                                  </packing>\
                                </child>\
                                <child>\
                                  <object class=\"GtkAlignment\" id=\"alignment3\">\
                                    <property name=\"visible\">True</property>\
                                    <property name=\"can_focus\">False</property>\
                                    <child>\
                                      <placeholder/>\
                                    </child>\
                                  </object>\
                                  <packing>\
                                    <property name=\"expand\">False</property>\
                                    <property name=\"fill\">True</property>\
                                    <property name=\"position\">2</property>\
                                  </packing>\
                                </child>\
                              </object>\
                            </child>\
                          </object>\
                        </child>\
                      </object>\
                      <packing>\
                        <property name=\"left_attach\">1</property>\
                        <property name=\"top_attach\">4</property>\
                        <property name=\"width\">2</property>\
                        <property name=\"height\">1</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <object class=\"GtkAlignment\" id=\"alignment1\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"valign\">start</property>\
                        <property name=\"hexpand\">True</property>\
                        <child>\
                          <placeholder/>\
                        </child>\
                      </object>\
                      <packing>\
                        <property name=\"left_attach\">2</property>\
                        <property name=\"top_attach\">0</property>\
                        <property name=\"width\">1</property>\
                        <property name=\"height\">3</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <object class=\"GtkLabel\" id=\"lbl_reported\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"halign\">end</property>\
                        <property name=\"xpad\">10</property>\
                        <property name=\"ypad\">5</property>\
                        <property name=\"label\" translatable=\"yes\">Reported</property>\
                        <attributes>\
                          <attribute name=\"foreground\" value=\"#87877e7e8080\"/>\
                        </attributes>\
                      </object>\
                      <packing>\
                        <property name=\"left_attach\">0</property>\
                        <property name=\"top_attach\">3</property>\
                        <property name=\"width\">1</property>\
                        <property name=\"height\">1</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <object class=\"GtkLabel\" id=\"lbl_reported_value\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"halign\">start</property>\
                        <property name=\"xpad\">5</property>\
                        <property name=\"label\">no</property>\
                      </object>\
                      <packing>\
                        <property name=\"left_attach\">1</property>\
                        <property name=\"top_attach\">3</property>\
                        <property name=\"width\">1</property>\
                        <property name=\"height\">1</property>\
                      </packing>\
                    </child>\
                    <child>\
                      <placeholder/>\
                    </child>\
                    <child>\
                      <placeholder/>\
                    </child>\
                  </object>\
                  <packing>\
                    <property name=\"left_attach\">1</property>\
                    <property name=\"top_attach\">1</property>\
                    <property name=\"width\">1</property>\
                    <property name=\"height\">1</property>\
                  </packing>\
                </child>\
                <child>\
                  <object class=\"GtkScrolledWindow\" id=\"gsw_problem_messages\">\
                    <property name=\"visible\">True</property>\
                    <property name=\"can_focus\">True</property>\
                    <property name=\"vexpand\">True</property>\
                    <child>\
                      <object class=\"GtkViewport\" id=\"gvp_problem_messages\">\
                        <property name=\"visible\">True</property>\
                        <property name=\"can_focus\">False</property>\
                        <property name=\"vexpand\">True</property>\
                        <property name=\"shadow_type\">none</property>\
                        <child>\
                          <object class=\"GtkBox\" id=\"vbx_problem_messages\">\
                            <property name=\"visible\">True</property>\
                            <property name=\"can_focus\">False</property>\
                            <property name=\"vexpand\">True</property>\
                            <property name=\"orientation\">vertical</property>\
                            <child>\
                              <placeholder/>\
                            </child>\
                          </object>\
                        </child>\
                      </object>\
                    </child>\
                  </object>\
                  <packing>\
                    <property name=\"left_attach\">1</property>\
                    <property name=\"top_attach\">2</property>\
                    <property name=\"width\">1</property>\
                    <property name=\"height\">1</property>\
                  </packing>\
                </child>\
                <child>\
                  <placeholder/>\
                </child>\
                <child>\
                  <placeholder/>\
                </child>\
              </object>\
            </child>\
            <child type=\"tab\">\
              <object class=\"GtkLabel\" id=\"lbl_page_problem\">\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">False</property>\
                <property name=\"label\">Problem page</property>\
              </object>\
              <packing>\
                <property name=\"tab_fill\">False</property>\
              </packing>\
            </child>\
            <child>\
              <object class=\"GtkBox\" id=\"vbx_empty_page\">\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">False</property>\
                <property name=\"orientation\">vertical</property>\
                <child>\
                  <object class=\"GtkLabel\" id=\"lbl_no_oopses\">\
                    <property name=\"visible\">True</property>\
                    <property name=\"can_focus\">False</property>\
                    <property name=\"label\" translatable=\"yes\">No problems detected!</property>\
                  </object>\
                  <packing>\
                    <property name=\"expand\">False</property>\
                    <property name=\"fill\">True</property>\
                    <property name=\"position\">0</property>\
                  </packing>\
                </child>\
              </object>\
              <packing>\
                <property name=\"position\">1</property>\
              </packing>\
            </child>\
            <child type=\"tab\">\
              <object class=\"GtkLabel\" id=\"lbl_page_empty\">\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">False</property>\
                <property name=\"label\">Empty page</property>\
              </object>\
              <packing>\
                <property name=\"position\">1</property>\
                <property name=\"tab_fill\">False</property>\
              </packing>\
            </child>\
            <child>\
              <object class=\"GtkBox\" id=\"vbx_no_source_page\">\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">False</property>\
                <property name=\"orientation\">vertical</property>\
                <child>\
                  <object class=\"GtkLabel\" id=\"lbl_no_source\">\
                    <property name=\"visible\">True</property>\
                    <property name=\"can_focus\">False</property>\
                    <property name=\"label\" translatable=\"yes\">No source selected!</property>\
                  </object>\
                  <packing>\
                    <property name=\"expand\">False</property>\
                    <property name=\"fill\">True</property>\
                    <property name=\"position\">0</property>\
                  </packing>\
                </child>\
              </object>\
              <packing>\
                <property name=\"position\">2</property>\
              </packing>\
            </child>\
            <child type=\"tab\">\
              <object class=\"GtkLabel\" id=\"lbl_page_no_source\">\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">False</property>\
                <property name=\"label\" translatable=\"yes\">No source</property>\
              </object>\
              <packing>\
                <property name=\"position\">2</property>\
                <property name=\"tab_fill\">False</property>\
              </packing>\
            </child>\
          </object>\
          <packing>\
            <property name=\"left_attach\">1</property>\
            <property name=\"top_attach\">1</property>\
            <property name=\"width\">1</property>\
            <property name=\"height\">1</property>\
          </packing>\
        </child>\
        <child>\
          <object class=\"GtkBox\" id=\"vbox_problems\">\
            <property name=\"visible\">True</property>\
            <property name=\"can_focus\">False</property>\
            <property name=\"margin_top\">10</property>\
            <property name=\"orientation\">vertical</property>\
            <child>\
              <object class=\"GtkBox\" id=\"hbox_source_btns\">\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">False</property>\
                <child>\
                  <placeholder/>\
                </child>\
                <child>\
                  <placeholder/>\
                </child>\
                <child>\
                  <placeholder/>\
                </child>\
              </object>\
              <packing>\
                <property name=\"expand\">False</property>\
                <property name=\"fill\">True</property>\
                <property name=\"position\">0</property>\
              </packing>\
            </child>\
            <child>\
              <object class=\"GtkScrolledWindow\" id=\"sw_problems\">\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">True</property>\
                <property name=\"shadow_type\">in</property>\
                <property name=\"min_content_width\">300</property>\
                <child>\
                  <object class=\"GtkTreeView\" id=\"tv_problems\">\
                    <property name=\"visible\">True</property>\
                    <property name=\"can_focus\">True</property>\
                    <property name=\"model\">ls_problems</property>\
                    <property name=\"headers_visible\">False</property>\
                    <property name=\"headers_clickable\">False</property>\
                    <property name=\"enable_search\">False</property>\
                    <property name=\"search_column\">0</property>\
                    <property name=\"enable_grid_lines\">horizontal</property>\
                    <signal name=\"button-press-event\" handler=\"on_tv_problems_button_press_event\" swapped=\"no\"/>\
                    <child internal-child=\"selection\">\
                      <object class=\"GtkTreeSelection\" id=\"tvs_problems\">\
                        <property name=\"mode\">multiple</property>\
                        <signal name=\"changed\" handler=\"on_tvs_problems_changed\" swapped=\"no\"/>\
                      </object>\
                    </child>\
                    <child>\
                      <object class=\"GtkTreeViewColumn\" id=\"tvc_application\">\
                        <property name=\"min_width\">0</property>\
                        <property name=\"title\" translatable=\"yes\">App</property>\
                        <child>\
                          <object class=\"GtkCellRendererText\" id=\"cellrenderertext1\">\
                            <property name=\"markup\">python</property>\
                          </object>\
                          <attributes>\
                            <attribute name=\"text\">0</attribute>\
                          </attributes>\
                        </child>\
                      </object>\
                    </child>\
                    <child>\
                      <object class=\"GtkTreeViewColumn\" id=\"tvc_date\">\
                        <property name=\"title\" translatable=\"yes\">Date</property>\
                        <child>\
                          <object class=\"GtkCellRendererText\" id=\"cellrenderertext3\">\
                            <property name=\"alignment\">right</property>\
                          </object>\
                          <attributes>\
                            <attribute name=\"text\">1</attribute>\
                          </attributes>\
                        </child>\
                      </object>\
                    </child>\
                  </object>\
                </child>\
              </object>\
              <packing>\
                <property name=\"expand\">True</property>\
                <property name=\"fill\">True</property>\
                <property name=\"position\">1</property>\
              </packing>\
            </child>\
          </object>\
          <packing>\
            <property name=\"left_attach\">0</property>\
            <property name=\"top_attach\">1</property>\
            <property name=\"width\">1</property>\
            <property name=\"height\">1</property>\
          </packing>\
        </child>\
        <child>\
          <object class=\"GtkBox\" id=\"vbx_menu_buttons\">\
            <property name=\"visible\">True</property>\
            <property name=\"can_focus\">False</property>\
            <child>\
              <object class=\"GtkAlignment\" id=\"alignment5\">\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">False</property>\
                <property name=\"hexpand\">True</property>\
                <child>\
                  <placeholder/>\
                </child>\
              </object>\
              <packing>\
                <property name=\"expand\">False</property>\
                <property name=\"fill\">True</property>\
                <property name=\"position\">0</property>\
              </packing>\
            </child>\
            <child>\
              <object class=\"GtkButton\" id=\"btn_delete\">\
                <property name=\"related_action\">gac_delete</property>\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">True</property>\
                <property name=\"receives_default\">True</property>\
                <property name=\"halign\">end</property>\
                <property name=\"margin_right\">5</property>\
              </object>\
              <packing>\
                <property name=\"expand\">False</property>\
                <property name=\"fill\">True</property>\
                <property name=\"position\">1</property>\
              </packing>\
            </child>\
            <child>\
              <object class=\"GtkButton\" id=\"btn_report\">\
                <property name=\"related_action\">gac_report</property>\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">True</property>\
                <property name=\"receives_default\">True</property>\
                <property name=\"halign\">end</property>\
                <property name=\"margin_left\">5</property>\
                <property name=\"margin_right\">5</property>\
              </object>\
              <packing>\
                <property name=\"expand\">False</property>\
                <property name=\"fill\">True</property>\
                <property name=\"position\">2</property>\
              </packing>\
            </child>\
            <child>\
              <object class=\"GtkButton\" id=\"btn_detail\">\
                <property name=\"related_action\">gac_detail</property>\
                <property name=\"visible\">True</property>\
                <property name=\"can_focus\">True</property>\
                <property name=\"receives_default\">True</property>\
                <property name=\"no_show_all\">True</property>\
                <property name=\"halign\">end</property>\
                <property name=\"margin_left\">5</property>\
                <property name=\"use_underline\">True</property>\
              </object>\
              <packing>\
                <property name=\"expand\">False</property>\
                <property name=\"fill\">True</property>\
                <property name=\"position\">3</property>\
              </packing>\
            </child>\
          </object>\
          <packing>\
            <property name=\"left_attach\">1</property>\
            <property name=\"top_attach\">0</property>\
            <property name=\"width\">1</property>\
            <property name=\"height\">1</property>\
          </packing>\
        </child>\
      </object>\
    </child>\
  </object>\
</interface>\
"
