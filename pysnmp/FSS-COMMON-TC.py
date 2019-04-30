#
# PySNMP MIB module FSS-COMMON-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FSS-COMMON-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 19:02:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
fssCommon, = mibBuilder.importSymbols("FSS-COMMON-SMI", "fssCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, Counter64, Bits, Integer32, ObjectIdentity, iso, Counter32, Unsigned32, NotificationType, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter64", "Bits", "Integer32", "ObjectIdentity", "iso", "Counter32", "Unsigned32", "NotificationType", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
fcTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 211, 1, 24, 12, 1))
fcTc.setRevisions(('2016-01-20 00:00',))
if mibBuilder.loadTexts: fcTc.setLastUpdated('201601200000Z')
if mibBuilder.loadTexts: fcTc.setOrganization('Fujitsu Network Communications, Inc.')
class FCSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(9999, 0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 9999), ("na", 0), ("critical", 1), ("major", 2), ("minor", 3), ("not-alarmed", 4), ("not-reported", 5), ("warning", 6), ("indeterminate", 7))

class FCCondEffect(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(9999, 0, 1, 2, 3))
    namedValues = NamedValues(("other", 9999), ("na", 0), ("cl", 1), ("sc", 2), ("tc", 3))

class FCServEffect(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(9999, 0, 1, 2))
    namedValues = NamedValues(("other", 9999), ("na", 0), ("sa", 1), ("nsa", 2))

class FCLocation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(9999, 0, 1, 2))
    namedValues = NamedValues(("other", 9999), ("na", 0), ("nend", 1), ("fend", 2))

class FCDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(9999, 0, 1, 2))
    namedValues = NamedValues(("other", 9999), ("na", 0), ("receive", 1), ("transmit", 2))

class FCTimePeriod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(9999, 0, 1, 2, 3, 4))
    namedValues = NamedValues(("other", 9999), ("na", 0), ("min-15", 1), ("hr-24", 2), ("week-1", 3), ("month-1", 4))

class FCTrapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(9999, 0, 1, 2, 3))
    namedValues = NamedValues(("other", 9999), ("na", 0), ("cond", 1), ("tca", 2), ("dbchg", 3))

class FCObjectName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 80)

class FCCondType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 100, 101, 102, 103, 104, 105, 106, 107, 108, 200, 201, 300, 301, 302, 303, 305, 306, 307, 308, 350, 351, 352, 400, 450, 451, 452, 470, 500, 600, 601, 602, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036, 1037, 1038, 1039, 1040, 1041, 1042, 1043, 1044, 1045, 1046, 1047, 1048, 1049, 1050, 1051, 1052, 1053, 1054, 1055, 1056, 1057, 1058, 1059, 1060, 1061, 1062, 1063, 1064, 1065, 1066, 1067, 1068, 1069, 1070, 1071, 1072, 1073, 1074, 1075, 1076, 1077, 1078, 1079, 1080, 1081, 1082, 1083, 1084, 1500, 1600, 1700))
    namedValues = NamedValues(("prod-specific", 0), ("equipmentFault", 1), ("equipmentRemoved", 2), ("equipmentMismatchAttributes", 3), ("equipmentWarmup", 4), ("equipmentLedOn", 5), ("administrativeDown", 6), ("administrativeTesting", 7), ("overTemperatureEquipment", 8), ("incompatibleSffHardware", 9), ("configurationStandBy", 10), ("shelfProvisioningMode", 11), ("equipmentInterConnectFailure", 12), ("equipmentMiscabledConnection", 13), ("fanCoolingFail", 14), ("equipmentCurrExceededFeed", 15), ("interConnectFailureBladePiu", 16), ("lampTest", 17), ("otdrScanInProgress", 18), ("databaseCorruption", 100), ("databaseLockedSoftwareUpgradeInProgress", 101), ("databaseLockedDbRestoreInProgress", 102), ("databaseLockedSysInitInProgress", 103), ("databaseLockedDbAlarmPresent", 104), ("databaseLockedIlfViolation", 105), ("databaseLockedShelfProvModePresent", 106), ("databaseVersionMismatch", 107), ("databaseSystemSignatureMismatch", 108), ("softwareVersionMismatch", 200), ("softwareStageInProgress", 201), ("firmwareVersionMismatch", 300), ("firmwareInitInProgress", 301), ("firmwareBackwardCompatibleLimited", 302), ("firmwareBackwardCompatibleAll", 303), ("firmwareDownloadOrActivationFailure", 305), ("incompatibleFirmware", 306), ("incompatibleHardware", 307), ("noFirmware", 308), ("ilfViolation", 350), ("ilfViolationCritical", 351), ("ilfViolationMajor", 352), ("softwareReset", 400), ("sysNtpNotSynchronized", 450), ("interConnectFailure", 451), ("sysNameChanged", 452), ("certificateNotInstalled", 470), ("generalCommunicationChannel0Failure", 500), ("powerProblem", 600), ("powerProblemA", 601), ("powerProblemB", 602), ("opticalPowerReceive", 1001), ("opticalPowerTransmit", 1002), ("lossOfSignal", 1003), ("lossOfFrame", 1004), ("lossOfMultiframe", 1005), ("backwardDefectIndication", 1006), ("forwardDefectIndication", 1007), ("signalDegrade", 1008), ("trailTraceMismatch", 1009), ("backwardIncomingAlignmentError", 1010), ("incomingAlignmentError", 1011), ("alarmIndicationSignal", 1012), ("openConnectionIndication", 1013), ("locked", 1014), ("lossofTandemConnection", 1015), ("payloadMismatch", 1016), ("clientSignalFailDefect", 1017), ("multiplexStructureIdentifierMismatch", 1018), ("lossOfOmfIndication", 1019), ("lossOfFrameAndLossOfMultiframe", 1020), ("cnOutOfRange", 1021), ("cnLossOfSynchronization", 1022), ("highBER", 1023), ("localFault", 1024), ("remoteFault", 1025), ("lossOfAlignment", 1026), ("lossOfSynchronization", 1027), ("lossOfFECAlignment", 1028), ("remoteLANFault", 1029), ("lanTransmitLocalFault", 1030), ("lanTransmitRemoteFault", 1031), ("lanTransmitOff", 1032), ("facilityLoopbackActive", 1033), ("facilityLoopback2Active", 1034), ("terminalLoopbackActive", 1035), ("facilityTestsignalActive", 1036), ("terminalTestsignalActive", 1037), ("linkDown", 1038), ("powerOutOfSpecification", 1039), ("powerOutOfSpecificationHigh", 1040), ("powerOutOfSpecificationHighL1", 1041), ("powerOutOfSpecificationHighL2", 1042), ("powerOutOfSpecificationHighL3", 1043), ("powerOutOfSpecificationHighL4", 1044), ("powerOutOfSpecificationLow", 1045), ("powerOutOfSpecificationLowL1", 1046), ("powerOutOfSpecificationLowL2", 1047), ("powerOutOfSpecificationLowL3", 1048), ("powerOutOfSpecificationLowL4", 1049), ("fanFilterShouldBeReplaced", 1050), ("fanFilterShouldBeCleaned", 1051), ("equipmentOverTemperature", 1052), ("portLossOfLight", 1053), ("thresholdCrossingAlertSpanlossVariationTooLow", 1054), ("thresholdCrossingAlertSpanlossVariationTooHigh", 1055), ("thresholdCrossingAlertOscOpticalReceivePowerTooHigh", 1056), ("thresholdCrossingAlertOscOpticalReceivePowerTooLow", 1057), ("thresholdCrossingAlertOscOpticalTransmitPowerTooHigh", 1058), ("thresholdCrossingAlertOscOpticalTransmitPowerTooLow", 1059), ("thresholdCrossingAlertOpticalReceivePowerTooHigh", 1060), ("thresholdCrossingAlertOpticalReceivePowerTooLow", 1061), ("thresholdCrossingAlertOpticalTransmitPowerTooHigh", 1062), ("thresholdCrossingAlertOpticalTransmitPowerTooLow", 1063), ("postBlockAutoLaserShutdown", 1064), ("postBlockAutoPowerReduction", 1065), ("postBlockManualLaserShutdown", 1066), ("preBlockSpanAdjustmentInProgress", 1067), ("postBlockSpanAdjustmentInProgress", 1068), ("payloadMissingIndication", 1069), ("manualOverrideActive", 1070), ("unequippedIndication", 1071), ("reflectionTooHigh", 1072), ("oscPowerOutOfSpecificationHigh", 1073), ("oscPowerOutOfSpecificationLow", 1074), ("oscControlFailure", 1075), ("modeMismatch", 1076), ("omsPowerOutOfSpecificationHigh", 1077), ("omsPowerOutOfSpecificationLow", 1078), ("otsSpanlossPowerOutOfSpecificationHigh", 1079), ("otsSpanlossPowerOutOfSpecificationLow", 1080), ("autoPowerReduction", 1081), ("postBlockAutoShutoffDisabled", 1082), ("totalpowerOutOfSpecificationHigh", 1083), ("totalpowerOutOfSpecificationLow", 1084), ("dipSessionActive", 1500), ("pPPFailure", 1600), ("lldpFail", 1700))

class FCTcCondType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 10001, 10002, 10003, 10004, 10005, 10100, 10101, 10102, 10200, 10201, 10202, 10300, 10301, 10302, 10303, 10304, 10305, 10306, 10307, 10308, 10400, 10401, 10500, 10501, 10600, 10601, 10602, 10603, 10700, 10701, 10702, 10703, 10704, 10705, 10800, 10801, 10900, 10901, 10902, 10903, 10904, 10905, 10906, 11000, 11001, 11002, 11003, 11004, 11100, 11101, 11102, 11200, 11300, 11301))
    namedValues = NamedValues(("prod-specific", 0), ("manualSwitch", 10001), ("workingSwitchProtection", 10002), ("workingSwitchProtectionManual", 10003), ("workingSwitchProtectionForced", 10004), ("workingSwitchWorking", 10005), ("databaseActivation", 10100), ("databaseActivationFailure", 10101), ("databaseActivationReversion", 10102), ("firmwareActivation", 10200), ("firmwareActivationComplete", 10201), ("firmwareActivationFailure", 10202), ("softwareActivation", 10300), ("softwareActivationComplete", 10301), ("softwareActivationFailure", 10302), ("softwareReversion", 10303), ("cancelValidationTimerInProgress", 10304), ("cancelValidationTimerComplete", 10305), ("cancelValidationTimerFailed", 10306), ("uBootFailOver", 10307), ("softwareFailOver", 10308), ("daylightSavingTimeAdjustment", 10400), ("dateTimeModified", 10401), ("sysNtpSynchronized", 10500), ("sysNtpSwitchOver", 10501), ("systemRestartCold", 10600), ("systemRestartWarm", 10601), ("systemRestartDbInitialization", 10602), ("systemRestartShfprov", 10603), ("copyFileInProgress", 10700), ("copyFileComplete", 10701), ("copyFileFailure", 10702), ("copyFileFailureTransfer", 10703), ("copyFileFailureMd5check", 10704), ("copyFileFailureVerification", 10705), ("equipmentPlugin", 10800), ("equipmentPlugout", 10801), ("entityOperStatusChangeToUp", 10900), ("entityOperStatusChangeToDown", 10901), ("entityOperStatusChangeToTesting", 10902), ("entityOperStatusChangeToUnknown", 10903), ("entityOperStatusChangeToDormant", 10904), ("entityOperStatusChangeToNotPresent", 10905), ("entityOperStatusChangeToLowerLayerDown", 10906), ("autoLogoffAssociationCancellation", 11000), ("autoLogoffSessionTimeout", 11001), ("autoLogoffCableDisconnect", 11002), ("autoLogoffPasswordChanged", 11003), ("forcedLogoff", 11004), ("ipNotReachable", 11100), ("ipReachable", 11101), ("ipPingRequestTimedOut", 11102), ("lldpNbrInfoChanged", 11200), ("otdrScanComplete", 11300), ("otdrScanFailure", 11301))

class FCTcaCondType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213))
    namedValues = NamedValues(("prod-specific", 0), ("tCAOpticalReceivePowerTooLow", 1), ("tCAOpticalReceivePowerTooHigh", 2), ("tCAOpticalTransmitPowerTooLow", 3), ("tCAOpticalTransmitPowerTooHigh", 4), ("tCALaserBiasCurrentTooHigh", 5), ("tCAOpticalReceivePowerLane1TooLow", 6), ("tCAOpticalReceivePowerLane1TooHigh", 7), ("tCAOpticalTransmitPowerLane1TooLow", 8), ("tCAOpticalTransmitPowerLane1TooHigh", 9), ("tCALaserBiasCurrentLane1TooHigh", 10), ("tCAOpticalReceivePowerLane2TooLow", 11), ("tCAOpticalReceivePowerLane2TooHigh", 12), ("tCAOpticalTransmitPowerLane2TooLow", 13), ("tCAOpticalTransmitPowerLane2TooHigh", 14), ("tCALaserBiasCurrentLane2TooHigh", 15), ("tCAOpticalReceivePowerLane3TooLow", 16), ("tCAOpticalReceivePowerLane3TooHigh", 17), ("tCAOpticalTransmitPowerLane3TooLow", 18), ("tCAOpticalTransmitPowerLane3TooHigh", 19), ("tCALaserBiasCurrentLane3TooHigh", 20), ("tCAOpticalReceivePowerLane4TooLow", 21), ("tCAOpticalReceivePowerLane4TooHigh", 22), ("tCAOpticalTransmitPowerLane4TooLow", 23), ("tCAOpticalTransmitPowerLane4TooHigh", 24), ("tCALaserBiasCurrentLane4TooHigh", 25), ("tCATotalOpticalReceivePowerTooLow", 26), ("tCATotalOpticalReceivePowerTooHigh", 27), ("tCASpanlossVariationTooLow", 28), ("tCASpanlossVariationTooHigh", 29), ("tCAOpticalReceivePowerOscTooLow", 30), ("tCAOpticalReceivePowerOscTooHigh", 31), ("tCAOpticalTransmitPowerOscTooLow", 32), ("tCAOpticalTransmitPowerOscTooHigh", 33), ("tCAFECCorrectedCodewords", 201), ("tCAFECUncorrectedCodewords", 202), ("tCAFECCorrectedSymbols", 203), ("tCACodingViolations", 204), ("tCAErroredSeconds", 205), ("tCASeverelyErroredSeconds", 206), ("tCAFECUncorrectedBlocks", 207), ("tCAFECCorrectedBits", 208), ("tCASDFECCorrectedBits", 209), ("tCABackgroundBlockErrors", 210), ("tCADelayMeasurement", 211), ("tCAUnavailableSeconds", 212), ("tCAErroredBlocks", 213))

class FCStdObjectIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FCStdTypeIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FCTrapHistIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class FCMonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0))
    namedValues = NamedValues(("prod-specific", 0))

mibBuilder.exportSymbols("FSS-COMMON-TC", FCObjectName=FCObjectName, FCTcaCondType=FCTcaCondType, FCDirection=FCDirection, FCStdObjectIndex=FCStdObjectIndex, PYSNMP_MODULE_ID=fcTc, FCServEffect=FCServEffect, FCTrapHistIndex=FCTrapHistIndex, fcTc=fcTc, FCCondType=FCCondType, FCMonType=FCMonType, FCTimePeriod=FCTimePeriod, FCLocation=FCLocation, FCCondEffect=FCCondEffect, FCTrapType=FCTrapType, FCSeverity=FCSeverity, FCTcCondType=FCTcCondType, FCStdTypeIndex=FCStdTypeIndex)
