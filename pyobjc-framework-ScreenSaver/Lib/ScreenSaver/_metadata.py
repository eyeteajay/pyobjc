# This file is generated by objective.metadata
#
# Last update: Sun Mar 22 17:45:28 2020
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
constants = """$$"""
enums = """$$"""
misc.update({})
functions = {
    "SSRandomPointForSizeWithinRect": (
        sel32or64(
            b"{_NSPoint=ff}{_NSSize=ff}{_NSRect={_NSPoint=ff}{_NSSize=ff}}",
            b"{CGPoint=dd}{CGSize=dd}{CGRect={CGPoint=dd}{CGSize=dd}}",
        ),
    ),
    "SSRandomIntBetween": (b"iii",),
    "SSRandomFloatBetween": (sel32or64(b"fff", b"ddd"),),
    "SSCenteredRectInRect": (
        sel32or64(
            b"{_NSRect={_NSPoint=ff}{_NSSize=ff}}{_NSRect={_NSPoint=ff}{_NSSize=ff}}{_NSRect={_NSPoint=ff}{_NSSize=ff}}",
            b"{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}{CGRect={CGPoint=dd}{CGSize=dd}}",
        ),
    ),
}
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(b"ScreenSaverView", b"hasConfigureSheet", {"retval": {"type": "Z"}})
    r(
        b"ScreenSaverView",
        b"initWithFrame:isPreview:",
        {"arguments": {3: {"type": "Z"}}},
    )
    r(b"ScreenSaverView", b"isAnimating", {"retval": {"type": "Z"}})
    r(b"ScreenSaverView", b"isPreview", {"retval": {"type": "Z"}})
    r(b"ScreenSaverView", b"performGammaFade", {"retval": {"type": "Z"}})
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
