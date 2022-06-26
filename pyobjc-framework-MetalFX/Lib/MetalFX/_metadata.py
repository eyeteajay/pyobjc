# This file is generated by objective.metadata
#
# Last update: Sun Jun 26 10:58:27 2022
#
# flake8: noqa

import objc, sys
from typing import NewType

if sys.maxsize > 2**32:

    def sel32or64(a, b):
        return b

else:

    def sel32or64(a, b):
        return a


if objc.arch == "arm64":

    def selAorI(a, b):
        return a

else:

    def selAorI(a, b):
        return b


misc = {}
constants = """$$"""
enums = """$MTLFXSpatialScalerColorProcessingMode_HDR@2$MTLFXSpatialScalerColorProcessingMode_Linear@1$MTLFXSpatialScalerColorProcessingMode_Perceptual@0$MTLFXSpatialScalerVersion_End@1$MTLFXSpatialScalerVersion_v1@0$MTLFXTemporalScalerVersion_End@1$MTLFXTemporalScalerVersion_v1@0$"""
misc.update(
    {
        "MTLFXTemporalScalerVersion": NewType("MTLFXTemporalScalerVersion", int),
        "MTLFXSpatialScalerVersion": NewType("MTLFXSpatialScalerVersion", int),
        "MTLFXSpatialScalerColorProcessingMode": NewType(
            "MTLFXSpatialScalerColorProcessingMode", int
        ),
    }
)
misc.update({})
misc.update({})
r = objc.registerMetaDataForSelector
objc._updatingMetadata(True)
try:
    r(
        b"MTLFXTemporalScalerDescriptor",
        b"enableInputContentProperties",
        {"retval": {"type": b"Z"}},
    )
    r(
        b"MTLFXTemporalScalerDescriptor",
        b"setEnableInputContentProperties:",
        {"arguments": {2: {"type": b"Z"}}},
    )
    r(b"NSObject", b"colorProcessingMode", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"colorTexture", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"colorTextureFormat", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"colorTextureUsage", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"depthTexture", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"depthTextureFormat", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"depthTextureUsage", {"required": True, "retval": {"type": b"Q"}})
    r(
        b"NSObject",
        b"encodeToCommandBuffer:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(b"NSObject", b"fence", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"inputContentHeight", {"required": True, "retval": {"type": b"Q"}})
    r(
        b"NSObject",
        b"inputContentMaxScale",
        {"required": True, "retval": {"type": b"f"}},
    )
    r(
        b"NSObject",
        b"inputContentMinScale",
        {"required": True, "retval": {"type": b"f"}},
    )
    r(b"NSObject", b"inputContentWidth", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"inputHeight", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"inputWidth", {"required": True, "retval": {"type": b"Q"}})
    r(
        b"NSObject",
        b"jitterOffset",
        {"required": True, "retval": {"type": b"{CGPoint=dd}"}},
    )
    r(b"NSObject", b"motionTexture", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"motionTextureFormat", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"motionTextureUsage", {"required": True, "retval": {"type": b"Q"}})
    r(
        b"NSObject",
        b"motionVectorScale",
        {"required": True, "retval": {"type": b"{CGPoint=dd}"}},
    )
    r(b"NSObject", b"outputHeight", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"outputTexture", {"required": True, "retval": {"type": b"@"}})
    r(b"NSObject", b"outputTextureFormat", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"outputTextureUsage", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"outputWidth", {"required": True, "retval": {"type": b"Q"}})
    r(b"NSObject", b"reset", {"required": True, "retval": {"type": b"Z"}})
    r(b"NSObject", b"reversedDepth", {"required": True, "retval": {"type": b"Z"}})
    r(
        b"NSObject",
        b"setColorTexture:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setDepthTexture:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setFence:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setInputContentHeight:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"Q"}}},
    )
    r(
        b"NSObject",
        b"setInputContentWidth:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"Q"}}},
    )
    r(
        b"NSObject",
        b"setJitterOffset:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"{CGPoint=dd}"}},
        },
    )
    r(
        b"NSObject",
        b"setMotionTexture:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setMotionVectorScale:",
        {
            "required": True,
            "retval": {"type": b"v"},
            "arguments": {2: {"type": b"{CGPoint=dd}"}},
        },
    )
    r(
        b"NSObject",
        b"setOutputTexture:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"@"}}},
    )
    r(
        b"NSObject",
        b"setReset:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"Z"}}},
    )
    r(
        b"NSObject",
        b"setReversedDepth:",
        {"required": True, "retval": {"type": b"v"}, "arguments": {2: {"type": b"Z"}}},
    )
finally:
    objc._updatingMetadata(False)
expressions = {}

# END OF FILE
