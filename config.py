#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8558068232:AAH5KdtBDzqBFjVJ0Tam7z9CgbUVOG8RXWo")
    API_ID = int(os.environ.get("API_ID", "27351883"))
    API_HASH = os.environ.get("API_HASH", "e571454385d31ca3035c0c9dd69e78fa")
    AUTH_USERS = "8245649452"


