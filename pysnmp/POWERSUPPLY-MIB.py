#
# PySNMP MIB module POWERSUPPLY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/POWERSUPPLY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:32:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Bits, IpAddress, Counter64, Counter32, NotificationType, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, MibIdentifier, TimeTicks, Unsigned32, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "IpAddress", "Counter64", "Counter32", "NotificationType", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "MibIdentifier", "TimeTicks", "Unsigned32", "Integer32", "Gauge32")
TruthValue, TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "MacAddress", "DisplayString")
hpicfPsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55))
hpicfPsMIB.setRevisions(('2013-08-20 00:00', '2013-06-13 00:00', '2013-03-07 10:00', '2008-08-27 10:00',))
if mibBuilder.loadTexts: hpicfPsMIB.setLastUpdated('201308200000Z')
if mibBuilder.loadTexts: hpicfPsMIB.setOrganization('HP Networking')
hpicfEntityPs = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1))
class HpicfDcPsIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'

class HpicfDcPsState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("psNotPresent", 1), ("psNotPlugged", 2), ("psPowered", 3), ("psFailed", 4), ("psPermFailure", 5), ("psMax", 6), ("psAuxFailure", 7), ("psNotPowered", 8), ("psAuxNotPowered", 9))

class HpicfXpsConnectionStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("notConnected", 0), ("unavailable", 1), ("available", 2), ("active", 3), ("mismatch", 4), ("notReady", 5), ("overCurrent", 6), ("cannotPower", 7), ("autoDisabled", 8))

class HpicfXpsZoneStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notConnected", 1), ("notReady", 2), ("faulted", 3), ("powered", 4), ("inReset", 5))

hpicfPsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1), )
if mibBuilder.loadTexts: hpicfPsTable.setStatus('current')
hpicfPsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1), ).setIndexNames((0, "POWERSUPPLY-MIB", "hpicfPsBayNum"))
if mibBuilder.loadTexts: hpicfPsEntry.setStatus('current')
hpicfPsBayNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 1), HpicfDcPsIndex())
if mibBuilder.loadTexts: hpicfPsBayNum.setStatus('current')
hpicfPsState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 2), HpicfDcPsState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPsState.setStatus('current')
hpicfPsFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPsFailures.setStatus('current')
hpicfPsTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPsTemp.setStatus('current')
hpicfPsVoltageInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPsVoltageInfo.setStatus('current')
hpicfPsWattageCur = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPsWattageCur.setStatus('current')
hpicfPsWattageMax = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPsWattageMax.setStatus('current')
hpicfPsLastCall = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPsLastCall.setStatus('current')
hpicfPsModel = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfPsModel.setStatus('current')
hpicfXpsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2), )
if mibBuilder.loadTexts: hpicfXpsTable.setStatus('current')
hpicfXpsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "POWERSUPPLY-MIB", "hpicfXpsConnectingPort"))
if mibBuilder.loadTexts: hpicfXpsEntry.setStatus('current')
hpicfXpsConnectingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: hpicfXpsConnectingPort.setStatus('current')
hpicfXpsPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsPortOperStatus.setStatus('current')
hpicfXpsSwitchSerialNo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsSwitchSerialNo.setStatus('current')
hpicfXpsConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 4), HpicfXpsConnectionStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsConnectionState.setStatus('current')
hpicfXpsSysName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsSysName.setStatus('current')
hpicfXpsMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsMACAddress.setStatus('current')
hpicfXpsSwitchOSVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsSwitchOSVersion.setStatus('current')
hpicfXpsSwitchIpsVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 8), Unsigned32()).setUnits('Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsSwitchIpsVoltage.setStatus('current')
hpicfXpsSwitchIpsWattage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 9), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsSwitchIpsWattage.setStatus('current')
hpicfXpsPower = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 10), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsPower.setStatus('current')
hpicfXpsSupportedCableVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsSupportedCableVersion.setStatus('current')
hpicfXpsSupportedZoneVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsSupportedZoneVersion.setStatus('current')
hpicfXpsSwitchModType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsSwitchModType.setStatus('current')
hpicfXpsSwitchConfigTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3), )
if mibBuilder.loadTexts: hpicfXpsSwitchConfigTable.setStatus('current')
hpicfXpsSwitchConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfXpsSwitchConfigEntry.setStatus('current')
hpicfXpsSwitchAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfXpsSwitchAdminStatus.setStatus('current')
hpicfXpsSwitchAutoRecovery = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2))).clone('yes')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfXpsSwitchAutoRecovery.setStatus('current')
hpicfXpsAllowPortsSupported = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(2, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfXpsAllowPortsSupported.setStatus('current')
hpicfXpsReset = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noReset", 1), ("factoryReset", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfXpsReset.setStatus('current')
hpicfXpsType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsType.setStatus('current')
hpicfXpsSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsSerialNum.setStatus('current')
hpicfXpsModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsModuleName.setStatus('current')
hpicfXpsPowerShareReqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("inProgress", 2), ("success", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsPowerShareReqStatus.setStatus('current')
hpicfXpsResetReqStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("inProgress", 2), ("success", 3), ("failed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsResetReqStatus.setStatus('current')
hpicfXpsZoneTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4), )
if mibBuilder.loadTexts: hpicfXpsZoneTable.setStatus('current')
hpicfXpsZoneEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: hpicfXpsZoneEntry.setStatus('current')
hpicfXpsZoneNo = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsZoneNo.setStatus('current')
hpicfXpsZoneState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 2), HpicfXpsZoneStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsZoneState.setStatus('current')
hpicfXpsZonePowerShareMap = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfXpsZonePowerShareMap.setStatus('current')
hpicfXpsZoneVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 4), Unsigned32()).setUnits('Volts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsZoneVoltage.setStatus('current')
hpicfXpsZoneWattage = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 5), Unsigned32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsZoneWattage.setStatus('current')
hpicfXpsPSURev = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsPSURev.setStatus('current')
hpicfXpsPSUModule = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsPSUModule.setStatus('current')
hpicfXpsZonePowerShareForce = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 8), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfXpsZonePowerShareForce.setStatus('current')
hpicfXpsZoneRecordVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 1, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfXpsZoneRecordVersion.setStatus('current')
hpicfPsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2))
hpicfPsCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1))
hpicfPsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2))
hpicfDcPsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1, 1)).setObjects(("POWERSUPPLY-MIB", "hpicfPsGroup"), ("POWERSUPPLY-MIB", "hpicfPsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDcPsCompliance = hpicfDcPsCompliance.setStatus('deprecated')
hpicfXpsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1, 2)).setObjects(("POWERSUPPLY-MIB", "hpicfXpsGroup"), ("POWERSUPPLY-MIB", "hpicfXpsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfXpsCompliance = hpicfXpsCompliance.setStatus('current')
hpicfXpsZoneCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1, 3)).setObjects(("POWERSUPPLY-MIB", "hpicfXpsZoneGroup"), ("POWERSUPPLY-MIB", "hpicfXpsZoneGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfXpsZoneCompliance = hpicfXpsZoneCompliance.setStatus('current')
hpicfDcPsCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 1, 4)).setObjects(("POWERSUPPLY-MIB", "hpicfPsGroup1"), ("POWERSUPPLY-MIB", "hpicfPsGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDcPsCompliance1 = hpicfDcPsCompliance1.setStatus('current')
hpicfPsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2, 1)).setObjects(("POWERSUPPLY-MIB", "hpicfPsState"), ("POWERSUPPLY-MIB", "hpicfPsFailures"), ("POWERSUPPLY-MIB", "hpicfPsTemp"), ("POWERSUPPLY-MIB", "hpicfPsVoltageInfo"), ("POWERSUPPLY-MIB", "hpicfPsWattageCur"), ("POWERSUPPLY-MIB", "hpicfPsWattageMax"), ("POWERSUPPLY-MIB", "hpicfPsLastCall"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPsGroup = hpicfPsGroup.setStatus('deprecated')
hpicfXpsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2, 2)).setObjects(("POWERSUPPLY-MIB", "hpicfXpsPortOperStatus"), ("POWERSUPPLY-MIB", "hpicfXpsSwitchSerialNo"), ("POWERSUPPLY-MIB", "hpicfXpsConnectionState"), ("POWERSUPPLY-MIB", "hpicfXpsSysName"), ("POWERSUPPLY-MIB", "hpicfXpsMACAddress"), ("POWERSUPPLY-MIB", "hpicfXpsSwitchOSVersion"), ("POWERSUPPLY-MIB", "hpicfXpsSwitchIpsVoltage"), ("POWERSUPPLY-MIB", "hpicfXpsSwitchIpsWattage"), ("POWERSUPPLY-MIB", "hpicfXpsPower"), ("POWERSUPPLY-MIB", "hpicfXpsSwitchAdminStatus"), ("POWERSUPPLY-MIB", "hpicfXpsSwitchAutoRecovery"), ("POWERSUPPLY-MIB", "hpicfXpsAllowPortsSupported"), ("POWERSUPPLY-MIB", "hpicfXpsReset"), ("POWERSUPPLY-MIB", "hpicfXpsType"), ("POWERSUPPLY-MIB", "hpicfXpsSerialNum"), ("POWERSUPPLY-MIB", "hpicfXpsModuleName"), ("POWERSUPPLY-MIB", "hpicfXpsPowerShareReqStatus"), ("POWERSUPPLY-MIB", "hpicfXpsResetReqStatus"), ("POWERSUPPLY-MIB", "hpicfXpsSupportedCableVersion"), ("POWERSUPPLY-MIB", "hpicfXpsSupportedZoneVersion"), ("POWERSUPPLY-MIB", "hpicfXpsSwitchModType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfXpsGroup = hpicfXpsGroup.setStatus('current')
hpicfXpsZoneGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2, 3)).setObjects(("POWERSUPPLY-MIB", "hpicfXpsZoneNo"), ("POWERSUPPLY-MIB", "hpicfXpsZoneState"), ("POWERSUPPLY-MIB", "hpicfXpsZonePowerShareMap"), ("POWERSUPPLY-MIB", "hpicfXpsZoneVoltage"), ("POWERSUPPLY-MIB", "hpicfXpsZoneWattage"), ("POWERSUPPLY-MIB", "hpicfXpsPSURev"), ("POWERSUPPLY-MIB", "hpicfXpsPSUModule"), ("POWERSUPPLY-MIB", "hpicfXpsZonePowerShareForce"), ("POWERSUPPLY-MIB", "hpicfXpsZoneRecordVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfXpsZoneGroup = hpicfXpsZoneGroup.setStatus('current')
hpicfPsGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 55, 2, 2, 4)).setObjects(("POWERSUPPLY-MIB", "hpicfPsState"), ("POWERSUPPLY-MIB", "hpicfPsFailures"), ("POWERSUPPLY-MIB", "hpicfPsTemp"), ("POWERSUPPLY-MIB", "hpicfPsVoltageInfo"), ("POWERSUPPLY-MIB", "hpicfPsWattageCur"), ("POWERSUPPLY-MIB", "hpicfPsWattageMax"), ("POWERSUPPLY-MIB", "hpicfPsLastCall"), ("POWERSUPPLY-MIB", "hpicfPsModel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfPsGroup1 = hpicfPsGroup1.setStatus('current')
mibBuilder.exportSymbols("POWERSUPPLY-MIB", hpicfXpsSerialNum=hpicfXpsSerialNum, hpicfEntityPs=hpicfEntityPs, hpicfDcPsCompliance1=hpicfDcPsCompliance1, hpicfXpsSwitchOSVersion=hpicfXpsSwitchOSVersion, hpicfPsTemp=hpicfPsTemp, hpicfXpsReset=hpicfXpsReset, PYSNMP_MODULE_ID=hpicfPsMIB, hpicfPsGroup1=hpicfPsGroup1, hpicfXpsMACAddress=hpicfXpsMACAddress, hpicfXpsZoneNo=hpicfXpsZoneNo, hpicfXpsSwitchAutoRecovery=hpicfXpsSwitchAutoRecovery, hpicfXpsZoneVoltage=hpicfXpsZoneVoltage, hpicfXpsZoneWattage=hpicfXpsZoneWattage, hpicfPsLastCall=hpicfPsLastCall, hpicfXpsCompliance=hpicfXpsCompliance, hpicfPsGroups=hpicfPsGroups, hpicfXpsPowerShareReqStatus=hpicfXpsPowerShareReqStatus, hpicfXpsSwitchIpsWattage=hpicfXpsSwitchIpsWattage, hpicfPsVoltageInfo=hpicfPsVoltageInfo, hpicfXpsResetReqStatus=hpicfXpsResetReqStatus, hpicfXpsZonePowerShareForce=hpicfXpsZonePowerShareForce, hpicfPsTable=hpicfPsTable, hpicfXpsSwitchConfigEntry=hpicfXpsSwitchConfigEntry, hpicfXpsZoneEntry=hpicfXpsZoneEntry, hpicfXpsModuleName=hpicfXpsModuleName, hpicfXpsZoneRecordVersion=hpicfXpsZoneRecordVersion, hpicfXpsPSURev=hpicfXpsPSURev, HpicfDcPsState=HpicfDcPsState, hpicfXpsPortOperStatus=hpicfXpsPortOperStatus, hpicfXpsPSUModule=hpicfXpsPSUModule, hpicfXpsSwitchSerialNo=hpicfXpsSwitchSerialNo, hpicfXpsPower=hpicfXpsPower, HpicfXpsConnectionStatus=HpicfXpsConnectionStatus, hpicfPsState=hpicfPsState, HpicfXpsZoneStatus=HpicfXpsZoneStatus, hpicfXpsSwitchIpsVoltage=hpicfXpsSwitchIpsVoltage, hpicfXpsZoneGroup=hpicfXpsZoneGroup, hpicfXpsZonePowerShareMap=hpicfXpsZonePowerShareMap, hpicfPsMIB=hpicfPsMIB, hpicfPsModel=hpicfPsModel, hpicfDcPsCompliance=hpicfDcPsCompliance, hpicfXpsZoneTable=hpicfXpsZoneTable, hpicfXpsTable=hpicfXpsTable, hpicfXpsSupportedCableVersion=hpicfXpsSupportedCableVersion, hpicfXpsSwitchConfigTable=hpicfXpsSwitchConfigTable, hpicfXpsZoneCompliance=hpicfXpsZoneCompliance, hpicfXpsSwitchAdminStatus=hpicfXpsSwitchAdminStatus, hpicfPsConformance=hpicfPsConformance, HpicfDcPsIndex=HpicfDcPsIndex, hpicfXpsZoneState=hpicfXpsZoneState, hpicfXpsConnectingPort=hpicfXpsConnectingPort, hpicfPsGroup=hpicfPsGroup, hpicfPsFailures=hpicfPsFailures, hpicfXpsGroup=hpicfXpsGroup, hpicfPsEntry=hpicfPsEntry, hpicfXpsSwitchModType=hpicfXpsSwitchModType, hpicfXpsSupportedZoneVersion=hpicfXpsSupportedZoneVersion, hpicfXpsAllowPortsSupported=hpicfXpsAllowPortsSupported, hpicfXpsSysName=hpicfXpsSysName, hpicfPsWattageCur=hpicfPsWattageCur, hpicfXpsConnectionState=hpicfXpsConnectionState, hpicfPsBayNum=hpicfPsBayNum, hpicfPsCompliance=hpicfPsCompliance, hpicfXpsEntry=hpicfXpsEntry, hpicfPsWattageMax=hpicfPsWattageMax, hpicfXpsType=hpicfXpsType)