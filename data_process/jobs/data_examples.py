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

condition_json_str = '''
[
    {
        "desc": {
            "read_write_ctrl": 2,
            "value": "Default"
        },
        "shadow_config": {
            "read_write_ctrl": null,
            "value": {
                "is_default": true,
                "case_id": "",
                "condition_id": "condition_1"
            }
        },
        "branch_rule": {
            "read_write_ctrl": 2,
            "value": {
                "groups": [],
                "logics": null
            }
        },
        "branch_action": {
            "read_write_ctrl": 2,
            "value": "jump_node"
        },
        "jump_node": {
            "read_write_ctrl": 2,
            "value": {
                "taskbot_id": "SOP15",
                "next_node_id": "SOP15_Node22",
                "port_id": "58e22d3c-f4f5-4c0b-9b67-1522f7f6c126"
            }
        },
        "variate_assignment": {
            "read_write_ctrl": 2,
            "value": []
        },
        "show_condition": {
            "read_write_ctrl": null,
            "value": false
        },
        "node_template_id": "chatbot_system",
        "advance_setting": {
            "read_write_ctrl": null,
            "value": {
                "feedback": false,
                "end_tag": false,
                "follow_up": false,
                "next_node": {
                    "taskbot_id": "",
                    "next_node_id": ""
                },
                "open_data_tracking": false,
                "data_tracking": null,
                "chat_with_seller": false,
                "agent_case_id": 0
            }
        }
    },
    {
        "desc": {
            "read_write_ctrl": 2,
            "value": "To Pay"
        },
        "shadow_config": {
            "read_write_ctrl": 2,
            "value": {
                "is_default": false,
                "case_id": "",
                "condition_id": "condition_2"
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
                                        "value": "API",
                                        "render": "API"
                                    },
                                    {
                                        "source_type": 1,
                                        "value": "get_order_info_by_order_id.chatbot_order_status",
                                        "api_id": "get_order_info_by_order_id",
                                        "render": "Chatbot order status",
                                        "api_name": "getOrderInfoByOrderId"
                                    },
                                    {
                                        "value": "options",
                                        "render": "Options"
                                    },
                                    {
                                        "source_type": 3,
                                        "value": "1",
                                        "render": "Buyer To Pay"
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
        "branch_action": {
            "read_write_ctrl": 2,
            "value": "jump_node"
        },
        "jump_node": {
            "read_write_ctrl": 2,
            "value": {
                "taskbot_id": "SOP15",
                "next_node_id": "SOP15_Node28",
                "port_id": "60563061-724c-4dfd-9888-c2e221bffb00"
            }
        },
        "variate_assignment": {
            "read_write_ctrl": 2,
            "value": []
        },
        "show_condition": {
            "read_write_ctrl": null,
            "value": false
        },
        "node_template_id": "chatbot_system",
        "advance_setting": {
            "read_write_ctrl": null,
            "value": {
                "feedback": false,
                "end_tag": false,
                "follow_up": false,
                "next_node": {
                    "taskbot_id": "",
                    "next_node_id": ""
                },
                "open_data_tracking": false,
                "data_tracking": null,
                "chat_with_seller": false,
                "agent_case_id": 0
            }
        }
    },
    {
        "desc": {
            "read_write_ctrl": null,
            "value": "To Ship"
        },
        "shadow_config": {
            "read_write_ctrl": null,
            "value": {
                "is_default": false,
                "case_id": "",
                "condition_id": "condition_3"
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
                                        "value": "API",
                                        "render": "API"
                                    },
                                    {
                                        "source_type": 1,
                                        "value": "get_order_info_by_order_id.chatbot_order_status",
                                        "api_id": "get_order_info_by_order_id",
                                        "render": "Chatbot order status",
                                        "api_name": "getOrderInfoByOrderId"
                                    },
                                    {
                                        "value": "options",
                                        "render": "Options"
                                    },
                                    {
                                        "source_type": 3,
                                        "value": "2",
                                        "render": "Buyer To Ship"
                                    }
                                ],
                                "operators": [
                                    "10"
                                ]
                            }
                        ],
                        "logics": []
                    },
                    {
                        "rules": [
                            {
                                "variables": [
                                    {
                                        "source_type": 7,
                                        "value": "API",
                                        "render": "API"
                                    },
                                    {
                                        "source_type": 1,
                                        "value": "get_order_info_by_order_id.chatbot_order_status",
                                        "api_id": "get_order_info_by_order_id",
                                        "render": "Chatbot order status",
                                        "api_name": "getOrderInfoByOrderId"
                                    },
                                    {
                                        "value": "options",
                                        "render": "Options"
                                    },
                                    {
                                        "source_type": 3,
                                        "value": "4",
                                        "render": "Buyer To Ship - Waiting pickup"
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
                "logics": [
                    2
                ]
            }
        },
        "branch_action": {
            "read_write_ctrl": 2,
            "value": "jump_node"
        },
        "jump_node": {
            "read_write_ctrl": 2,
            "value": {
                "taskbot_id": "SOP15",
                "next_node_id": "SOP15_Node44",
                "port_id": "73bc8e21-53f2-4977-8d13-62cf090806f8"
            }
        },
        "variate_assignment": {
            "read_write_ctrl": 2,
            "value": []
        },
        "show_condition": {
            "read_write_ctrl": null,
            "value": false
        },
        "node_template_id": "chatbot_system",
        "advance_setting": {
            "read_write_ctrl": null,
            "value": {
                "feedback": false,
                "end_tag": false,
                "follow_up": false,
                "next_node": {
                    "taskbot_id": "",
                    "next_node_id": ""
                },
                "open_data_tracking": false,
                "data_tracking": null,
                "chat_with_seller": false,
                "agent_case_id": 0
            }
        }
    },
    {
        "desc": {
            "read_write_ctrl": null,
            "value": "To Receive"
        },
        "shadow_config": {
            "read_write_ctrl": null,
            "value": {
                "is_default": false,
                "case_id": "",
                "condition_id": "condition_4"
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
                                        "value": "API",
                                        "render": "API"
                                    },
                                    {
                                        "source_type": 1,
                                        "value": "get_order_info_by_order_id.chatbot_order_status",
                                        "api_id": "get_order_info_by_order_id",
                                        "render": "Chatbot order status",
                                        "api_name": "getOrderInfoByOrderId"
                                    },
                                    {
                                        "value": "options",
                                        "render": "Options"
                                    },
                                    {
                                        "source_type": 3,
                                        "value": "3",
                                        "render": "Buyer To Receive - Shipped Non-Integrated"
                                    }
                                ],
                                "operators": [
                                    "10"
                                ]
                            }
                        ],
                        "logics": []
                    },
                    {
                        "rules": [
                            {
                                "variables": [
                                    {
                                        "source_type": 7,
                                        "value": "API",
                                        "render": "API"
                                    },
                                    {
                                        "source_type": 1,
                                        "value": "get_order_info_by_order_id.chatbot_order_status",
                                        "api_id": "get_order_info_by_order_id",
                                        "render": "Chatbot order status",
                                        "api_name": "getOrderInfoByOrderId"
                                    },
                                    {
                                        "value": "options",
                                        "render": "Options"
                                    },
                                    {
                                        "source_type": 3,
                                        "value": "5",
                                        "render": "Buyer To Receive - Shipped Integrated"
                                    }
                                ],
                                "operators": [
                                    "10"
                                ]
                            }
                        ],
                        "logics": []
                    },
                    {
                        "rules": [
                            {
                                "variables": [
                                    {
                                        "source_type": 7,
                                        "value": "API",
                                        "render": "API"
                                    },
                                    {
                                        "source_type": 1,
                                        "value": "get_order_info_by_order_id.chatbot_order_status",
                                        "api_id": "get_order_info_by_order_id",
                                        "render": "Chatbot order status",
                                        "api_name": "getOrderInfoByOrderId"
                                    },
                                    {
                                        "value": "options",
                                        "render": "Options"
                                    },
                                    {
                                        "source_type": 3,
                                        "value": "6",
                                        "render": "Buyer To Receive - Delivered Integrated"
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
                "logics": [
                    2,
                    2
                ]
            }
        },
        "branch_action": {
            "read_write_ctrl": 2,
            "value": "jump_node"
        },
        "jump_node": {
            "read_write_ctrl": 2,
            "value": {
                "taskbot_id": "SOP15",
                "next_node_id": "SOP15_Node23",
                "port_id": "912ecc66-63d3-43d7-84c9-6fdf80c438b4"
            }
        },
        "variate_assignment": {
            "read_write_ctrl": 2,
            "value": []
        },
        "show_condition": {
            "read_write_ctrl": null,
            "value": false
        },
        "node_template_id": "chatbot_system",
        "advance_setting": {
            "read_write_ctrl": null,
            "value": {
                "feedback": false,
                "end_tag": false,
                "follow_up": false,
                "next_node": {
                    "taskbot_id": "",
                    "next_node_id": ""
                },
                "open_data_tracking": false,
                "data_tracking": null,
                "chat_with_seller": false,
                "agent_case_id": 0
            }
        }
    },
    {
        "desc": {
            "read_write_ctrl": null,
            "value": "Completed"
        },
        "shadow_config": {
            "read_write_ctrl": null,
            "value": {
                "is_default": false,
                "case_id": "",
                "condition_id": "condition_5"
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
                                        "value": "API",
                                        "render": "API"
                                    },
                                    {
                                        "source_type": 1,
                                        "value": "get_order_info_by_order_id.chatbot_order_status",
                                        "api_id": "get_order_info_by_order_id",
                                        "render": "Chatbot order status",
                                        "api_name": "getOrderInfoByOrderId"
                                    },
                                    {
                                        "value": "options",
                                        "render": "Options"
                                    },
                                    {
                                        "source_type": 3,
                                        "value": "7",
                                        "render": "Buyer Completed"
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
        "branch_action": {
            "read_write_ctrl": 2,
            "value": "jump_node"
        },
        "jump_node": {
            "read_write_ctrl": 2,
            "value": {
                "taskbot_id": "SOP10",
                "next_node_id": "SOP10_Node32",
                "port_id": "ca12284e-8b63-43d9-869d-f8c5bb12ec8d"
            }
        },
        "variate_assignment": {
            "read_write_ctrl": 2,
            "value": []
        },
        "show_condition": {
            "read_write_ctrl": null,
            "value": false
        },
        "node_template_id": "chatbot_system",
        "advance_setting": {
            "read_write_ctrl": null,
            "value": {
                "feedback": false,
                "end_tag": false,
                "follow_up": false,
                "next_node": {
                    "taskbot_id": "",
                    "next_node_id": ""
                },
                "open_data_tracking": false,
                "data_tracking": null,
                "chat_with_seller": false,
                "agent_case_id": 0
            }
        }
    },
    {
        "desc": {
            "read_write_ctrl": null,
            "value": "Cancelled"
        },
        "shadow_config": {
            "read_write_ctrl": null,
            "value": {
                "is_default": false,
                "case_id": "",
                "condition_id": "condition_6"
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
                                        "value": "API",
                                        "render": "API"
                                    },
                                    {
                                        "source_type": 1,
                                        "value": "get_order_info_by_order_id.chatbot_order_status",
                                        "api_id": "get_order_info_by_order_id",
                                        "render": "Chatbot order status",
                                        "api_name": "getOrderInfoByOrderId"
                                    },
                                    {
                                        "value": "options",
                                        "render": "Options"
                                    },
                                    {
                                        "source_type": 3,
                                        "value": "8",
                                        "render": "Buyer Cancelled"
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
        "branch_action": {
            "read_write_ctrl": 2,
            "value": "jump_node"
        },
        "jump_node": {
            "read_write_ctrl": 2,
            "value": {
                "taskbot_id": "SOP15",
                "next_node_id": "SOP15_Node26",
                "port_id": "80b5dd55-5261-43d0-b526-236f90f17a30"
            }
        },
        "variate_assignment": {
            "read_write_ctrl": 2,
            "value": []
        },
        "show_condition": {
            "read_write_ctrl": null,
            "value": false
        },
        "node_template_id": "chatbot_system",
        "advance_setting": {
            "read_write_ctrl": null,
            "value": {
                "feedback": false,
                "end_tag": false,
                "follow_up": false,
                "next_node": {
                    "taskbot_id": "",
                    "next_node_id": ""
                },
                "open_data_tracking": false,
                "data_tracking": null,
                "chat_with_seller": false,
                "agent_case_id": 0
            }
        }
    },
    {
        "desc": {
            "read_write_ctrl": null,
            "value": "Return/Refund"
        },
        "shadow_config": {
            "read_write_ctrl": null,
            "value": {
                "is_default": false,
                "case_id": "",
                "condition_id": "condition_7"
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
                                        "value": "API",
                                        "render": "API"
                                    },
                                    {
                                        "source_type": 1,
                                        "value": "get_order_info_by_order_id.chatbot_order_status",
                                        "api_id": "get_order_info_by_order_id",
                                        "render": "Chatbot order status",
                                        "api_name": "getOrderInfoByOrderId"
                                    },
                                    {
                                        "value": "options",
                                        "render": "Options"
                                    },
                                    {
                                        "source_type": 3,
                                        "value": "9",
                                        "render": "Buyer Return Refund"
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
        "branch_action": {
            "read_write_ctrl": 2,
            "value": "jump_node"
        },
        "jump_node": {
            "read_write_ctrl": 2,
            "value": {
                "taskbot_id": "SOP15",
                "next_node_id": "SOP15_Node25",
                "port_id": "35c0bf82-6a15-468a-9d86-44f543ed74d4"
            }
        },
        "variate_assignment": {
            "read_write_ctrl": 2,
            "value": []
        },
        "show_condition": {
            "read_write_ctrl": null,
            "value": false
        },
        "node_template_id": "chatbot_system",
        "advance_setting": {
            "read_write_ctrl": null,
            "value": {
                "feedback": false,
                "end_tag": false,
                "follow_up": false,
                "next_node": {
                    "taskbot_id": "",
                    "next_node_id": ""
                },
                "open_data_tracking": false,
                "data_tracking": null,
                "chat_with_seller": false,
                "agent_case_id": 0
            }
        }
    }
]'''
