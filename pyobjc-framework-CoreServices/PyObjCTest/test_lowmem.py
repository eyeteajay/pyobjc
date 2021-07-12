import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestLowMem(TestCase):
    def assert_not_wrapped(self, name):
        self.assertTrue(
            not hasattr(CoreServices, name), f"{name!r} exposed in bindings"
        )

    def test_not_wrapped(self):
        self.assert_not_wrapped("LMGetMemTop")
        self.assert_not_wrapped("LMSetMemTop")
        self.assert_not_wrapped("LMGetBufPtr")
        self.assert_not_wrapped("LMSetBufPtr")
        self.assert_not_wrapped("LMGetHeapEnd")
        self.assert_not_wrapped("LMSetHeapEnd")
        self.assert_not_wrapped("LMGetCPUFlag")
        self.assert_not_wrapped("LMSetCPUFlag")
        self.assert_not_wrapped("LMGetRndSeed")
        self.assert_not_wrapped("LMSetRndSeed")
        self.assert_not_wrapped("LMGetSEvtEnb")
        self.assert_not_wrapped("LMSetSEvtEnb")
        self.assert_not_wrapped("LMGetBootDrive")
        self.assert_not_wrapped("LMSetBootDrive")
        self.assert_not_wrapped("LMGetSdVolume")
        self.assert_not_wrapped("LMSetSdVolume")
        self.assert_not_wrapped("LMGetSoundPtr")
        self.assert_not_wrapped("LMSetSoundPtr")
        self.assert_not_wrapped("LMGetSoundBase")
        self.assert_not_wrapped("LMSetSoundBase")
        self.assert_not_wrapped("LMGetSoundLevel")
        self.assert_not_wrapped("LMSetSoundLevel")
        self.assert_not_wrapped("LMGetCurPitch")
        self.assert_not_wrapped("LMSetCurPitch")
        self.assert_not_wrapped("LMGetScrDmpEnb")
        self.assert_not_wrapped("LMSetScrDmpEnb")
        self.assert_not_wrapped("LMGetBufTgFNum")
        self.assert_not_wrapped("LMSetBufTgFNum")
        self.assert_not_wrapped("LMGetBufTgFFlg")
        self.assert_not_wrapped("LMSetBufTgFFlg")
        self.assert_not_wrapped("LMGetBufTgFBkNum")
        self.assert_not_wrapped("LMSetBufTgFBkNum")
        self.assert_not_wrapped("LMGetBufTgDate")
        self.assert_not_wrapped("LMSetBufTgDate")
        self.assert_not_wrapped("LMGetMinStack")
        self.assert_not_wrapped("LMSetMinStack")
        self.assert_not_wrapped("LMGetDefltStack")
        self.assert_not_wrapped("LMSetDefltStack")
        self.assert_not_wrapped("LMGetGZRootHnd")
        self.assert_not_wrapped("LMSetGZRootHnd")
        self.assert_not_wrapped("LMGetGZMoveHnd")
        self.assert_not_wrapped("LMSetGZMoveHnd")
        self.assert_not_wrapped("LMGetToExtFS")
        self.assert_not_wrapped("LMSetToExtFS")
        self.assert_not_wrapped("LMGetJStash")
        self.assert_not_wrapped("LMSetJStash")
        self.assert_not_wrapped("LMGetCurApRefNum")
        self.assert_not_wrapped("LMSetCurApRefNum")
        self.assert_not_wrapped("LMGetCurStackBase")
        self.assert_not_wrapped("LMSetCurStackBase")
        self.assert_not_wrapped("LMGetCurPageOption")
        self.assert_not_wrapped("LMSetCurPageOption")
        self.assert_not_wrapped("LMGetPrintErr")
        self.assert_not_wrapped("LMSetPrintErr")
        self.assert_not_wrapped("LMGetApFontID")
        self.assert_not_wrapped("LMSetApFontID")
        self.assert_not_wrapped("LMGetOneOne")
        self.assert_not_wrapped("LMSetOneOne")
        self.assert_not_wrapped("LMGetMinusOne")
        self.assert_not_wrapped("LMSetMinusOne")
        self.assert_not_wrapped("LMGetSysMap")
        self.assert_not_wrapped("LMSetSysMap")
        self.assert_not_wrapped("LMGetResLoad")
        self.assert_not_wrapped("LMSetResLoad")
        self.assert_not_wrapped("LMGetResErr")
        self.assert_not_wrapped("LMSetResErr")
        self.assert_not_wrapped("LMGetTmpResLoad")
        self.assert_not_wrapped("LMSetTmpResLoad")
        self.assert_not_wrapped("LMGetIntlSpec")
        self.assert_not_wrapped("LMSetIntlSpec")
        self.assert_not_wrapped("LMGetSysFontFam")
        self.assert_not_wrapped("LMSetSysFontFam")
        self.assert_not_wrapped("LMGetSysFontSize")
        self.assert_not_wrapped("LMSetSysFontSize")
        self.assert_not_wrapped("LMGetCurApName")
        self.assert_not_wrapped("LMSetCurApName")
        self.assert_not_wrapped("LMGetSysResName")
        self.assert_not_wrapped("LMSetSysResName")
        self.assert_not_wrapped("LMGetFinderName")
        self.assert_not_wrapped("LMSetFinderName")
        self.assert_not_wrapped("LMGetToolScratch")
        self.assert_not_wrapped("LMSetToolScratch")
        self.assert_not_wrapped("LMGetLvl2DT")
        self.assert_not_wrapped("LMSetLvl2DT")
        self.assert_not_wrapped("LMGetHighHeapMark")
        self.assert_not_wrapped("LMSetHighHeapMark")
        self.assert_not_wrapped("LMGetStackLowPoint")
        self.assert_not_wrapped("LMSetStackLowPoint")
        self.assert_not_wrapped("LMGetDiskFormatingHFSDefaults")
        self.assert_not_wrapped("LMSetDiskFormatingHFSDefaults")
