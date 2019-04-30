#
# PySNMP MIB module MERU-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MERU-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:01:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
meru_modules, = mibBuilder.importSymbols("MERU-SMI", "meru-modules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, Counter32, Integer32, ModuleIdentity, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, MibIdentifier, Unsigned32, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter32", "Integer32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "MibIdentifier", "Unsigned32", "TimeTicks", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
meruTextualConventions = ModuleIdentity((1, 3, 6, 1, 4, 1, 15983, 1, 2, 1))
if mibBuilder.loadTexts: meruTextualConventions.setLastUpdated('200506050000Z')
if mibBuilder.loadTexts: meruTextualConventions.setOrganization('Meru Networks')
class MwlAclEnvState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("aclEnvDisabled", 0), ("aclEnvAllow", 1), ("aclEnvDeny", 2))

class MwlAddressAssignmentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("ipAssignmentStatic", 1), ("ipAssignmentDynamic", 2), ("ipAssignmentDynamicDhcp", 3), ("ipAssignmentUnknown", 4))

class MwlAddressIfAssignmentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ifIpAssignmentNone", 0), ("ifIpAssignmentStatic", 1), ("ifIpAssignmentDhcp", 2))

class MwlApIpAssignmentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("apIpAssignmentNone", 0), ("apIpAssignmentStatic", 1), ("apIpAssignmentDhcp", 2))

class MwlAdministrativeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("adminStateUnlocked", 1), ("adminStateLocked", 2), ("adminStateShuttingDown", 3), ("adminStateUnknown", 4), ("adminStateForceShuttingDown", 5))

class MwlAdmissionControl(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("admitall", 0), ("pendingflag", 1), ("rejectflag", 2))

class MwlAntennaSet(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("antennaSetUnknown", 0), ("antennaSetInternal", 1), ("antennaSetExternal", 2), ("antennaSetExternalDualMode", 3), ("antennaSetRsAntenna", 4))

class MwlApAssignType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("assignApUnknown", 0), ("siblingAp", 1), ("assignedAp", 2), ("discoveredAp", 3))

class MwlApType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("apUnknown", 0), ("apStation", 1), ("apAccessPoint", 2))

class MwlApIndoorOutdoorType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("apIndoor", 0), ("apOutdoor", 1))

class MwlApMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 100))
    namedValues = NamedValues(("apModeNormal", 1), ("apModeScanning", 100))

class MwlAuthenticationAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("nmsAuthenticationAlg8021x", 1), ("nmsAuthenticationAlgMd5", 2), ("nmsAuthenticationAlgTls", 3), ("nmsAuthenticationAlgTtls", 4), ("nmsAuthenticationAlgPeap", 5), ("nmsAuthenticationAlgWeb", 6))

class MwlAuthenticationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("nmsAuthenticationTypeLocal", 1), ("nmsAuthenticationTypeRadius", 2), ("nmsAuthenticationTypeTacacs", 3))

class MwlCaptivePortalAuthenticationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nmsCaptivePortalAuthenticationTypeRadius", 0), ("nmsCaptivePortalAuthenticationTypeLocal", 1), ("nmsCaptivePortalAuthenticationTypeLocalRadius", 2))

class MwlAuthSuiteBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("authNone", 0), ("authEap", 1), ("authPsk", 2), ("authCert", 3), ("authAll", 4))

class MwlActionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("actionNone", 0), ("actionStart", 1), ("actionStop", 2), ("actionInProgress", 3), ("actionError", 4), ("actionDone", 5), ("actionForceStart", 6))

class MwlAlarmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("alarmStateNoAlarm", 1), ("alarmStateMinor", 2), ("alarmStateMajor", 3), ("alarmStateCritical", 4))

class MwlAlarmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48))
    namedValues = NamedValues(("alarmUnknown", 0), ("alarmLinkUp", 1), ("alarmLinkDown", 2), ("alarmColdStart", 3), ("alarmWarmStart", 4), ("alarmAuthFail", 5), ("alarmAscDown", 6), ("alarmApDown", 7), ("alarmApNeighborLoss", 8), ("alarmHandOffFail", 9), ("alarmResourceThresholdExceed", 10), ("alarmSystemFailure", 11), ("alarmWatchdogFailure", 12), ("alarmAscApAdd", 13), ("alarmAscApRemove", 14), ("alarmAscApModify", 15), ("alarmStaApAdd", 16), ("alarmStaApRemove", 17), ("alarmStaApModify", 18), ("alarmRogueApDetected", 19), ("alarmWncCertError", 20), ("alarmApSoftwareVersionMismatch", 21), ("alarmApBootimageVersionMismatch", 22), ("alarmApTemperature", 23), ("alarmHardwareDiagnostic", 24), ("alarmApInitFailure", 25), ("alarmRadioCardFailure", 26), ("alarmSoftwareLicenseExpired", 27), ("alarm8021xAuthFailure", 28), ("alarmMicFailureAp", 29), ("alarmMicCountermeasureActivation", 30), ("alarmRadiusServerSwitchover", 31), ("alarmRadiusServerSwitchoverFailed", 32), ("alarmPrimaryRadiusServerRestored", 33), ("alarmAcctRadiusServerSwitchover", 34), ("alarmAcctRadiusServerSwitchoverFailed", 35), ("alarmMasterDown", 36), ("alarmMasterUp", 37), ("alarmMacFilterDeny", 38), ("alarmCacLimitReached", 39), ("alarmRadarDetected", 40), ("alarmOperChannelChange", 41), ("alarm8021xAuthAttempt", 42), ("alarmWirelessAssoc", 43), ("alarmLicensingServerDown", 44), ("alarmNupgradeLicenseCheckoutFail", 45), ("alarmNoLicenseEnforcementExpired", 46), ("alarmApRuntimeError", 47), ("alarmTotal", 48))

class MwlAlarmSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("alarmSevInfo", 0), ("alarmSevMajor", 1), ("alarmSevMinor", 2), ("alarmSevCritical", 3), ("alarmSevClear", 4))

class MwlAntenna(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("antennaNothing", 0), ("antenna1", 1), ("antenna2", 2), ("antennaBoth", 3), ("antennaAll", 4))

class MwlAssignmentAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("assignmentAlgoRssi", 1), ("assignmentAlgoPressure", 2), ("assignmentAlgoActivity", 3), ("assignmentAlgoRssiTrending", 4), ("assignmentAlgoAvailRsrc", 5), ("assignmentAlgoUnknown", 6))

class MwlAssociationState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("assocstateprobing", 0), ("assocstateauthentication", 1), ("assocstateassociated", 2))

class MwlApAuthState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("apAuthKeyed", 0), ("apAuthNokey", 1), ("apUnauth", 2))

class MwlAvailabilityStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("availStatusPowerOff", 1), ("availStatusOffline", 2), ("availStatusOnline", 3), ("availStatusFailed", 4), ("availStatusInTest", 5), ("availStatusNotInstalled", 6))

class MwlBeaconCoordinationMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("beaconCoordinationModeCoordinated", 0), ("beaconCoordinationModeLocal", 1), ("beaconCoordinationModeDistributed", 2))

class MwlBlock(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("blockNone", 0), ("blockSelected", 1), ("blockAll", 2), ("wiredRogue", 3))

class MwlCoordAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("coordAlgoDefault", 1), ("coordAlgoUnknown", 2))

class MwlCypherSuiteBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("cypherNone", 0), ("cypherWep40", 1), ("cypherWep104", 2), ("cypherTkip", 4), ("cypherCcmp", 8), ("cypherCcmpTkip", 16), ("cypherWpiSms4", 32), ("cypherClear", 64), ("cypherAll", 127))

class MwlL2BridgingsBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bridgingNone", 0), ("bridgingAirf", 1), ("bridgingIpv6", 2), ("bridgingAtalk", 4))

class MwlDropPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("drophead", 0), ("droptail", 1))

class MwlDataplaneMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("dataplaneModeTunneled", 0), ("dataplaneModeBridged", 1))

class MwlProfileOwner(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("profileOwnerController", 0), ("profileOwnerNmsServer", 1))

class MwlApRole(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("apRoleAccess", 0), ("apRoleGateway", 1), ("apRoleWireless", 2))

class MwlEncryptionAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("encryptionWep", 1), ("encryptionTkip", 2), ("encryptionCcmp", 3), ("encryptionUnknown", 4), ("encryptionClear", 5))

class MwlIfAdministrativeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("adminStateDown", 1), ("adminStateUp", 2), ("adminStateTesting", 3))

class MwlEssApAdminMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("essApAdminModeDown", 1), ("essApAdminModeUp", 2), ("essApAdminModeScan", 3), ("essApAdminModeUnlicensed", 4), ("essAdminModeDisabled", 5), ("essAdminModeNoservice", 6), ("essApAdminModePowerdown", 7))

class MwlLedMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("ledModeNormal", 0), ("ledModeNodeId", 1), ("ledModeBlink", 2), ("ledModeDark", 3))

class MwlLogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("logSevEmerg", 0), ("logSevAlert", 1), ("logSevCritical", 2), ("logSevError", 3), ("logSevWarn", 4), ("logSevNotice", 5), ("logSevInfo", 6), ("logSevDebug", 7), ("logSevTotal", 8))

class MwlLogType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("logUnknown", 0), ("logApDetected", 1), ("logDbBackup", 2), ("logDbRestore", 3), ("logSwUpgrade", 4), ("logConfigAdd", 5), ("logConfigMod", 6), ("logConfigDel", 7), ("logCertExpiry", 8), ("logVlan", 9), ("logHaStart", 10), ("logHaShutdown", 11), ("logHaNodeDead", 12), ("logHaStatus", 13), ("logHaConfigErr", 14), ("logHaLinkStatus", 15), ("logApAdministrativeReboot", 16), ("logControllerAdministrativeReboot", 17), ("logDiscLicensingFailure", 18), ("logMicCountermeasure", 19), ("logMicFailureAp", 20), ("logMicFailureClient", 21), ("logTypeTotal", 22))

class MwlMimoMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nmsMimoMode2x2", 0), ("nmsMimoMode3x3", 1), ("nmsMimoMode1x1", 2))

class MwlNatType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("natTypeNone", 1), ("natTypeStaticOneToOne", 2), ("natTypeDynamicOneToOne", 3), ("natTypeDynamicNapt", 4), ("natTypeUnknown", 5))

class MwlNetProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 6, 17))
    namedValues = NamedValues(("nmsIpprotoUnknown", 0), ("nmsIpprotoTcp", 6), ("nmsIpprotoUdp", 17))

class MwlNmsInterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ifTypeActive", 0), ("ifTypeRedundant", 1))

class MwlNodeRelationship(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noderelationshipnone", 1), ("noderelationshipbound", 2), ("noderelationshipvisible", 3))

class MwlNodeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 10, 11, 12))
    namedValues = NamedValues(("nodeTypeWnc", 1), ("nodeTypeAp", 2), ("nodeTypeAsc", 3), ("nodeTypeSta", 10), ("nodeTypeOther", 11), ("nodeTypeUnknown", 12))

class MwlOperationalState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("operationalStateUnknown", 0), ("operationalStateEnabled", 1), ("operationalStateDisabled", 2), ("operationalStateUnlicensed", 3), ("operationalStateEnabledWith11nlic", 4), ("operationalStatePowerDown", 5))

class MwlPowerSupply(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("powerSupply8023Af", 0), ("powerSupply8023At", 1), ("powerSupply5vDc", 2), ("powerSupplyDual8023Af", 3), ("powerSupply12vDc", 4))

class MwlRadiusMacDelimiter(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))
    namedValues = NamedValues(("radiusMacDelimiterNone", 0), ("radiusMacDelimiterHyphen", 1), ("radiusMacDelimiterSingleHyphen", 2), ("radiusMacDelimiterColon", 4))

class MwlRadiusPasswordType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("radiusPasswordTypeSharedSecret", 0), ("radiusPasswordTypeMacAddress", 1))

class MwlWlanOptimize(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("optimizeNone", 0), ("optimizePerformance", 1), ("optimizeHandoff", 2), ("optimizeCoverage", 3), ("optimizeInteroperability", 4), ("optimizeRogueap", 5))

class MwlOnOffSwitch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("nmsOff", 0), ("nmsOn", 1))

class MwlPublishEssId(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("publishEssidOff", 0), ("publishEssidOn", 1), ("publishEssid24g", 2), ("publishEssid5g", 3))

class MwlAllOnSelectedSwitch(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("nmsSelected", 0), ("nmsAllOn", 1))

class MwlPrivacyBit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("privacyBitAuto", 0), ("privacyBitOn", 1), ("privacyBitOff", 2))

class MwlQosAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("nmsQosActionForward", 1), ("nmsQosActionCapture", 2), ("nmsQosActionDrop", 3))

class MwlQosCodec(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("nmsCodecDefault", 1), ("nmsCodecaG711ULaw64k", 2), ("nmsCodeca1016", 3), ("nmsCodecaG721", 4), ("nmsCodecaGsm", 5), ("nmsCodecaG7231", 6), ("nmsCodecaDv14", 7), ("nmsCodecaDv142", 8), ("nmsCodecaLpc", 9), ("nmsCodecaG711ALaw64k", 10), ("nmsCodecaG722", 11), ("nmsCodecaG7221", 12), ("nmsCodecaG722132k", 13), ("nmsCodecaMpa", 14), ("nmsCodecaG728", 15), ("nmsCodecaG729", 16), ("nmsCodecaRed", 17), ("nmsCodecaSiren", 18), ("nmsCodecvH261", 19), ("nmsCodecvH263", 20))

class MwlQosProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("qosprotocolsip", 1), ("qosprotocolh323", 2), ("qosprotocolsccp", 3), ("qosprotocolhttp", 4), ("qosprotocolother", 5), ("qosprotocolnone", 6), ("qosprotocolunknown", 7))

class MwlQosCodecProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("qoscodecprotocolsip", 1), ("qoscodecprotocolh323", 2), ("qoscodecprotocolsccp", 3), ("qoscodecprotocolhttp", 4), ("qoscodecprotocolnone", 5), ("qoscodecprotocolunknown", 6))

class MwlQosCallState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("qoscalldisconnectedstate", 0), ("qoscallconnectedstate", 1), ("qoscallholdstate", 2), ("qoscallconferencingstate", 3))

class MwlServiceAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("nmsServiceActionAdd", 1), ("nmsServiceActionRemove", 2), ("nmsServiceActionChange", 3))

class MwlSecurityPolicyAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("securityPolicyActionDeny", 0), ("securityPolicyActionAllow", 1), ("securityPolicyActionRedirect", 2), ("securityPolicyActionNum", 3))

class MwlL2SecurityModeBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("l2SecurityModeNone", 0), ("l2SecurityModeOpen", 1), ("l2SecurityMode8021x", 2), ("l2SecurityModeSwk", 4), ("l2SecurityModeWpa", 8), ("l2SecurityModeWpaPsk", 16), ("l2SecurityModeWpa2", 32), ("l2SecurityModeWpa2Psk", 64), ("l2SecurityModeMixed", 128), ("l2SecurityModeMixedPsk", 256), ("l2SecurityModeWai", 512), ("l2SecurityModeWaiPsk", 1024), ("l2SecurityModeAll", 2047))

class MwlL2SecurityMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2047))
    namedValues = NamedValues(("l2SecurityModeNone", 0), ("l2SecurityModeOpen", 1), ("l2SecurityMode8021x", 2), ("l2SecurityModeSwk", 4), ("l2SecurityModeWpa", 8), ("l2SecurityModeWpaPsk", 16), ("l2SecurityModeWpa2", 32), ("l2SecurityModeWpa2Psk", 64), ("l2SecurityModeMixed", 128), ("l2SecurityModeMixedPsk", 256), ("l2SecurityModeWai", 512), ("l2SecurityModeWaiPsk", 1024), ("l2SecurityModeAll", 2047))

class MwlTunnelTerminationModeBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("tunnelTerminationNone", 0), ("tunnelTerminationPeap", 1), ("tunnelTerminationTtls", 2))

class MwlL2SecurityDetailMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 511, 512, 1024, 2048, 4096, 8192, 16384, 32768))
    namedValues = NamedValues(("stationSecurityModeNone", 0), ("stationSecurityModeOpen", 1), ("stationSecurityMode8021x", 2), ("stationSecurityModeSwk", 4), ("stationSecurityModeWpa", 8), ("stationSecurityModeWpaPsk", 16), ("stationSecurityModeWpa2", 32), ("stationSecurityModeWpa2Psk", 64), ("stationSecurityModeMixed", 128), ("stationSecurityModeMixedPsk", 256), ("stationSecurityModeAll", 511), ("stationSecurityMode8021xInProgress", 512), ("stationSecurityModeWpaInProgress", 1024), ("stationSecurityModeWpaPskInProgress", 2048), ("stationSecurityModeWpa2InProgress", 4096), ("stationSecurityModeWpa2PskInProgress", 8192), ("stationSecurityModeMixedInProgress", 16384), ("stationSecurityModeMixedPskInProgress", 32768))

class MwlL3SecurityMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4, 7))
    namedValues = NamedValues(("l3SecurityModeOpen", 1), ("l3SecurityModeVpn", 2), ("l3SecurityModeWebauth", 4), ("l3SecurityModeAll", 7))

class MwlCaptivePortalMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("captivePortalDisabled", 0), ("captivePortalModeVpn", 1), ("captivePortalModeWebauth", 2), ("captivePortalModeAll", 3))

class MwlCaptivePortalAuthState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("captivePortalStateClear", 0), ("captivePortalStateWebauth", 1))

class MwlCaptivePortalAuthMethod(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("captivePortalAuthMethodInternal", 0), ("captivePortalAuthMethodExternal", 1))

class MwlSnmpPrivilege(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("snmpRo", 1), ("snmpRw", 2))

class MwlSnmpV3AuthProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("snmpV3UsmNoAuth", 0), ("snmpV3UsmHmacMd5Auth", 1), ("snmpV3UsmHmacShaAuth", 2))

class MwlSnmpV3PrivProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("snmpV3UsmNoPriv", 0), ("snmpV3UsmDesPriv", 1))

class MwlTransmitRateBGBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("bgtransmitRateNotSupported", 0), ("bgtransmitRate1", 1), ("bgtransmitRate2", 2), ("bgtransmitRate55", 4), ("bgtransmitRate11", 8), ("bgtransmitRate6", 16), ("bgtransmitRate9", 32), ("bgtransmitRate12", 64), ("bgtransmitRate18", 128), ("bgtransmitRate22", 256), ("bgtransmitRate24", 512), ("bgtransmitRate33", 1024), ("bgtransmitRate36", 2048), ("bgtransmitRate48", 4096), ("bgtransmitRate54", 8192))

class MwlTransmitRateBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("transmitRateNotSupported", 0), ("transmitRate1", 1), ("transmitRate2", 2), ("transmitRate55", 4), ("transmitRate11", 8))

class MwlTransmitRateAGBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("agtransmitRateNotSupported", 0), ("agtransmitRate6", 16), ("agtransmitRate9", 32), ("agtransmitRate12", 64), ("agtransmitRate18", 128), ("agtransmitRate22", 256), ("agtransmitRate24", 512), ("agtransmitRate33", 1024), ("agtransmitRate36", 2048), ("agtransmitRate48", 4096), ("agtransmitRate54", 8192))

class MwlTransmitRateHTBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("httransmitRateNotSupported", 0), ("httransmitRate0", 1), ("httransmitRate1", 2), ("httransmitRate2", 4), ("httransmitRate3", 8), ("httransmitRate4", 16), ("httransmitRate5", 32), ("httransmitRate6", 64), ("httransmitRate7", 128), ("httransmitRate8", 256), ("httransmitRate9", 512), ("httransmitRate10", 1024), ("httransmitRate11", 2048), ("httransmitRate12", 4096), ("httransmitRate13", 8192), ("httransmitRate14", 16384), ("httransmitRate15", 32768), ("httransmitRate16", 65536), ("httransmitRate17", 131072), ("httransmitRate18", 262144), ("httransmitRate19", 524288), ("httransmitRate20", 1048576), ("httransmitRate21", 2097152), ("httransmitRate22", 4194304), ("httransmitRate23", 8388608))

class MwlUpgradeState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("upgradeStart", 1), ("upgradeInProgress", 2), ("upgradeFailed", 3), ("upgradeDone", 4))

class MwlVlanType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("vlanNone", 0), ("vlanDefaultOnly", 1), ("vlanRadiusOnly", 2), ("vlanRadiusAndDefault", 3), ("vlanGre", 4))

class MwlAirFirewall(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("airfirewallNone", 0), ("airfirewallOuis", 1))

class MwlOffHours(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("offhoursNone", 0), ("offhours", 1))

class MwlOffHoursService(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("offhoursNoservice", 0), ("offhoursNowireless", 1))

class MwlDailyOutOfService(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("noDailyOutOfService", 0), ("dailyOutOfServiceOff", 1), ("dailyOutOfServiceOn", 2))

class MwlVpnStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5))
    namedValues = NamedValues(("clearActive", 0), ("vpnBypass", 1), ("vpnActive", 2), ("webAuthActive", 4), ("vpnWebActive", 5))

class MwlVpnDetailStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 8, 16, 32))
    namedValues = NamedValues(("stationClearActive", 0), ("stationVpnBypass", 1), ("stationVpnActive", 2), ("stationWebAuthActive", 4), ("stationVpnWebActive", 5), ("stationVpnInProgress", 8), ("stationWebauthInProgress", 16), ("stationVpnWebauthInProgress", 32))

class MwlSslUsrAuthProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("sslAuthProtocolUnknown", 0), ("sslAuthProtocolNone", 1), ("sslAuthProtocolChap", 2))

class MwlDhGroupType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5))
    namedValues = NamedValues(("dhGroup2", 2), ("dhGroup3", 3), ("dhGroup4", 4), ("dhGroup5", 5))

class MwlIpSecModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ipsecUnknownMode", 0), ("ipsecTunnelMode", 1))

class MwlIpSecDataChannelType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ipsecUnknown", 0), ("ipsecEsp", 1))

class MwlIpEncryptionAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("encryptionUnknownAlgorithm", 0), ("encryption3des", 1))

class MwlIpAuthenticateAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("authUnknown", 0), ("authPreShareKey", 1))

class MwlIpHashAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("hashUnknown", 0), ("hashSha", 1), ("hashMd5", 2))

class MwlIpSecAuthAlgorithm(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("ipsecAuthUnknown", 0), ("ipsecAuthShaHmac", 1), ("ipsecAuthMd5Hmac", 2))

class MwlCertFileType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("certUnknownType", 0), ("certPemType", 1), ("certPfxType", 2))

class MwlUrlType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cliBadUrl", 0), ("cliFtpUrl", 1), ("cliTftpUrl", 2), ("cliSftpUrl", 3), ("cliHttpUrl", 4), ("cliHttpsUrl", 5), ("cliScpUrl", 6), ("cliFileUrl", 7))

class MwlCertificateFormType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("nmsShortForm", 0), ("nmsLongForm", 1))

class MwlRadiusServerSelect(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("nmsRadiusServerNone", 0), ("nmsRadiusServerPrimary", 1), ("nmsRadiusServerSecondary", 2), ("nmsRadiusServerAll", 3))

class MwlDiscoveryOrder(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("discoveryFromL2First", 0), ("discoveryFromL2Only", 1), ("discoveryFromL3First", 2), ("discoveryFromL3Only", 3))

class MwlApDiscoveryState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("noDiscoveryLayer", 0), ("discoveryFromL2", 1), ("discoveryFromL3", 2))

class MwlLicenseType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("featureTrial", 0), ("featurePermanent", 1))

class MwlLicenseReserveType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("countedLicense", 0), ("uncountedLicense", 1))

class MwlSofwFeatureType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("sofwControllerBasic", 0), ("sofwApBasic", 1), ("sofwFeatMax", 2))

class MwlSofwControllerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("sofwAll", 0), ("sofwController", 1), ("sofwStdbyController", 2))

class MwlDscpType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(-1, 0, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 46, 48, 56))
    namedValues = NamedValues(("dscpDisabled", -1), ("dscpCs0", 0), ("dscpCs1", 8), ("dscpAf11", 10), ("dscpAf12", 12), ("dscpAf13", 14), ("dscpCs2", 16), ("dscpAf21", 18), ("dscpAf22", 20), ("dscpAf23", 22), ("dscpCs3", 24), ("dscpAf31", 26), ("dscpAf32", 28), ("dscpAf33", 30), ("dscpCs4", 32), ("dscpAf41", 34), ("dscpAf42", 36), ("dscpAf43", 38), ("dscpCs5", 40), ("dscpEfphb", 46), ("dscpCs6", 48), ("dscpCs7", 56))

class MwlControllerHwType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 18, 19, 20))
    namedValues = NamedValues(("wncUnknownModel", 0), ("wncDevelPc", 1), ("wncMc1000", 2), ("wncMc1100", 3), ("wncMc3000", 4), ("wncMc500", 5), ("wncMc500a", 6), ("wncMc5000", 7), ("wncMc4000", 8), ("wncMc4100", 9), ("wncMc1500", 11), ("wncMc3200", 13), ("wncMc4200", 14), ("wncMc6000", 15), ("wncMc1500v", 16), ("wncMc3200v", 17), ("wncMc4200v", 18), ("wncMc1550", 19), ("wncMc1550v", 20))

class MwlWncControllerState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("wncStandalone", 0), ("wncMaster", 1), ("wncSlave", 2), ("wncCluster", 3))

class MwlApHwType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 12, 13, 14, 15, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43))
    namedValues = NamedValues(("apUnknownModel", 0), ("ap300", 12), ("ap310", 13), ("ap311", 14), ("ap320", 15), ("ap301", 18), ("ap302", 19), ("ap301i", 20), ("ap310i", 21), ("ap302i", 22), ("ap320i", 23), ("ap1010", 24), ("ap1020", 25), ("psm3x", 26), ("ap400", 27), ("ap433e", 28), ("ap433i", 29), ("ap432e", 30), ("ap432i", 31), ("ap1010e", 32), ("ap1020e", 33), ("ap433is", 34), ("ap433es", 35), ("oap432e", 36), ("oap433e", 37), ("oap433es", 38), ("ap110", 39), ("ap120", 40), ("ap1014i", 41), ("ap332e", 42), ("ap332i", 43))

class MwlApRegulatoryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("ap1000RegIndex", 1), ("ap300Mb72RegIndex", 2), ("ap300Mb82RegIndex", 3), ("ap400RegIndex", 4), ("ap110RegIndex", 5), ("ap330RegIndex", 6))

class MwlApRfType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("apRfUnknownModel", 0), ("apRf1", 1), ("apRf2", 2), ("apRf3", 3), ("apRf4", 4), ("apRf5", 5), ("apRf6", 6), ("apRf7", 7), ("apRf8", 8), ("apRf9", 9), ("apRf10", 10), ("apRf11", 11), ("apRf12", 12), ("apRf13", 13), ("apRf14", 14), ("apRf15", 15))

class MwlApIfModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("apModeUnknown", 0), ("apBMode", 1), ("apAMode", 2), ("apAbMode", 3), ("apGMode", 4), ("apBgMode", 5), ("apAgMode", 6), ("apAbgMode", 7), ("apNMode", 8), ("apBnMode", 9), ("apAnMode", 10), ("apAbnMode", 11), ("apGnMode", 12), ("apBgnMode", 13), ("apAgnMode", 14), ("apAbgnMode", 15), ("apAn1s20Mode", 16), ("apAn1s40Mode", 17), ("apAn2s20Mode", 18), ("apAn2s40Mode", 19), ("apAn3s20Mode", 20), ("apAn3s40Mode", 21), ("apBgn1s20Mode", 22), ("apBgn1s40Mode", 23), ("apBgn2s20Mode", 24), ("apBgn2s40Mode", 25), ("apBgn3s20Mode", 26), ("apBgn3s40Mode", 27))

class MwlApIfConfigModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 5, 10, 13))
    namedValues = NamedValues(("apConfigModeUnknown", 0), ("apConfigBMode", 1), ("apConfigAMode", 2), ("apConfigGMode", 4), ("apConfigBgMode", 5), ("apConfigAnMode", 10), ("apConfigBgnMode", 13))

class MwlAntennaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("antennaConnNone", 0), ("antennaConn24g", 1), ("antennaConn5g", 2), ("antennaConnDual", 3), ("antennaConnExt", 4), ("antennaConnInt", 5))

class MwlBandType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rfband24g", 1), ("rfband5g", 2))

class MwlChannelBandType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("channelBMode", 1), ("channelAMode", 2), ("channelGMode", 3), ("channelBgMode", 4), ("channelAbgnMode20mhz", 5), ("channelAbgnMode40mhzAbove", 6), ("channelAbgnMode40mhzBelow", 7), ("channelNMode20mhz", 8), ("channelNMode40mhzAbove", 9), ("channelNMode40mhzBelow", 10))

class MwlAntennaSetLocation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096))
    namedValues = NamedValues(("antennaSetLocUnknown", 0), ("antennaSetLocLeft", 1), ("antennaSetLocRight", 2), ("antennaSetLoc1", 4), ("antennaSetLoc2", 8), ("antennaSetLoc3", 16), ("antennaSetLoc4", 32), ("antennaSetLoc5", 64), ("antennaSetLoc6", 128), ("antennaSetLoc7", 256), ("antennaSetLoc8", 512), ("antennaSetLoc9", 1024), ("antennaSetLocIntegrated", 2048), ("antennaSetLocInternal", 4096))

class MwlIfDataRateOptionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("dataRateManual", 0), ("dataRateAuto", 1))

class MwlAntennaLinkType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("antennaLinkUnknown", 0), ("antennaLinkPmp", 1), ("antennaLinkPtp", 2))

class MwlDuplexModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("nmsDuplexFull", 0), ("nmsDuplexHalf", 1))

class MwlBgProtectionModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("bgProtectionAuto", 0), ("bgProtectionOn", 1), ("bgProtectionOff", 2))

class MwlHtProtectionModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("htProtectionAuto", 0), ("htProtectionOn", 1), ("htProtectionOff", 2))

class MwlIpProxyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("nmsGeneric", 0), ("nmsIpPathFinder", 1), ("nmsEnumerationHeader", 2))

class MwlFirewallCapability(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("firewallNone", 0), ("firewallConfigured", 1), ("firewallRadiusConfigured", 2))

class MwlSecurityLogging(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("securityloggingOff", 0), ("securityloggingAllow", 1), ("securityloggingDeny", 2), ("securityloggingAll", 3))

class MwlPMKcachingBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("pmkCachingDisabled", 0), ("pmkCachingEnabled", 1))

class MwlKDDI(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("kddiDisabled", 0), ("kddiEnabled", 1))

class MwlVcellType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("nmsVcellPap", 0), ("nmsVcellVcell", 1))

class MwlFilterModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("exclude", 0), ("include", 1))

class MwlBgRadioMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("virtualMode", 1), ("nonVirtualMode", 2))

class MwlThrdPartyIdsIps(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("thrdPidsIpsSnortWireless", 1), ("thrdPidsIpsNone", 2))

class MwlQosRulesMatchClassBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("qosrulesmatchclassOff", 0), ("qosrulesmatchclassOn", 1))

class MwlQosRulesMatchClass(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("qosrulesmatchclassOff", 0), ("qosrulesmatchclassOn", 1))

class MwlChannelWidth(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("channelWidth20", 1), ("channelWidth40Above", 2), ("channelWidth40Below", 3))

class MwlBonding(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("bondingSingle", 0), ("bondingDual", 1), ("bondingNone", 2))

class MwlConnectivityStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("nmsDisconnected", 0), ("nmsConnected", 1))

class MwlCapabilityModeBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("nmsStaCapabilityNone", 0), ("nmsStaWmmMode", 1), ("nmsStaApsdMode", 2))

class MwlClientType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("nmsClientData", 1), ("nmsClientSipPhone", 2))

class MwlDeviceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("nmsStationWireless", 0), ("nmsStationWired", 1))

class MwlStationState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("nmsStationStateUnknown", 0), ("nmsStationStateInit", 1), ("nmsStationStateVlan", 2), ("nmsStationStateAssign", 3), ("nmsStationStateAssociated", 4), ("nmsStationState8021x", 5), ("nmsStationStateKey", 6), ("nmsStationStateIpDiscover", 7), ("nmsStationStateCaptivePortal", 8), ("nmsStationStateDisassociated", 9))

class MwlStaDiagStap(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))
    namedValues = NamedValues(("staMacFilterAclCnt", 1), ("staMacFilterAclFailCnt", 2), ("staWepKeyIndexMismatchCnt", 3), ("staAssignFailCnt", 4), ("staAssociationCnt", 5), ("staKeyExchangeCnt", 6), ("staKeyExchangeFailCnt", 7), ("staMicFailCnt", 8), ("staIpDiscoveryCnt", 9), ("staRadiusAuthCnt", 10), ("staRadiusAuthFailCnt", 11), ("staCpGuestUserAuthCnt", 12), ("staCpGuestUserFailCnt", 13), ("staDecryptFailCnt", 14), ("staSoftHandoffCnt", 15))

class MwlEnableDisableOption(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("nmsDisable", 0), ("nmsEnable", 1))

class MwlPacketCaptureMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("l2Mode", 0), ("l3Mode", 1))

class MwlRxTxOption(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("rxOnly", 0), ("txOnly", 1), ("rxTxBoth", 2))

class MwlRateLimitMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("station", 0), ("cumulative", 1))

class MwlBandSteeringMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("bandSteeringDisable", 0), ("bandASteering", 1), ("bandNSteering", 2))

class MwlPapBroadcastSsidMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("papBroadcastSsidDisabled", 0), ("papBroadcastSsidAlways", 1), ("papBroadcastSsidTillAssociation", 2))

class MwlEncapsulationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("ppi", 0), ("legacy", 1))

class MwlUplinkType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("nmsUplink", 0), ("nmsDownlink", 1))

class MwlVpnConnectivityStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("vpnDisconnected", 0), ("vpnConnected", 1))

class MwlVpnAuthenticationStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("vpnUnknown", 0), ("vpnNoCertificate", 1), ("vpnValidCertificate", 2), ("vpnInvalidCertificate", 3), ("vpnCertificateRevoked", 4), ("vpnCertificateExpired", 5), ("vpnCertificateUnknownCa", 6))

class MwlVpnAuthenticationType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("vpnAuthTypeUnknown", 0), ("vpnAuthTypeX509Certificate", 1))

class MwlCertificateStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("certStatusUnknown", 0), ("certStatusNotInstalled", 1), ("certStatusInstalled", 2))

class MwlCertRequestStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("certReqStatusNone", 0), ("certReqStatusCsrGenerated", 1), ("certReqStatusCsrGenerationInProgress", 2), ("certReqStatusCsrGenerationFailed", 3), ("certReqStatusCsrUploadFailed", 4), ("certReqStatusCertInstalled", 5), ("certReqStatusCertInstallationInProgress", 6), ("certReqStatusCertDownloadFailed", 7), ("certReqStatusCertInstallationFailed", 8), ("certReqStatusCertDeleted", 9), ("certReqStatusCertDeletionInProgress", 10), ("certReqStatusCertDeletionFailed", 11), ("certReqStatusCaCertDownloaded", 12), ("certReqStatusCaCertDownloadInProgress", 13), ("certReqStatusCaCertDownloadFailed", 14))

class MwlFastEthernetType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("nmsPrimaryFastethernet", 1), ("nmsSecondaryFastethernet", 2))

class MwlVpnMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("modeNonVpn", 0), ("modeVpn", 1))

class MwlRegionSettings(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("regionUnknown", 0), ("regionUs", 1), ("regionIntl", 2))

class MwlArrayDataTypeAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("addValue", 1), ("deleteValue", 2), ("updateValue", 3))

mibBuilder.exportSymbols("MERU-TC", MwlPowerSupply=MwlPowerSupply, MwlAlarmSeverity=MwlAlarmSeverity, MwlVpnAuthenticationType=MwlVpnAuthenticationType, MwlAvailabilityStatus=MwlAvailabilityStatus, MwlActionStatus=MwlActionStatus, MwlUpgradeState=MwlUpgradeState, MwlVlanType=MwlVlanType, MwlIpAuthenticateAlgorithm=MwlIpAuthenticateAlgorithm, MwlSofwControllerType=MwlSofwControllerType, MwlDataplaneMode=MwlDataplaneMode, MwlApDiscoveryState=MwlApDiscoveryState, MwlApIfModeType=MwlApIfModeType, MwlCertRequestStatus=MwlCertRequestStatus, MwlIpSecAuthAlgorithm=MwlIpSecAuthAlgorithm, MwlRadiusPasswordType=MwlRadiusPasswordType, MwlPublishEssId=MwlPublishEssId, MwlAssignmentAlgorithm=MwlAssignmentAlgorithm, MwlMimoMode=MwlMimoMode, MwlSslUsrAuthProtocolType=MwlSslUsrAuthProtocolType, MwlQosCodec=MwlQosCodec, MwlOperationalState=MwlOperationalState, MwlAntennaSetLocation=MwlAntennaSetLocation, MwlNodeType=MwlNodeType, MwlCapabilityModeBits=MwlCapabilityModeBits, MwlAuthenticationAlgorithm=MwlAuthenticationAlgorithm, MwlCypherSuiteBits=MwlCypherSuiteBits, MwlAuthenticationType=MwlAuthenticationType, MwlL2BridgingsBits=MwlL2BridgingsBits, MwlRxTxOption=MwlRxTxOption, MwlVpnConnectivityStatus=MwlVpnConnectivityStatus, MwlChannelWidth=MwlChannelWidth, MwlL2SecurityMode=MwlL2SecurityMode, MwlAirFirewall=MwlAirFirewall, MwlPapBroadcastSsidMode=MwlPapBroadcastSsidMode, MwlQosCodecProtocol=MwlQosCodecProtocol, MwlDscpType=MwlDscpType, MwlDuplexModeType=MwlDuplexModeType, MwlQosCallState=MwlQosCallState, MwlLicenseReserveType=MwlLicenseReserveType, MwlIpSecModeType=MwlIpSecModeType, MwlLogSeverity=MwlLogSeverity, MwlLicenseType=MwlLicenseType, MwlPacketCaptureMode=MwlPacketCaptureMode, MwlSofwFeatureType=MwlSofwFeatureType, MwlTransmitRateBGBits=MwlTransmitRateBGBits, MwlQosRulesMatchClassBits=MwlQosRulesMatchClassBits, MwlBgRadioMode=MwlBgRadioMode, MwlArrayDataTypeAction=MwlArrayDataTypeAction, MwlWlanOptimize=MwlWlanOptimize, MwlDeviceType=MwlDeviceType, MwlIfDataRateOptionType=MwlIfDataRateOptionType, MwlIpEncryptionAlgorithm=MwlIpEncryptionAlgorithm, MwlQosRulesMatchClass=MwlQosRulesMatchClass, MwlLogType=MwlLogType, MwlIfAdministrativeState=MwlIfAdministrativeState, MwlL3SecurityMode=MwlL3SecurityMode, MwlEncapsulationType=MwlEncapsulationType, MwlFirewallCapability=MwlFirewallCapability, MwlRegionSettings=MwlRegionSettings, MwlNodeRelationship=MwlNodeRelationship, MwlKDDI=MwlKDDI, MwlAntenna=MwlAntenna, MwlBandSteeringMode=MwlBandSteeringMode, MwlApAuthState=MwlApAuthState, MwlL2SecurityModeBits=MwlL2SecurityModeBits, MwlQosAction=MwlQosAction, MwlIpSecDataChannelType=MwlIpSecDataChannelType, MwlEnableDisableOption=MwlEnableDisableOption, meruTextualConventions=meruTextualConventions, MwlHtProtectionModeType=MwlHtProtectionModeType, MwlStationState=MwlStationState, MwlAntennaType=MwlAntennaType, MwlVpnStatus=MwlVpnStatus, MwlRadiusMacDelimiter=MwlRadiusMacDelimiter, MwlVpnDetailStatus=MwlVpnDetailStatus, MwlBonding=MwlBonding, MwlAclEnvState=MwlAclEnvState, MwlDhGroupType=MwlDhGroupType, MwlApType=MwlApType, MwlOnOffSwitch=MwlOnOffSwitch, MwlApIpAssignmentType=MwlApIpAssignmentType, MwlCaptivePortalAuthMethod=MwlCaptivePortalAuthMethod, MwlOffHoursService=MwlOffHoursService, MwlTransmitRateAGBits=MwlTransmitRateAGBits, MwlAddressAssignmentType=MwlAddressAssignmentType, MwlFastEthernetType=MwlFastEthernetType, MwlSnmpV3PrivProtocol=MwlSnmpV3PrivProtocol, MwlLedMode=MwlLedMode, MwlEssApAdminMode=MwlEssApAdminMode, PYSNMP_MODULE_ID=meruTextualConventions, MwlCoordAlgorithm=MwlCoordAlgorithm, MwlPMKcachingBits=MwlPMKcachingBits, MwlAuthSuiteBits=MwlAuthSuiteBits, MwlNetProtocol=MwlNetProtocol, MwlOffHours=MwlOffHours, MwlAntennaLinkType=MwlAntennaLinkType, MwlChannelBandType=MwlChannelBandType, MwlAllOnSelectedSwitch=MwlAllOnSelectedSwitch, MwlClientType=MwlClientType, MwlCaptivePortalAuthState=MwlCaptivePortalAuthState, MwlProfileOwner=MwlProfileOwner, MwlCaptivePortalMode=MwlCaptivePortalMode, MwlCaptivePortalAuthenticationType=MwlCaptivePortalAuthenticationType, MwlControllerHwType=MwlControllerHwType, MwlVpnAuthenticationStatus=MwlVpnAuthenticationStatus, MwlAlarmState=MwlAlarmState, MwlIpProxyType=MwlIpProxyType, MwlTransmitRateBits=MwlTransmitRateBits, MwlRateLimitMode=MwlRateLimitMode, MwlAdmissionControl=MwlAdmissionControl, MwlEncryptionAlgorithm=MwlEncryptionAlgorithm, MwlDiscoveryOrder=MwlDiscoveryOrder, MwlBeaconCoordinationMode=MwlBeaconCoordinationMode, MwlRadiusServerSelect=MwlRadiusServerSelect, MwlBlock=MwlBlock, MwlPrivacyBit=MwlPrivacyBit, MwlAssociationState=MwlAssociationState, MwlSnmpV3AuthProtocol=MwlSnmpV3AuthProtocol, MwlAdministrativeState=MwlAdministrativeState, MwlThrdPartyIdsIps=MwlThrdPartyIdsIps, MwlVcellType=MwlVcellType, MwlApMode=MwlApMode, MwlSecurityPolicyAction=MwlSecurityPolicyAction, MwlDailyOutOfService=MwlDailyOutOfService, MwlCertFileType=MwlCertFileType, MwlUrlType=MwlUrlType, MwlServiceAction=MwlServiceAction, MwlSnmpPrivilege=MwlSnmpPrivilege, MwlWncControllerState=MwlWncControllerState, MwlApRfType=MwlApRfType, MwlApRole=MwlApRole, MwlNmsInterfaceType=MwlNmsInterfaceType, MwlApIndoorOutdoorType=MwlApIndoorOutdoorType, MwlCertificateStatus=MwlCertificateStatus, MwlFilterModeType=MwlFilterModeType, MwlTransmitRateHTBits=MwlTransmitRateHTBits, MwlIpHashAlgorithm=MwlIpHashAlgorithm, MwlStaDiagStap=MwlStaDiagStap, MwlApAssignType=MwlApAssignType, MwlNatType=MwlNatType, MwlVpnMode=MwlVpnMode, MwlApIfConfigModeType=MwlApIfConfigModeType, MwlQosProtocol=MwlQosProtocol, MwlDropPolicy=MwlDropPolicy, MwlBandType=MwlBandType, MwlCertificateFormType=MwlCertificateFormType, MwlAddressIfAssignmentType=MwlAddressIfAssignmentType, MwlBgProtectionModeType=MwlBgProtectionModeType, MwlApHwType=MwlApHwType, MwlConnectivityStatus=MwlConnectivityStatus, MwlAlarmType=MwlAlarmType, MwlSecurityLogging=MwlSecurityLogging, MwlUplinkType=MwlUplinkType, MwlAntennaSet=MwlAntennaSet, MwlTunnelTerminationModeBits=MwlTunnelTerminationModeBits, MwlL2SecurityDetailMode=MwlL2SecurityDetailMode, MwlApRegulatoryType=MwlApRegulatoryType)
