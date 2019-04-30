#
# PySNMP MIB module ADVA-FSPR7-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADVA-FSPR7-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:59:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
fspR7, = mibBuilder.importSymbols("ADVA-MIB", "fspR7")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, MibIdentifier, Counter32, ObjectIdentity, IpAddress, Counter64, Unsigned32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress", "Counter64", "Unsigned32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
advaFspR7Tc = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 11, 8))
advaFspR7Tc.setRevisions(('2014-10-15 00:00', '2014-09-29 00:00', '2013-12-04 00:00', '2013-08-20 00:00', '2011-05-22 00:00',))
if mibBuilder.loadTexts: advaFspR7Tc.setLastUpdated('201410150000Z')
if mibBuilder.loadTexts: advaFspR7Tc.setOrganization('ADVA Optical Networking')
class ApsRevertMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("nonrevertive", 1), ("revertive", 2))

class ApsRevertModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNonrevertive", 1), ("capRevertive", 2))

class ApsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20))
    namedValues = NamedValues(("undefined", 0), ("line", 2), ("sncN", 3), ("sncI", 4), ("sncS", 5), ("eth", 6), ("phys", 7), ("sncNPM", 8), ("sncNTCM", 9), ("sncISM", 10), ("mux", 11), ("pcs", 12), ("ethSncI", 13), ("ethSncN", 14), ("ethSncS", 15), ("ethSncT", 16), ("sncNLine", 18), ("sncNPath", 19), ("path", 20))

class ApsTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capLine", 2), ("capSncN", 3), ("capSncI", 4), ("capSncS", 5), ("capEth", 6), ("capPhys", 7), ("capSncNPM", 8), ("capSncNTCM", 9), ("capSncISM", 10), ("capMux", 11), ("capPcs", 12), ("capEthSncI", 13), ("capEthSncN", 14), ("capEthSncS", 15), ("capEthSncT", 16), ("capSncNLine", 18), ("capSncNPath", 19), ("capPath", 20))

class ConnectionNotation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("fromToNotation", 1), ("toFromNotation", 2))

class Counter64StringCaps(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class EntityClassName(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 37, 38, 39, 40, 41, 42, 43, 44, 46, 47, 49, 57, 58, 64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 105, 106, 111, 116, 118, 119, 141, 144, 145, 146))
    namedValues = NamedValues(("undefined", 0), ("ne", 1), ("shelf", 2), ("fcuc", 3), ("fcu", 4), ("modc", 5), ("mod", 6), ("psh", 7), ("plc", 8), ("pl", 9), ("fanc", 10), ("fan", 11), ("ptp", 12), ("fpl", 13), ("ol", 14), ("om", 15), ("ch", 16), ("pch", 17), ("vch", 18), ("sts1", 19), ("sts3c", 20), ("sts24c", 21), ("sts48c", 22), ("vc3", 23), ("vc4", 24), ("vs1", 25), ("sdcc", 26), ("ldcc", 27), ("pdcc", 28), ("eoc", 29), ("gcc0", 30), ("gcc1", 31), ("gcc2", 32), ("sc", 33), ("link", 34), ("otl", 37), ("tifi", 38), ("tifo", 39), ("sh", 40), ("lan", 41), ("conn", 42), ("ffpCh", 43), ("ffpOm", 44), ("crsDcn", 46), ("crsCh", 47), ("wch", 49), ("eth", 57), ("veth", 58), ("fch", 64), ("vc4c8", 65), ("vc4c16", 66), ("vs0", 67), ("vsch", 68), ("ech", 69), ("vtp", 70), ("vech", 72), ("vconn", 73), ("otlg", 74), ("owlg", 75), ("rat", 105), ("tc", 106), ("vsffpCh", 111), ("vom", 116), ("vch1", 118), ("ffpVch1", 119), ("pc", 141), ("whitelist", 144), ("uch", 145), ("fc", 146))

class EntityType(TextualConvention, Integer32):
    status = 'current'

class EquipmentState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("equipped", 1), ("unequipped", 2))

class FfpType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("normal", 1), ("forced", 2))

class FfpTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNormal", 1), ("capForced", 2))

class Grade(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("gradeA", 1), ("gradeB", 2), ("gradeGdps", 3), ("gradeC", 4))

class FspR7AdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("uas", 1), ("is", 2), ("ains", 3), ("mgt", 4), ("mt", 5), ("dsbld", 6), ("pps", 7))

class FspR7AdminStateCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capUas", 1), ("capIs", 2), ("capAins", 3), ("capMgt", 4), ("capMt", 5), ("capDsbld", 6), ("capPps", 7))

class FspR7AidType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("sys", 2), ("eqpt", 3), ("ch", 4), ("dcn", 5), ("ol", 6), ("om", 7), ("sts1", 8), ("sts3c", 9), ("sts24c", 10), ("sts48c", 11), ("vc3", 12), ("vc4", 13), ("vs1", 14), ("vs4c", 15), ("sh", 16), ("lif", 17), ("lifCp", 18), ("tnlWdm", 19), ("vc4c8", 20), ("vc4c16", 21), ("otl", 22), ("tnlEth", 24), ("tnlOtn", 25))

class FspR7AlarmListType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 96, 97, 99, 100, 101, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 119, 120, 122, 123, 125, 127, 128, 129, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 263, 264, 265, 266, 267, 268, 269, 272, 274, 276, 277, 278, 279, 280, 281, 283, 285, 287, 289, 291, 293, 294, 295, 296, 297, 298, 300, 301, 302), SingleValueConstraint(304, 306, 308, 310, 311, 313, 315, 317, 319, 321, 323, 325, 327, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 350, 352, 354, 356, 358, 360, 362, 364, 366, 367, 368, 369, 370, 371, 373, 375, 377, 379, 381, 383, 385, 386, 387, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 406, 407, 408, 409, 410, 411, 412, 413, 414, 420, 422, 423, 424, 432, 434, 435))
    namedValues = NamedValues(("undefined", 0), ("terminalLoopback", 5), ("oosDisabled", 6), ("oosManagement", 7), ("oosMaintenance", 8), ("oosAins", 9), ("removed", 10), ("lossOfSignal", 11), ("optInputPwrReceivedTooLow", 12), ("optInputPwrReceivedTooHigh", 13), ("laserTemperatureTooHigh", 14), ("laserTemperatureTooLow", 15), ("optOutputPowerTransTooLow", 16), ("optOutputPowerTransTooHigh", 17), ("autoShutdownToHighTemp", 18), ("autoShutdownToHighTxPwr", 19), ("laserEndOfLife", 20), ("serverSignalFailureVf", 21), ("equalizationProgress", 22), ("uPortFailure", 23), ("autoShutdownBlock", 24), ("autoPowerShutdown", 25), ("confOutPowerTransTooHigh", 26), ("confOutPowerTransTooLow", 27), ("optSignalFailure", 28), ("dsbdChannelPowerTooHigh", 29), ("lossOfSignalCPort", 30), ("lossOfSignalNPort", 31), ("outputPowerFault", 32), ("eqlzAdjust", 33), ("ampFailure", 34), ("eqptProvMismatch", 35), ("backreflectionTooHigh", 36), ("fiberConnLos", 48), ("fiberConnOptFault", 49), ("fiberConnInvalid", 50), ("fiberConnMismatch", 51), ("fiberConnCommError", 52), ("fiberConnProtocolFailure", 53), ("fiberConnDataFailure", 54), ("fiberAttenuationHigh", 55), ("laserBiasCurrAbnormal", 57), ("fiberConnInvalidTx", 58), ("fiberConnMismatchTx", 59), ("fiberAttenuationHighTx", 60), ("laserFailure", 61), ("lossOfReceiverClockRecovery", 62), ("fiberAttenuationCond", 63), ("channelMismatch", 64), ("alarmIndicationSignalLine", 65), ("alarmIndicationSignalLowerOrderPath", 66), ("alarmIndicationSignalOdu", 67), ("alarmIndicationSignalOpu", 68), ("alarmIndicationSignalOtu", 69), ("alarmIndicationSignalHigherOrderPath", 70), ("alarmIndicationSignalOduTcmA", 71), ("alarmIndicationSignalOduTcmB", 72), ("alarmIndicationSignalOduTcmC", 73), ("virtualChannelAis", 74), ("amplifierAbnormal", 75), ("automaticPowerReduction", 76), ("automaticPowerReductionForEyeSafety", 77), ("apsConfigMismatch", 80), ("apsProtocolFailure", 81), ("aseLow", 82), ("aseTableGenFailLow", 83), ("aseTableGenFailHighBackreflection", 84), ("aseTableGenFailOscMissing", 85), ("aseTableGenFailPilot", 86), ("aseTableGenFailSignalinput", 87), ("aseTableNotAvailable", 88), ("aseTableGenProgress", 89), ("encryptionPortAuthPasswdMissing", 90), ("backwardDefectIndicationOdu", 92), ("backwardDefectIndicationOtu", 93), ("backwardDefectIndicationOduTcmA", 94), ("backwardDefectIndicationOduTcmB", 95), ("backwardDefectIndicationOduTcmC", 96), ("topologyDataCalculationInProgress", 97), ("dispertionTunningCondition", 99), ("lossOfCharSync", 100), ("lossOfCharSyncFromFarEnd", 101), ("encryptionPortEncryptionSwitchOffEnabled", 103), ("encryptionModuleCryPasswdMissing", 104), ("encryptionModuleSelfTestStarted", 107), ("encryptionPortEncryptionSwitchedOff", 108), ("opuClientSignalFail", 109), ("databaseMismatch", 110), ("databaseFailure", 111), ("databaseNcuMismatch", 112), ("dbReplicationIncompleted", 113), ("databaseVersionMismatch", 114), ("xfpDecisionThresSetFailed", 115), ("duplexLinkFailure", 116), ("singleFanFailure", 118), ("multipleFanFailure", 119), ("lossOfSignalTransmitter", 120), ("farEndIpAddressUnknown", 122), ("farEndCommFailure", 123), ("backupForcedToHalt", 125), ("facilityForcedOn", 127), ("fwdAseTableFailPilot", 128), ("fwdAseTableOnPilot", 129), ("encryptionModuleFwpUpdateEnabled", 131), ("fwpMismatchDownloadNotServiceAffecting", 132), ("fwpMismatchDownloadServiceAffecting", 133), ("gainTiltNotSettable", 135), ("highBer", 136), ("receiverOverloadProtection", 137), ("hwInitializing", 138), ("hwOprReachedHT", 139), ("hwDegrade", 140), ("hwFailure", 141), ("switchtoProtectionInhibited", 142), ("switchtoWorkingInhibited", 143), ("encryptionPortKeyInitExchgMissed", 148), ("encryptionPortMaxKeyExchgFailuresReachedIs", 149), ("encryptionPortMaxKeyExchgFailuresReachedOos", 150), ("encryptionPortKeyExchangedForced", 151), ("laserOnDelay", 152), ("lockedDefectOdu", 153), ("lockedDefectOduTcmA", 154), ("lockedDefectOduTcmB", 155), ("lockedDefectOduTcmC", 156), ("linkControlProtocolFailure", 157), ("linkDown", 158), ("autoShutdownSendingAisLine", 159), ("autoShutdownSendingAisOdu", 160), ("autoShutdownSendingAisOpu", 161), ("clientFailForwarding", 162), ("autoShutdownAls", 163), ("autoAmpShutdown", 164), ("autoShutdownAmpAps", 165), ("aseTableBuild", 166), ("autoShutdownOpuClientSignalFail", 167), ("autoShutdownSendingEPC", 168), ("autoShutdownSendingLckOdu", 169), ("autoShutdownSendingOciOdu", 170), ("autoShutdownLaserOffDueToErrFwd", 171), ("autoShutdownTxRxLasersDueToHighTemp", 172), ("localFault", 173), ("localOscLevelAbnormal", 174), ("lossOfGfpFrame", 175), ("lossOfFrameMux", 176), ("lossOfFrameOtu", 177), ("lossOfFrame", 178), ("lossOfFrameLossOfMultiFrameOdu", 179), ("lossOfLane", 180), ("lossofMultiframeLowerOrderPath", 181), ("lossOfMultiFrameOtu", 182), ("lossofMultiframeHigherOrderPath", 183), ("lossOfPointerLowerOrderPath", 184), ("lossOfPointerHigherOrderPath", 185), ("losAttProgress", 186), ("lossOsc", 187), ("gfpLossOfClientSig", 188), ("loopbackError", 189), ("facilityLoopback", 190), ("lossofTandemConnectionOduTcmA", 191), ("lossofTandemConnectionOduTcmB", 192), ("lossofTandemConnectionOduTcmC", 193), ("mansw", 194), ("equipmentNotAccepted", 197), ("equipmentNotApproved", 198), ("capabilityLevelMismatch", 199), ("equipmentMismatch", 200), ("equipmentNotSupportedByPhysicalLayer", 201), ("meaSwRevision", 202), ("mismatch", 203), ("midstageFault", 204), ("multiplexStructureIdentifierMismatchOPU", 205), ("backupNotResponding", 206), ("openConnectionIndicationOdu", 207), ("openConnectionIndicationOduTcmA", 208), ("openConnectionIndicationOduTcmB", 209), ("openConnectionIndicationOduTcmC", 210), ("oduTribMsiMismatch", 211), ("transmitterDisabledOff", 212), ("receiverDisabled", 213), ("opmAbnormalCondition", 214), ("faultOnOpm", 215), ("thresOptPowerCtrlFailureHigh", 216), ("thresOptPowerCtrlFailureLow", 217), ("txPowerLimited", 218), ("oscOpticalPowerControlFailHigh", 219), ("oscOpticalPowerControlFailLow", 220), ("oTDRMeasuringinProgress", 221), ("encryptionModuleCryPasswdError", 222), ("peerLink", 223), ("pilotReceiveLevelHigh", 224), ("lossOfPilotSignal", 225), ("payloadMismatchGfp", 226), ("payloadMismatchLowerOrderPath", 227), ("payloadMismatchOPU", 228), ("payloadMismatchHigherOrderPath", 229), ("provPayloadMismatch", 230), ("prbsLossOfSeqSynch", 231), ("prbsRcvActivated", 232), ("prbsTrmtActivated", 233), ("protectionNotAvailable", 234), ("powerSupplyUnitFailure", 235), ("maxPowerConsProvModulesToHigh", 236), ("maxPowerConsEquipModulesToHigh", 237), ("powerMissing", 238), ("remoteDefectIndicationLine", 239), ("remoteDefectIndicationLowerOrderPath", 240), ("remoteDefectIndicationHigherOrderPath", 241), ("dcnCommunicationFail", 243), ("ntpForSchedEqlzRequired", 244), ("signalDegradeOlm", 245), ("signalDegradeLine", 246), ("signalDegradationonLinkVector", 247), ("signalDegradeOdu", 248), ("signalDegradeOtu", 249), ("pcsSignalDegrade", 250), ("signalDegradeScn", 251), ("signalDegradeOduTcmA", 252), ("signalDegradeOduTcmB", 253), ("signalDegradeOduTcmC", 254), ("encryptionModuleSelfTestFail", 255), ("encryptionModuleSelfTestFailCritical", 256), ("signalFailureOnLink", 257), ("signalFailureonLinkVector", 258), ("signalFailureOPU", 259), ("serverSignalFailTx", 260), ("facilityDataRateNotSupported", 261), ("lossofSequenceLowerOrderPath", 263), ("lossofSequenceHigherOrderPath", 264), ("serverSignalFail", 265), ("serverSignalFailureGfp", 266), ("serverSignalFailureODU", 267), ("serverSignalFailurePath", 268), ("serverSignalFailureSectionRS", 269), ("switchToDuplexInhibited", 272), ("switchFailed", 274), ("currentTooHigh", 276), ("attOnReceiverFiberHigherThanMonitor", 277), ("attOnReceiverFiberLowerThanMonitor", 278), ("attOnTransmitterFiberHigherThanMonitor", 279), ("attOnTransmitterFiberLowerThanMonitor", 280), ("thres15MinExceededOduBbe", 281), ("thres15MinExceededOtuBbe", 283), ("thres15MinExceededOduTcmABbe", 285), ("thres15MinExceededOduTcmBBbe", 287), ("thres15MinExceededOduTcmCBbe", 289), ("thres15MinExceededFecBERCE", 291), ("brPwrRxTooHigh", 293), ("chromaticDispersionTooHigh", 294), ("chromaticDispersionTooLow", 295), ("dispersionCompensationTooHigh", 296), ("dispersionCompensationTooLow", 297), ("thres15MinExceededFecCE", 298), ("carrierFreqOffsetTooHigh", 300), ("carrierFreqOffsetTooLow", 301), ("thres15MinExceededSonetLineCV", 302)) + NamedValues(("thres15MinExceededPhysConvCV", 304), ("thres15MinExceededSonetSectCV", 306), ("thres15MinExceededPhysConvDE", 308), ("differentialGroupDelayTooHigh", 310), ("thres15MinExceededFecES", 311), ("thres15MinExceededSonetLineES", 313), ("thres15MinExceededOduES", 315), ("thres15MinExceededOtuES", 317), ("thres15MinExceededPhysConvES", 319), ("thres15MinExceededSonetSectES", 321), ("thres15MinExceededOduTcmAES", 323), ("thres15MinExceededOduTcmBES", 325), ("thres15MinExceededOduTcmCES", 327), ("latencyTooHigh", 329), ("latencyTooLow", 330), ("laserBiasCurrentNormalizedtooHigh", 331), ("localOscTemperatureTooHigh", 332), ("localOscTemperatureTooLow", 333), ("pumpLaser1TempTooHigh", 334), ("pumpLaser1TempTooLow", 335), ("pumpLaser2TempTooHigh", 336), ("pumpLaser2TempTooLow", 337), ("pumpLaser3TempTooHigh", 338), ("pumpLaser3TempTooLow", 339), ("pumpLaser4TempTooHigh", 340), ("pumpLaser4TempTooLow", 341), ("oscPwrTooHigh", 342), ("oscPwrTooLow", 343), ("ramanPumpPwrTooHigh", 344), ("ramanPumpPwrTooLow", 345), ("roundTripDelayTooHigh", 346), ("roundTripDelayTooLow", 347), ("thres15MinExceededSonetSectSEFS", 348), ("thres15MinExceededFecSES", 350), ("thres15MinExceededSonetLineSES", 352), ("thres15MinExceededOduSES", 354), ("thres15MinExceededOtuSES", 356), ("thres15MinExceededSonetSectSES", 358), ("thres15MinExceededOduTcmASES", 360), ("thres15MinExceededOduTcmBSES", 362), ("thres15MinExceededOduTcmCSES", 364), ("logicalLanesSkewTooHigh", 366), ("signalToNoiseRatioTooLow", 367), ("subModuleTempTooHigh", 368), ("temperatureTooHigh", 369), ("temperatureTooLow", 370), ("thres15MinExceededSonetLineUAS", 371), ("thres15MinExceededOduUAS", 373), ("thres15MinExceededOtuUAS", 375), ("thres15MinExceededOduTcmAUAS", 377), ("thres15MinExceededOduTcmBUAS", 379), ("thres15MinExceededOduTcmCUAS", 381), ("thres15MinExceededFecUBE", 383), ("encryptionModuleTamperDetected", 385), ("thermoElectricCoolerEndOfLife", 386), ("alarmInputTIF", 387), ("traceIdentifierMismatchOdu", 389), ("traceIdentifierMismatchOtu", 390), ("sectionTraceMismatch", 391), ("traceIdentifierMismatchOduTcmA", 392), ("traceIdentifierMismatchOduTcmB", 393), ("traceIdentifierMismatchOduTcmC", 394), ("turnupFailed", 395), ("turnupCondition", 396), ("unequippedLowerOrderPath", 397), ("unequippedHigherOrderPath", 398), ("voaControlFail", 399), ("voltageOutOfRange", 400), ("inputVoltageFailure", 401), ("inputVoltageFailurePort1", 402), ("inputVoltageFailurePort2", 403), ("wtrTimerRunning", 406), ("lossOfLaneOtu", 407), ("lossOfTestSeqSynchOpu", 408), ("lossOfMfiOpu", 409), ("oosDisabledLckOduTrmt", 410), ("configurationMismatch", 411), ("oduAutoShutdownRxAIS", 412), ("oduAutoShutdownTxAIS", 413), ("oosDisabledLckOduRx", 414), ("thres15MinExceededBbePcs", 420), ("autoShutdownGAis", 422), ("equipmentMismatchAllow", 423), ("warmUp", 424), ("networkPathRestricted", 432), ("vfClientSignalFail", 434), ("autoShutdownVfCSF", 435))

class FspR7AlarmProfileList(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93, 94, 95, 96, 97, 99, 100, 101, 103, 104, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 118, 119, 120, 122, 123, 125, 127, 128, 129, 131, 132, 133, 135, 136, 137, 138, 139, 140, 141, 142, 143, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 263, 264, 265, 266, 267, 268, 269, 272, 274, 276, 277, 278, 279, 280, 281, 283, 285, 287, 289, 291, 293, 294, 295, 296, 297, 298, 300, 301, 302), SingleValueConstraint(304, 306, 308, 310, 311, 313, 315, 317, 319, 321, 323, 325, 327, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 350, 352, 354, 356, 358, 360, 362, 364, 366, 367, 368, 369, 370, 371, 373, 375, 377, 379, 381, 383, 385, 386, 387, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 406, 407, 408, 409, 410, 411, 412, 413, 414, 420, 422, 423, 424, 432, 434, 435, 13006, 13007, 13008, 13009, 13010, 100005, 100006, 100009, 100010, 100011, 100012, 100013, 100014, 100015, 100016, 120004, 120005, 120006, 120007, 120008, 120009, 120010, 120011, 120012))
    namedValues = NamedValues(("undefined", 0), ("terminalLoopback", 5), ("oosDisabled", 6), ("oosManagement", 7), ("oosMaintenance", 8), ("oosAins", 9), ("removed", 10), ("lossOfSignal", 11), ("optInputPwrReceivedTooLow", 12), ("optInputPwrReceivedTooHigh", 13), ("laserTemperatureTooHigh", 14), ("laserTemperatureTooLow", 15), ("optOutputPowerTransTooLow", 16), ("optOutputPowerTransTooHigh", 17), ("autoShutdownToHighTemp", 18), ("autoShutdownToHighTxPwr", 19), ("laserEndOfLife", 20), ("serverSignalFailureVf", 21), ("equalizationProgress", 22), ("uPortFailure", 23), ("autoShutdownBlock", 24), ("autoPowerShutdown", 25), ("confOutPowerTransTooHigh", 26), ("confOutPowerTransTooLow", 27), ("optSignalFailure", 28), ("dsbdChannelPowerTooHigh", 29), ("lossOfSignalCPort", 30), ("lossOfSignalNPort", 31), ("outputPowerFault", 32), ("eqlzAdjust", 33), ("ampFailure", 34), ("eqptProvMismatch", 35), ("backreflectionTooHigh", 36), ("fiberConnLos", 48), ("fiberConnOptFault", 49), ("fiberConnInvalid", 50), ("fiberConnMismatch", 51), ("fiberConnCommError", 52), ("fiberConnProtocolFailure", 53), ("fiberConnDataFailure", 54), ("fiberAttenuationHigh", 55), ("laserBiasCurrAbnormal", 57), ("fiberConnInvalidTx", 58), ("fiberConnMismatchTx", 59), ("fiberAttenuationHighTx", 60), ("laserFailure", 61), ("lossOfReceiverClockRecovery", 62), ("fiberAttenuationCond", 63), ("channelMismatch", 64), ("alarmIndicationSignalLine", 65), ("alarmIndicationSignalLowerOrderPath", 66), ("alarmIndicationSignalOdu", 67), ("alarmIndicationSignalOpu", 68), ("alarmIndicationSignalOtu", 69), ("alarmIndicationSignalHigherOrderPath", 70), ("alarmIndicationSignalOduTcmA", 71), ("alarmIndicationSignalOduTcmB", 72), ("alarmIndicationSignalOduTcmC", 73), ("virtualChannelAis", 74), ("amplifierAbnormal", 75), ("automaticPowerReduction", 76), ("automaticPowerReductionForEyeSafety", 77), ("apsConfigMismatch", 80), ("apsProtocolFailure", 81), ("aseLow", 82), ("aseTableGenFailLow", 83), ("aseTableGenFailHighBackreflection", 84), ("aseTableGenFailOscMissing", 85), ("aseTableGenFailPilot", 86), ("aseTableGenFailSignalinput", 87), ("aseTableNotAvailable", 88), ("aseTableGenProgress", 89), ("encryptionPortAuthPasswdMissing", 90), ("backwardDefectIndicationOdu", 92), ("backwardDefectIndicationOtu", 93), ("backwardDefectIndicationOduTcmA", 94), ("backwardDefectIndicationOduTcmB", 95), ("backwardDefectIndicationOduTcmC", 96), ("topologyDataCalculationInProgress", 97), ("dispertionTunningCondition", 99), ("lossOfCharSync", 100), ("lossOfCharSyncFromFarEnd", 101), ("encryptionPortEncryptionSwitchOffEnabled", 103), ("encryptionModuleCryPasswdMissing", 104), ("encryptionModuleSelfTestStarted", 107), ("encryptionPortEncryptionSwitchedOff", 108), ("opuClientSignalFail", 109), ("databaseMismatch", 110), ("databaseFailure", 111), ("databaseNcuMismatch", 112), ("dbReplicationIncompleted", 113), ("databaseVersionMismatch", 114), ("xfpDecisionThresSetFailed", 115), ("duplexLinkFailure", 116), ("singleFanFailure", 118), ("multipleFanFailure", 119), ("lossOfSignalTransmitter", 120), ("farEndIpAddressUnknown", 122), ("farEndCommFailure", 123), ("backupForcedToHalt", 125), ("facilityForcedOn", 127), ("fwdAseTableFailPilot", 128), ("fwdAseTableOnPilot", 129), ("encryptionModuleFwpUpdateEnabled", 131), ("fwpMismatchDownloadNotServiceAffecting", 132), ("fwpMismatchDownloadServiceAffecting", 133), ("gainTiltNotSettable", 135), ("highBer", 136), ("receiverOverloadProtection", 137), ("hwInitializing", 138), ("hwOprReachedHT", 139), ("hwDegrade", 140), ("hwFailure", 141), ("switchtoProtectionInhibited", 142), ("switchtoWorkingInhibited", 143), ("encryptionPortKeyInitExchgMissed", 148), ("encryptionPortMaxKeyExchgFailuresReachedIs", 149), ("encryptionPortMaxKeyExchgFailuresReachedOos", 150), ("encryptionPortKeyExchangedForced", 151), ("laserOnDelay", 152), ("lockedDefectOdu", 153), ("lockedDefectOduTcmA", 154), ("lockedDefectOduTcmB", 155), ("lockedDefectOduTcmC", 156), ("linkControlProtocolFailure", 157), ("linkDown", 158), ("autoShutdownSendingAisLine", 159), ("autoShutdownSendingAisOdu", 160), ("autoShutdownSendingAisOpu", 161), ("clientFailForwarding", 162), ("autoShutdownAls", 163), ("autoAmpShutdown", 164), ("autoShutdownAmpAps", 165), ("aseTableBuild", 166), ("autoShutdownOpuClientSignalFail", 167), ("autoShutdownSendingEPC", 168), ("autoShutdownSendingLckOdu", 169), ("autoShutdownSendingOciOdu", 170), ("autoShutdownLaserOffDueToErrFwd", 171), ("autoShutdownTxRxLasersDueToHighTemp", 172), ("localFault", 173), ("localOscLevelAbnormal", 174), ("lossOfGfpFrame", 175), ("lossOfFrameMux", 176), ("lossOfFrameOtu", 177), ("lossOfFrame", 178), ("lossOfFrameLossOfMultiFrameOdu", 179), ("lossOfLane", 180), ("lossofMultiframeLowerOrderPath", 181), ("lossOfMultiFrameOtu", 182), ("lossofMultiframeHigherOrderPath", 183), ("lossOfPointerLowerOrderPath", 184), ("lossOfPointerHigherOrderPath", 185), ("losAttProgress", 186), ("lossOsc", 187), ("gfpLossOfClientSig", 188), ("loopbackError", 189), ("facilityLoopback", 190), ("lossofTandemConnectionOduTcmA", 191), ("lossofTandemConnectionOduTcmB", 192), ("lossofTandemConnectionOduTcmC", 193), ("mansw", 194), ("equipmentNotAccepted", 197), ("equipmentNotApproved", 198), ("capabilityLevelMismatch", 199), ("equipmentMismatch", 200), ("equipmentNotSupportedByPhysicalLayer", 201), ("meaSwRevision", 202), ("mismatch", 203), ("midstageFault", 204), ("multiplexStructureIdentifierMismatchOPU", 205), ("backupNotResponding", 206), ("openConnectionIndicationOdu", 207), ("openConnectionIndicationOduTcmA", 208), ("openConnectionIndicationOduTcmB", 209), ("openConnectionIndicationOduTcmC", 210), ("oduTribMsiMismatch", 211), ("transmitterDisabledOff", 212), ("receiverDisabled", 213), ("opmAbnormalCondition", 214), ("faultOnOpm", 215), ("thresOptPowerCtrlFailureHigh", 216), ("thresOptPowerCtrlFailureLow", 217), ("txPowerLimited", 218), ("oscOpticalPowerControlFailHigh", 219), ("oscOpticalPowerControlFailLow", 220), ("oTDRMeasuringinProgress", 221), ("encryptionModuleCryPasswdError", 222), ("peerLink", 223), ("pilotReceiveLevelHigh", 224), ("lossOfPilotSignal", 225), ("payloadMismatchGfp", 226), ("payloadMismatchLowerOrderPath", 227), ("payloadMismatchOPU", 228), ("payloadMismatchHigherOrderPath", 229), ("provPayloadMismatch", 230), ("prbsLossOfSeqSynch", 231), ("prbsRcvActivated", 232), ("prbsTrmtActivated", 233), ("protectionNotAvailable", 234), ("powerSupplyUnitFailure", 235), ("maxPowerConsProvModulesToHigh", 236), ("maxPowerConsEquipModulesToHigh", 237), ("powerMissing", 238), ("remoteDefectIndicationLine", 239), ("remoteDefectIndicationLowerOrderPath", 240), ("remoteDefectIndicationHigherOrderPath", 241), ("dcnCommunicationFail", 243), ("ntpForSchedEqlzRequired", 244), ("signalDegradeOlm", 245), ("signalDegradeLine", 246), ("signalDegradationonLinkVector", 247), ("signalDegradeOdu", 248), ("signalDegradeOtu", 249), ("pcsSignalDegrade", 250), ("signalDegradeScn", 251), ("signalDegradeOduTcmA", 252), ("signalDegradeOduTcmB", 253), ("signalDegradeOduTcmC", 254), ("encryptionModuleSelfTestFail", 255), ("encryptionModuleSelfTestFailCritical", 256), ("signalFailureOnLink", 257), ("signalFailureonLinkVector", 258), ("signalFailureOPU", 259), ("serverSignalFailTx", 260), ("facilityDataRateNotSupported", 261), ("lossofSequenceLowerOrderPath", 263), ("lossofSequenceHigherOrderPath", 264), ("serverSignalFail", 265), ("serverSignalFailureGfp", 266), ("serverSignalFailureODU", 267), ("serverSignalFailurePath", 268), ("serverSignalFailureSectionRS", 269), ("switchToDuplexInhibited", 272), ("switchFailed", 274), ("currentTooHigh", 276), ("attOnReceiverFiberHigherThanMonitor", 277), ("attOnReceiverFiberLowerThanMonitor", 278), ("attOnTransmitterFiberHigherThanMonitor", 279), ("attOnTransmitterFiberLowerThanMonitor", 280), ("thres15MinExceededOduBbe", 281), ("thres15MinExceededOtuBbe", 283), ("thres15MinExceededOduTcmABbe", 285), ("thres15MinExceededOduTcmBBbe", 287), ("thres15MinExceededOduTcmCBbe", 289), ("thres15MinExceededFecBERCE", 291), ("brPwrRxTooHigh", 293), ("chromaticDispersionTooHigh", 294), ("chromaticDispersionTooLow", 295), ("dispersionCompensationTooHigh", 296), ("dispersionCompensationTooLow", 297), ("thres15MinExceededFecCE", 298), ("carrierFreqOffsetTooHigh", 300), ("carrierFreqOffsetTooLow", 301), ("thres15MinExceededSonetLineCV", 302)) + NamedValues(("thres15MinExceededPhysConvCV", 304), ("thres15MinExceededSonetSectCV", 306), ("thres15MinExceededPhysConvDE", 308), ("differentialGroupDelayTooHigh", 310), ("thres15MinExceededFecES", 311), ("thres15MinExceededSonetLineES", 313), ("thres15MinExceededOduES", 315), ("thres15MinExceededOtuES", 317), ("thres15MinExceededPhysConvES", 319), ("thres15MinExceededSonetSectES", 321), ("thres15MinExceededOduTcmAES", 323), ("thres15MinExceededOduTcmBES", 325), ("thres15MinExceededOduTcmCES", 327), ("latencyTooHigh", 329), ("latencyTooLow", 330), ("laserBiasCurrentNormalizedtooHigh", 331), ("localOscTemperatureTooHigh", 332), ("localOscTemperatureTooLow", 333), ("pumpLaser1TempTooHigh", 334), ("pumpLaser1TempTooLow", 335), ("pumpLaser2TempTooHigh", 336), ("pumpLaser2TempTooLow", 337), ("pumpLaser3TempTooHigh", 338), ("pumpLaser3TempTooLow", 339), ("pumpLaser4TempTooHigh", 340), ("pumpLaser4TempTooLow", 341), ("oscPwrTooHigh", 342), ("oscPwrTooLow", 343), ("ramanPumpPwrTooHigh", 344), ("ramanPumpPwrTooLow", 345), ("roundTripDelayTooHigh", 346), ("roundTripDelayTooLow", 347), ("thres15MinExceededSonetSectSEFS", 348), ("thres15MinExceededFecSES", 350), ("thres15MinExceededSonetLineSES", 352), ("thres15MinExceededOduSES", 354), ("thres15MinExceededOtuSES", 356), ("thres15MinExceededSonetSectSES", 358), ("thres15MinExceededOduTcmASES", 360), ("thres15MinExceededOduTcmBSES", 362), ("thres15MinExceededOduTcmCSES", 364), ("logicalLanesSkewTooHigh", 366), ("signalToNoiseRatioTooLow", 367), ("subModuleTempTooHigh", 368), ("temperatureTooHigh", 369), ("temperatureTooLow", 370), ("thres15MinExceededSonetLineUAS", 371), ("thres15MinExceededOduUAS", 373), ("thres15MinExceededOtuUAS", 375), ("thres15MinExceededOduTcmAUAS", 377), ("thres15MinExceededOduTcmBUAS", 379), ("thres15MinExceededOduTcmCUAS", 381), ("thres15MinExceededFecUBE", 383), ("encryptionModuleTamperDetected", 385), ("thermoElectricCoolerEndOfLife", 386), ("alarmInputTIF", 387), ("traceIdentifierMismatchOdu", 389), ("traceIdentifierMismatchOtu", 390), ("sectionTraceMismatch", 391), ("traceIdentifierMismatchOduTcmA", 392), ("traceIdentifierMismatchOduTcmB", 393), ("traceIdentifierMismatchOduTcmC", 394), ("turnupFailed", 395), ("turnupCondition", 396), ("unequippedLowerOrderPath", 397), ("unequippedHigherOrderPath", 398), ("voaControlFail", 399), ("voltageOutOfRange", 400), ("inputVoltageFailure", 401), ("inputVoltageFailurePort1", 402), ("inputVoltageFailurePort2", 403), ("wtrTimerRunning", 406), ("lossOfLaneOtu", 407), ("lossOfTestSeqSynchOpu", 408), ("lossOfMfiOpu", 409), ("oosDisabledLckOduTrmt", 410), ("configurationMismatch", 411), ("oduAutoShutdownRxAIS", 412), ("oduAutoShutdownTxAIS", 413), ("oosDisabledLckOduRx", 414), ("thres15MinExceededBbePcs", 420), ("autoShutdownGAis", 422), ("equipmentMismatchAllow", 423), ("warmUp", 424), ("networkPathRestricted", 432), ("vfClientSignalFail", 434), ("autoShutdownVfCSF", 435), ("cfmRemoteDefectIndication", 13006), ("cfmCcmMacStatus", 13007), ("cfmCcmError", 13008), ("cfmCcmLost", 13009), ("cfmCcmXConn", 13010), ("mepNotPresentL2", 100005), ("priVidNotEqualExtVidL2", 100006), ("sfCfmLevel0L2", 100009), ("sfCfmLevel1L2", 100010), ("sfCfmLevel2L2", 100011), ("sfCfmLevel3L2", 100012), ("sfCfmLevel4L2", 100013), ("sfCfmLevel5L2", 100014), ("sfCfmLevel6L2", 100015), ("sfCfmLevel7L2", 100016), ("messageLossSpeq", 120004), ("oscFiberMissingSpeq", 120005), ("optLowSpeq", 120006), ("ppcOutOfRangeSpeq", 120007), ("gainTooHighSpeq", 120008), ("gainTooLowSpeq", 120009), ("gainAdoptFailedSpeq", 120010), ("processLockedOutSpeq", 120011), ("ppcLimitExceededSpeq", 120012))

class FspR7AlsMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("advaALS", 1), ("sonetALS", 2), ("noALS", 3), ("fastAls", 4))

class FspR7AlsModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capAdvaALS", 1), ("capSonetALS", 2), ("capNoALS", 3), ("capFastAls", 4))

class FspR7AppType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 0), ("lct", 1), ("snmp", 2), ("tl1", 3), ("tcli", 4), ("controlplane", 5), ("system", 6))

class FspR7ApsChannel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("line", 2), ("path", 3), ("pm", 4), ("tcm1", 5), ("tcm2", 6), ("tcm3", 7), ("tcm4", 8), ("tcm5", 9), ("tcm6", 10), ("sm", 11), ("gfp", 12), ("prop", 13))

class FspR7APSCommand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("release", 1), ("manualSwitch", 2))

class FspR7APSCommandCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRelease", 1), ("capManualSwitch", 2))

class FspR7AseTabOpr(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("build", 2))

class FspR7AseTabOprCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capBuild", 2))

class FspR7EquipmentAssignState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("assigned", 1), ("assignable", 2), ("notAssignable", 3))

class FspR7AutoThresReset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("rtf", 2))

class FspR7AutoThresResetCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capRtf", 2))

class FspR7Baund(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("baud2400", 1), ("baud4800", 2), ("baud9600", 3), ("baud19200", 4), ("baud38400", 5), ("baud57600", 6), ("baud115200", 7))

class FspR7BaundCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capBaud2400", 1), ("capBaud4800", 2), ("capBaud9600", 3), ("capBaud19200", 4), ("capBaud38400", 5), ("capBaud57600", 6), ("capBaud115200", 7))

class FspR7BERThreshold(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("exp5", 1), ("exp6", 2), ("exp7", 3), ("exp8", 4), ("exp9", 5))

class FspR7BERThresholdCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capExp5", 1), ("capExp6", 2), ("capExp7", 3), ("capExp8", 4), ("capExp9", 5))

class FspR7BERThresholdSection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("exp7", 3), ("exp8", 4), ("exp9", 5))

class FspR7BERThresholdSectionCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capExp7", 3), ("capExp8", 4), ("capExp9", 5))

class FspR7BidirectionalChannel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("tx1310rx1490", 1), ("tx1490rx1310", 2))

class FspR7BidirectionalChannelCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capTx1310rx1490", 1), ("capTx1490rx1310", 2))

class FspR7Bitrate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("bitrate10", 1), ("bitrate100", 2), ("bitrate1000", 3), ("bitrate10000", 4))

class FspR7BitrateCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capBitrate10", 1), ("capBitrate100", 2), ("capBitrate1000", 3), ("capBitrate10000", 4))

class FspR7CapInventory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 50))
    namedValues = NamedValues(("undefined", 0), ("level0", 1), ("level1", 2), ("level2", 3), ("level3", 4), ("level4", 5), ("level5", 6), ("unknown", 50))

class FspR7CapInventoryCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capLevel0", 1), ("capLevel1", 2), ("capLevel2", 3), ("capLevel3", 4), ("capLevel4", 5), ("capLevel5", 6), ("capUnknown", 50))

class FspR7Category(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("undefined", 0), ("shelf", 1), ("channelMod", 2), ("plug", 3), ("filter", 4), ("amplifier", 5), ("dcm", 6), ("switch", 7), ("oscm", 8), ("dummy", 9), ("common", 10), ("att", 11), ("jumper", 12), ("accessory", 13), ("fiber", 14), ("protectionMod", 15), ("any", 16), ("roadm", 17), ("ethernetMod", 18), ("powerSplitter", 19), ("adm", 20))

class FspR7CertApply(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("apply", 2))

class FspR7CertApplyCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNone", 1), ("capApply", 2))

class FspR7ChannelBandwidth(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("undefined", 0), ("band50G", 1), ("band75G", 2), ("band100G", 3), ("band125G", 4), ("band150G", 5), ("band175G", 6), ("band200G", 7), ("band225G", 8), ("band250G", 9), ("band275G", 10), ("band300G", 11))

class FspR7ChannelBandwidthCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capBand50G", 1), ("capBand75G", 2), ("capBand100G", 3), ("capBand125G", 4), ("capBand150G", 5), ("capBand175G", 6), ("capBand200G", 7), ("capBand225G", 8), ("capBand250G", 9), ("capBand275G", 10), ("capBand300G", 11))

class FspR7ChannelIdentifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263), SingleValueConstraint(264, 265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 382, 383, 384, 385, 386, 387, 388, 389, 390, 392, 393, 394, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418, 419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500))
    namedValues = NamedValues(("undefined", 0), ("d01", 1), ("d02", 2), ("d03", 3), ("d04", 4), ("d05", 5), ("d06", 6), ("d07", 7), ("d08", 8), ("d09", 9), ("d10", 10), ("d11", 11), ("d12", 12), ("d13", 13), ("d14", 14), ("d15", 15), ("d16", 16), ("d17", 17), ("d18", 18), ("d19", 19), ("d20", 20), ("d21", 21), ("d22", 22), ("d23", 23), ("d24", 24), ("d25", 25), ("d26", 26), ("d27", 27), ("d28", 28), ("d29", 29), ("d30", 30), ("d31", 31), ("d32", 32), ("d33", 33), ("d34", 34), ("d35", 35), ("d36", 36), ("d37", 37), ("d38", 38), ("d39", 39), ("d40", 40), ("d41", 41), ("d42", 42), ("d43", 43), ("d44", 44), ("d45", 45), ("d46", 46), ("d47", 47), ("d48", 48), ("d49", 49), ("d50", 50), ("d51", 51), ("d52", 52), ("d53", 53), ("d54", 54), ("d55", 55), ("d56", 56), ("d57", 57), ("d58", 58), ("d59", 59), ("d60", 60), ("d61", 61), ("d62", 62), ("d63", 63), ("d64", 64), ("dc1", 65), ("dc2", 66), ("dc3", 67), ("dc4", 68), ("dc5", 69), ("dc6", 70), ("dc7", 71), ("dc8", 72), ("dl1", 73), ("dl2", 74), ("dl3", 75), ("dl4", 76), ("dl5", 77), ("dl6", 78), ("dl7", 79), ("dl8", 80), ("dc9", 81), ("dl9", 82), ("c1470", 91), ("c1490", 92), ("c1510", 93), ("c1530", 94), ("c1550", 95), ("c1570", 96), ("c1590", 97), ("c1610", 98), ("s1310", 99), ("s1630", 100), ("g850", 101), ("g1310", 102), ("g1550", 103), ("notInGrid", 105), ("s1510", 106), ("f19610", 107), ("f19595", 108), ("f19585", 109), ("f19575", 110), ("f19565", 111), ("f19555", 112), ("f19545", 113), ("f19535", 114), ("f19525", 115), ("f19515", 116), ("f19505", 117), ("f19495", 118), ("f19485", 119), ("f19475", 120), ("f19465", 121), ("f19455", 122), ("f19445", 123), ("f19435", 124), ("f19425", 125), ("f19415", 126), ("f19405", 127), ("f19395", 128), ("f19385", 129), ("f19375", 130), ("f19365", 131), ("f19355", 132), ("f19345", 133), ("f19335", 134), ("f19325", 135), ("f19315", 136), ("f19305", 137), ("f19295", 138), ("f19285", 139), ("f19275", 140), ("f19265", 141), ("f19255", 142), ("f19245", 143), ("f19235", 144), ("f19225", 145), ("f19215", 146), ("f19205", 147), ("f19600", 148), ("f19590", 149), ("f19580", 150), ("f19570", 151), ("f19560", 152), ("f19550", 153), ("f19540", 154), ("f19530", 155), ("f19520", 156), ("f19510", 157), ("f19500", 158), ("f19490", 159), ("f19480", 160), ("f19470", 161), ("f19460", 162), ("f19450", 163), ("f19440", 164), ("f19430", 165), ("f19420", 166), ("f19410", 167), ("f19400", 168), ("f19390", 169), ("f19380", 170), ("f19370", 171), ("f19360", 172), ("f19350", 173), ("f19340", 174), ("f19330", 175), ("f19320", 176), ("f19310", 177), ("f19300", 178), ("f19290", 179), ("f19280", 180), ("f19270", 181), ("f19260", 182), ("f19250", 183), ("f19240", 184), ("f19230", 185), ("f19220", 186), ("f19210", 187), ("f19200", 188), ("c1270", 189), ("c1290", 190), ("c1310", 191), ("c1330", 192), ("c1350", 193), ("c1370", 194), ("c1430", 195), ("c1450", 196), ("s1610", 197), ("t1650", 198), ("s1490", 199), ("f19598", 200), ("f19597", 201), ("f19596", 202), ("f19593", 203), ("f19592", 204), ("f19591", 205), ("f19588", 206), ("f19587", 207), ("f19586", 208), ("f19583", 209), ("f19582", 210), ("f19581", 211), ("f19578", 212), ("f19577", 213), ("f19576", 214), ("f19573", 215), ("f19572", 216), ("f19571", 217), ("f19568", 218), ("f19567", 219), ("f19566", 220), ("f19563", 221), ("f19562", 222), ("f19561", 223), ("f19558", 224), ("f19557", 225), ("f19556", 226), ("f19553", 227), ("f19552", 228), ("f19551", 229), ("f19548", 230), ("f19547", 231), ("f19546", 232), ("f19543", 233), ("f19542", 234), ("f19541", 235), ("f19538", 236), ("f19537", 237), ("f19536", 238), ("f19533", 239), ("f19532", 240), ("f19531", 241), ("f19528", 242), ("f19527", 243), ("f19526", 244), ("f19523", 245), ("f19522", 246), ("f19521", 247), ("f19518", 248), ("f19517", 249), ("f19516", 250), ("f19513", 251), ("f19512", 252), ("f19511", 253), ("f19508", 254), ("f19507", 255), ("f19506", 256), ("f19503", 257), ("f19502", 258), ("f19501", 259), ("f19498", 260), ("f19497", 261), ("f19496", 262), ("f19493", 263)) + NamedValues(("f19492", 264), ("f19491", 265), ("f19488", 266), ("f19487", 267), ("f19486", 268), ("f19483", 269), ("f19482", 270), ("f19481", 271), ("f19478", 272), ("f19477", 273), ("f19476", 274), ("f19473", 275), ("f19472", 276), ("f19471", 277), ("f19468", 278), ("f19467", 279), ("f19466", 280), ("f19463", 281), ("f19462", 282), ("f19461", 283), ("f19458", 284), ("f19457", 285), ("f19456", 286), ("f19453", 287), ("f19452", 288), ("f19451", 289), ("f19448", 290), ("f19447", 291), ("f19446", 292), ("f19443", 293), ("f19442", 294), ("f19441", 295), ("f19438", 296), ("f19437", 297), ("f19436", 298), ("f19433", 299), ("f19432", 300), ("f19431", 301), ("f19428", 302), ("f19427", 303), ("f19426", 304), ("f19423", 305), ("f19422", 306), ("f19421", 307), ("f19418", 308), ("f19417", 309), ("f19416", 310), ("f19413", 311), ("f19412", 312), ("f19411", 313), ("f19408", 314), ("f19407", 315), ("f19406", 316), ("f19403", 317), ("f19402", 318), ("f19401", 319), ("f19398", 320), ("f19397", 321), ("f19396", 322), ("f19393", 323), ("f19392", 324), ("f19391", 325), ("f19388", 326), ("f19387", 327), ("f19386", 328), ("f19383", 329), ("f19382", 330), ("f19381", 331), ("f19378", 332), ("f19377", 333), ("f19376", 334), ("f19373", 335), ("f19372", 336), ("f19371", 337), ("f19368", 338), ("f19367", 339), ("f19366", 340), ("f19363", 341), ("f19362", 342), ("f19361", 343), ("f19358", 344), ("f19357", 345), ("f19356", 346), ("f19353", 347), ("f19352", 348), ("f19351", 349), ("f19348", 350), ("f19347", 351), ("f19346", 352), ("f19343", 353), ("f19342", 354), ("f19341", 355), ("f19338", 356), ("f19337", 357), ("f19336", 358), ("f19333", 359), ("f19332", 360), ("f19331", 361), ("f19328", 362), ("f19327", 363), ("f19326", 364), ("f19323", 365), ("f19322", 366), ("f19321", 367), ("f19318", 368), ("f19317", 369), ("f19316", 370), ("f19313", 371), ("f19312", 372), ("f19311", 373), ("f19296", 382), ("f19293", 383), ("f19292", 384), ("f19291", 385), ("f19288", 386), ("f19287", 387), ("f19286", 388), ("f19283", 389), ("f19282", 390), ("f19278", 392), ("f19277", 393), ("f19276", 394), ("f19273", 395), ("f19272", 396), ("f19271", 397), ("f19268", 398), ("f19267", 399), ("f19266", 400), ("f19263", 401), ("f19262", 402), ("f19261", 403), ("f19258", 404), ("f19257", 405), ("f19256", 406), ("f19253", 407), ("f19252", 408), ("f19251", 409), ("f19248", 410), ("f19247", 411), ("f19246", 412), ("f19243", 413), ("f19242", 414), ("f19241", 415), ("f19238", 416), ("f19237", 417), ("f19236", 418), ("f19233", 419), ("f19232", 420), ("f19231", 421), ("f19228", 422), ("f19227", 423), ("f19226", 424), ("f19223", 425), ("f19222", 426), ("f19221", 427), ("f19218", 428), ("f19217", 429), ("f19216", 430), ("f19213", 431), ("f19212", 432), ("f19211", 433), ("f19208", 434), ("f19207", 435), ("f19206", 436), ("f19203", 437), ("f19202", 438), ("f19201", 439), ("f19198", 440), ("f19197", 441), ("f19196", 442), ("f19195", 443), ("f19193", 444), ("f19192", 445), ("f19191", 446), ("f19190", 447), ("f19188", 448), ("f19187", 449), ("f19186", 450), ("f19185", 451), ("f19183", 452), ("f19182", 453), ("f19181", 454), ("f19180", 455), ("f19178", 456), ("f19177", 457), ("f19176", 458), ("f19175", 459), ("f19173", 460), ("f19172", 461), ("f19171", 462), ("f19170", 463), ("f19168", 464), ("f19167", 465), ("f19166", 466), ("f19165", 467), ("f19163", 468), ("f19162", 469), ("f19161", 470), ("f19160", 471), ("f19158", 472), ("f19157", 473), ("f19156", 474), ("f19155", 475), ("f19153", 476), ("f19152", 477), ("f19151", 478), ("f19150", 479), ("f19148", 480), ("f19147", 481), ("f19146", 482), ("f19145", 483), ("f19143", 484), ("f19142", 485), ("f19141", 486), ("f19140", 487), ("f19138", 488), ("f19137", 489), ("f19136", 490), ("f19135", 491), ("f19133", 492), ("f19132", 493), ("f19131", 494), ("f19130", 495), ("f19128", 496), ("f19127", 497), ("f19126", 498), ("f19125", 499), ("notDefined", 500))

class FspR7ChannelIdentifierCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capD01", 1), ("capD02", 2), ("capD03", 3), ("capD04", 4), ("capD05", 5), ("capD06", 6), ("capD07", 7), ("capD08", 8), ("capD09", 9), ("capD10", 10), ("capD11", 11), ("capD12", 12), ("capD13", 13), ("capD14", 14), ("capD15", 15), ("capD16", 16), ("capD17", 17), ("capD18", 18), ("capD19", 19), ("capD20", 20), ("capD21", 21), ("capD22", 22), ("capD23", 23), ("capD24", 24), ("capD25", 25), ("capD26", 26), ("capD27", 27), ("capD28", 28), ("capD29", 29), ("capD30", 30), ("capD31", 31), ("capD32", 32), ("capD33", 33), ("capD34", 34), ("capD35", 35), ("capD36", 36), ("capD37", 37), ("capD38", 38), ("capD39", 39), ("capD40", 40), ("capD41", 41), ("capD42", 42), ("capD43", 43), ("capD44", 44), ("capD45", 45), ("capD46", 46), ("capD47", 47), ("capD48", 48), ("capD49", 49), ("capD50", 50), ("capD51", 51), ("capD52", 52), ("capD53", 53), ("capD54", 54), ("capD55", 55), ("capD56", 56), ("capD57", 57), ("capD58", 58), ("capD59", 59), ("capD60", 60), ("capD61", 61), ("capD62", 62), ("capD63", 63), ("capD64", 64), ("capDc1", 65), ("capDc2", 66), ("capDc3", 67), ("capDc4", 68), ("capDc5", 69), ("capDc6", 70), ("capDc7", 71), ("capDc8", 72), ("capDl1", 73), ("capDl2", 74), ("capDl3", 75), ("capDl4", 76), ("capDl5", 77), ("capDl6", 78), ("capDl7", 79), ("capDl8", 80), ("capDc9", 81), ("capDl9", 82), ("capC1470", 91), ("capC1490", 92), ("capC1510", 93), ("capC1530", 94), ("capC1550", 95), ("capC1570", 96), ("capC1590", 97), ("capC1610", 98), ("capS1310", 99), ("capS1630", 100), ("capG850", 101), ("capG1310", 102), ("capG1550", 103), ("capNotInGrid", 105), ("capS1510", 106), ("capF19610", 107), ("capF19595", 108), ("capF19585", 109), ("capF19575", 110), ("capF19565", 111), ("capF19555", 112), ("capF19545", 113), ("capF19535", 114), ("capF19525", 115), ("capF19515", 116), ("capF19505", 117), ("capF19495", 118), ("capF19485", 119), ("capF19475", 120), ("capF19465", 121), ("capF19455", 122), ("capF19445", 123), ("capF19435", 124), ("capF19425", 125), ("capF19415", 126), ("capF19405", 127), ("capF19395", 128), ("capF19385", 129), ("capF19375", 130), ("capF19365", 131), ("capF19355", 132), ("capF19345", 133), ("capF19335", 134), ("capF19325", 135), ("capF19315", 136), ("capF19305", 137), ("capF19295", 138), ("capF19285", 139), ("capF19275", 140), ("capF19265", 141), ("capF19255", 142), ("capF19245", 143), ("capF19235", 144), ("capF19225", 145), ("capF19215", 146), ("capF19205", 147), ("capF19600", 148), ("capF19590", 149), ("capF19580", 150), ("capF19570", 151), ("capF19560", 152), ("capF19550", 153), ("capF19540", 154), ("capF19530", 155), ("capF19520", 156), ("capF19510", 157), ("capF19500", 158), ("capF19490", 159), ("capF19480", 160), ("capF19470", 161), ("capF19460", 162), ("capF19450", 163), ("capF19440", 164), ("capF19430", 165), ("capF19420", 166), ("capF19410", 167), ("capF19400", 168), ("capF19390", 169), ("capF19380", 170), ("capF19370", 171), ("capF19360", 172), ("capF19350", 173), ("capF19340", 174), ("capF19330", 175), ("capF19320", 176), ("capF19310", 177), ("capF19300", 178), ("capF19290", 179), ("capF19280", 180), ("capF19270", 181), ("capF19260", 182), ("capF19250", 183), ("capF19240", 184), ("capF19230", 185), ("capF19220", 186), ("capF19210", 187), ("capF19200", 188), ("capC1270", 189), ("capC1290", 190), ("capC1310", 191), ("capC1330", 192), ("capC1350", 193), ("capC1370", 194), ("capC1430", 195), ("capC1450", 196), ("capS1610", 197), ("capT1650", 198), ("capS1490", 199), ("capF19598", 200), ("capF19597", 201), ("capF19596", 202), ("capF19593", 203), ("capF19592", 204), ("capF19591", 205), ("capF19588", 206), ("capF19587", 207), ("capF19586", 208), ("capF19583", 209), ("capF19582", 210), ("capF19581", 211), ("capF19578", 212), ("capF19577", 213), ("capF19576", 214), ("capF19573", 215), ("capF19572", 216), ("capF19571", 217), ("capF19568", 218), ("capF19567", 219), ("capF19566", 220), ("capF19563", 221), ("capF19562", 222), ("capF19561", 223), ("capF19558", 224), ("capF19557", 225), ("capF19556", 226), ("capF19553", 227), ("capF19552", 228), ("capF19551", 229), ("capF19548", 230), ("capF19547", 231), ("capF19546", 232), ("capF19543", 233), ("capF19542", 234), ("capF19541", 235), ("capF19538", 236), ("capF19537", 237), ("capF19536", 238), ("capF19533", 239), ("capF19532", 240), ("capF19531", 241), ("capF19528", 242), ("capF19527", 243), ("capF19526", 244), ("capF19523", 245), ("capF19522", 246), ("capF19521", 247), ("capF19518", 248), ("capF19517", 249), ("capF19516", 250), ("capF19513", 251), ("capF19512", 252), ("capF19511", 253), ("capF19508", 254), ("capF19507", 255), ("capF19506", 256), ("capF19503", 257), ("capF19502", 258), ("capF19501", 259), ("capF19498", 260), ("capF19497", 261), ("capF19496", 262), ("capF19493", 263)) + NamedValues(("capF19492", 264), ("capF19491", 265), ("capF19488", 266), ("capF19487", 267), ("capF19486", 268), ("capF19483", 269), ("capF19482", 270), ("capF19481", 271), ("capF19478", 272), ("capF19477", 273), ("capF19476", 274), ("capF19473", 275), ("capF19472", 276), ("capF19471", 277), ("capF19468", 278), ("capF19467", 279), ("capF19466", 280), ("capF19463", 281), ("capF19462", 282), ("capF19461", 283), ("capF19458", 284), ("capF19457", 285), ("capF19456", 286), ("capF19453", 287), ("capF19452", 288), ("capF19451", 289), ("capF19448", 290), ("capF19447", 291), ("capF19446", 292), ("capF19443", 293), ("capF19442", 294), ("capF19441", 295), ("capF19438", 296), ("capF19437", 297), ("capF19436", 298), ("capF19433", 299), ("capF19432", 300), ("capF19431", 301), ("capF19428", 302), ("capF19427", 303), ("capF19426", 304), ("capF19423", 305), ("capF19422", 306), ("capF19421", 307), ("capF19418", 308), ("capF19417", 309), ("capF19416", 310), ("capF19413", 311), ("capF19412", 312), ("capF19411", 313), ("capF19408", 314), ("capF19407", 315), ("capF19406", 316), ("capF19403", 317), ("capF19402", 318), ("capF19401", 319), ("capF19398", 320), ("capF19397", 321), ("capF19396", 322), ("capF19393", 323), ("capF19392", 324), ("capF19391", 325), ("capF19388", 326), ("capF19387", 327), ("capF19386", 328), ("capF19383", 329), ("capF19382", 330), ("capF19381", 331), ("capF19378", 332), ("capF19377", 333), ("capF19376", 334), ("capF19373", 335), ("capF19372", 336), ("capF19371", 337), ("capF19368", 338), ("capF19367", 339), ("capF19366", 340), ("capF19363", 341), ("capF19362", 342), ("capF19361", 343), ("capF19358", 344), ("capF19357", 345), ("capF19356", 346), ("capF19353", 347), ("capF19352", 348), ("capF19351", 349), ("capF19348", 350), ("capF19347", 351), ("capF19346", 352), ("capF19343", 353), ("capF19342", 354), ("capF19341", 355), ("capF19338", 356), ("capF19337", 357), ("capF19336", 358), ("capF19333", 359), ("capF19332", 360), ("capF19331", 361), ("capF19328", 362), ("capF19327", 363), ("capF19326", 364), ("capF19323", 365), ("capF19322", 366), ("capF19321", 367), ("capF19318", 368), ("capF19317", 369), ("capF19316", 370), ("capF19313", 371), ("capF19312", 372), ("capF19311", 373), ("capF19296", 382), ("capF19293", 383), ("capF19292", 384), ("capF19291", 385), ("capF19288", 386), ("capF19287", 387), ("capF19286", 388), ("capF19283", 389), ("capF19282", 390), ("capF19278", 392), ("capF19277", 393), ("capF19276", 394), ("capF19273", 395), ("capF19272", 396), ("capF19271", 397), ("capF19268", 398), ("capF19267", 399), ("capF19266", 400), ("capF19263", 401), ("capF19262", 402), ("capF19261", 403), ("capF19258", 404), ("capF19257", 405), ("capF19256", 406), ("capF19253", 407), ("capF19252", 408), ("capF19251", 409), ("capF19248", 410), ("capF19247", 411), ("capF19246", 412), ("capF19243", 413), ("capF19242", 414), ("capF19241", 415), ("capF19238", 416), ("capF19237", 417), ("capF19236", 418), ("capF19233", 419), ("capF19232", 420), ("capF19231", 421), ("capF19228", 422), ("capF19227", 423), ("capF19226", 424), ("capF19223", 425), ("capF19222", 426), ("capF19221", 427), ("capF19218", 428), ("capF19217", 429), ("capF19216", 430), ("capF19213", 431), ("capF19212", 432), ("capF19211", 433), ("capF19208", 434), ("capF19207", 435), ("capF19206", 436), ("capF19203", 437), ("capF19202", 438), ("capF19201", 439), ("capF19198", 440), ("capF19197", 441), ("capF19196", 442), ("capF19195", 443), ("capF19193", 444), ("capF19192", 445), ("capF19191", 446), ("capF19190", 447), ("capF19188", 448), ("capF19187", 449), ("capF19186", 450), ("capF19185", 451), ("capF19183", 452), ("capF19182", 453), ("capF19181", 454), ("capF19180", 455), ("capF19178", 456), ("capF19177", 457), ("capF19176", 458), ("capF19175", 459), ("capF19173", 460), ("capF19172", 461), ("capF19171", 462), ("capF19170", 463), ("capF19168", 464), ("capF19167", 465), ("capF19166", 466), ("capF19165", 467), ("capF19163", 468), ("capF19162", 469), ("capF19161", 470), ("capF19160", 471), ("capF19158", 472), ("capF19157", 473), ("capF19156", 474), ("capF19155", 475), ("capF19153", 476), ("capF19152", 477), ("capF19151", 478), ("capF19150", 479), ("capF19148", 480), ("capF19147", 481), ("capF19146", 482), ("capF19145", 483), ("capF19143", 484), ("capF19142", 485), ("capF19141", 486), ("capF19140", 487), ("capF19138", 488), ("capF19137", 489), ("capF19136", 490), ("capF19135", 491), ("capF19133", 492), ("capF19132", 493), ("capF19131", 494), ("capF19130", 495), ("capF19128", 496), ("capF19127", 497), ("capF19126", 498), ("capF19125", 499), ("capNotDefined", 500))

class FspR7ChannelNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215))
    namedValues = NamedValues(("undefined", 0), ("f19600", 1), ("f19590", 2), ("f19580", 3), ("f19570", 4), ("f19550", 5), ("f19540", 6), ("f19530", 7), ("f19520", 8), ("f19500", 9), ("f19490", 10), ("f19480", 11), ("f19470", 12), ("f19450", 13), ("f19440", 14), ("f19430", 15), ("f19420", 16), ("f19380", 17), ("f19370", 18), ("f19360", 19), ("f19350", 20), ("f19330", 21), ("f19320", 22), ("f19310", 23), ("f19300", 24), ("f19280", 25), ("f19270", 26), ("f19260", 27), ("f19250", 28), ("f19230", 29), ("f19220", 30), ("f19210", 31), ("f19200", 32), ("f19100", 33), ("f19090", 34), ("f19080", 35), ("f19070", 36), ("f19050", 37), ("f19040", 38), ("f19030", 39), ("f19020", 40), ("f19000", 41), ("f18990", 42), ("f18980", 43), ("f18970", 44), ("f18950", 45), ("f18940", 46), ("f18930", 47), ("f18920", 48), ("f18880", 49), ("f18870", 50), ("f18860", 51), ("f18850", 52), ("f18830", 53), ("f18820", 54), ("f18810", 55), ("f18800", 56), ("f18780", 57), ("f18770", 58), ("f18760", 59), ("f18750", 60), ("f18730", 61), ("f18720", 62), ("f18710", 63), ("f18700", 64), ("f19560", 65), ("f19510", 66), ("f19460", 67), ("f19410", 68), ("f19390", 69), ("f19340", 70), ("f19290", 71), ("f19240", 72), ("f19060", 73), ("f19010", 74), ("f18960", 75), ("f18910", 76), ("f18890", 77), ("f18840", 78), ("f18790", 79), ("f18740", 80), ("f19400", 81), ("f18900", 82), ("f19640", 83), ("f19635", 84), ("f19630", 85), ("f19625", 86), ("f19620", 87), ("f19615", 88), ("f19605", 89), ("c1470", 90), ("c1490", 91), ("c1510", 92), ("c1530", 93), ("c1550", 94), ("c1570", 95), ("c1590", 96), ("c1610", 97), ("s1310", 98), ("s1630", 99), ("g850", 100), ("g1310", 101), ("g1550", 102), ("null", 103), ("nig", 104), ("s1510", 105), ("f19610", 106), ("f19595", 107), ("f19585", 108), ("f19575", 109), ("f19565", 110), ("f19555", 111), ("f19545", 112), ("f19535", 113), ("f19525", 114), ("f19515", 115), ("f19505", 116), ("f19495", 117), ("f19485", 118), ("f19475", 119), ("f19465", 120), ("f19455", 121), ("f19445", 122), ("f19435", 123), ("f19425", 124), ("f19415", 125), ("f19405", 126), ("f19395", 127), ("f19385", 128), ("f19375", 129), ("f19365", 130), ("f19355", 131), ("f19345", 132), ("f19335", 133), ("f19325", 134), ("f19315", 135), ("f19305", 136), ("f19295", 137), ("f19285", 138), ("f19275", 139), ("f19265", 140), ("f19255", 141), ("f19245", 142), ("f19235", 143), ("f19225", 144), ("f19215", 145), ("f19205", 146), ("f19195", 147), ("f19190", 148), ("f19185", 149), ("f19180", 150), ("f19175", 151), ("f19170", 152), ("f19165", 153), ("f19160", 154), ("f19155", 155), ("f19150", 156), ("f19145", 157), ("f19140", 158), ("f19135", 159), ("f19130", 160), ("f19125", 161), ("f19120", 162), ("f19115", 163), ("f19110", 164), ("f19105", 165), ("f19095", 166), ("f19085", 167), ("f19075", 168), ("f19065", 169), ("f19055", 170), ("f19045", 171), ("f19035", 172), ("f19025", 173), ("f19015", 174), ("f19005", 175), ("f18995", 176), ("f18985", 177), ("f18975", 178), ("f18965", 179), ("f18955", 180), ("f18945", 181), ("f18935", 182), ("f18925", 183), ("f18915", 184), ("f18905", 185), ("f18895", 186), ("f18885", 187), ("f18875", 188), ("f18865", 189), ("f18855", 190), ("f18845", 191), ("f18835", 192), ("f18825", 193), ("f18815", 194), ("f18805", 195), ("f18795", 196), ("f18785", 197), ("f18775", 198), ("f18765", 199), ("f18755", 200), ("f18745", 201), ("f18735", 202), ("f18725", 203), ("f18715", 204), ("f18705", 205), ("c1270", 206), ("c1290", 207), ("c1310", 208), ("c1330", 209), ("c1350", 210), ("c1370", 211), ("c1430", 212), ("c1450", 213), ("t1650", 214), ("s1490", 215))

class FspR7ChannelNumberCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capF19600", 1), ("capF19590", 2), ("capF19580", 3), ("capF19570", 4), ("capF19550", 5), ("capF19540", 6), ("capF19530", 7), ("capF19520", 8), ("capF19500", 9), ("capF19490", 10), ("capF19480", 11), ("capF19470", 12), ("capF19450", 13), ("capF19440", 14), ("capF19430", 15), ("capF19420", 16), ("capF19380", 17), ("capF19370", 18), ("capF19360", 19), ("capF19350", 20), ("capF19330", 21), ("capF19320", 22), ("capF19310", 23), ("capF19300", 24), ("capF19280", 25), ("capF19270", 26), ("capF19260", 27), ("capF19250", 28), ("capF19230", 29), ("capF19220", 30), ("capF19210", 31), ("capF19200", 32), ("capF19100", 33), ("capF19090", 34), ("capF19080", 35), ("capF19070", 36), ("capF19050", 37), ("capF19040", 38), ("capF19030", 39), ("capF19020", 40), ("capF19000", 41), ("capF18990", 42), ("capF18980", 43), ("capF18970", 44), ("capF18950", 45), ("capF18940", 46), ("capF18930", 47), ("capF18920", 48), ("capF18880", 49), ("capF18870", 50), ("capF18860", 51), ("capF18850", 52), ("capF18830", 53), ("capF18820", 54), ("capF18810", 55), ("capF18800", 56), ("capF18780", 57), ("capF18770", 58), ("capF18760", 59), ("capF18750", 60), ("capF18730", 61), ("capF18720", 62), ("capF18710", 63), ("capF18700", 64), ("capF19560", 65), ("capF19510", 66), ("capF19460", 67), ("capF19410", 68), ("capF19390", 69), ("capF19340", 70), ("capF19290", 71), ("capF19240", 72), ("capF19060", 73), ("capF19010", 74), ("capF18960", 75), ("capF18910", 76), ("capF18890", 77), ("capF18840", 78), ("capF18790", 79), ("capF18740", 80), ("capF19400", 81), ("capF18900", 82), ("capF19640", 83), ("capF19635", 84), ("capF19630", 85), ("capF19625", 86), ("capF19620", 87), ("capF19615", 88), ("capF19605", 89), ("capC1470", 90), ("capC1490", 91), ("capC1510", 92), ("capC1530", 93), ("capC1550", 94), ("capC1570", 95), ("capC1590", 96), ("capC1610", 97), ("capS1310", 98), ("capS1630", 99), ("capG850", 100), ("capG1310", 101), ("capG1550", 102), ("capNull", 103), ("capNig", 104), ("capS1510", 105), ("capF19610", 106), ("capF19595", 107), ("capF19585", 108), ("capF19575", 109), ("capF19565", 110), ("capF19555", 111), ("capF19545", 112), ("capF19535", 113), ("capF19525", 114), ("capF19515", 115), ("capF19505", 116), ("capF19495", 117), ("capF19485", 118), ("capF19475", 119), ("capF19465", 120), ("capF19455", 121), ("capF19445", 122), ("capF19435", 123), ("capF19425", 124), ("capF19415", 125), ("capF19405", 126), ("capF19395", 127), ("capF19385", 128), ("capF19375", 129), ("capF19365", 130), ("capF19355", 131), ("capF19345", 132), ("capF19335", 133), ("capF19325", 134), ("capF19315", 135), ("capF19305", 136), ("capF19295", 137), ("capF19285", 138), ("capF19275", 139), ("capF19265", 140), ("capF19255", 141), ("capF19245", 142), ("capF19235", 143), ("capF19225", 144), ("capF19215", 145), ("capF19205", 146), ("capF19195", 147), ("capF19190", 148), ("capF19185", 149), ("capF19180", 150), ("capF19175", 151), ("capF19170", 152), ("capF19165", 153), ("capF19160", 154), ("capF19155", 155), ("capF19150", 156), ("capF19145", 157), ("capF19140", 158), ("capF19135", 159), ("capF19130", 160), ("capF19125", 161), ("capF19120", 162), ("capF19115", 163), ("capF19110", 164), ("capF19105", 165), ("capF19095", 166), ("capF19085", 167), ("capF19075", 168), ("capF19065", 169), ("capF19055", 170), ("capF19045", 171), ("capF19035", 172), ("capF19025", 173), ("capF19015", 174), ("capF19005", 175), ("capF18995", 176), ("capF18985", 177), ("capF18975", 178), ("capF18965", 179), ("capF18955", 180), ("capF18945", 181), ("capF18935", 182), ("capF18925", 183), ("capF18915", 184), ("capF18905", 185), ("capF18895", 186), ("capF18885", 187), ("capF18875", 188), ("capF18865", 189), ("capF18855", 190), ("capF18845", 191), ("capF18835", 192), ("capF18825", 193), ("capF18815", 194), ("capF18805", 195), ("capF18795", 196), ("capF18785", 197), ("capF18775", 198), ("capF18765", 199), ("capF18755", 200), ("capF18745", 201), ("capF18735", 202), ("capF18725", 203), ("capF18715", 204), ("capF18705", 205), ("capC1270", 206), ("capC1290", 207), ("capC1310", 208), ("capC1330", 209), ("capC1350", 210), ("capC1370", 211), ("capC1430", 212), ("capC1450", 213), ("capT1650", 214), ("capS1490", 215))

class FspR7ChannelSpacing(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("spacing50Ghz", 1), ("spacing100Ghz", 2), ("spacing200Ghz", 3), ("spacing25GHz", 4), ("spacingFlex", 5))

class FspR7ChannelSpacingCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capSpacing50Ghz", 1), ("capSpacing100Ghz", 2), ("capSpacing200Ghz", 3), ("capSpacing25GHz", 4), ("capSpacingFlex", 5))

class FspR7CodeGain(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("high", 1), ("mean", 2), ("low", 3))

class FspR7CodeGainCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capHigh", 1), ("capMean", 2), ("capLow", 3))

class FspR7ColumnMark(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("false", 1), ("true", 2))

class FspR7Conn(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("bi", 1), ("uni", 2))

class FspR7ConnCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capBi", 1), ("capUni", 2))

class FspR7ConnectorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("undefined", 0), ("lc", 1), ("rj45", 2), ("mupc", 3), ("dsub8", 4), ("usbS", 5), ("dsub44hd", 6), ("fcApc", 7), ("mpo", 8), ("mbnc", 9), ("hdBnc", 10), ("din", 11))

class FspR7ConnectorTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capLc", 1), ("capRj45", 2), ("capMupc", 3), ("capDsub8", 4), ("capUsbS", 5), ("capDsub44hd", 6), ("capFcApc", 7), ("capMpo", 8), ("capMbnc", 9), ("capHdBnc", 10), ("capDin", 11))

class FspR7ConnectState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("idle", 1), ("idleReceive", 2), ("idleTransmit", 3), ("busy", 4))

class FspR7CpAuthType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("simple", 2), ("md5", 3))

class FspR7CpAuthTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNone", 1), ("capSimple", 2), ("capMd5", 3))

class FspR7DCFiberType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("singleMode", 1), ("trueWaveRs", 2))

class FspR7DCFiberTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capSingleMode", 1), ("capTrueWaveRs", 2))

class FspR7DeploymentScenario(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("generic", 1), ("backToBack", 2), ("clientProt", 3), ("passThrough", 4))

class FspR7DeploymentScenarioCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capGeneric", 1), ("capBackToBack", 2), ("capClientProt", 3), ("capPassThrough", 4))

class FspR7DisableEnable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("disable", 1), ("enable", 2))

class FspR7DisableEnableCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capDisable", 1), ("capEnable", 2))

class FspR7DispersionCompensation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("undefined", 0), ("dispertion10", 1), ("dispertion20", 2), ("dispertion40", 3), ("dispertion60", 4), ("dispertion80", 5), ("dispertion100", 6), ("dispertion30", 7), ("dispertion50", 8), ("dispertion70", 9), ("dispertion90", 10), ("dispertion160", 11), ("dispertion240", 12), ("dispertion320", 13))

class FspR7DispersionCompensationCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capDispertion10", 1), ("capDispertion20", 2), ("capDispertion40", 3), ("capDispertion60", 4), ("capDispertion80", 5), ("capDispertion100", 6), ("capDispertion30", 7), ("capDispertion50", 8), ("capDispertion70", 9), ("capDispertion90", 10), ("capDispertion160", 11), ("capDispertion240", 12), ("capDispertion320", 13))

class FspR7DispersionConfig(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("oprCdc", 2))

class FspR7DispersionConfigCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capOprCdc", 2))

class FspR7DispersionModes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("auto", 1), ("man", 2))

class FspR7DispersionModesCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capAuto", 1), ("capMan", 2))

class FspR7EocProtAvailability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2))

class FspR7EdfaOutputPowerRating(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("undefined", 0), ("pwrOut10", 1), ("pwrOut17", 2), ("pwrOut18", 3), ("pwrOut20", 4), ("pwrOut15", 5), ("pwrOut27", 6), ("pwrOut26", 7), ("pwrOut20UN10NU", 8))

class FspR7EdfaOutputPowerRatingCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capPwrOut10", 1), ("capPwrOut17", 2), ("capPwrOut18", 3), ("capPwrOut20", 4), ("capPwrOut15", 5), ("capPwrOut27", 6), ("capPwrOut26", 7), ("capPwrOut20UN10NU", 8))

class FspR7EnableDisable(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("enable", 1), ("disable", 2))

class FspR7EnableDisableCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capEnable", 1), ("capDisable", 2))

class FspR7EncapsulationMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("tttgmp", 2), ("gmp", 3), ("gfpT", 4), ("gfpF", 5))

class FspR7EntitySecondaryStates(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ueq", 0), ("meaState", 1), ("sgeo", 2), ("lpbkState", 3), ("lkdo", 4), ("frcdState", 5), ("faf", 6), ("flt", 7), ("act", 8), ("stbyh", 9), ("psi", 10), ("pri", 11), ("dgn", 12), ("busy", 13), ("idleState", 14), ("receiveIdleState", 15), ("transmitIdleState", 16), ("sgeoSrv", 17), ("farEndPlugOutage", 18), ("aseTableBuildState", 19), ("testState", 20), ("testFailed", 21), ("stby", 22), ("stbyInh", 23), ("noBackup", 24), ("degrade", 25), ("swdl", 26))

class FspR7EntityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 122, 123, 124, 125, 126, 127, 130, 131, 132, 133, 137, 138, 140, 141, 142, 143, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 180, 182, 183, 185, 186, 187, 188, 190, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 213, 214, 215, 216, 217, 218, 219, 220, 223, 224, 225, 226, 227, 228, 229, 234, 235, 236, 237, 239, 240, 241, 242, 243, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 260, 261, 499, 501, 502, 503, 504, 505, 506, 507, 508, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528, 529, 534, 536, 537, 538, 539, 540, 541, 542), SingleValueConstraint(543, 544, 545, 546, 547, 548, 549, 550, 551, 552, 554, 555, 556, 557, 558, 559, 560, 561, 562, 564, 565, 566, 567, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 660, 661, 662, 663, 664, 665, 667, 668, 669, 670, 673, 674, 678, 681, 684, 685, 688, 689, 692, 693, 694, 695, 699, 700, 701, 702, 703, 704, 705, 1000, 1001, 1002, 1003, 1004, 1005, 1006, 1101, 1102, 1103, 1104, 1105, 1106, 1107, 1108, 1109))
    namedValues = NamedValues(("undefined", 0), ("eqpSh1hu", 1), ("eqpSh1huDc", 2), ("eqpSh3hu", 3), ("eqpSh7hu", 4), ("eqpF2kSh5hu", 5), ("eqpF2kSh6hu", 6), ("eqpDcm", 7), ("eqpSh9hu", 8), ("eqpUnknown", 19), ("eqpNcu", 20), ("eqpNcutif", 21), ("eqpScu", 22), ("eqpScue", 23), ("eqpR6cu", 24), ("eqpPsu1huac", 25), ("eqpPsu7huac", 26), ("eqpPsu7hudc", 27), ("eqpFcu7hu", 28), ("eqp2clsmd", 29), ("eqp2absmc", 30), ("eqp2bsmd", 31), ("eqp1Gsmud", 32), ("eqp4gsmd", 33), ("eqp8gsmd", 34), ("eqp1csmuc", 35), ("eqp1csmuewc", 36), ("eqp4csmd", 37), ("eqp4csmud", 38), ("eqp4csmc", 39), ("eqpOsfm", 40), ("eqp1pm", 41), ("eqp2pm", 42), ("eqp40csmd", 43), ("eqpDcf", 44), ("eqpEdfas", 45), ("eqpEdfasgc", 46), ("eqpEdfadgc", 47), ("eqpRaman", 48), ("eqp4tcc2g5", 49), ("eqp4tcc2g5d", 50), ("eqp4tcc10gd", 51), ("eqp4tcc10gc", 52), ("eqpWcc10gd", 53), ("eqpWcc10gc", 54), ("eqpWcc2g71N", 55), ("eqpWcc2g7d", 56), ("eqp2tcm2g5", 57), ("eqp2tca2g5", 58), ("eqp8tca10gd", 59), ("eqp8tca10gc", 60), ("eqpWca10gd", 61), ("eqpWca10gc", 62), ("eqp4tca4gd", 63), ("eqp4tca4gc", 64), ("eqpwca2g5", 65), ("eqp4tca1g3d", 66), ("eqp4tca1g3c", 67), ("eqp8tce2g5d", 68), ("eqp8tce2g5c", 69), ("eqpWcelsd", 70), ("eqpWcelsc", 71), ("eqpVsm", 72), ("eqpRsmolm", 73), ("eqpRsmsf", 74), ("eqpOscm", 75), ("eqp2oscm", 76), ("eqpDrm", 77), ("eqpXfpG", 78), ("eqpsfpd", 79), ("eqpSfpc", 80), ("eqpSfpg", 81), ("eqpSfpe", 82), ("eqpSh1hudcm", 83), ("eqpCustomc", 84), ("eqpCustomd", 85), ("eqpPsu1hudc", 86), ("eqpWcc2g7c", 87), ("eqp1csmuEwD", 88), ("eqp1csmuG", 89), ("eqp3BsmC", 90), ("eqp2Tca2g5s", 91), ("eqp8Csmuc", 92), ("eqpEdfaDgcb", 93), ("eqpOscmPn", 94), ("eqp4Tcc10gtd", 95), ("eqp4Tca4g", 96), ("eqpDcg", 97), ("eqp2Tcm2g5d", 98), ("eqp2Tcm2g5c", 99), ("eqpWcm2g5d", 100), ("eqpWcm2g5c", 101), ("eqpEdfmSgc", 102), ("eqpF2kDemiV2", 103), ("eqpPsm", 104), ("eqpNcu2e", 105), ("eqp8TceGl2g5d", 106), ("eqp8TceGl2g5c", 107), ("eqpDcf1hu", 108), ("eqp10tcc10gtd", 109), ("eqp10tcc10gd", 110), ("eqp10tcc10gc", 111), ("eqp16csmSfd", 112), ("eqpOsfmSf", 113), ("eqp2clsmSfd", 114), ("eqp3bsmEwc", 115), ("eqpEdfaSgcb", 116), ("eqpEdfaDgcv", 117), ("eqpWcc10gtd", 118), ("eqp2csmuEwc", 119), ("eqpEroadmDc", 120), ("eqpScuS", 122), ("eqp4opcm", 123), ("eqpUtm", 124), ("eqpPscu", 125), ("eqp40Csm2hu", 126), ("eqp2Twcc2g7", 127), ("eqp2Wca10g", 130), ("eqpNcuHp", 131), ("eqpNcu20085hu", 132), ("eqp20Pca10G", 133), ("eqpXfpC", 137), ("eqpXfpD", 138), ("eqpWcc40gtd", 140), ("eqpIlm", 141), ("eqpNcuII", 142), ("eqpCem9hu", 143), ("eqp8roadmC40", 148), ("eqp4Tcc40gtd", 149), ("eqp2pca10g", 150), ("eqp10pca10g", 151), ("eqp1csmuD", 152), ("eqpSfpOsC", 153), ("eqpSfpOdC", 154), ("eqpSfpOsG", 155), ("eqpSfpOdG", 156), ("eqpRoadmC80", 157), ("eqpccm8", 158), ("eqpPsu9hudc", 159), ("eqp4tca4gus", 160), ("eqp40Csm3huD", 161), ("eqp5psm", 162), ("eqpFan9hu", 163), ("eqp5tce10gtd", 164), ("eqp10tccs10gtd", 165), ("eqp40Csm3hudcD", 166), ("eqp40Csm3hudcDi", 167), ("eqp5gsmD", 169), ("eqp8csmD", 170), ("eqp2otfm", 171), ("eqp8otdr3hu", 172), ("eqpXfptD", 173), ("eqp40Csm3huDi", 174), ("eqp8CcmC80", 175), ("eqpEdfaD27", 176), ("eqp2Wcc10g", 177), ("eqp8RoadmC80", 178), ("eqp2Wcc10gAes", 180), ("eqp5tce10gtaesd", 182), ("eqpSh1hupf", 183), ("eqpFan1hu", 185), ("eqp10tcc10g", 186), ("eqpXfpOtnD", 187), ("eqpNcu2p", 188), ("eqpPsu9huac", 190), ("eqp2Raman", 192), ("eqpEdfaS26", 193), ("eqp5tces10gtd", 194), ("eqpScuII", 195), ("eqp11RoadmC96", 196), ("eqp8AdmC96", 197), ("eqp8CxmC96", 198), ("eqp8Shm", 199), ("eqpAmpShgcv", 200), ("eqpAmpSlgcv", 201), ("eqp2RamanC15", 202), ("eqpWcc100gtD", 203), ("eqpCfp4g", 204), ("eqpCfp10g", 205), ("eqpXfpTlnD", 213), ("eqp5tces10gtaesd", 214), ("eqp10tce100g", 215), ("eqp96Csm4HuD", 216), ("eqp4CfptD", 217), ("eqp2psm", 218), ("eqpWce100G", 219), ("eqp10Wxc10g", 220), ("eqp10tcc100gtbD", 223), ("eqp9RoadmC96", 224), ("eqp4Wce16g", 225), ("eqpSfpBG", 226), ("eqpSfpCdrG", 227), ("eqp10tce100gGf", 228), ("eqpSfpCdrC", 229), ("eqp5tce10gaes", 234), ("eqp5tce10g", 235), ("eqp5tces10gaes", 236), ("eqp5tces10g", 237), ("eqp4roadmC96", 239), ("eqpWcc100gtbD", 240), ("eqpEdfaS20", 241), ("eqp10tccSdi10g", 242), ("eqp4roadmEC96", 243), ("eqpSfptD", 245), ("eqpSfp2TxG", 246), ("eqpSfp2RxG", 247), ("eqpSfp2Txe", 248), ("eqpSfp2Rxe", 249), ("eqp2EdfaS20S10", 250), ("eqp10Tce100Gb", 251), ("eqp10Tce100gAes", 252), ("eqpSfpCdrD", 253), ("eqpSh1huDcEtemp", 254), ("eqp8psm", 255), ("eqp9ccmC96", 256), ("eqpWce100GB", 257), ("eqp5wca16G", 260), ("eqpCfptCd", 261), ("eqpPtp", 499), ("ifTypeOtu1", 501), ("ifTypeOtu2", 502), ("ifType10GbE", 503), ("ifTypeOc192", 504), ("ifTypeOc48", 505), ("ifTypeStm16", 506), ("ifTypeStm64", 507), ("ifType10GFC", 508), ("ifTypeF1062", 510), ("ifTypeF1250", 511), ("ifTypeFC", 512), ("ifTypeF125", 513), ("ifTypeF200", 514), ("ifTypeF9953", 515), ("ifTypeF10312", 516), ("ifTypeF10518", 517), ("ifTypeF2488", 518), ("ifTypeGfpF", 519), ("ifTypeGfpT", 520), ("ifTypeDccL", 521), ("ifTypeDccS", 522), ("ifTypeDccP", 523), ("ifTypeOdu1", 524), ("ifTypeGcc0", 525), ("ifTypeGcc1", 526), ("ifTypeGcc2", 527), ("ifTypeoch", 528), ("ifTypeOm", 529), ("ifTypeOt", 534), ("ifTypeE10or100bt", 536), ("ifTypeE100fx", 537), ("ifTypeCl", 538), ("ifType2GFC", 539), ("ifType2GCL", 540), ("ifType1GbE", 541), ("ifTypeEoc", 542)) + NamedValues(("ifTypeSwitch", 543), ("ifTypePassive", 544), ("ifTypeF2500", 545), ("ifTypeSc", 546), ("ifTypeUch", 547), ("ifTypeF155", 548), ("ifTypeF622", 549), ("ifTypeF2125", 550), ("ifTypeF2666", 551), ("ifTypeF4250", 552), ("ifTypeF10709", 554), ("ifTypeF11095", 555), ("ifTypeF11318", 556), ("ifTypeLs", 557), ("ifType4Gfc", 558), ("ifTypeGcc0S", 559), ("ifType2R", 560), ("ifTypePppIp", 561), ("ifTypeLanIp", 562), ("ifTypeSerial", 564), ("ifTypeModem", 565), ("ifTypeAdapt", 566), ("ifTypeAdaptd", 567), ("ifTypeGBEFR", 569), ("ifTypeVc4", 570), ("ifTypeVc3", 571), ("ifTypeSts1", 572), ("ifTypeEdfa", 573), ("ifTypeEdfaMid", 574), ("ifType10Gdw", 575), ("ifTypeOtu2Lan", 576), ("ifTypeOtu1Lan", 577), ("ifTypeOtu1Fc", 578), ("ifTypeOtu1Fc2G", 579), ("ifTypeF197", 580), ("ifTypeTif", 581), ("ifTypeSts3c", 582), ("ifTypeVs1", 583), ("ifType1GbETH", 584), ("ifTypeStm1", 585), ("ifTypeStm4", 586), ("ifTypeOc3", 587), ("ifTypeOc12", 588), ("ifTypeOtu1Stm1", 589), ("ifTypeOtu1Stm4", 590), ("ifTypeF166", 591), ("ifTypeF666", 592), ("ifTypeI2C", 593), ("ifTypeLifIP", 594), ("ifTypeSts24c", 595), ("ifTypeSts48c", 596), ("ifTypeLifte", 597), ("ifTypeRaman", 598), ("ifTypeIpWhiteList", 599), ("ifTypeOspfIp", 600), ("ifTypeEncapIp", 601), ("ifTypeOtu3", 602), ("ifTypeStm256", 603), ("ifTypeOc768", 604), ("ifTypeF10664", 605), ("ifTypeOdu2", 606), ("ifTypeF39813", 607), ("ifTypeVc4c8", 608), ("ifTypeVc4c16", 609), ("ifTypeF8500", 610), ("ifTypePb", 611), ("ifTypePolicer", 612), ("ifTypeQueue", 613), ("ifTypeFlowPoint", 614), ("ifTypeLag", 615), ("ifTypeElinePPP", 616), ("ifTypeEtree", 617), ("ifTypeEline", 618), ("ifTypeElan", 619), ("ifTypeCtrans", 620), ("ifTypeVs0", 621), ("ifTypeTug", 622), ("ifTypeMd", 623), ("ifTypeMa", 624), ("ifTypeDownMep", 625), ("ifTypeFMep", 626), ("ifType8Gfc", 627), ("ifType10Gib", 628), ("ifTypeF10000", 629), ("ifTypeOtu2pFC8", 630), ("ifTypeOtu2pIB", 631), ("ifTypeOtu2pFC", 632), ("ifTypeOtu2pLAN", 633), ("ifTypeOtu2p", 634), ("ifTypeUpMep", 635), ("ifTypeOtdrCh", 636), ("ifTypeMaNet", 637), ("ifTypeMaComp", 638), ("ifTypeBridge", 639), ("ifType1000BaseT", 640), ("ifTypeOtu2E", 641), ("ifTypeOtu1E", 642), ("ifTypeOtu2F", 643), ("ifTypeF11049", 644), ("ifTypeLifteNum", 645), ("ifTypeLifteUnn", 646), ("ifTypeLifPbNum", 647), ("ifTypeLifSubUnn", 648), ("ifType5Gib", 649), ("ifTypeF5000", 650), ("ifTypeOtu2eEth", 651), ("ifTypeOdu0", 652), ("ifTypeFcu", 653), ("ifTypeOtu4", 654), ("ifType100GbE", 660), ("ifTypeOptical", 661), ("ifType10GbEWan", 662), ("ifType10GbELan", 663), ("ifTypeOduFlx", 664), ("ifTypeOtlc", 665), ("ifTypeOtu2ps", 667), ("ifTypeOdu2E", 668), ("ifTypeOdu1E", 669), ("ifTypeOdu2Lan", 670), ("ifTypeLifVTeNum", 673), ("ifTypeLifVTeUnn", 674), ("ifTypeF14025", 678), ("ifTypeF270", 681), ("ifTypeF1485", 684), ("ifTypeF2970", 685), ("ifTypeF1483", 688), ("ifTypeF2967", 689), ("ifType40GbE", 692), ("ifTypeOdu3", 693), ("ifTypeF41250", 694), ("ifTypeF103125", 695), ("ifTypeF1228", 699), ("ifTypeF2457", 700), ("ifTypeF3072", 701), ("ifTypeF4915", 702), ("ifTypeF6144", 703), ("ifTypeF9830", 704), ("ifTypeF10137", 705), ("grpffpCh", 1000), ("grpffpOm", 1001), ("grpCrsDcn", 1002), ("grpLanDcn", 1003), ("grpConn", 1004), ("grpffpVchN", 1005), ("grpVirtualConn", 1006), ("conFanContainer", 1101), ("conModContainer", 1102), ("conPlugContainer", 1103), ("grpCrsCh", 1104), ("physTermPoint", 1105), ("virtualTermPoint", 1106), ("fanContainer", 1107), ("protectionCable", 1108), ("filterCable", 1109))

class FspR7EqlzAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("enabled", 1), ("disabled", 2))

class FspR7EqlzAdminStateCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capEnabled", 1), ("capDisabled", 2))

class FspR7ErrorFwdMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 0), ("ais", 1), ("epc", 2), ("idle", 3), ("lsrOff", 4), ("lsrBrk", 5), ("txOff", 6))

class FspR7ErrorFwdModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capAis", 1), ("capEpc", 2), ("capIdle", 3), ("capLsrOff", 4), ("capLsrBrk", 5), ("capTxOff", 6))

class FspR7FanMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("eco", 1), ("high1", 2))

class FspR7FanProfile(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("eco", 1), ("high1", 2))

class FspR7FDStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("enabled", 1), ("disabledSystem", 2), ("disabledModule", 3), ("disabledPtp", 4), ("disabledAdmin", 5))

class FspR7FDStatusCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capEnabled", 1), ("capDisabledSystem", 2), ("capDisabledModule", 3), ("capDisabledPtp", 4), ("capDisabledAdmin", 5))

class FspR7FecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("undefined", 0), ("gFec", 1), ("eFec", 2), ("noFec", 3), ("eFec1", 4), ("eFec2", 5), ("eFec3", 6), ("eFec4", 7), ("eFecX", 8), ("eFec5", 9), ("eFec6", 10))

class FspR7FecTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capGFec", 1), ("capEFec", 2), ("capNoFec", 3), ("capEFec1", 4), ("capEFec2", 5), ("capEFec3", 6), ("capEFec4", 7), ("capEFecX", 8), ("capEFec5", 9), ("capEFec6", 10))

class FspR7FiberBrand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("undefined", 0), ("g652", 1), ("g653", 2), ("g655", 3), ("smf28e", 4), ("allWave", 5), ("leaf", 6), ("twRs", 7), ("twPl", 8), ("twCl", 9), ("teraLight", 10), ("smfLs", 11), ("metrocor", 12))

class FspR7FiberBrandCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capG652", 1), ("capG653", 2), ("capG655", 3), ("capSmf28e", 4), ("capAllWave", 5), ("capLeaf", 6), ("capTwRs", 7), ("capTwPl", 8), ("capTwCl", 9), ("capTeraLight", 10), ("capSmfLs", 11), ("capMetrocor", 12))

class FspR7FiberDetect(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("enabled", 1), ("disabled", 2))

class FspR7FiberDetectCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capEnabled", 1), ("capDisabled", 2))

class FspR7FlowControlMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("hwControl", 2), ("pause", 3))

class FspR7FlowControlModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNone", 1), ("capHwControl", 2), ("capPause", 3))

class FspR7ForceConfig(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("release", 1), ("force", 2))

class FspR7ForceConfigCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRelease", 1), ("capForce", 2))

class FspR7ForcedStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("active", 1), ("forcedDestroy", 2))

class FspR7ForcedStatusCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capActive", 1), ("capForcedDestroy", 2))

class FspR7FrameFormat(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 99))
    namedValues = NamedValues(("undefined", 0), ("otn", 1), ("sdh", 2), ("sonet", 3), ("ethernet", 4), ("fiberchannel", 5), ("infiniband", 6), ("couplinglink", 7), ("transparent", 8), ("notDefined", 99))

class FspR7FrameFormatCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capOtn", 1), ("capSdh", 2), ("capSonet", 3), ("capEthernet", 4), ("capFiberchannel", 5), ("capInfiniband", 6), ("capCouplinglink", 7), ("capTransparent", 8), ("capNotDefined", 99))

class FspR7FunctionCrs(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("add", 1), ("drop", 2), ("pass", 3), ("hairpin", 4), ("select", 5), ("addDrop", 6), ("dropCont", 7))

class FspR7FunctionCrsCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capAdd", 1), ("capDrop", 2), ("capPass", 3), ("capHairpin", 4), ("capSelect", 5), ("capAddDrop", 6), ("capDropCont", 7))

class FspR7Gain(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("gain24", 1), ("gain25", 2))

class FspR7GainCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capGain24", 1), ("capGain25", 2))

class FspR7GainRange(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("high", 1), ("low", 2), ("lowUNlowNU", 3))

class FspR7GainRangeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capHigh", 1), ("capLow", 2), ("capLowUNlowNU", 3))

class FspR7GropticsType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("sr4", 1), ("lr4", 2), ("user", 3), ("sr10", 4))

class FspR7GropticsTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capSr4", 1), ("capLr4", 2), ("capUser", 3), ("capSr10", 4))

class FspR7InitEqualization(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("opr", 2))

class FspR7InitEqualizationCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capOpr", 2))

class FspR7Integer32Caps(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d:4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class FspR7InterfaceFunction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("undefined", 0), ("transport", 1), ("switch", 2), ("edfa", 3), ("super", 4), ("passive", 5), ("active", 6), ("raman", 7), ("physicalTerm", 8))

class FspR7InterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 34, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 66, 67, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 160, 161, 162, 163, 164, 165, 167, 168, 169, 170, 173, 174, 178, 181, 184, 185, 188, 189, 192, 193, 194, 195, 199, 200, 201, 202, 203, 204, 205))
    namedValues = NamedValues(("undefined", 0), ("ifTypeOtu1", 1), ("ifTypeOtu2", 2), ("ifType10GbE", 3), ("ifTypeOc192", 4), ("ifTypeOc48", 5), ("ifTypeStm16", 6), ("ifTypeStm64", 7), ("ifType10GFC", 8), ("ifTypeF1062", 10), ("ifTypeF1250", 11), ("ifTypeFC", 12), ("ifTypeF125", 13), ("ifTypeF200", 14), ("ifTypeF9953", 15), ("ifTypeF10312", 16), ("ifTypeF10518", 17), ("ifTypeF2488", 18), ("ifTypeGfpF", 19), ("ifTypeGfpT", 20), ("ifTypeDccL", 21), ("ifTypeDccS", 22), ("ifTypeDccP", 23), ("ifTypeOdu1", 24), ("ifTypeGcc0", 25), ("ifTypeGcc1", 26), ("ifTypeGcc2", 27), ("ifTypeoch", 28), ("ifTypeOm", 29), ("ifTypeOt", 34), ("ifTypeE10or100bt", 36), ("ifTypeE100fx", 37), ("ifTypeCl", 38), ("ifType2GFC", 39), ("ifType2GCL", 40), ("ifType1GbE", 41), ("ifTypeEoc", 42), ("ifTypeSwitch", 43), ("ifTypePassive", 44), ("ifTypeF2500", 45), ("ifTypeSc", 46), ("ifTypeUch", 47), ("ifTypeF155", 48), ("ifTypeF622", 49), ("ifTypeF2125", 50), ("ifTypeF2666", 51), ("ifTypeF4250", 52), ("ifTypeF10709", 54), ("ifTypeF11095", 55), ("ifTypeF11318", 56), ("ifTypeLs", 57), ("ifType4Gfc", 58), ("ifTypeGcc0S", 59), ("ifType2R", 60), ("ifTypePppIp", 61), ("ifTypeLanIp", 62), ("ifTypeSerial", 64), ("ifTypeModem", 65), ("ifTypeAdapt", 66), ("ifTypeAdaptd", 67), ("ifTypeGBEFR", 69), ("ifTypeVc4", 70), ("ifTypeVc3", 71), ("ifTypeSts1", 72), ("ifTypeEdfa", 73), ("ifTypeEdfaMid", 74), ("ifType10Gdw", 75), ("ifTypeOtu2Lan", 76), ("ifTypeOtu1Lan", 77), ("ifTypeOtu1Fc", 78), ("ifTypeOtu1Fc2G", 79), ("ifTypeF197", 80), ("ifTypeTif", 81), ("ifTypeSts3c", 82), ("ifTypeVs1", 83), ("ifType1GbETH", 84), ("ifTypeStm1", 85), ("ifTypeStm4", 86), ("ifTypeOc3", 87), ("ifTypeOc12", 88), ("ifTypeOtu1Stm1", 89), ("ifTypeOtu1Stm4", 90), ("ifTypeF166", 91), ("ifTypeF666", 92), ("ifTypeI2C", 93), ("ifTypeLifIP", 94), ("ifTypeSts24c", 95), ("ifTypeSts48c", 96), ("ifTypeLifte", 97), ("ifTypeRaman", 98), ("ifTypeIpWhiteList", 99), ("ifTypeOspfIp", 100), ("ifTypeEncapIp", 101), ("ifTypeOtu3", 102), ("ifTypeStm256", 103), ("ifTypeOc768", 104), ("ifTypeF10664", 105), ("ifTypeOdu2", 106), ("ifTypeF39813", 107), ("ifTypeVc4c8", 108), ("ifTypeVc4c16", 109), ("ifTypeF8500", 110), ("ifTypePb", 111), ("ifTypePolicer", 112), ("ifTypeQueue", 113), ("ifTypeFlowPoint", 114), ("ifTypeLag", 115), ("ifTypeElinePPP", 116), ("ifTypeEtree", 117), ("ifTypeEline", 118), ("ifTypeElan", 119), ("ifTypeCtrans", 120), ("ifTypeVs0", 121), ("ifTypeTug", 122), ("ifTypeMd", 123), ("ifTypeMa", 124), ("ifTypeDownMep", 125), ("ifTypeFMep", 126), ("ifType8Gfc", 127), ("ifType10Gib", 128), ("ifTypeF10000", 129), ("ifTypeOtu2pFC8", 130), ("ifTypeOtu2pIB", 131), ("ifTypeOtu2pFC", 132), ("ifTypeOtu2pLAN", 133), ("ifTypeOtu2p", 134), ("ifTypeUpMep", 135), ("ifTypeOtdrCh", 136), ("ifTypeMaNet", 137), ("ifTypeMaComp", 138), ("ifTypeBridge", 139), ("ifType1000BaseT", 140), ("ifTypeOtu2E", 141), ("ifTypeOtu1E", 142), ("ifTypeOtu2F", 143), ("ifTypeF11049", 144), ("ifTypeLifteNum", 145), ("ifTypeLifteUnn", 146), ("ifTypeLifPbNum", 147), ("ifTypeLifSubUnn", 148), ("ifType5Gib", 149), ("ifTypeF5000", 150), ("ifTypeOtu2eEth", 151), ("ifTypeOdu0", 152), ("ifTypeFcu", 153), ("ifTypeOtu4", 154), ("ifType100GbE", 160), ("ifTypeOptical", 161), ("ifType10GbEWan", 162), ("ifType10GbELan", 163), ("ifTypeOduFlx", 164), ("ifTypeOtlc", 165), ("ifTypeOtu2ps", 167), ("ifTypeOdu2E", 168), ("ifTypeOdu1E", 169), ("ifTypeOdu2Lan", 170), ("ifTypeLifVTeNum", 173), ("ifTypeLifVTeUnn", 174), ("ifTypeF14025", 178), ("ifTypeF270", 181), ("ifTypeF1485", 184), ("ifTypeF2970", 185), ("ifTypeF1483", 188), ("ifTypeF2967", 189), ("ifType40GbE", 192), ("ifTypeOdu3", 193), ("ifTypeF41250", 194), ("ifTypeF103125", 195), ("ifTypeF1228", 199), ("ifTypeF2457", 200), ("ifTypeF3072", 201), ("ifTypeF4915", 202), ("ifTypeF6144", 203), ("ifTypeF9830", 204), ("ifTypeF10137", 205))

class FspR7InterfaceTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capIfTypeOtu1", 1), ("capIfTypeOtu2", 2), ("capIfType10GbE", 3), ("capIfTypeOc192", 4), ("capIfTypeOc48", 5), ("capIfTypeStm16", 6), ("capIfTypeStm64", 7), ("capIfType10GFC", 8), ("capIfTypeF1062", 10), ("capIfTypeF1250", 11), ("capIfTypeFC", 12), ("capIfTypeF125", 13), ("capIfTypeF200", 14), ("capIfTypeF9953", 15), ("capIfTypeF10312", 16), ("capIfTypeF10518", 17), ("capIfTypeF2488", 18), ("capIfTypeGfpF", 19), ("capIfTypeGfpT", 20), ("capIfTypeDccL", 21), ("capIfTypeDccS", 22), ("capIfTypeDccP", 23), ("capIfTypeOdu1", 24), ("capIfTypeGcc0", 25), ("capIfTypeGcc1", 26), ("capIfTypeGcc2", 27), ("capIfTypeoch", 28), ("capIfTypeOm", 29), ("capIfTypeOt", 34), ("capIfTypeE10or100bt", 36), ("capIfTypeE100fx", 37), ("capIfTypeCl", 38), ("capIfType2GFC", 39), ("capIfType2GCL", 40), ("capIfType1GbE", 41), ("capIfTypeEoc", 42), ("capIfTypeSwitch", 43), ("capIfTypePassive", 44), ("capIfTypeF2500", 45), ("capIfTypeSc", 46), ("capIfTypeUch", 47), ("capIfTypeF155", 48), ("capIfTypeF622", 49), ("capIfTypeF2125", 50), ("capIfTypeF2666", 51), ("capIfTypeF4250", 52), ("capIfTypeF10709", 54), ("capIfTypeF11095", 55), ("capIfTypeF11318", 56), ("capIfTypeLs", 57), ("capIfType4Gfc", 58), ("capIfTypeGcc0S", 59), ("capIfType2R", 60), ("capIfTypePppIp", 61), ("capIfTypeLanIp", 62), ("capIfTypeSerial", 64), ("capIfTypeModem", 65), ("capIfTypeAdapt", 66), ("capIfTypeAdaptd", 67), ("capIfTypeGBEFR", 69), ("capIfTypeVc4", 70), ("capIfTypeVc3", 71), ("capIfTypeSts1", 72), ("capIfTypeEdfa", 73), ("capIfTypeEdfaMid", 74), ("capIfType10Gdw", 75), ("capIfTypeOtu2Lan", 76), ("capIfTypeOtu1Lan", 77), ("capIfTypeOtu1Fc", 78), ("capIfTypeOtu1Fc2G", 79), ("capIfTypeF197", 80), ("capIfTypeTif", 81), ("capIfTypeSts3c", 82), ("capIfTypeVs1", 83), ("capIfType1GbETH", 84), ("capIfTypeStm1", 85), ("capIfTypeStm4", 86), ("capIfTypeOc3", 87), ("capIfTypeOc12", 88), ("capIfTypeOtu1Stm1", 89), ("capIfTypeOtu1Stm4", 90), ("capIfTypeF166", 91), ("capIfTypeF666", 92), ("capIfTypeI2C", 93), ("capIfTypeLifIP", 94), ("capIfTypeSts24c", 95), ("capIfTypeSts48c", 96), ("capIfTypeLifte", 97), ("capIfTypeRaman", 98), ("capIfTypeIpWhiteList", 99), ("capIfTypeOspfIp", 100), ("capIfTypeEncapIp", 101), ("capIfTypeOtu3", 102), ("capIfTypeStm256", 103), ("capIfTypeOc768", 104), ("capIfTypeF10664", 105), ("capIfTypeOdu2", 106), ("capIfTypeF39813", 107), ("capIfTypeVc4c8", 108), ("capIfTypeVc4c16", 109), ("capIfTypeF8500", 110), ("capIfTypePb", 111), ("capIfTypePolicer", 112), ("capIfTypeQueue", 113), ("capIfTypeFlowPoint", 114), ("capIfTypeLag", 115), ("capIfTypeElinePPP", 116), ("capIfTypeEtree", 117), ("capIfTypeEline", 118), ("capIfTypeElan", 119), ("capIfTypeCtrans", 120), ("capIfTypeVs0", 121), ("capIfTypeTug", 122), ("capIfTypeMd", 123), ("capIfTypeMa", 124), ("capIfTypeDownMep", 125), ("capIfTypeFMep", 126), ("capIfType8Gfc", 127), ("capIfType10Gib", 128), ("capIfTypeF10000", 129), ("capIfTypeOtu2pFC8", 130), ("capIfTypeOtu2pIB", 131), ("capIfTypeOtu2pFC", 132), ("capIfTypeOtu2pLAN", 133), ("capIfTypeOtu2p", 134), ("capIfTypeUpMep", 135), ("capIfTypeOtdrCh", 136), ("capIfTypeMaNet", 137), ("capIfTypeMaComp", 138), ("capIfTypeBridge", 139), ("capIfType1000BaseT", 140), ("capIfTypeOtu2E", 141), ("capIfTypeOtu1E", 142), ("capIfTypeOtu2F", 143), ("capIfTypeF11049", 144), ("capIfTypeLifteNum", 145), ("capIfTypeLifteUnn", 146), ("capIfTypeLifPbNum", 147), ("capIfTypeLifSubUnn", 148), ("capIfType5Gib", 149), ("capIfTypeF5000", 150), ("capIfTypeOtu2eEth", 151), ("capIfTypeOdu0", 152), ("capIfTypeFcu", 153), ("capIfTypeOtu4", 154), ("capIfType100GbE", 160), ("capIfTypeOptical", 161), ("capIfType10GbEWan", 162), ("capIfType10GbELan", 163), ("capIfTypeOduFlx", 164), ("capIfTypeOtlc", 165), ("capIfTypeOtu2ps", 167), ("capIfTypeOdu2E", 168), ("capIfTypeOdu1E", 169), ("capIfTypeOdu2Lan", 170), ("capIfTypeLifVTeNum", 173), ("capIfTypeLifVTeUnn", 174), ("capIfTypeF14025", 178), ("capIfTypeF270", 181), ("capIfTypeF1485", 184), ("capIfTypeF2970", 185), ("capIfTypeF1483", 188), ("capIfTypeF2967", 189), ("capIfType40GbE", 192), ("capIfTypeOdu3", 193), ("capIfTypeF41250", 194), ("capIfTypeF103125", 195), ("capIfTypeF1228", 199), ("capIfTypeF2457", 200), ("capIfTypeF3072", 201), ("capIfTypeF4915", 202), ("capIfTypeF6144", 203), ("capIfTypeF9830", 204), ("capIfTypeF10137", 205))

class FspR7InvertTelemetryInputLogic(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("almClosed", 1), ("almOpen", 2))

class FspR7InvertTelemetryInputLogicCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capAlmClosed", 1), ("capAlmOpen", 2))

class FspR7IpType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("unnumbered", 1), ("numbered", 2))

class FspR7IpTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capUnnumbered", 1), ("capNumbered", 2))

class FspR7IpMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("ipv4", 2), ("ipv4ipv6", 3), ("ipv6", 4))

class FspR7IpModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNone", 1), ("capIpv4", 2), ("capIpv4ipv6", 3), ("capIpv6", 4))

class FspR7Ipv6Address(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class FspR7IPv6Type(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("numbered", 2))

class FspR7IPv6TypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNone", 1), ("capNumbered", 2))

class FspR7KeyLength(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("length2048", 1), ("length4096", 2))

class FspR7KeyLengthCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capLength2048", 1), ("capLength4096", 2))

class FspR7LacpMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("active", 1), ("passive", 2), ("disable", 3))

class FspR7LacpModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capActive", 1), ("capPassive", 2), ("capDisable", 3))

class FspR7LacpTimeout(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("advaExtraShort", 1), ("short", 2), ("long", 3))

class FspR7LacpTimeoutCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capAdvaExtraShort", 1), ("capShort", 2), ("capLong", 3))

class FspR7LaneGroupInventory(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("f19595f19520", 1), ("f19515f19440", 2), ("f19435f19360", 3), ("f19355f19280", 4), ("f19275f19200", 5), ("f19600f19200", 6), ("f19600f19125", 7))

class FspR7LaneGroupInventoryCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capF19595f19520", 1), ("capF19515f19440", 2), ("capF19435f19360", 3), ("capF19355f19280", 4), ("capF19275f19200", 5), ("capF19600f19200", 6), ("capF19600f19125", 7))

class FspR7LagFendState(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2)

class FspR7LagIdFend(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 10)

class FspR7LagPorts(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 200)

class FspR7LagPortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("type1gb", 1), ("type10gb", 2))

class FspR7LagPortTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capType1gb", 1), ("capType10gb", 2))

class FspR7LagStandby(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 200)

class FspR7LagState(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2)

class FspR7LagSysIdFend(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class FspR7LaserDelayTimer(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("disable", 1), ("enableLsrOffTm", 2), ("enableLsrOnTm", 3))

class FspR7LaserDelayTimerCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capDisable", 1), ("capEnableLsrOffTm", 2), ("capEnableLsrOnTm", 3))

class FspR7LaserForcedOperation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("opr", 2))

class FspR7LaserForcedOperationCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capOpr", 2))

class FspR7LineCoding(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 99))
    namedValues = NamedValues(("undefined", 0), ("ookNrz", 1), ("dpsk", 2), ("qpsk", 3), ("dpQpsk", 4), ("odbPsbt", 5), ("mQam", 6), ("ofdm", 7), ("notDefined", 99))

class FspR7LineCodingCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capOokNrz", 1), ("capDpsk", 2), ("capQpsk", 3), ("capDpQpsk", 4), ("capOdbPsbt", 5), ("capMQam", 6), ("capOfdm", 7), ("capNotDefined", 99))

class FspR7LossAttenuation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("opr", 2))

class FspR7LossAttenuationCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capOpr", 2))

class FspR7NoYes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("no", 1), ("yes", 2))

class FspR7NoYesCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNo", 1), ("capYes", 2))

class FspR7ManualAuto(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("manual", 1), ("automatic", 2))

class FspR7ManualAutoCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capManual", 1), ("capAutomatic", 2))

class FspR7MaxBitErrorRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("undefined", 0), ("ber1e2", 1), ("ber1e3", 2), ("ber1e4", 3), ("ber1e5", 4), ("ber1e6", 5), ("ber1e7", 6), ("ber1e8", 7), ("ber1e9", 8), ("ber1e10", 9), ("ber1e11", 10), ("ber1e12", 11), ("ber1e13", 12), ("ber1e14", 13), ("ber1e15", 14))

class FspR7MaxBitErrorRateCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capBer1e2", 1), ("capBer1e3", 2), ("capBer1e4", 3), ("capBer1e5", 4), ("capBer1e6", 5), ("capBer1e7", 6), ("capBer1e8", 7), ("capBer1e9", 8), ("capBer1e10", 9), ("capBer1e11", 10), ("capBer1e12", 11), ("capBer1e13", 12), ("capBer1e14", 13), ("capBer1e15", 14))

class FspR7Mapping(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("frame", 1), ("trans", 2))

class FspR7MappingCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capFrame", 1), ("capTrans", 2))

class FspR7MonLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("undefined", 0), ("phys", 1), ("otnOtu", 2), ("otnOdu", 3), ("otnOpu", 4), ("sonetSection", 5), ("sonetLine", 6), ("sonetPath", 7), ("pcs", 8))

class FspR7MuxMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("sdhSonet", 1), ("otn", 2))

class FspR7MuxMethodCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capSdhSonet", 1), ("capOtn", 2))

class FspR7NCTraceId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("undefined", 0), ("id1", 1), ("id2", 2), ("id3", 3), ("id4", 4), ("id5", 5), ("id6", 6), ("id7", 7), ("id8", 8))

class FspR7NCTRouteType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("fiber", 2), ("cable", 3), ("backPlane", 4), ("equipment", 5), ("provisioned", 6))

class FspR7NdpCleanup(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("opr", 2))

class FspR7NdpCleanupCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capOpr", 2))

class FspR7NewSshHostKey(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("apply", 2))

class FspR7NtpAdminState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 2, 6))
    namedValues = NamedValues(("undefined", 0), ("is", 2), ("dsbld", 6))

class FspR7NtpSyncStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("noData", 1), ("systemPeer", 2), ("falseTicker", 3), ("candidate", 4), ("discarded", 5), ("inProgress", 6), ("notApplicable", 7))

class FspR7NtpTest(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("ntpTest", 2))

class FspR7NtpTestStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("success", 1), ("fail", 2), ("idle", 3), ("inProgress", 4))

class FspR7NumberOfChannels(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("channels20", 1), ("channels40", 2), ("channels80", 3), ("channels96", 4), ("channels8", 5))

class FspR7NumberOfChannelsCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capChannels20", 1), ("capChannels40", 2), ("capChannels80", 3), ("capChannels96", 4), ("capChannels8", 5))

class FspR7NumberOfChannelsProv(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("channels20", 1), ("channels40", 2), ("channels80", 3))

class FspR7NumberOfChannelsProvCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capChannels20", 1), ("capChannels40", 2), ("capChannels80", 3))

class FspR7OdtuType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("undefined", 0), ("odtu01", 1), ("odtu12", 2), ("odtu2dsh1", 3), ("odtu2dshTS", 4), ("odtu13", 5), ("odtu23", 6), ("odtu3dsh1", 7), ("odtu3dsh9", 8), ("odtu3dshTS", 9), ("odtu4dsh1", 10), ("odtu4dsh2", 11), ("odtu4dsh8", 12), ("odtu4dsh31", 13), ("odtu4dshTS", 14))

class FspR7OperState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("nr", 1), ("anr", 2), ("out", 3), ("un", 4))

class FspR7OpticalBand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 0), ("bandC", 1), ("bandL", 2), ("bandA", 3), ("bandB", 4), ("bandCi", 5), ("bandCandCi", 6))

class FspR7OpticalBandCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capBandC", 1), ("capBandL", 2), ("capBandA", 3), ("capBandB", 4), ("capBandCi", 5), ("capBandCandCi", 6))

class FspR7OpticalFiberType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("singleMode", 1), ("multiMode", 2), ("any", 3))

class FspR7OpticalFiberTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capSingleMode", 1), ("capMultiMode", 2), ("capAny", 3))

class FspR7OpticalGroup(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31))
    namedValues = NamedValues(("undefined", 0), ("d01d04", 1), ("d05d08", 2), ("d09d12", 3), ("d13d16", 4), ("d17d20", 5), ("d21d24", 6), ("d25d28", 7), ("d29d32", 8), ("d33d36", 9), ("d37d40", 10), ("d41d44", 11), ("d45d48", 12), ("d49d52", 13), ("d53d56", 14), ("d57d60", 15), ("d61d64", 16), ("f19590f19560", 17), ("f19550f19520", 18), ("f19510f19480", 19), ("f19470f19440", 20), ("f19430f19400", 21), ("f19390f19360", 22), ("f19350f19320", 23), ("f19310f19280", 24), ("f19270f19240", 25), ("f19230f19200", 26), ("f19590f19520", 27), ("f19510f19440", 28), ("f19430f19360", 29), ("f19350f19280", 30), ("f19270f19200", 31))

class FspR7OpticalGroupCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capD01d04", 1), ("capD05d08", 2), ("capD09d12", 3), ("capD13d16", 4), ("capD17d20", 5), ("capD21d24", 6), ("capD25d28", 7), ("capD29d32", 8), ("capD33d36", 9), ("capD37d40", 10), ("capD41d44", 11), ("capD45d48", 12), ("capD49d52", 13), ("capD53d56", 14), ("capD57d60", 15), ("capD61d64", 16), ("capF19590f19560", 17), ("capF19550f19520", 18), ("capF19510f19480", 19), ("capF19470f19440", 20), ("capF19430f19400", 21), ("capF19390f19360", 22), ("capF19350f19320", 23), ("capF19310f19280", 24), ("capF19270f19240", 25), ("capF19230f19200", 26), ("capF19590f19520", 27), ("capF19510f19440", 28), ("capF19430f19360", 29), ("capF19350f19280", 30), ("capF19270f19200", 31))

class FspR7OpticalInterfaceReach(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("undefined", 0), ("intra", 1), ("short", 2), ("long", 4), ("vlong", 5), ("ulong", 6), ("reg", 7), ("xlong", 8), ("longn", 10), ("extended", 11), ("hyperlong", 12), ("longNR", 13), ("ulongHaul", 14), ("shortIntra", 15), ("ulongHaulC", 16))

class FspR7OpticalInterfaceReachCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capIntra", 1), ("capShort", 2), ("capLong", 4), ("capVlong", 5), ("capUlong", 6), ("capReg", 7), ("capXlong", 8), ("capLongn", 10), ("capExtended", 11), ("capHyperlong", 12), ("capLongNR", 13), ("capUlongHaul", 14), ("capShortIntra", 15), ("capUlongHaulC", 16))

class FspR7OpticalLanes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("undefined", 0), ("lanesNumber4", 1))

class FspR7OpticalMultiplexLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("undefined", 0), ("levelOm1D", 1), ("levelOm1C", 2), ("levelOm4D", 3), ("levelOm4C", 4), ("levelOm16D", 5), ("levelOm32D", 6), ("levelOm40D", 7), ("levelOmC", 9), ("levelOmD", 10), ("levelOtD", 11), ("levelOtC", 12), ("levelOt", 13))

class FspR7OpticalSubBand(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("d01d16", 1), ("d17d32", 2), ("d33d48", 3), ("d49d64", 4))

class FspR7OpticalSubBandCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capD01d16", 1), ("capD17d32", 2), ("capD33d48", 3), ("capD49d64", 4))

class FspR7OpuPayloadType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37))
    namedValues = NamedValues(("undefined", 0), ("pt01", 1), ("pt02", 2), ("pt03", 3), ("pt04", 4), ("pt05", 5), ("pt06", 6), ("pt07", 7), ("pt08", 8), ("pt09", 9), ("pt0A", 10), ("pt0B", 11), ("pt0C", 12), ("pt0D", 13), ("pt0E", 14), ("pt0F", 15), ("pt10", 16), ("pt11", 17), ("pt20", 18), ("pt21", 19), ("pt80", 20), ("pt81", 21), ("pt82", 22), ("pt83", 23), ("pt84", 24), ("pt85", 25), ("pt86", 26), ("pt87", 27), ("pt88", 28), ("pt89", 29), ("pt8A", 30), ("pt8B", 31), ("pt8C", 32), ("pt8D", 33), ("pt8E", 34), ("pt8F", 35), ("ptFD", 36), ("ptFE", 37))

class FspR7OpuPayloadTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capPt01", 1), ("capPt02", 2), ("capPt03", 3), ("capPt04", 4), ("capPt05", 5), ("capPt06", 6), ("capPt07", 7), ("capPt08", 8), ("capPt09", 9), ("capPt0A", 10), ("capPt0B", 11), ("capPt0C", 12), ("capPt0D", 13), ("capPt0E", 14), ("capPt0F", 15), ("capPt10", 16), ("capPt11", 17), ("capPt20", 18), ("capPt21", 19), ("capPt80", 20), ("capPt81", 21), ("capPt82", 22), ("capPt83", 23), ("capPt84", 24), ("capPt85", 25), ("capPt86", 26), ("capPt87", 27), ("capPt88", 28), ("capPt89", 29), ("capPt8A", 30), ("capPt8B", 31), ("capPt8C", 32), ("capPt8D", 33), ("capPt8E", 34), ("capPt8F", 35), ("capPtFD", 36), ("capPtFE", 37))

class FspR7OptUpdate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("opr", 2))

class FspR7OptUpdateCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capOpr", 2))

class FspR7OscChannel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 99, 100, 106, 197))
    namedValues = NamedValues(("undefined", 0), ("s1310", 99), ("s1630", 100), ("s1510", 106), ("s1610", 197))

class FspR7OscChannelCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capS1310", 99), ("capS1630", 100), ("capS1510", 106), ("capS1610", 197))

class FspR7OscUsage(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("osctxctrl", 2), ("oscrx", 3), ("osctxandrx", 4))

class FspR7OscUsageCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNone", 1), ("capOsctxctrl", 2), ("capOscrx", 3), ("capOsctxandrx", 4))

class FspR7OspfMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("enable", 1), ("disable", 2), ("passive", 3))

class FspR7OspfModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capEnable", 1), ("capDisable", 2), ("capPassive", 3))

class FspR7OtdrPeriod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("periodNone", 1), ("period5ms", 2), ("period20ms", 3), ("period40ms", 4), ("period60ms", 5))

class FspR7OtdrPeriodCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capPeriodNone", 1), ("capPeriod5ms", 2), ("capPeriod20ms", 3), ("capPeriod40ms", 4), ("capPeriod60ms", 5))

class FspR7ParityBit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("undefined", 0), ("no", 1))

class FspR7ParityBitCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNo", 1))

class FspR7PathNode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118))
    namedValues = NamedValues(("undefined", 0), ("node1", 1), ("node2", 2), ("node3", 3), ("node4", 4), ("node5", 5), ("node6", 6), ("node7", 7), ("node8", 8), ("node9", 9), ("node10", 10), ("node11", 11), ("node12", 12), ("node13", 13), ("node14", 14), ("node15", 15), ("node16", 16), ("node17", 17), ("node18", 18), ("node19", 19), ("node20", 20), ("node21", 21), ("node22", 22), ("node23", 23), ("node24", 24), ("node25", 25), ("node26", 26), ("node27", 27), ("node28", 28), ("node29", 29), ("node30", 30), ("node31", 31), ("node32", 32), ("node33", 33), ("node34", 34), ("node35", 35), ("node36", 36), ("node37", 37), ("node38", 38), ("node39", 39), ("node40", 40), ("node41", 41), ("node42", 42), ("node43", 43), ("node44", 44), ("node45", 45), ("node46", 46), ("node47", 47), ("node48", 48), ("node49", 49), ("node50", 50), ("node51", 51), ("node52", 52), ("node53", 53), ("node54", 54), ("node55", 55), ("node56", 56), ("node57", 57), ("node58", 58), ("node59", 59), ("node60", 60), ("node61", 61), ("node62", 62), ("node63", 63), ("node64", 64), ("node65", 65), ("node66", 66), ("node67", 67), ("node68", 68), ("node69", 69), ("node70", 70), ("node71", 71), ("node72", 72), ("node73", 73), ("node74", 74), ("node75", 75), ("node76", 76), ("node77", 77), ("node78", 78), ("node79", 79), ("node80", 80), ("node81", 81), ("node82", 82), ("node83", 83), ("node84", 84), ("node85", 85), ("node86", 86), ("node87", 87), ("node88", 88), ("node89", 89), ("node90", 90), ("node91", 91), ("node92", 92), ("node93", 93), ("node94", 94), ("node95", 95), ("node96", 96), ("node97", 97), ("node98", 98), ("node99", 99), ("node100", 100), ("node101", 101), ("node102", 102), ("node103", 103), ("node104", 104), ("node105", 105), ("node106", 106), ("node107", 107), ("node108", 108), ("node109", 109), ("node110", 110), ("node111", 111), ("node112", 112), ("node113", 113), ("node114", 114), ("node115", 115), ("node116", 116), ("node117", 117), ("node118", 118))

class FspR7PathNodeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNode1", 1), ("capNode2", 2), ("capNode3", 3), ("capNode4", 4), ("capNode5", 5), ("capNode6", 6), ("capNode7", 7), ("capNode8", 8), ("capNode9", 9), ("capNode10", 10), ("capNode11", 11), ("capNode12", 12), ("capNode13", 13), ("capNode14", 14), ("capNode15", 15), ("capNode16", 16), ("capNode17", 17), ("capNode18", 18), ("capNode19", 19), ("capNode20", 20), ("capNode21", 21), ("capNode22", 22), ("capNode23", 23), ("capNode24", 24), ("capNode25", 25), ("capNode26", 26), ("capNode27", 27), ("capNode28", 28), ("capNode29", 29), ("capNode30", 30), ("capNode31", 31), ("capNode32", 32), ("capNode33", 33), ("capNode34", 34), ("capNode35", 35), ("capNode36", 36), ("capNode37", 37), ("capNode38", 38), ("capNode39", 39), ("capNode40", 40), ("capNode41", 41), ("capNode42", 42), ("capNode43", 43), ("capNode44", 44), ("capNode45", 45), ("capNode46", 46), ("capNode47", 47), ("capNode48", 48), ("capNode49", 49), ("capNode50", 50), ("capNode51", 51), ("capNode52", 52), ("capNode53", 53), ("capNode54", 54), ("capNode55", 55), ("capNode56", 56), ("capNode57", 57), ("capNode58", 58), ("capNode59", 59), ("capNode60", 60), ("capNode61", 61), ("capNode62", 62), ("capNode63", 63), ("capNode64", 64), ("capNode65", 65), ("capNode66", 66), ("capNode67", 67), ("capNode68", 68), ("capNode69", 69), ("capNode70", 70), ("capNode71", 71), ("capNode72", 72), ("capNode73", 73), ("capNode74", 74), ("capNode75", 75), ("capNode76", 76), ("capNode77", 77), ("capNode78", 78), ("capNode79", 79), ("capNode80", 80), ("capNode81", 81), ("capNode82", 82), ("capNode83", 83), ("capNode84", 84), ("capNode85", 85), ("capNode86", 86), ("capNode87", 87), ("capNode88", 88), ("capNode89", 89), ("capNode90", 90), ("capNode91", 91), ("capNode92", 92), ("capNode93", 93), ("capNode94", 94), ("capNode95", 95), ("capNode96", 96), ("capNode97", 97), ("capNode98", 98), ("capNode99", 99), ("capNode100", 100), ("capNode101", 101), ("capNode102", 102), ("capNode103", 103), ("capNode104", 104), ("capNode105", 105), ("capNode106", 106), ("capNode107", 107), ("capNode108", 108), ("capNode109", 109), ("capNode110", 110), ("capNode111", 111), ("capNode112", 112), ("capNode113", 113), ("capNode114", 114), ("capNode115", 115), ("capNode116", 116), ("capNode117", 117), ("capNode118", 118))

class FspR7PathProt(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("unprotActive", 2), ("unprotIdle", 3), ("protected", 4))

class FspR7PlugDataRate(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("undefined", 0), ("rateCouplingLink", 1), ("rateHighSpeed", 2), ("rateGBe", 3), ("rate2G1", 4), ("rate2G5", 5), ("rate4G", 6), ("rate10G", 7), ("any", 8), ("rate11G", 9), ("rateFE", 10), ("rate10G2R", 11), ("rate8G", 12), ("rate103G", 13), ("rate112G", 14), ("rate16G", 15), ("rate3gSdi", 16))

class FspR7PlugDataRateCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRateCouplingLink", 1), ("capRateHighSpeed", 2), ("capRateGBe", 3), ("capRate2G1", 4), ("capRate2G5", 5), ("capRate4G", 6), ("capRate10G", 7), ("capAny", 8), ("capRate11G", 9), ("capRateFE", 10), ("capRate10G2R", 11), ("capRate8G", 12), ("capRate103G", 13), ("capRate112G", 14), ("capRate16G", 15), ("capRate3gSdi", 16))

class FspR7PmReset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("all", 2), ("curr", 3))

class FspR7PmResetCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNone", 1), ("capAll", 2), ("capCurr", 3))

class FspR7PmSnapshotStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("inProgress", 2), ("success", 3), ("error", 4))

class FspR7PmSnapshotParameterTypes(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("undefined", 0), ("outputPower", 1), ("inputPower", 2), ("attenuation", 3), ("attenuationOfVoa", 4), ("oscGain", 5), ("backreflectionPowerReceived", 6), ("ramanPumpPower", 7), ("oscPowerReceived", 8), ("variableGain", 9), ("txLineAttenuation", 10), ("rxLineAttenuation", 11))

class FspR7PortBehaviour(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("client", 1), ("network", 2))

class FspR7PortBehaviourCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capClient", 1), ("capNetwork", 2))

class FspR7PortMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("port", 1), ("cTag", 2), ("sTag", 3))

class FspR7PortModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capPort", 1), ("capCTag", 2), ("capSTag", 3))

class FspR7PortRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("uni", 1), ("iNni", 2), ("nni", 3))

class FspR7PortRoleCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capUni", 1), ("capINni", 2), ("capNni", 3))

class FspR7PrbsPmReset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("all", 2))

class FspR7PrbsPmResetCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNone", 1), ("capAll", 2))

class FspR7ProtectionRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("wkg", 1), ("protn", 2), ("na", 3))

class FspR7ProtectionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("dpring", 1), ("line", 2))

class FspR7ProtectionTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capDpring", 1), ("capLine", 2))

class FspR7Protocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("local", 1), ("static", 2), ("ospf", 3))

class FspR7PsuOutputPower(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("undefined", 0), ("pwrOut120w", 1), ("pwrOut130w", 2), ("pwrOut400w", 3), ("pwrOut600w", 4), ("pwrOut170w", 5), ("pwrOut200w", 6), ("pwrOut1000w", 7), ("pwrOut0w", 8), ("pwrOut800w", 9), ("pwrOut150w", 10))

class FspR7PsuOutputPowerCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capPwrOut120w", 1), ("capPwrOut130w", 2), ("capPwrOut400w", 3), ("capPwrOut600w", 4), ("capPwrOut170w", 5), ("capPwrOut200w", 6), ("capPwrOut1000w", 7), ("capPwrOut0w", 8), ("capPwrOut800w", 9), ("capPwrOut150w", 10))

class FspR7RedLinedState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2))

class FspR7RedLinedStateCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capYes", 1), ("capNo", 2))

class FspR7RenewMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("automatic", 1), ("manual", 2))

class FspR7RenewModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capAutomatic", 1), ("capManual", 2))

class FspR7RlsMan(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("man", 2))

class FspR7RlsManCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capMan", 2))

class FspR7RoadmNumber(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("undefined", 0), ("rNo1", 1), ("rNo2", 2), ("rNo3", 3), ("rNo4", 4), ("rNo5", 5), ("rNo6", 6), ("rNo7", 7), ("rNo8", 8), ("rNo9", 9), ("rNo10", 10))

class FspR7RoadmNumberCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRNo1", 1), ("capRNo2", 2), ("capRNo3", 3), ("capRNo4", 4), ("capRNo5", 5), ("capRNo6", 6), ("capRNo7", 7), ("capRNo8", 8), ("capRNo9", 9), ("capRNo10", 10))

class FspR7RowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("undefined", 0), ("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

class FspR7RowStatusCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capActive", 1), ("capNotInService", 2), ("capNotReady", 3), ("capCreateAndGo", 4), ("capCreateAndWait", 5), ("capDestroy", 6))

class FspR7Scrambling(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("enable", 1), ("disable", 2))

class FspR7ScramblingCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capEnable", 1), ("capDisable", 2))

class FspR7ScuRing(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("enable", 1), ("disable", 2))

class FspR7SignalDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("networkToClient", 1), ("cientToNetwork", 2), ("upgradeToNetwork", 3), ("networkToUpgrade", 4))

class FspR7SingleFiberLocation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("locationA", 1), ("locationB", 2))

class FspR7SingleFiberLocationCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capLocationA", 1), ("capLocationB", 2))

class FspR7SnmpHexString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class FspR7SnmpLongString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 65535)

class FspR7SshHostKeyEncryptAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("rsa", 1), ("dsa", 2), ("rsa1", 3))

class FspR7SshHostKeyLength(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("length2048", 1), ("length4096", 2))

class FspR7Stages(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("st1", 1), ("st2", 2))

class FspR7StartPmSnapshot(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("apply", 2))

class FspR7StateConnection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("undefined", 0), ("standard", 1), ("mismatchEquipment", 2), ("mismatchConnection", 3), ("mismatchChannel", 4), ("mismatchPhysical", 5), ("invalidConfig", 6), ("nonStandard", 7), ("standardSpeq", 8))

class FspR7Stuff(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2))

class FspR7StuffCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capYes", 1), ("capNo", 2))

class FspR7SupplyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("front", 1), ("rear", 2))

class FspR7SupplyTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capFront", 1), ("capRear", 2))

class FspR7SwitchOverCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 9, 10, 11))
    namedValues = NamedValues(("undefined", 0), ("notApplicable", 1), ("removed", 2), ("softwareException", 3), ("noResponse", 4), ("gracefulShutdown", 9), ("switchToDuplex", 10), ("buttonPushed", 11))

class FspR7SwitchOverCauseCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNotApplicable", 1), ("capRemoved", 2), ("capSoftwareException", 3), ("capNoResponse", 4), ("capGracefulShutdown", 9), ("capSwitchToDuplex", 10), ("capButtonPushed", 11))

class FspR7TelemetryOutput(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("undefined", 0), ("neAlmCr", 1), ("neAlmMj", 2), ("neAlmMn", 3), ("neAlmMjGe", 4), ("neAlmMnGe", 5), ("fcuAlmCr", 6), ("fcuAlmMj", 7), ("fcuAlmMn", 8), ("fcuAlmMjGe", 9), ("fcuAlmMnGe", 10), ("psuAlmCr", 11), ("psuAlmMj", 12), ("psuAlmMn", 13), ("psuAlmMjGe", 14), ("psuAlmMnGe", 15), ("none", 16))

class FspR7TelemetryOutputCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capNeAlmCr", 1), ("capNeAlmMj", 2), ("capNeAlmMn", 3), ("capNeAlmMjGe", 4), ("capNeAlmMnGe", 5), ("capFcuAlmCr", 6), ("capFcuAlmMj", 7), ("capFcuAlmMn", 8), ("capFcuAlmMjGe", 9), ("capFcuAlmMnGe", 10), ("capPsuAlmCr", 11), ("capPsuAlmMj", 12), ("capPsuAlmMn", 13), ("capPsuAlmMjGe", 14), ("capPsuAlmMnGe", 15), ("capNone", 16))

class FspR7PRBSTest(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("iPRBS31", 2))

class FspR7PRBSTestCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capIPRBS31", 2))

class FspR7TifOutputReset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("opr", 2))

class FspR7TifOutputResetCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capOpr", 2))

class FspR7TiltSet(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("minus1dB0", 1), ("minus1dB5", 2), ("minus2dB0", 3))

class FspR7TiltSetCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capMinus1dB0", 1), ("capMinus1dB5", 2), ("capMinus2dB0", 3))

class FspR7Topology(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("standAlone", 1), ("backToBack", 2), ("mesh", 3), ("fabric", 4))

class FspR7TopologyCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capStandAlone", 1), ("capBackToBack", 2), ("capMesh", 3), ("capFabric", 4))

class FspR7TopologyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("lad", 1), ("ring", 2), ("p2p", 3), ("unknown", 4))

class FspR7TrafficDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("bidi", 1), ("uniCton", 2), ("uniNtoc", 3), ("uniWtoe", 4), ("uniEtow", 5), ("txcrs", 6), ("rxcrs", 7))

class FspR7TrafficDirectionCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capBidi", 1), ("capUniCton", 2), ("capUniNtoc", 3), ("capUniWtoe", 4), ("capUniEtow", 5), ("capTxcrs", 6), ("capRxcrs", 7))

class FspR7TrapModeLegacy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("false", 1), ("true", 2))

class FspR7TransmissionMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 21, 22))
    namedValues = NamedValues(("undefined", 0), ("trans", 1), ("transE", 2), ("transW", 3), ("transHst", 4), ("mux", 5), ("muxE", 6), ("muxW", 7), ("muxHst", 8), ("regen1Way", 9), ("regen2Way", 10), ("obsolete", 11), ("adm", 12), ("transDual", 13), ("muxDual", 14), ("nFixed", 15), ("cSelect", 16), ("dualClient", 17), ("xc", 20), ("transQuad", 21), ("transQuintuple", 22))

class FspR7TransmissionModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capTrans", 1), ("capTransE", 2), ("capTransW", 3), ("capTransHst", 4), ("capMux", 5), ("capMuxE", 6), ("capMuxW", 7), ("capMuxHst", 8), ("capRegen1Way", 9), ("capRegen2Way", 10), ("capObsolete", 11), ("capAdm", 12), ("capTransDual", 13), ("capMuxDual", 14), ("capNFixed", 15), ("capCSelect", 16), ("capDualClient", 17), ("capXc", 20), ("capTransQuad", 21), ("capTransQuintuple", 22))

class FspR7TurnupConfig(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("rls", 1), ("oprTurnup", 2))

class FspR7TurnupConfigCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capRls", 1), ("capOprTurnup", 2))

class FspR7TxOffOnTm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("disable", 1), ("enableTxOffTm", 2), ("enableTxOnTm", 3))

class FspR7TxOffOnTmCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capDisable", 1), ("capEnableTxOffTm", 2), ("capEnableTxOnTm", 3))

class FspR7TypeConnection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("connection1Way", 1), ("connection2Way", 2))

class FspR7TypeConnectionCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capConnection1Way", 1), ("capConnection2Way", 2))

class FspR7TypeCrs(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("undefined", 0), ("connection1Way", 1), ("connection2Way", 2), ("connection1WayProt", 3), ("connection2WayProt", 4), ("connection1WayMc", 5), ("connection1WayDc", 6), ("connection1WayDcProt", 7), ("connection1WayMcProt", 8), ("connection1WayCont", 9), ("connection2WayCont", 10))

class FspR7TypeCrsCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capConnection1Way", 1), ("capConnection2Way", 2), ("capConnection1WayProt", 3), ("capConnection2WayProt", 4), ("capConnection1WayMc", 5), ("capConnection1WayDc", 6), ("capConnection1WayDcProt", 7), ("capConnection1WayMcProt", 8), ("capConnection1WayCont", 9), ("capConnection2WayCont", 10))

class FspR7Unsigned32Caps(TextualConvention, OctetString):
    status = 'current'
    displayHint = '4d:4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 8)

class FspR7UntaggedFrames(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("accept", 1), ("reject", 2))

class FspR7UntaggedFramesCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capAccept", 1), ("capReject", 2))

class FspR7ValidityPeriod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("oneYear", 1), ("twoYears", 2), ("threeYears", 3), ("fourYears", 4), ("fiveYears", 5))

class FspR7ValidityPeriodCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capOneYear", 1), ("capTwoYears", 2), ("capThreeYears", 3), ("capFourYears", 4), ("capFiveYears", 5))

class FspR7VoaMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("power", 1), ("att", 2))

class FspR7VoaModeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capPower", 1), ("capAtt", 2))

class FspR7VSessChangeReason(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("undefined", 0), ("none", 1), ("requestIssued", 2), ("requestApproved", 3), ("requestDenied", 4), ("requestTimeout", 5), ("accessTimeout", 6), ("accessRevoked", 7))

class FspR7VSessStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("normal", 1), ("writeAcsRequested", 2), ("writeAcsGranted", 3))

class FspR7VSessWriteAccess(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("undefined", 0), ("request", 1), ("revoke", 2), ("grant", 3), ("none", 4))

class FspR7XfpDecisionThres(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("standard", 1), ("forwardRaman", 2))

class FspR7XfpDecisionThresCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capStandard", 1), ("capForwardRaman", 2))

class FspR7YcableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("undefined", 0), ("ycabSmLc", 1), ("ycabMmLc", 2), ("ycabSmScLc", 3), ("ycabMmScLc", 4), ("ycabSmFcLc", 5))

class FspR7YcableTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capYcabSmLc", 1), ("capYcabMmLc", 2), ("capYcabSmScLc", 3), ("capYcabMmScLc", 4), ("capYcabSmFcLc", 5))

class FspR7FltrCableType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("undefined", 0), ("fltrCabLr4SmLc", 1))

class FspR7FltrCableTypeCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capFltrCabLr4SmLc", 1))

class FspR7YesNo(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("undefined", 0), ("yes", 1), ("no", 2))

class FspR7YesNoCaps(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("capUndefined", 0), ("capYes", 1), ("capNo", 2))

mibBuilder.exportSymbols("ADVA-FSPR7-TC-MIB", FspR7InvertTelemetryInputLogic=FspR7InvertTelemetryInputLogic, FspR7ForcedStatus=FspR7ForcedStatus, FspR7OdtuType=FspR7OdtuType, FspR7LagSysIdFend=FspR7LagSysIdFend, FspR7LaserDelayTimerCaps=FspR7LaserDelayTimerCaps, FspR7StartPmSnapshot=FspR7StartPmSnapshot, FspR7NCTraceId=FspR7NCTraceId, FspR7EnableDisableCaps=FspR7EnableDisableCaps, FspR7LaserForcedOperation=FspR7LaserForcedOperation, FspR7RlsMan=FspR7RlsMan, EntityType=EntityType, FspR7BidirectionalChannelCaps=FspR7BidirectionalChannelCaps, FspR7PortRoleCaps=FspR7PortRoleCaps, FspR7LagPorts=FspR7LagPorts, FspR7SnmpLongString=FspR7SnmpLongString, FspR7MuxMethodCaps=FspR7MuxMethodCaps, FspR7NoYes=FspR7NoYes, FspR7DispersionModesCaps=FspR7DispersionModesCaps, FspR7Category=FspR7Category, FspR7LagStandby=FspR7LagStandby, FspR7LaserDelayTimer=FspR7LaserDelayTimer, FspR7PathProt=FspR7PathProt, FspR7ScuRing=FspR7ScuRing, FspR7DispersionCompensation=FspR7DispersionCompensation, FspR7OptUpdateCaps=FspR7OptUpdateCaps, FspR7SnmpHexString=FspR7SnmpHexString, FspR7TrapModeLegacy=FspR7TrapModeLegacy, FspR7FltrCableTypeCaps=FspR7FltrCableTypeCaps, FspR7EqlzAdminState=FspR7EqlzAdminState, FspR7NumberOfChannelsProvCaps=FspR7NumberOfChannelsProvCaps, FspR7ForceConfigCaps=FspR7ForceConfigCaps, FspR7FlowControlMode=FspR7FlowControlMode, FspR7GainRangeCaps=FspR7GainRangeCaps, FspR7LagPortTypeCaps=FspR7LagPortTypeCaps, FspR7VSessWriteAccess=FspR7VSessWriteAccess, ApsTypeCaps=ApsTypeCaps, EntityClassName=EntityClassName, FspR7AlsMode=FspR7AlsMode, FspR7RedLinedState=FspR7RedLinedState, FspR7SshHostKeyLength=FspR7SshHostKeyLength, FspR7ConnectorTypeCaps=FspR7ConnectorTypeCaps, FspR7OpuPayloadTypeCaps=FspR7OpuPayloadTypeCaps, FspR7Bitrate=FspR7Bitrate, FspR7OspfMode=FspR7OspfMode, FspR7PortRole=FspR7PortRole, FspR7Mapping=FspR7Mapping, FspR7ManualAuto=FspR7ManualAuto, FspR7DeploymentScenarioCaps=FspR7DeploymentScenarioCaps, FspR7NtpTest=FspR7NtpTest, FspR7OpticalGroupCaps=FspR7OpticalGroupCaps, FspR7BERThresholdSectionCaps=FspR7BERThresholdSectionCaps, FspR7PortBehaviour=FspR7PortBehaviour, FspR7PsuOutputPower=FspR7PsuOutputPower, FspR7Stages=FspR7Stages, FspR7Topology=FspR7Topology, ApsType=ApsType, FspR7ManualAutoCaps=FspR7ManualAutoCaps, FspR7BERThreshold=FspR7BERThreshold, FspR7NCTRouteType=FspR7NCTRouteType, FspR7ValidityPeriodCaps=FspR7ValidityPeriodCaps, FspR7EntitySecondaryStates=FspR7EntitySecondaryStates, FspR7NewSshHostKey=FspR7NewSshHostKey, FspR7TopologyType=FspR7TopologyType, FspR7ScramblingCaps=FspR7ScramblingCaps, FspR7KeyLength=FspR7KeyLength, FspR7LagFendState=FspR7LagFendState, FspR7IpMode=FspR7IpMode, FspR7InterfaceTypeCaps=FspR7InterfaceTypeCaps, FspR7Integer32Caps=FspR7Integer32Caps, FspR7XfpDecisionThresCaps=FspR7XfpDecisionThresCaps, FspR7NtpAdminState=FspR7NtpAdminState, FspR7ConnectorType=FspR7ConnectorType, FspR7EdfaOutputPowerRating=FspR7EdfaOutputPowerRating, FspR7CodeGain=FspR7CodeGain, FspR7FlowControlModeCaps=FspR7FlowControlModeCaps, FspR7OscUsage=FspR7OscUsage, FspR7OpticalGroup=FspR7OpticalGroup, FspR7YesNoCaps=FspR7YesNoCaps, FspR7ChannelNumberCaps=FspR7ChannelNumberCaps, FspR7DispersionCompensationCaps=FspR7DispersionCompensationCaps, FspR7AlarmProfileList=FspR7AlarmProfileList, FspR7TelemetryOutput=FspR7TelemetryOutput, FspR7VoaMode=FspR7VoaMode, FspR7OpticalInterfaceReach=FspR7OpticalInterfaceReach, FspR7LossAttenuation=FspR7LossAttenuation, FspR7OtdrPeriod=FspR7OtdrPeriod, FspR7PathNodeCaps=FspR7PathNodeCaps, FspR7AseTabOpr=FspR7AseTabOpr, FspR7SwitchOverCause=FspR7SwitchOverCause, FspR7OpticalBandCaps=FspR7OpticalBandCaps, FspR7StuffCaps=FspR7StuffCaps, FspR7ForceConfig=FspR7ForceConfig, FspR7VoaModeCaps=FspR7VoaModeCaps, FspR7PlugDataRate=FspR7PlugDataRate, FspR7ConnectState=FspR7ConnectState, FspR7BitrateCaps=FspR7BitrateCaps, FspR7ChannelIdentifierCaps=FspR7ChannelIdentifierCaps, FspR7PathNode=FspR7PathNode, FspR7ProtectionRole=FspR7ProtectionRole, FspR7RedLinedStateCaps=FspR7RedLinedStateCaps, FspR7Baund=FspR7Baund, FspR7RoadmNumberCaps=FspR7RoadmNumberCaps, FspR7TelemetryOutputCaps=FspR7TelemetryOutputCaps, FspR7UntaggedFramesCaps=FspR7UntaggedFramesCaps, FspR7PmReset=FspR7PmReset, FspR7DCFiberTypeCaps=FspR7DCFiberTypeCaps, FspR7FanProfile=FspR7FanProfile, FspR7NoYesCaps=FspR7NoYesCaps, FspR7MaxBitErrorRate=FspR7MaxBitErrorRate, FspR7OscChannel=FspR7OscChannel, FspR7Gain=FspR7Gain, FspR7Stuff=FspR7Stuff, FspR7SupplyType=FspR7SupplyType, FspR7YesNo=FspR7YesNo, FspR7TiltSet=FspR7TiltSet, ApsRevertModeCaps=ApsRevertModeCaps, FspR7AppType=FspR7AppType, FspR7OptUpdate=FspR7OptUpdate, FspR7PsuOutputPowerCaps=FspR7PsuOutputPowerCaps, FspR7OscChannelCaps=FspR7OscChannelCaps, FspR7SwitchOverCauseCaps=FspR7SwitchOverCauseCaps, FspR7Conn=FspR7Conn, FspR7TxOffOnTm=FspR7TxOffOnTm, FspR7IpType=FspR7IpType, FspR7BaundCaps=FspR7BaundCaps, FspR7LacpTimeoutCaps=FspR7LacpTimeoutCaps, FspR7TrafficDirection=FspR7TrafficDirection, FspR7EntityType=FspR7EntityType, FspR7AutoThresResetCaps=FspR7AutoThresResetCaps, FspR7DeploymentScenario=FspR7DeploymentScenario, FspR7EqlzAdminStateCaps=FspR7EqlzAdminStateCaps, FspR7AdminState=FspR7AdminState, FspR7IpTypeCaps=FspR7IpTypeCaps, FspR7LacpModeCaps=FspR7LacpModeCaps, FspR7CertApplyCaps=FspR7CertApplyCaps, FspR7TopologyCaps=FspR7TopologyCaps, FspR7FiberBrand=FspR7FiberBrand, FspR7ChannelSpacingCaps=FspR7ChannelSpacingCaps, FspR7LacpMode=FspR7LacpMode, FspR7InitEqualization=FspR7InitEqualization, FspR7ChannelBandwidth=FspR7ChannelBandwidth, FspR7SshHostKeyEncryptAlgorithm=FspR7SshHostKeyEncryptAlgorithm, FspR7GainRange=FspR7GainRange, FspR7Unsigned32Caps=FspR7Unsigned32Caps, FspR7FiberDetectCaps=FspR7FiberDetectCaps, FspR7GropticsType=FspR7GropticsType, FspR7InterfaceType=FspR7InterfaceType, FspR7OpticalFiberType=FspR7OpticalFiberType, FspR7PRBSTest=FspR7PRBSTest, FspR7ErrorFwdMode=FspR7ErrorFwdMode, FspR7ChannelNumber=FspR7ChannelNumber, ApsRevertMode=ApsRevertMode, FspR7RowStatusCaps=FspR7RowStatusCaps, FspR7FiberDetect=FspR7FiberDetect, FspR7EocProtAvailability=FspR7EocProtAvailability, FspR7TypeConnectionCaps=FspR7TypeConnectionCaps, FspR7APSCommandCaps=FspR7APSCommandCaps, FspR7FunctionCrsCaps=FspR7FunctionCrsCaps, FspR7CpAuthType=FspR7CpAuthType, FspR7PortModeCaps=FspR7PortModeCaps, FspR7IPv6Type=FspR7IPv6Type, FspR7TifOutputReset=FspR7TifOutputReset, FspR7FecTypeCaps=FspR7FecTypeCaps, FspR7TransmissionModeCaps=FspR7TransmissionModeCaps, FspR7CodeGainCaps=FspR7CodeGainCaps, FspR7DispersionModes=FspR7DispersionModes, FspR7FDStatus=FspR7FDStatus, FspR7NumberOfChannelsProv=FspR7NumberOfChannelsProv, FspR7ApsChannel=FspR7ApsChannel, FspR7MonLevel=FspR7MonLevel, FspR7MuxMethod=FspR7MuxMethod, FspR7ProtectionType=FspR7ProtectionType, EquipmentState=EquipmentState, FspR7LossAttenuationCaps=FspR7LossAttenuationCaps, FspR7RenewModeCaps=FspR7RenewModeCaps, FspR7CapInventoryCaps=FspR7CapInventoryCaps, FspR7OpticalInterfaceReachCaps=FspR7OpticalInterfaceReachCaps, FspR7SingleFiberLocationCaps=FspR7SingleFiberLocationCaps, FspR7APSCommand=FspR7APSCommand, FspR7OpticalSubBandCaps=FspR7OpticalSubBandCaps, FspR7RlsManCaps=FspR7RlsManCaps, FspR7AdminStateCaps=FspR7AdminStateCaps, FspR7OpticalBand=FspR7OpticalBand, FspR7OpticalMultiplexLevel=FspR7OpticalMultiplexLevel, FspR7RenewMode=FspR7RenewMode, FspR7RowStatus=FspR7RowStatus, FspR7StateConnection=FspR7StateConnection, FspR7SupplyTypeCaps=FspR7SupplyTypeCaps, FspR7VSessStatus=FspR7VSessStatus, FspR7OpuPayloadType=FspR7OpuPayloadType, FspR7PortBehaviourCaps=FspR7PortBehaviourCaps, FspR7ColumnMark=FspR7ColumnMark, FspR7ForcedStatusCaps=FspR7ForcedStatusCaps, FspR7Ipv6Address=FspR7Ipv6Address, FspR7OpticalSubBand=FspR7OpticalSubBand, FspR7LagPortType=FspR7LagPortType, FspR7OperState=FspR7OperState, FspR7LineCodingCaps=FspR7LineCodingCaps, FspR7PrbsPmReset=FspR7PrbsPmReset, FspR7OtdrPeriodCaps=FspR7OtdrPeriodCaps, FspR7BidirectionalChannel=FspR7BidirectionalChannel, FspR7DispersionConfig=FspR7DispersionConfig, FspR7GropticsTypeCaps=FspR7GropticsTypeCaps, FspR7IpModeCaps=FspR7IpModeCaps, FspR7CapInventory=FspR7CapInventory, FspR7FiberBrandCaps=FspR7FiberBrandCaps, FspR7Scrambling=FspR7Scrambling, FspR7TypeCrsCaps=FspR7TypeCrsCaps, FspR7PmSnapshotStatus=FspR7PmSnapshotStatus, FspR7Protocol=FspR7Protocol, FspR7TiltSetCaps=FspR7TiltSetCaps, FspR7XfpDecisionThres=FspR7XfpDecisionThres, FspR7ConnCaps=FspR7ConnCaps, FspR7LaneGroupInventoryCaps=FspR7LaneGroupInventoryCaps, FspR7FltrCableType=FspR7FltrCableType, PYSNMP_MODULE_ID=advaFspR7Tc, FspR7AutoThresReset=FspR7AutoThresReset, FspR7LacpTimeout=FspR7LacpTimeout, FspR7FDStatusCaps=FspR7FDStatusCaps, FspR7TifOutputResetCaps=FspR7TifOutputResetCaps, FspR7LineCoding=FspR7LineCoding, FspR7LaserForcedOperationCaps=FspR7LaserForcedOperationCaps, FspR7NumberOfChannelsCaps=FspR7NumberOfChannelsCaps, FspR7BERThresholdSection=FspR7BERThresholdSection, FspR7DCFiberType=FspR7DCFiberType, FspR7EdfaOutputPowerRatingCaps=FspR7EdfaOutputPowerRatingCaps, FspR7InterfaceFunction=FspR7InterfaceFunction, FspR7PmResetCaps=FspR7PmResetCaps, FspR7MappingCaps=FspR7MappingCaps, FspR7NdpCleanupCaps=FspR7NdpCleanupCaps, FspR7PRBSTestCaps=FspR7PRBSTestCaps, FspR7IPv6TypeCaps=FspR7IPv6TypeCaps, FspR7NdpCleanup=FspR7NdpCleanup, ConnectionNotation=ConnectionNotation, FspR7CertApply=FspR7CertApply, FspR7InvertTelemetryInputLogicCaps=FspR7InvertTelemetryInputLogicCaps, FspR7AlsModeCaps=FspR7AlsModeCaps, FspR7ParityBitCaps=FspR7ParityBitCaps, FspR7InitEqualizationCaps=FspR7InitEqualizationCaps, Counter64StringCaps=Counter64StringCaps, FspR7FecType=FspR7FecType, FspR7ChannelSpacing=FspR7ChannelSpacing, FspR7ValidityPeriod=FspR7ValidityPeriod, FspR7OscUsageCaps=FspR7OscUsageCaps, FspR7ProtectionTypeCaps=FspR7ProtectionTypeCaps, Grade=Grade, FspR7LaneGroupInventory=FspR7LaneGroupInventory, FspR7OpticalFiberTypeCaps=FspR7OpticalFiberTypeCaps, FspR7KeyLengthCaps=FspR7KeyLengthCaps, FspR7ChannelIdentifier=FspR7ChannelIdentifier, FspR7RoadmNumber=FspR7RoadmNumber, FspR7GainCaps=FspR7GainCaps, FspR7YcableType=FspR7YcableType, FspR7OspfModeCaps=FspR7OspfModeCaps)
mibBuilder.exportSymbols("ADVA-FSPR7-TC-MIB", FspR7TrafficDirectionCaps=FspR7TrafficDirectionCaps, FspR7FrameFormatCaps=FspR7FrameFormatCaps, FspR7DisableEnableCaps=FspR7DisableEnableCaps, FspR7MaxBitErrorRateCaps=FspR7MaxBitErrorRateCaps, FspR7OpticalLanes=FspR7OpticalLanes, FspR7PlugDataRateCaps=FspR7PlugDataRateCaps, FspR7DispersionConfigCaps=FspR7DispersionConfigCaps, FspR7TxOffOnTmCaps=FspR7TxOffOnTmCaps, FspR7ChannelBandwidthCaps=FspR7ChannelBandwidthCaps, FspR7LagState=FspR7LagState, FspR7SignalDirection=FspR7SignalDirection, advaFspR7Tc=advaFspR7Tc, FspR7LagIdFend=FspR7LagIdFend, FspR7YcableTypeCaps=FspR7YcableTypeCaps, FspR7ErrorFwdModeCaps=FspR7ErrorFwdModeCaps, FspR7AseTabOprCaps=FspR7AseTabOprCaps, FspR7UntaggedFrames=FspR7UntaggedFrames, FspR7VSessChangeReason=FspR7VSessChangeReason, FfpTypeCaps=FfpTypeCaps, FspR7AlarmListType=FspR7AlarmListType, FspR7FunctionCrs=FspR7FunctionCrs, FspR7TypeCrs=FspR7TypeCrs, FspR7TypeConnection=FspR7TypeConnection, FspR7NtpSyncStatus=FspR7NtpSyncStatus, FspR7EquipmentAssignState=FspR7EquipmentAssignState, FspR7BERThresholdCaps=FspR7BERThresholdCaps, FspR7FanMode=FspR7FanMode, FspR7ParityBit=FspR7ParityBit, FspR7PrbsPmResetCaps=FspR7PrbsPmResetCaps, FspR7EnableDisable=FspR7EnableDisable, FspR7SingleFiberLocation=FspR7SingleFiberLocation, FspR7NtpTestStatus=FspR7NtpTestStatus, FspR7TurnupConfigCaps=FspR7TurnupConfigCaps, FfpType=FfpType, FspR7EncapsulationMethod=FspR7EncapsulationMethod, FspR7PortMode=FspR7PortMode, FspR7TurnupConfig=FspR7TurnupConfig, FspR7AidType=FspR7AidType, FspR7NumberOfChannels=FspR7NumberOfChannels, FspR7CpAuthTypeCaps=FspR7CpAuthTypeCaps, FspR7FrameFormat=FspR7FrameFormat, FspR7TransmissionMode=FspR7TransmissionMode, FspR7DisableEnable=FspR7DisableEnable, FspR7PmSnapshotParameterTypes=FspR7PmSnapshotParameterTypes)
