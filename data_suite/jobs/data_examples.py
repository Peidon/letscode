clarify_fail_str = """
{
  "interaction": {
    "read_write_ctrl": 2,
    "value": 5
  },
  "variable_to_clarify": {
    "read_write_ctrl": 2,
    "value": "lovito_nlu"
  },
  "clarification_utterance": {
    "read_write_ctrl": 2,
    "value": "<p>dfsdfgds</p>"
  },
  "options_setting": {
    "read_write_ctrl": 2,
    "value": {
      "option_from": "Poduct Variation.option",
      "option_mode": "Appended List",
      "selection_result": {
        "source_type": 6,
        "value": "attribute_key"
      }
    }
  },
  "input_setting": {
    "read_write_ctrl": 2,
    "value": {
      "allow_input_by_texting": true,
      "key_information": [
        "Color",
        "Size"
      ]
    }
  },
  "reclarification_setting": {
    "read_write_ctrl": 2,
    "value": {
      "allow_reclarification": true,
      "reclarification_utterance": [
        {
          "nlu_reclarification_utterance_value": "<p>abc</p>"
        }
      ],
      "failed_action": 2,
      "next_node": {
        "taskbot_id": "",
        "next_node_id": ""
      }
    }
  },
  "advanced_setting": {
    "read_write_ctrl": 2,
    "value": {
      "single_option_action": 1,
      "next_node": {
        "taskbot_id": "SOP163",
        "next_node_id": "",
        "port_id": "59ca95cd-de31-4bde-bb4b-adfc9ece6316"
      }
    }
  },
  "next_node": {
    "read_write_ctrl": null,
    "value": {
      "taskbot_id": "SOP82",
      "next_node_id": "SOP82_Node36",
      "port_id": "d5fd44e1-58e4-4972-89c0-3518d3daeac1"
    }
  },
  "node_template_id": "chatbot_variation_collector"
}"""

clarify_node_json_str = """
{
  "interaction": {
    "read_write_ctrl": 2,
    "value": 2
  },
  "button_selection_utterance": {
    "read_write_ctrl": null,
    "value": "",
    "message_type": 0,
    "rich_text": "",
    "variables": null,
    "jump_node_list": null
  },
  "answer_options": {
    "read_write_ctrl": 2,
    "value": [
      {
        "button_text": "",
        "button_id": "btn_01",
        "value": ""
      },
      {
        "button_text": "",
        "button_id": "btn_02",
        "value": ""
      }
    ]
  },
  "display_mode": {
    "read_write_ctrl": null,
    "value": 0
  },
  "button_selection_result": {
    "read_write_ctrl": null,
    "value": {
      "source_type": 2,
      "value": ""
    }
  },
  "card_type": {
    "read_write_ctrl": 2,
    "value": 1
  },
  "order_card_utterance": {
    "read_write_ctrl": 2,
    "value": "order card",
    "message_type": 1,
    "rich_text": "",
    "variables": null,
    "jump_node_list": []
  },
  "order_card_status_display": {
    "read_write_ctrl": 2,
    "value": {
      "maximal_display": 3,
      "status_to_display": [
        1
      ],
      "default_type": 1,
      "select_prioritization": {
        "prioritization": 1,
        "first_status": -1
      }
    }
  },
  "order_card_tips": {
    "read_write_ctrl": 2,
    "value": {
      "select_tip": {
        "button_text": "a",
        "button_id": "btn_18",
        "value": ""
      },
      "others_tip": {
        "button_text": "b",
        "button_id": "btn_11",
        "value": ""
      }
    }
  },
  "order_card_style": {
    "read_write_ctrl": 2,
    "value": 0
  },
  "topup_card_utterance": {
    "read_write_ctrl": null,
    "value": "",
    "message_type": 0,
    "rich_text": "",
    "variables": null,
    "jump_node_list": null
  },
  "topup_card_status_display": {
    "read_write_ctrl": null,
    "value": {
      "maximal_display": 3,
      "status_to_display": []
    }
  },
  "topup_card_tips": {
    "read_write_ctrl": null,
    "value": {
      "select_tip": {
        "button_text": "",
        "button_id": "btn_1",
        "value": ""
      },
      "others_tip": {
        "button_text": "",
        "button_id": "btn_2",
        "value": ""
      }
    }
  },
  "topup_card_still_not_found": {
    "read_write_ctrl": null,
    "still_not_found_text": "",
    "transaction_not_found_text": "",
    "check_button": {
      "button_text": "",
      "button_id": "btn_3",
      "value": ""
    },
    "jump_after_click": {
      "read_write_ctrl": null,
      "value": {
        "taskbot_id": "",
        "next_node_id": ""
      }
    }
  },
  "withdrawal_card_utterance": {
    "read_write_ctrl": null,
    "value": "",
    "message_type": 0,
    "rich_text": "",
    "variables": null,
    "jump_node_list": null
  },
  "withdrawal_card_status_display": {
    "read_write_ctrl": null,
    "value": {
      "maximal_display": 3,
      "status_to_display": []
    }
  },
  "withdrawal_card_tips": {
    "read_write_ctrl": null,
    "value": {
      "select_tip": {
        "button_text": "",
        "button_id": "btn_4",
        "value": ""
      },
      "others_tip": {
        "button_text": "",
        "button_id": "btn_5",
        "value": ""
      }
    }
  },
  "withdrawal_card_still_not_found": {
    "read_write_ctrl": null,
    "still_not_found_text": "",
    "transaction_not_found_text": "",
    "check_button": {
      "button_text": "",
      "button_id": "btn_6",
      "value": ""
    },
    "jump_after_click": {
      "read_write_ctrl": null,
      "value": {
        "taskbot_id": "",
        "next_node_id": ""
      }
    }
  },
  "popup_title": {
    "read_write_ctrl": null,
    "value": ""
  },
  "popup_content": {
    "read_write_ctrl": null,
    "value": {
      "rich_text": "",
      "variables": null,
      "jump_node_list": null
    }
  },
  "popup_button_setting": {
    "read_write_ctrl": null,
    "value": {
      "left_button": {
        "button_text": "",
        "button_id": "btn_7",
        "value": ""
      },
      "right_button": {
        "button_text": "",
        "button_id": "btn_8",
        "value": ""
      }
    }
  },
  "popup_selection_result": {
    "read_write_ctrl": null,
    "value": {
      "source_type": 2,
      "value": ""
    }
  },
  "selector_utterance": {
    "read_write_ctrl": null,
    "value": "",
    "message_type": 0,
    "rich_text": "",
    "variables": null,
    "jump_node_list": null
  },
  "selector_intent": {
    "read_write_ctrl": null,
    "value": [
      {
        "sub_intents": [],
        "intent_text": "",
        "jump_node": {
          "taskbot_id": "",
          "next_node_id": "",
          "port_id": "18a55391-4fa5-4c1f-b59d-9ce1240582ec"
        },
        "button_id": "btn_9"
      }
    ]
  },
  "nlu_setting": {
    "read_write_ctrl": 2,
    "value": {
      "is_opened": true,
      "answer_options": [
        {
          "source_type": 0,
          "taskbot_nlu_intent_id": 2001,
          "taskbot_nlu_intent_name": "Order Selection",
          "option_text": "",
          "value": "",
          "entity_setting": [
            {
              "entity_id": 1,
              "entity_name": "Order ID",
              "entity_type": "order_sn",
              "variable_id": "",
              "variable_name": ""
            }
          ]
        }
      ],
      "taskbot_nlu_intent_clarification": [
        {
          "utterance_rich_text": "<p>a</p>"
        },
        {
          "utterance_rich_text": "<p>b</p>"
        },
        {
          "utterance_rich_text": "<p>{variable:get_current_time.current_time,name:current time,dateFormat:DD-MM-yyyy}</p>"
        }
      ]
    }
  },
  "next_node": {
    "read_write_ctrl": null,
    "value": {
      "taskbot_id": "SOP95",
      "next_node_id": "",
      "port_id": "9778e49e-95ec-4b87-8fa8-4d14b2d0b383"
    }
  },
  "node_template_id": "chatbot_order_card_old"
}
"""

answer_node_str = """
{
  "answer_branch_list": {
    "read_write_ctrl": 2,
    "value": [
      {
        "name": {
          "read_write_ctrl": 2,
          "value": "Default"
        },
        "shadow_config": {
          "read_write_ctrl": 2,
          "value": {
            "is_default": true,
            "case_id": "case_1",
            "condition_id": "",
            "btn_id_prefix": "btn_1"
          }
        },
        "branch_rule": {
          "read_write_ctrl": 2,
          "value": {
            "groups": null,
            "logics": null
          }
        },
        "answer_action": {
          "read_write_ctrl": 2,
          "value": {
            "action": 1,
            "message_type": 1,
            "content": "",
            "variables": [],
            "jump_node_list": []
          }
        },
        "card_setting": {
          "read_write_ctrl": 2,
          "value": {
            "type": null
          }
        },
        "button_setting": {
          "read_write_ctrl": 2,
          "value": {
            "button_switch": true,
            "buttons": [
              {
                "button_id": "btn_2",
                "button_style": 2,
                "button_function": 4,
                "inhouse_queue": {
                  "entry_point": "",
                  "user_type": "",
                  "enquiry_type": "",
                  "user_type_label": ""
                }
              },
              {
                "button_id": "btn_3",
                "button_style": 1,
                "button_function": 4,
                "inhouse_queue": {
                  "entry_point": "",
                  "user_type": "",
                  "enquiry_type": "",
                  "user_type_label": ""
                }
              },
              {
                "button_id": "btn_4",
                "button_function": 4,
                "inhouse_queue": {
                  "entry_point": "",
                  "user_type": "",
                  "enquiry_type": "",
                  "user_type_label": ""
                }
              }
            ]
          }
        },
        "related_intents": {
          "read_write_ctrl": 2,
          "value": [
            -1,
            -1,
            -1
          ]
        },
        "advance_setting": {
          "read_write_ctrl": 2,
          "value": {
            "feedback": true,
            "end_tag": true,
            "follow_up": false
          }
        },
        "variate_assignment": {
          "read_write_ctrl": 2,
          "value": []
        },
        "node_template_id": "chatbot_message"
      },
      {
        "name": {
          "read_write_ctrl": 2,
          "value": "Case #1"
        },
        "shadow_config": {
          "read_write_ctrl": 2,
          "value": {
            "is_default": false,
            "case_id": "case_2",
            "condition_id": "",
            "btn_id_prefix": "btn_5"
          }
        },
        "branch_rule": {
          "read_write_ctrl": 2,
          "value": {
            "groups": [
              {
                "rules": [
                  {
                    "variables": [],
                    "operators": []
                  }
                ],
                "logics": []
              }
            ],
            "logics": []
          }
        },
        "answer_action": {
          "read_write_ctrl": 2,
          "value": {
            "action": 1,
            "message_type": 1,
            "content": "",
            "variables": [],
            "jump_node_list": []
          }
        },
        "card_setting": {
          "read_write_ctrl": 2,
          "value": {
            "type": null
          }
        },
        "button_setting": {
          "read_write_ctrl": 2,
          "value": {
            "button_switch": true,
            "buttons": []
          }
        },
        "related_intents": {
          "read_write_ctrl": 2,
          "value": [
            -1,
            -1,
            -1
          ]
        },
        "advance_setting": {
          "read_write_ctrl": 2,
          "value": {
            "feedback": true,
            "end_tag": true,
            "follow_up": false
          }
        },
        "variate_assignment": {
          "read_write_ctrl": 2,
          "value": []
        },
        "node_template_id": "chatbot_message"
      }
    ]
  }
}
"""

answer_node_case_str = """
{
  "answer_branch_list": {
    "read_write_ctrl": 2,
    "value": [
      {
        "name": {
          "read_write_ctrl": 2,
          "value": "Default"
        },
        "shadow_config": {
          "read_write_ctrl": 2,
          "value": {
            "is_default": true,
            "case_id": "case_1",
            "condition_id": "",
            "btn_id_prefix": "btn_1"
          }
        },
        "branch_rule": {
          "read_write_ctrl": 2,
          "value": {
            "groups": null,
            "logics": null
          }
        },
        "answer_action": {
          "read_write_ctrl": 2,
          "value": {
            "action": 1,
            "message_type": 2,
            "rich_text": "<p>345</p>",
            "variables": [],
            "jump_node_list": null
          }
        },
        "card_setting": {
          "read_write_ctrl": null,
          "value": {
            "type": 1,
            "timeline_card": {
              "milestones": [
                {
                  "date_content": "{variable:get_current_time.current_time,name:current time,dateFormat:DD-MM-yyyy}12",
                  "extra_info": "",
                  "title": "12345678901234567890123456789012345678901234567890123456789012345",
                  "description": "<p></p>",
                  "jump_node_list": [],
                  "is_future": false,
                  "button_switch": true,
                  "buttons": [
                    {
                      "button_style": 1,
                      "button_text": "hello",
                      "button_function": 5,
                      "intent_id": 9051,
                      "intent_name": "[Keamanan Akun] Bagaimana cara mengetahui penipuan?"
                    }
                  ]
                },
                {
                  "date_content": "{variable:get_current_time.current_time,name:current time}DDDMMM ",
                  "extra_info": "extrainfo",
                  "title": "title",
                  "description": "<p>description<a href=\"variable:get_current_time.current_time?dateFormat=DD-MM-yyyy+HH%3Amm\" rel=\"noopener noreferrer\" target=\"_blank\" class=\"chatbot-text-link-variable\">current time</a></p>",
                  "jump_node_list": [],
                  "is_future": true,
                  "button_switch": true,
                  "buttons": [
                    {
                      "button_style": 1,
                      "button_text": "123",
                      "button_function": 5,
                      "intent_id": 9051,
                      "intent_name": "[Keamanan Akun] Bagaimana cara mengetahui penipuan?"
                    }
                  ]
                }
              ],
              "title": "<p></p>"
            }
          }
        },
        "button_setting": {
          "read_write_ctrl": 2,
          "value": {
            "button_switch": true,
            "buttons": []
          }
        },
        "related_intents": {
          "read_write_ctrl": 2,
          "value": [
            -1,
            -1,
            -1
          ]
        },
        "advance_setting": {
          "read_write_ctrl": 2,
          "value": {
            "feedback": true,
            "end_tag": true,
            "follow_up": false,
            "agent_case_id": 0
          }
        },
        "variate_assignment": {
          "read_write_ctrl": null,
          "value": null
        },
        "node_template_id": "chatbot_timeline_card"
      },
      {
        "node_template_id": "chatbot_contact_card",
        "name": {
          "read_write_ctrl": 2,
          "value": "Case #1"
        },
        "shadow_config": {
          "read_write_ctrl": 2,
          "value": {
            "is_default": false
          }
        },
        "branch_rule": {
          "read_write_ctrl": 2,
          "value": {
            "groups": [
              {
                "rules": [
                  {
                    "variables": [
                      {
                        "source_type": 7,
                        "value": "Variables",
                        "render": "General Variables"
                      },
                      {
                        "source_type": 6,
                        "value": "current_time",
                        "render": "Current Time"
                      },
                      {
                        "value": "customize",
                        "render": "Customize"
                      },
                      {
                        "source_type": 4,
                        "value": "1695179310",
                        "render": "2023-09-20 11:08:30"
                      }
                    ],
                    "operators": [
                      "10"
                    ]
                  }
                ],
                "logics": []
              }
            ],
            "logics": []
          }
        },
        "answer_action": {
          "read_write_ctrl": 2,
          "value": {
            "action": 1,
            "message_type": 1,
            "variables": [],
            "jump_node_list": [],
            "content": "condition"
          }
        },
        "card_setting": {
          "read_write_ctrl": 2,
          "value": {
            "type": 3,
            "courier_card": {
              "logo": {},
              "links": [
                {
                  "source": "tracking_order",
                  "id": ""
                }
              ],
              "contacts_info": [],
              "operate_time": [],
              "show_driver_info": false,
              "title": "abc"
            }
          }
        },
        "button_setting": {
          "read_write_ctrl": 2,
          "value": {
            "button_switch": true,
            "buttons": [
              {
                "button_style": 1,
                "button_text": "afdf",
                "button_function": 8
              }
            ]
          }
        },
        "related_intents": {
          "read_write_ctrl": 2,
          "value": [
            1000005,
            -1,
            -1
          ]
        },
        "variate_assignment": {
          "read_write_ctrl": 2,
          "value": []
        },
        "advance_setting": {
          "read_write_ctrl": 2,
          "value": {
            "feedback": true,
            "end_tag": true,
            "follow_up": false
          }
        }
      }
    ]
  }
}
"""