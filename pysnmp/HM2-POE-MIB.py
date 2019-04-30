#
# PySNMP MIB module HM2-POE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-POE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
hm2IfacePhysIndex, = mibBuilder.importSymbols("HM2-DEVMGMT-MIB", "hm2IfacePhysIndex")
HmTimeHHMM24, hm2ConfigurationMibs, HmEnabledStatus = mibBuilder.importSymbols("HM2-TC-MIB", "HmTimeHHMM24", "hm2ConfigurationMibs", "HmEnabledStatus")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, Integer32, IpAddress, Bits, NotificationType, Gauge32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, TimeTicks, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Integer32", "IpAddress", "Bits", "NotificationType", "Gauge32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "TimeTicks", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hm2PoeMgmtMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 11, 12))
hm2PoeMgmtMib.setRevisions(('2011-10-31 00:00',))
if mibBuilder.loadTexts: hm2PoeMgmtMib.setLastUpdated('201110310000Z')
if mibBuilder.loadTexts: hm2PoeMgmtMib.setOrganization('Hirschmann Automation and Control GmbH')
hm2PoeMgmtMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 12, 0))
hm2PoeMgmtMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 12, 1))
hm2PoeMgmtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1))
hm2PoeMgmtGlobalGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 1))
hm2PoeMgmtAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 1, 1), HmEnabledStatus().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtAdminStatus.setStatus('current')
hm2PoeMgmtReservedPower = MibScalar((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtReservedPower.setStatus('current')
hm2PoeMgmtPsuTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 2), )
if mibBuilder.loadTexts: hm2PoeMgmtPsuTable.setStatus('current')
hm2PoeMgmtPsuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 2, 1), ).setIndexNames((0, "HM2-POE-MIB", "hm2PoeMgmtModulePowerSource"))
if mibBuilder.loadTexts: hm2PoeMgmtPsuEntry.setStatus('current')
hm2PoeMgmtPsuPower = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtPsuPower.setStatus('current')
hm2PoeMgmtPsuReservedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtPsuReservedPower.setStatus('current')
hm2PoeMgmtPsuDeliveredPower = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtPsuDeliveredPower.setStatus('current')
hm2PoeMgmtPortTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3), )
if mibBuilder.loadTexts: hm2PoeMgmtPortTable.setStatus('current')
hm2PoeMgmtPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1), ).setIndexNames((0, "HM2-DEVMGMT-MIB", "hm2IfacePhysIndex"))
if mibBuilder.loadTexts: hm2PoeMgmtPortEntry.setStatus('current')
hm2PoeMgmtPortAdminEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 1), HmEnabledStatus().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtPortAdminEnable.setStatus('current')
hm2PoeMgmtPortConsumptionPower = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtPortConsumptionPower.setStatus('current')
hm2PoeMgmtPortDetectionStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("searching", 2), ("deliveringPower", 3), ("fault", 4), ("test", 5), ("otherFault", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtPortDetectionStatus.setStatus('current')
hm2PoeMgmtPortPowerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3))).clone('low')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtPortPowerPriority.setStatus('current')
hm2PoeMgmtPortPowerClassification = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("class0", 1), ("class1", 2), ("class2", 3), ("class3", 4), ("class4", 5))).clone('class0')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtPortPowerClassification.setStatus('current')
hm2PoeMgmtPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)).clone(' ')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtPortName.setStatus('current')
hm2PoeMgmtPortAllowedClassBits = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 7), Bits().clone(namedValues=NamedValues(("class0", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4))).clone(namedValues=NamedValues(("class0", 0), ("class1", 1), ("class2", 2), ("class3", 3), ("class4", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtPortAllowedClassBits.setStatus('current')
hm2PoeMgmtPortAutoShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 8), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtPortAutoShutdown.setStatus('current')
hm2PoeMgmtPortAutoShutdownTimeStart = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 9), HmTimeHHMM24().clone('00:00')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtPortAutoShutdownTimeStart.setStatus('current')
hm2PoeMgmtPortAutoShutdownTimeEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 10), HmTimeHHMM24().clone('00:00')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtPortAutoShutdownTimeEnd.setStatus('current')
hm2PoeMgmtPortClassValid = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("invalid", 0), ("valid", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtPortClassValid.setStatus('current')
hm2PoeMgmtPortFastStartup = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 12), HmEnabledStatus().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtPortFastStartup.setStatus('current')
hm2PoeMgmtPortMaxConsumptionPower = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtPortMaxConsumptionPower.setStatus('current')
hm2PoeMgmtPortPowerLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtPortPowerLimit.setStatus('current')
hm2PoeMgmtModuleTable = MibTable((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4), )
if mibBuilder.loadTexts: hm2PoeMgmtModuleTable.setStatus('current')
hm2PoeMgmtModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1), ).setIndexNames((0, "HM2-POE-MIB", "hm2PoeMgmtModuleUnitIndex"), (0, "HM2-POE-MIB", "hm2PoeMgmtModuleSlotIndex"))
if mibBuilder.loadTexts: hm2PoeMgmtModuleEntry.setStatus('current')
hm2PoeMgmtModuleUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 1), Integer32())
if mibBuilder.loadTexts: hm2PoeMgmtModuleUnitIndex.setStatus('current')
hm2PoeMgmtModuleSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 2), Integer32())
if mibBuilder.loadTexts: hm2PoeMgmtModuleSlotIndex.setStatus('current')
hm2PoeMgmtModulePower = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000)).clone(1000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtModulePower.setStatus('current')
hm2PoeMgmtModuleMaximumPower = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtModuleMaximumPower.setStatus('current')
hm2PoeMgmtModuleReservedPower = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtModuleReservedPower.setStatus('current')
hm2PoeMgmtModuleDeliveredPower = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtModuleDeliveredPower.setStatus('current')
hm2PoeMgmtModulePowerSource = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("internal", 0), ("external", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2PoeMgmtModulePowerSource.setStatus('current')
hm2PoeMgmtModuleUsageThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99)).clone(90)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtModuleUsageThreshold.setStatus('current')
hm2PoeMgmtModuleNotificationControlEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 11, 12, 1, 1, 4, 1, 9), HmEnabledStatus().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2PoeMgmtModuleNotificationControlEnable.setStatus('current')
hm2PoeMgmtModulePowerUsageOnNotification = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 12, 0, 1)).setObjects(("HM2-POE-MIB", "hm2PoeMgmtModuleDeliveredPower"))
if mibBuilder.loadTexts: hm2PoeMgmtModulePowerUsageOnNotification.setStatus('current')
hm2PoeMgmtModulePowerUsageOffNotification = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 12, 0, 2)).setObjects(("HM2-POE-MIB", "hm2PoeMgmtModuleDeliveredPower"))
if mibBuilder.loadTexts: hm2PoeMgmtModulePowerUsageOffNotification.setStatus('current')
hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 248, 11, 12, 0, 3)).setObjects(("HM2-DEVMGMT-MIB", "hm2IfacePhysIndex"), ("HM2-POE-MIB", "hm2PoeMgmtPortMaxConsumptionPower"), ("HM2-POE-MIB", "hm2PoeMgmtPortPowerLimit"))
if mibBuilder.loadTexts: hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded.setStatus('current')
mibBuilder.exportSymbols("HM2-POE-MIB", hm2PoeMgmtPortTable=hm2PoeMgmtPortTable, hm2PoeMgmtPortConsumptionPower=hm2PoeMgmtPortConsumptionPower, hm2PoeMgmtPsuReservedPower=hm2PoeMgmtPsuReservedPower, hm2PoeMgmtModulePowerUsageOnNotification=hm2PoeMgmtModulePowerUsageOnNotification, hm2PoeMgmtModuleSlotIndex=hm2PoeMgmtModuleSlotIndex, hm2PoeMgmtPortAutoShutdownTimeStart=hm2PoeMgmtPortAutoShutdownTimeStart, hm2PoeMgmtModuleUsageThreshold=hm2PoeMgmtModuleUsageThreshold, hm2PoeMgmtPortPowerPriority=hm2PoeMgmtPortPowerPriority, hm2PoeMgmtReservedPower=hm2PoeMgmtReservedPower, hm2PoeMgmtModulePower=hm2PoeMgmtModulePower, hm2PoeMgmtModuleTable=hm2PoeMgmtModuleTable, hm2PoeMgmtPortAutoShutdownTimeEnd=hm2PoeMgmtPortAutoShutdownTimeEnd, hm2PoeMgmtMib=hm2PoeMgmtMib, hm2PoeMgmtPortAllowedClassBits=hm2PoeMgmtPortAllowedClassBits, hm2PoeMgmtPortAdminEnable=hm2PoeMgmtPortAdminEnable, hm2PoeMgmtPortName=hm2PoeMgmtPortName, hm2PoeMgmtPortMaxConsumptionPower=hm2PoeMgmtPortMaxConsumptionPower, hm2PoeMgmtPortAutoShutdown=hm2PoeMgmtPortAutoShutdown, hm2PoeMgmtModulePowerUsageOffNotification=hm2PoeMgmtModulePowerUsageOffNotification, hm2PoeMgmtPortDetectionStatus=hm2PoeMgmtPortDetectionStatus, hm2PoeMgmtModuleUnitIndex=hm2PoeMgmtModuleUnitIndex, hm2PoeMgmtGroup=hm2PoeMgmtGroup, hm2PoeMgmtMibNotifications=hm2PoeMgmtMibNotifications, hm2PoeMgmtModuleMaximumPower=hm2PoeMgmtModuleMaximumPower, hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded=hm2PoeMgmtPortMaxConfiguredPowerLimitExceeded, hm2PoeMgmtPortPowerLimit=hm2PoeMgmtPortPowerLimit, hm2PoeMgmtPsuTable=hm2PoeMgmtPsuTable, hm2PoeMgmtPsuPower=hm2PoeMgmtPsuPower, hm2PoeMgmtPortFastStartup=hm2PoeMgmtPortFastStartup, hm2PoeMgmtModuleReservedPower=hm2PoeMgmtModuleReservedPower, hm2PoeMgmtModuleDeliveredPower=hm2PoeMgmtModuleDeliveredPower, hm2PoeMgmtPsuDeliveredPower=hm2PoeMgmtPsuDeliveredPower, hm2PoeMgmtMibObjects=hm2PoeMgmtMibObjects, hm2PoeMgmtPortEntry=hm2PoeMgmtPortEntry, hm2PoeMgmtModulePowerSource=hm2PoeMgmtModulePowerSource, hm2PoeMgmtPsuEntry=hm2PoeMgmtPsuEntry, hm2PoeMgmtPortClassValid=hm2PoeMgmtPortClassValid, hm2PoeMgmtAdminStatus=hm2PoeMgmtAdminStatus, PYSNMP_MODULE_ID=hm2PoeMgmtMib, hm2PoeMgmtGlobalGroup=hm2PoeMgmtGlobalGroup, hm2PoeMgmtPortPowerClassification=hm2PoeMgmtPortPowerClassification, hm2PoeMgmtModuleEntry=hm2PoeMgmtModuleEntry, hm2PoeMgmtModuleNotificationControlEnable=hm2PoeMgmtModuleNotificationControlEnable)