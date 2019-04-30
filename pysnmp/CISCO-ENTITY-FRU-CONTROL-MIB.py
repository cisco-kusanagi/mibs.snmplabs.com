#
# PySNMP MIB module CISCO-ENTITY-FRU-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-FRU-CONTROL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:36:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalClass, entPhysicalName, entPhysicalContainedIn, entPhysicalIndex, entPhysicalModelName, entPhysicalVendorType = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalClass", "entPhysicalName", "entPhysicalContainedIn", "entPhysicalIndex", "entPhysicalModelName", "entPhysicalVendorType")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, ModuleIdentity, Counter32, iso, NotificationType, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, IpAddress, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "ModuleIdentity", "Counter32", "iso", "NotificationType", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "IpAddress", "Counter64", "TimeTicks")
TimeStamp, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "TextualConvention", "DisplayString", "TruthValue")
ciscoEntityFRUControlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 117))
ciscoEntityFRUControlMIB.setRevisions(('2013-08-19 00:00', '2011-12-22 00:00', '2011-03-18 00:00', '2010-12-10 00:00', '2008-10-08 00:00', '2007-06-21 00:00', '2007-03-14 00:00', '2006-06-23 00:00', '2005-09-06 00:00', '2004-12-09 00:00', '2004-10-19 00:00', '2003-11-24 00:00', '2003-10-27 00:00', '2003-10-23 00:00', '2003-07-22 00:00', '2002-10-16 00:00', '2002-10-03 00:00', '2002-09-15 00:00', '2002-07-12 00:00', '2001-05-22 00:00', '2000-01-13 00:00', '1999-04-05 00:00',))
if mibBuilder.loadTexts: ciscoEntityFRUControlMIB.setLastUpdated('201308190000Z')
if mibBuilder.loadTexts: ciscoEntityFRUControlMIB.setOrganization('Cisco Systems, Inc.')
cefcMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1))
cefcFRUMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 2))
cefcMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 3))
class PowerRedundancyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notsupported", 1), ("redundant", 2), ("combined", 3), ("nonRedundant", 4), ("psRedundant", 5), ("inPwrSrcRedundant", 6), ("psRedundantSingleInput", 7))

class PowerAdminType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("on", 1), ("off", 2), ("inlineAuto", 3), ("inlineOn", 4), ("powerCycle", 5))

class PowerOperType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("offEnvOther", 1), ("on", 2), ("offAdmin", 3), ("offDenied", 4), ("offEnvPower", 5), ("offEnvTemp", 6), ("offEnvFan", 7), ("failed", 8), ("onButFanFail", 9), ("offCooling", 10), ("offConnectorRating", 11), ("onButInlinePowerFail", 12))

class FRUCurrentType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-1000000000, 1000000000)

class ModuleAdminType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("reset", 3), ("outOfServiceAdmin", 4))

class ModuleOperType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("unknown", 1), ("ok", 2), ("disabled", 3), ("okButDiagFailed", 4), ("boot", 5), ("selfTest", 6), ("failed", 7), ("missing", 8), ("mismatchWithParent", 9), ("mismatchConfig", 10), ("diagFailed", 11), ("dormant", 12), ("outOfServiceAdmin", 13), ("outOfServiceEnvTemp", 14), ("poweredDown", 15), ("poweredUp", 16), ("powerDenied", 17), ("powerCycled", 18), ("okButPowerOverWarning", 19), ("okButPowerOverCritical", 20), ("syncInProgress", 21), ("upgrading", 22), ("okButAuthFailed", 23), ("mdr", 24), ("fwMismatchFound", 25), ("fwDownloadSuccess", 26), ("fwDownloadFailure", 27))

class ModuleResetReasonType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("unknown", 1), ("powerUp", 2), ("parityError", 3), ("clearConfigReset", 4), ("manualReset", 5), ("watchDogTimeoutReset", 6), ("resourceOverflowReset", 7), ("missingTaskReset", 8), ("lowVoltageReset", 9), ("controllerReset", 10), ("systemReset", 11), ("switchoverReset", 12), ("upgradeReset", 13), ("downgradeReset", 14), ("cacheErrorReset", 15), ("deviceDriverReset", 16), ("softwareExceptionReset", 17), ("restoreConfigReset", 18), ("abortRevReset", 19), ("burnBootReset", 20), ("standbyCdHealthierReset", 21), ("nonNativeConfigClearReset", 22), ("memoryProtectionErrorReset", 23))

class FRUTimeSeconds(TextualConvention, Unsigned32):
    status = 'current'

class FRUCoolingUnit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cfm", 1), ("watts", 2))

cefcFRUPower = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1))
cefcModule = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2))
cefcMIBNotificationEnables = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 3))
cefcFRUFan = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4))
cefcPhysical = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5))
cefcPowerCapacity = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6))
cefcCooling = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7))
cefcConnector = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8))
cefcFRUPowerSupplyGroupTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1), )
if mibBuilder.loadTexts: cefcFRUPowerSupplyGroupTable.setStatus('current')
cefcFRUPowerSupplyGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFRUPowerSupplyGroupEntry.setStatus('current')
cefcPowerRedundancyMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 1), PowerRedundancyType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcPowerRedundancyMode.setStatus('current')
cefcPowerUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPowerUnits.setStatus('current')
cefcTotalAvailableCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 3), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcTotalAvailableCurrent.setStatus('current')
cefcTotalDrawnCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 4), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcTotalDrawnCurrent.setStatus('current')
cefcPowerRedundancyOperMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 5), PowerRedundancyType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPowerRedundancyOperMode.setStatus('current')
cefcPowerNonRedundantReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplicable", 1), ("unknown", 2), ("singleSupply", 3), ("mismatchedSupplies", 4), ("supplyError", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPowerNonRedundantReason.setStatus('current')
cefcTotalDrawnInlineCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 7), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcTotalDrawnInlineCurrent.setStatus('current')
cefcFRUPowerStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2), )
if mibBuilder.loadTexts: cefcFRUPowerStatusTable.setStatus('current')
cefcFRUPowerStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFRUPowerStatusEntry.setStatus('current')
cefcFRUPowerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 1), PowerAdminType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcFRUPowerAdminStatus.setStatus('current')
cefcFRUPowerOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 2), PowerOperType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFRUPowerOperStatus.setStatus('current')
cefcFRUCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 3), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFRUCurrent.setStatus('current')
cefcFRUPowerCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 4), Bits().clone(namedValues=NamedValues(("realTimeCurrent", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFRUPowerCapability.setStatus('current')
cefcFRURealTimeCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 5), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFRURealTimeCurrent.setStatus('current')
cefcMaxDefaultInLinePower = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12500)).clone(12500)).setUnits('miliwatts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcMaxDefaultInLinePower.setStatus('deprecated')
cefcFRUPowerSupplyValueTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4), )
if mibBuilder.loadTexts: cefcFRUPowerSupplyValueTable.setStatus('current')
cefcFRUPowerSupplyValueEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFRUPowerSupplyValueEntry.setStatus('current')
cefcFRUTotalSystemCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 1), FRUCurrentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcFRUTotalSystemCurrent.setStatus('current')
cefcFRUDrawnSystemCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 2), FRUCurrentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcFRUDrawnSystemCurrent.setStatus('current')
cefcFRUTotalInlineCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 3), FRUCurrentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcFRUTotalInlineCurrent.setStatus('current')
cefcFRUDrawnInlineCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 4), FRUCurrentType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcFRUDrawnInlineCurrent.setStatus('current')
cefcMaxDefaultHighInLinePower = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 5), Unsigned32()).setUnits('miliwatts').setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcMaxDefaultHighInLinePower.setStatus('current')
cefcModuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1), )
if mibBuilder.loadTexts: cefcModuleTable.setStatus('current')
cefcModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcModuleEntry.setStatus('current')
cefcModuleAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 1), ModuleAdminType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcModuleAdminStatus.setStatus('current')
cefcModuleOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 2), ModuleOperType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleOperStatus.setStatus('current')
cefcModuleResetReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 3), ModuleResetReasonType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleResetReason.setStatus('current')
cefcModuleStatusLastChangeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleStatusLastChangeTime.setStatus('current')
cefcModuleLastClearConfigTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleLastClearConfigTime.setStatus('current')
cefcModuleResetReasonDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleResetReasonDescription.setStatus('current')
cefcModuleStateChangeReasonDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleStateChangeReasonDescr.setStatus('current')
cefcModuleUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 8), FRUTimeSeconds()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleUpTime.setStatus('current')
cefcIntelliModuleTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2), )
if mibBuilder.loadTexts: cefcIntelliModuleTable.setStatus('current')
cefcIntelliModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcIntelliModuleEntry.setStatus('current')
cefcIntelliModuleIPAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2, 1, 1), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcIntelliModuleIPAddrType.setStatus('current')
cefcIntelliModuleIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcIntelliModuleIPAddr.setStatus('current')
cefcModuleLocalSwitchingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 3), )
if mibBuilder.loadTexts: cefcModuleLocalSwitchingTable.setStatus('current')
cefcModuleLocalSwitchingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcModuleLocalSwitchingEntry.setStatus('current')
cefcModuleLocalSwitchingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcModuleLocalSwitchingMode.setStatus('current')
cefcFanTrayStatusTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 1), )
if mibBuilder.loadTexts: cefcFanTrayStatusTable.setStatus('current')
cefcFanTrayStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFanTrayStatusEntry.setStatus('current')
cefcFanTrayOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("up", 2), ("down", 3), ("warning", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanTrayOperStatus.setStatus('current')
cefcPhysicalTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5, 1), )
if mibBuilder.loadTexts: cefcPhysicalTable.setStatus('current')
cefcPhysicalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcPhysicalEntry.setStatus('current')
cefcPhysicalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("supported", 2), ("unsupported", 3), ("incompatible", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPhysicalStatus.setStatus('current')
cefcPowerSupplyInputTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1), )
if mibBuilder.loadTexts: cefcPowerSupplyInputTable.setStatus('current')
cefcPowerSupplyInputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerSupplyInputIndex"))
if mibBuilder.loadTexts: cefcPowerSupplyInputEntry.setStatus('current')
cefcPowerSupplyInputIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cefcPowerSupplyInputIndex.setStatus('current')
cefcPowerSupplyInputType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("acLow", 2), ("acHigh", 3), ("dcLow", 4), ("dcHigh", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPowerSupplyInputType.setStatus('current')
cefcPowerSupplyOutputTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2), )
if mibBuilder.loadTexts: cefcPowerSupplyOutputTable.setStatus('current')
cefcPowerSupplyOutputEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeIndex"))
if mibBuilder.loadTexts: cefcPowerSupplyOutputEntry.setStatus('current')
cefcPSOutputModeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: cefcPSOutputModeIndex.setStatus('current')
cefcPSOutputModeCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1, 2), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPSOutputModeCurrent.setStatus('current')
cefcPSOutputModeInOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcPSOutputModeInOperation.setStatus('current')
cefcChassisCoolingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1), )
if mibBuilder.loadTexts: cefcChassisCoolingTable.setStatus('current')
cefcChassisCoolingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcChassisCoolingEntry.setStatus('current')
cefcChassisPerSlotCoolingCap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcChassisPerSlotCoolingCap.setStatus('current')
cefcChassisPerSlotCoolingUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1, 1, 2), FRUCoolingUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcChassisPerSlotCoolingUnit.setStatus('current')
cefcFanCoolingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2), )
if mibBuilder.loadTexts: cefcFanCoolingTable.setStatus('current')
cefcFanCoolingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcFanCoolingEntry.setStatus('current')
cefcFanCoolingCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapacity.setStatus('current')
cefcFanCoolingCapacityUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2, 1, 2), FRUCoolingUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapacityUnit.setStatus('current')
cefcModuleCoolingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3), )
if mibBuilder.loadTexts: cefcModuleCoolingTable.setStatus('current')
cefcModuleCoolingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcModuleCoolingEntry.setStatus('current')
cefcModuleCooling = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleCooling.setStatus('current')
cefcModuleCoolingUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3, 1, 2), FRUCoolingUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModuleCoolingUnit.setStatus('current')
cefcFanCoolingCapTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4), )
if mibBuilder.loadTexts: cefcFanCoolingCapTable.setStatus('current')
cefcFanCoolingCapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapIndex"))
if mibBuilder.loadTexts: cefcFanCoolingCapEntry.setStatus('current')
cefcFanCoolingCapIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: cefcFanCoolingCapIndex.setStatus('current')
cefcFanCoolingCapModeDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapModeDescr.setStatus('current')
cefcFanCoolingCapCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapCapacity.setStatus('current')
cefcFanCoolingCapCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 4), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapCurrent.setStatus('current')
cefcFanCoolingCapCapacityUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 5), FRUCoolingUnit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcFanCoolingCapCapacityUnit.setStatus('current')
cefcConnectorRatingTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 1), )
if mibBuilder.loadTexts: cefcConnectorRatingTable.setStatus('current')
cefcConnectorRatingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcConnectorRatingEntry.setStatus('current')
cefcConnectorRating = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 1, 1, 1), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcConnectorRating.setStatus('current')
cefcModulePowerConsumptionTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 2), )
if mibBuilder.loadTexts: cefcModulePowerConsumptionTable.setStatus('current')
cefcModulePowerConsumptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: cefcModulePowerConsumptionEntry.setStatus('current')
cefcModulePowerConsumption = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 2, 1, 1), FRUCurrentType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cefcModulePowerConsumption.setStatus('current')
cefcMIBEnableStatusNotification = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 3, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcMIBEnableStatusNotification.setStatus('current')
cefcEnablePSOutputChangeNotif = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 3, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cefcEnablePSOutputChangeNotif.setStatus('current')
cefcMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0))
cefcModuleStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 1)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleOperStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStatusLastChangeTime"))
if mibBuilder.loadTexts: cefcModuleStatusChange.setStatus('current')
cefcPowerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 2)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerOperStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerAdminStatus"))
if mibBuilder.loadTexts: cefcPowerStatusChange.setStatus('current')
cefcFRUInserted = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 3)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"))
if mibBuilder.loadTexts: cefcFRUInserted.setStatus('current')
cefcFRURemoved = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 4)).setObjects(("ENTITY-MIB", "entPhysicalContainedIn"))
if mibBuilder.loadTexts: cefcFRURemoved.setStatus('current')
cefcUnrecognizedFRU = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 5)).setObjects(("ENTITY-MIB", "entPhysicalClass"), ("ENTITY-MIB", "entPhysicalVendorType"), ("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPhysicalStatus"))
if mibBuilder.loadTexts: cefcUnrecognizedFRU.setStatus('current')
cefcFanTrayStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 6)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanTrayOperStatus"))
if mibBuilder.loadTexts: cefcFanTrayStatusChange.setStatus('current')
cefcPowerSupplyOutputChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 7)).setObjects(("ENTITY-MIB", "entPhysicalName"), ("ENTITY-MIB", "entPhysicalModelName"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeCurrent"))
if mibBuilder.loadTexts: cefcPowerSupplyOutputChange.setStatus('current')
cefcMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1))
cefcMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2))
cefcMIBPowerCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 1)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance = cefcMIBPowerCompliance.setStatus('obsolete')
cefcMIBPowerCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 2)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance2 = cefcMIBPowerCompliance2.setStatus('deprecated')
cefcMIBPowerCompliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 3)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance3 = cefcMIBPowerCompliance3.setStatus('deprecated')
cefcMIBPowerCompliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 4)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance4 = cefcMIBPowerCompliance4.setStatus('deprecated')
cefcMIBPowerCompliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 5)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance5 = cefcMIBPowerCompliance5.setStatus('deprecated')
cefcMIBPowerCompliance6 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 6)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerOperModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleExtGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance6 = cefcMIBPowerCompliance6.setStatus('current')
cefcMIBPowerCompliance7 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 7)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerOperModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleExtGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerCapacityGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcCoolingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcConnectorRatingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance7 = cefcMIBPowerCompliance7.setStatus('deprecated')
cefcMIBPowerCompliance8 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 8)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerOperModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleExtGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerCapacityGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcCoolingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcConnectorRatingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup3"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerCurrentGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerRedundancyInfoGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance8 = cefcMIBPowerCompliance8.setStatus('deprecated')
cefcMIBPowerCompliance9 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 9)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUControlGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerControlGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleGroupRev1"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerFRUValueGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBFanTrayStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPhysicalGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerOperModeGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleExtGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerCapacityGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcConnectorRatingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBNotificationEnablesGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMgmtNotificationsGroup3"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBInLinePowerCurrentGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBPowerRedundancyInfoGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBModuleLocalSwitchingGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerRealTimeStatusGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerCapabilityGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUCoolingUnitGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUFanCoolingUnitGroup"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcCoolingGroup2"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerCompliance9 = cefcMIBPowerCompliance9.setStatus('current')
cefcMIBPowerModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 1)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerRedundancyMode"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerUnits"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcTotalAvailableCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcTotalDrawnCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerModeGroup = cefcMIBPowerModeGroup.setStatus('current')
cefcMIBPowerFRUControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 2)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerAdminStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerOperStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerFRUControlGroup = cefcMIBPowerFRUControlGroup.setStatus('current')
cefcMIBModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 3)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleAdminStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleOperStatus"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleResetReason"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStatusLastChangeTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBModuleGroup = cefcMIBModuleGroup.setStatus('current')
cefcMIBInLinePowerControlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 4)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMaxDefaultInLinePower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBInLinePowerControlGroup = cefcMIBInLinePowerControlGroup.setStatus('deprecated')
cefcMIBNotificationEnablesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 5)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBEnableStatusNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBNotificationEnablesGroup = cefcMIBNotificationEnablesGroup.setStatus('current')
cefcMgmtNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 6)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStatusChange"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerStatusChange"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUInserted"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRURemoved"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMgmtNotificationsGroup = cefcMgmtNotificationsGroup.setStatus('current')
cefcModuleGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 7)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleLastClearConfigTime"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleResetReasonDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcModuleGroupRev1 = cefcModuleGroupRev1.setStatus('current')
cefcMIBPowerFRUValueGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 8)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUTotalSystemCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUDrawnSystemCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUTotalInlineCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUDrawnInlineCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerFRUValueGroup = cefcMIBPowerFRUValueGroup.setStatus('current')
cefcMIBFanTrayStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 9)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanTrayOperStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBFanTrayStatusGroup = cefcMIBFanTrayStatusGroup.setStatus('current')
cefcMIBPhysicalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 10)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPhysicalStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPhysicalGroup = cefcMIBPhysicalGroup.setStatus('current')
cefcMgmtNotificationsGroup2 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 11)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcUnrecognizedFRU"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanTrayStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMgmtNotificationsGroup2 = cefcMgmtNotificationsGroup2.setStatus('current')
cefcMIBPowerOperModeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 12)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerRedundancyOperMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerOperModeGroup = cefcMIBPowerOperModeGroup.setStatus('current')
cefcMIBInLinePowerControlGroupRev1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 13)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMaxDefaultHighInLinePower"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBInLinePowerControlGroupRev1 = cefcMIBInLinePowerControlGroupRev1.setStatus('current')
cefcModuleExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 14)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStateChangeReasonDescr"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleUpTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcModuleExtGroup = cefcModuleExtGroup.setStatus('current')
cefcIntelliModuleGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 15)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleIPAddrType"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleIPAddr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcIntelliModuleGroup = cefcIntelliModuleGroup.setStatus('current')
cefcPowerCapacityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 16)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerSupplyInputType"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeCurrent"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeInOperation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcPowerCapacityGroup = cefcPowerCapacityGroup.setStatus('current')
cefcCoolingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 17)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcChassisPerSlotCoolingCap"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapacity"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleCooling"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcCoolingGroup = cefcCoolingGroup.setStatus('deprecated')
cefcConnectorRatingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 18)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcConnectorRating"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModulePowerConsumption"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcConnectorRatingGroup = cefcConnectorRatingGroup.setStatus('current')
cefcMIBNotificationEnablesGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 19)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcEnablePSOutputChangeNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBNotificationEnablesGroup2 = cefcMIBNotificationEnablesGroup2.setStatus('current')
cefcMgmtNotificationsGroup3 = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 20)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerSupplyOutputChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMgmtNotificationsGroup3 = cefcMgmtNotificationsGroup3.setStatus('current')
cefcMIBInLinePowerCurrentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 21)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcTotalDrawnInlineCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBInLinePowerCurrentGroup = cefcMIBInLinePowerCurrentGroup.setStatus('current')
cefcMIBPowerRedundancyInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 22)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerNonRedundantReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBPowerRedundancyInfoGroup = cefcMIBPowerRedundancyInfoGroup.setStatus('current')
cefcFanCoolingCapGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 23)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapModeDescr"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapCapacity"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFanCoolingCapGroup = cefcFanCoolingCapGroup.setStatus('current')
cefcMIBModuleLocalSwitchingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 24)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleLocalSwitchingMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcMIBModuleLocalSwitchingGroup = cefcMIBModuleLocalSwitchingGroup.setStatus('current')
cefcFRUPowerRealTimeStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 25)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRURealTimeCurrent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFRUPowerRealTimeStatusGroup = cefcFRUPowerRealTimeStatusGroup.setStatus('current')
cefcFRUPowerCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 26)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFRUPowerCapabilityGroup = cefcFRUPowerCapabilityGroup.setStatus('current')
cefcFRUCoolingUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 27)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcChassisPerSlotCoolingUnit"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleCoolingUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFRUCoolingUnitGroup = cefcFRUCoolingUnitGroup.setStatus('current')
cefcFRUFanCoolingUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 28)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapacityUnit"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapCapacityUnit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFRUFanCoolingUnitGroup = cefcFRUFanCoolingUnitGroup.setStatus('current')
cefcCoolingGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 29)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcChassisPerSlotCoolingCap"), ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleCooling"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcCoolingGroup2 = cefcCoolingGroup2.setStatus('current')
cefcFanCoolingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 30)).setObjects(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapacity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cefcFanCoolingGroup = cefcFanCoolingGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-FRU-CONTROL-MIB", PowerRedundancyType=PowerRedundancyType, cefcPowerStatusChange=cefcPowerStatusChange, cefcFRUPowerRealTimeStatusGroup=cefcFRUPowerRealTimeStatusGroup, cefcMIBFanTrayStatusGroup=cefcMIBFanTrayStatusGroup, cefcFRUPowerCapabilityGroup=cefcFRUPowerCapabilityGroup, cefcModuleEntry=cefcModuleEntry, cefcChassisCoolingEntry=cefcChassisCoolingEntry, cefcMIBPowerCompliance9=cefcMIBPowerCompliance9, cefcFRUInserted=cefcFRUInserted, cefcFanCoolingCapGroup=cefcFanCoolingCapGroup, cefcTotalAvailableCurrent=cefcTotalAvailableCurrent, cefcModuleOperStatus=cefcModuleOperStatus, cefcFRUFanCoolingUnitGroup=cefcFRUFanCoolingUnitGroup, cefcPowerNonRedundantReason=cefcPowerNonRedundantReason, PYSNMP_MODULE_ID=ciscoEntityFRUControlMIB, cefcFRUPowerStatusEntry=cefcFRUPowerStatusEntry, cefcEnablePSOutputChangeNotif=cefcEnablePSOutputChangeNotif, cefcMIBNotifications=cefcMIBNotifications, cefcConnectorRatingGroup=cefcConnectorRatingGroup, cefcModulePowerConsumptionEntry=cefcModulePowerConsumptionEntry, cefcMIBNotificationEnablesGroup=cefcMIBNotificationEnablesGroup, PowerAdminType=PowerAdminType, cefcFRUCurrent=cefcFRUCurrent, cefcMIBPowerCompliance7=cefcMIBPowerCompliance7, cefcMIBNotificationEnables=cefcMIBNotificationEnables, cefcPowerRedundancyMode=cefcPowerRedundancyMode, cefcFanCoolingGroup=cefcFanCoolingGroup, cefcMIBPowerCompliance4=cefcMIBPowerCompliance4, cefcMIBCompliances=cefcMIBCompliances, cefcMgmtNotificationsGroup2=cefcMgmtNotificationsGroup2, cefcPSOutputModeInOperation=cefcPSOutputModeInOperation, cefcConnector=cefcConnector, cefcPhysicalStatus=cefcPhysicalStatus, cefcMIBPowerCompliance5=cefcMIBPowerCompliance5, cefcMgmtNotificationsGroup=cefcMgmtNotificationsGroup, cefcPSOutputModeIndex=cefcPSOutputModeIndex, cefcMIBConformance=cefcMIBConformance, cefcIntelliModuleEntry=cefcIntelliModuleEntry, cefcFanTrayStatusChange=cefcFanTrayStatusChange, cefcPSOutputModeCurrent=cefcPSOutputModeCurrent, cefcFanCoolingCapacity=cefcFanCoolingCapacity, cefcMgmtNotificationsGroup3=cefcMgmtNotificationsGroup3, cefcModuleUpTime=cefcModuleUpTime, cefcFRURealTimeCurrent=cefcFRURealTimeCurrent, cefcModuleResetReason=cefcModuleResetReason, cefcMIBPowerFRUControlGroup=cefcMIBPowerFRUControlGroup, cefcFanTrayStatusEntry=cefcFanTrayStatusEntry, cefcChassisCoolingTable=cefcChassisCoolingTable, cefcFanCoolingCapTable=cefcFanCoolingCapTable, cefcMIBModuleGroup=cefcMIBModuleGroup, cefcMIBNotificationEnablesGroup2=cefcMIBNotificationEnablesGroup2, cefcPowerCapacityGroup=cefcPowerCapacityGroup, PowerOperType=PowerOperType, cefcModuleResetReasonDescription=cefcModuleResetReasonDescription, cefcPowerSupplyInputIndex=cefcPowerSupplyInputIndex, cefcUnrecognizedFRU=cefcUnrecognizedFRU, cefcIntelliModuleGroup=cefcIntelliModuleGroup, cefcMIBPowerOperModeGroup=cefcMIBPowerOperModeGroup, cefcFRUTotalInlineCurrent=cefcFRUTotalInlineCurrent, cefcModuleExtGroup=cefcModuleExtGroup, cefcMIBInLinePowerCurrentGroup=cefcMIBInLinePowerCurrentGroup, ModuleOperType=ModuleOperType, cefcMIBInLinePowerControlGroup=cefcMIBInLinePowerControlGroup, cefcModuleStatusLastChangeTime=cefcModuleStatusLastChangeTime, cefcFanTrayStatusTable=cefcFanTrayStatusTable, cefcFRUPowerSupplyValueEntry=cefcFRUPowerSupplyValueEntry, cefcFanCoolingCapModeDescr=cefcFanCoolingCapModeDescr, cefcPowerRedundancyOperMode=cefcPowerRedundancyOperMode, cefcMaxDefaultInLinePower=cefcMaxDefaultInLinePower, cefcMIBPhysicalGroup=cefcMIBPhysicalGroup, cefcFRUPowerOperStatus=cefcFRUPowerOperStatus, cefcFRUPowerSupplyGroupTable=cefcFRUPowerSupplyGroupTable, cefcFRUPowerCapability=cefcFRUPowerCapability, cefcModulePowerConsumption=cefcModulePowerConsumption, FRUCoolingUnit=FRUCoolingUnit, cefcModule=cefcModule, cefcFRUPower=cefcFRUPower, cefcMIBObjects=cefcMIBObjects, ModuleResetReasonType=ModuleResetReasonType, cefcPowerSupplyOutputEntry=cefcPowerSupplyOutputEntry, cefcPowerSupplyInputEntry=cefcPowerSupplyInputEntry, cefcModuleCoolingTable=cefcModuleCoolingTable, cefcCooling=cefcCooling, cefcModuleLocalSwitchingEntry=cefcModuleLocalSwitchingEntry, cefcMIBPowerRedundancyInfoGroup=cefcMIBPowerRedundancyInfoGroup, cefcModuleCoolingUnit=cefcModuleCoolingUnit, cefcIntelliModuleIPAddrType=cefcIntelliModuleIPAddrType, cefcFRUDrawnInlineCurrent=cefcFRUDrawnInlineCurrent, cefcModuleCooling=cefcModuleCooling, cefcModuleAdminStatus=cefcModuleAdminStatus, cefcMIBGroups=cefcMIBGroups, cefcPowerSupplyInputType=cefcPowerSupplyInputType, cefcFRUMIBNotificationPrefix=cefcFRUMIBNotificationPrefix, cefcPowerSupplyInputTable=cefcPowerSupplyInputTable, cefcFanCoolingTable=cefcFanCoolingTable, cefcConnectorRatingEntry=cefcConnectorRatingEntry, cefcMIBPowerFRUValueGroup=cefcMIBPowerFRUValueGroup, cefcCoolingGroup=cefcCoolingGroup, cefcFanCoolingCapEntry=cefcFanCoolingCapEntry, ciscoEntityFRUControlMIB=ciscoEntityFRUControlMIB, cefcMIBPowerCompliance3=cefcMIBPowerCompliance3, cefcModulePowerConsumptionTable=cefcModulePowerConsumptionTable, cefcModuleLastClearConfigTime=cefcModuleLastClearConfigTime, cefcPhysicalEntry=cefcPhysicalEntry, cefcFRURemoved=cefcFRURemoved, cefcFRUPowerStatusTable=cefcFRUPowerStatusTable, cefcMIBPowerCompliance6=cefcMIBPowerCompliance6, cefcPowerSupplyOutputChange=cefcPowerSupplyOutputChange, cefcMIBPowerCompliance=cefcMIBPowerCompliance, cefcPhysicalTable=cefcPhysicalTable, cefcFanCoolingCapCapacityUnit=cefcFanCoolingCapCapacityUnit, cefcMIBEnableStatusNotification=cefcMIBEnableStatusNotification, cefcFRUPowerSupplyGroupEntry=cefcFRUPowerSupplyGroupEntry, cefcModuleLocalSwitchingMode=cefcModuleLocalSwitchingMode, cefcPowerCapacity=cefcPowerCapacity, cefcMIBModuleLocalSwitchingGroup=cefcMIBModuleLocalSwitchingGroup, cefcIntelliModuleIPAddr=cefcIntelliModuleIPAddr, cefcConnectorRating=cefcConnectorRating, cefcPowerSupplyOutputTable=cefcPowerSupplyOutputTable, cefcCoolingGroup2=cefcCoolingGroup2, cefcFRUPowerSupplyValueTable=cefcFRUPowerSupplyValueTable, cefcFRUFan=cefcFRUFan, cefcIntelliModuleTable=cefcIntelliModuleTable, cefcModuleLocalSwitchingTable=cefcModuleLocalSwitchingTable, cefcFRUPowerAdminStatus=cefcFRUPowerAdminStatus, cefcChassisPerSlotCoolingCap=cefcChassisPerSlotCoolingCap, cefcModuleTable=cefcModuleTable, cefcMIBPowerCompliance8=cefcMIBPowerCompliance8, cefcFanTrayOperStatus=cefcFanTrayOperStatus, cefcChassisPerSlotCoolingUnit=cefcChassisPerSlotCoolingUnit, cefcModuleGroupRev1=cefcModuleGroupRev1, cefcConnectorRatingTable=cefcConnectorRatingTable, cefcMIBInLinePowerControlGroupRev1=cefcMIBInLinePowerControlGroupRev1, cefcTotalDrawnInlineCurrent=cefcTotalDrawnInlineCurrent, cefcPowerUnits=cefcPowerUnits, cefcModuleStateChangeReasonDescr=cefcModuleStateChangeReasonDescr, cefcFanCoolingCapCapacity=cefcFanCoolingCapCapacity, ModuleAdminType=ModuleAdminType, cefcFanCoolingCapIndex=cefcFanCoolingCapIndex, cefcFanCoolingCapacityUnit=cefcFanCoolingCapacityUnit, FRUTimeSeconds=FRUTimeSeconds, cefcFRUTotalSystemCurrent=cefcFRUTotalSystemCurrent, cefcPhysical=cefcPhysical, cefcModuleStatusChange=cefcModuleStatusChange, cefcMIBPowerModeGroup=cefcMIBPowerModeGroup, cefcFRUCoolingUnitGroup=cefcFRUCoolingUnitGroup, cefcMaxDefaultHighInLinePower=cefcMaxDefaultHighInLinePower, cefcFanCoolingCapCurrent=cefcFanCoolingCapCurrent, FRUCurrentType=FRUCurrentType, cefcFRUDrawnSystemCurrent=cefcFRUDrawnSystemCurrent, cefcTotalDrawnCurrent=cefcTotalDrawnCurrent, cefcMIBPowerCompliance2=cefcMIBPowerCompliance2, cefcModuleCoolingEntry=cefcModuleCoolingEntry, cefcFanCoolingEntry=cefcFanCoolingEntry)
