#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Appier Framework
# Copyright (C) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Appier Framework.
#
# Hive Appier Framework is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Appier Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Appier Framework. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

import imp
import types

import email.mime.text
import email.mime.multipart

def message(
    sender,
    receivers,
    contents,
    host = None,
    port = 25,
    username = None,
    password = None,
    stls = False
):
    is_contents = type(contents) in types.StringTypes
    if not is_contents: contents = contents.as_string()
    engine = smtp_engine()
    method = globals()["message_" + engine]
    return method(
        sender,
        receivers,
        contents,
        host = host,
        port = port,
        username = username,
        password = password,
        stls = stls
    )

def message_base(
    sender,
    receivers,
    contents,
    host = None,
    port = 25,
    username = None,
    password = None,
    stls = False,
    *args,
    **kwargs
):
    pass

def message_netius(
    sender,
    receivers,
    contents,
    host = None,
    port = 25,
    username = None,
    password = None,
    stls = False,
    *args,
    **kwargs
):
    import netius.clients
    smtp_client = netius.clients.SMTPClient(auto_close = True)
    smtp_client.message(
        [sender],
        receivers,
        contents,
        host = host,
        port = port,
        username = username,
        password = password,
        stls = stls
    )

def smtp_engine():
    try: imp.find_module("netius")
    except: return "base"
    return "netius"

def multipart():
    return email.mime.multipart.MIMEMultipart("alternative")

def plain(contents):
    return email.mime.text.MIMEText(contents, "plain")

def html(contents):
    return email.mime.text.MIMEText(contents, "html")