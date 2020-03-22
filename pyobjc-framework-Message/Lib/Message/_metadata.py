# This file is generated by objective.metadata
#
# Last update: Sun Mar 22 17:13:41 2020
#
# flake8: noqa

import objc, sys

if sys.maxsize > 2 ** 32:

    def sel32or64(a, b):
        return b


else:

    def sel32or64(a, b):
        return a


misc = {}
constants = """$NSASCIIMailFormat$NSMIMEMailFormat$NSSMTPDeliveryProtocol$NSSendmailDeliveryProtocol$"""
enums = """$$"""
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"NSMailDelivery",
        b"deliverMessage:headers:format:protocol:",
        {"retval": {"type": "Z"}},
    )
    r(b"NSMailDelivery", b"deliverMessage:subject:to:", {"retval": {"type": "Z"}})
    r(b"NSMailDelivery", b"hasDeliveryClassBeenConfigured", {"retval": {"type": "Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
