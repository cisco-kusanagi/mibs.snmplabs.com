#
# PySNMP MIB module POWER-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/POWER-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 16:51:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Unsigned32, IpAddress, Bits, Counter64, ObjectIdentity, Counter32, mib_2, NotificationType, TimeTicks, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Unsigned32", "IpAddress", "Bits", "Counter64", "ObjectIdentity", "Counter32", "mib-2", "NotificationType", "TimeTicks", "Integer32", "ModuleIdentity")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
powerEthernetMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 105))
powerEthernetMIB.setRevisions(('2003-11-24 00:00',))
if mibBuilder.loadTexts: powerEthernetMIB.setLastUpdated('200311240000Z')
if mibBuilder.loadTexts: powerEthernetMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
pethNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 0))
pethObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1))
pethConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2))
pethPsePortTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 1), )
if mibBuilder.loadTexts: pethPsePortTable.setStatus('current')
pethPsePortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 1, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethPsePortGroupIndex"), (0, "POWER-ETHERNET-MIB", "pethPsePortIndex"))
if mibBuilder.loadTexts: pethPsePortEntry.setStatus('current')
pethPsePortGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethPsePortGroupIndex.setStatus('current')
pethPsePortIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethPsePortIndex.setStatus('current')
pethPsePortAdminEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortAdminEnable.setStatus('current')
pethPsePortPowerPairsControlAbility = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerPairsControlAbility.setStatus('current')
pethPsePortPowerPairs = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("signal", 1), ("spare", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPairs.setStatus('current')
pethPsePortDetectionStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("disabled", 1), ("searching", 2), ("deliveringPower", 3), ("fault", 4), ("test", 5), ("otherFault", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortDetectionStatus.setStatus('current')
pethPsePortPowerPriority = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("critical", 1), ("high", 2), ("low", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortPowerPriority.setStatus('current')
pethPsePortMPSAbsentCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortMPSAbsentCounter.setStatus('current')
pethPsePortType = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 9), SnmpAdminString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethPsePortType.setStatus('current')
pethPsePortPowerClassifications = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("class0", 1), ("class1", 2), ("class2", 3), ("class3", 4), ("class4", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerClassifications.setStatus('current')
pethPsePortInvalidSignatureCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortInvalidSignatureCounter.setStatus('current')
pethPsePortPowerDeniedCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortPowerDeniedCounter.setStatus('current')
pethPsePortOverLoadCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortOverLoadCounter.setStatus('current')
pethPsePortShortCounter = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethPsePortShortCounter.setStatus('current')
pethMainPseObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1, 3))
pethMainPseTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 3, 1), )
if mibBuilder.loadTexts: pethMainPseTable.setStatus('current')
pethMainPseEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethMainPseGroupIndex"))
if mibBuilder.loadTexts: pethMainPseEntry.setStatus('current')
pethMainPseGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethMainPseGroupIndex.setStatus('current')
pethMainPsePower = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPsePower.setStatus('current')
pethMainPseOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("off", 2), ("faulty", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseOperStatus.setStatus('current')
pethMainPseConsumptionPower = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 4), Gauge32()).setUnits('Watts').setMaxAccess("readonly")
if mibBuilder.loadTexts: pethMainPseConsumptionPower.setStatus('current')
pethMainPseUsageThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 99))).setUnits('%').setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethMainPseUsageThreshold.setStatus('current')
pethNotificationControl = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 1, 4))
pethNotificationControlTable = MibTable((1, 3, 6, 1, 2, 1, 105, 1, 4, 1), )
if mibBuilder.loadTexts: pethNotificationControlTable.setStatus('current')
pethNotificationControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1), ).setIndexNames((0, "POWER-ETHERNET-MIB", "pethNotificationControlGroupIndex"))
if mibBuilder.loadTexts: pethNotificationControlEntry.setStatus('current')
pethNotificationControlGroupIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: pethNotificationControlGroupIndex.setStatus('current')
pethNotificationControlEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 105, 1, 4, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pethNotificationControlEnable.setStatus('current')
pethPsePortOnOffNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 1)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"))
if mibBuilder.loadTexts: pethPsePortOnOffNotification.setStatus('current')
pethMainPowerUsageOnNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 2)).setObjects(("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"))
if mibBuilder.loadTexts: pethMainPowerUsageOnNotification.setStatus('current')
pethMainPowerUsageOffNotification = NotificationType((1, 3, 6, 1, 2, 1, 105, 0, 3)).setObjects(("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"))
if mibBuilder.loadTexts: pethMainPowerUsageOffNotification.setStatus('current')
pethCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2, 1))
pethGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 105, 2, 2))
pethCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 105, 2, 1, 1)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortGroup"), ("POWER-ETHERNET-MIB", "pethPsePortNotificationGroup"), ("POWER-ETHERNET-MIB", "pethNotificationControlGroup"), ("POWER-ETHERNET-MIB", "pethMainPseGroup"), ("POWER-ETHERNET-MIB", "pethMainPowerNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethCompliance = pethCompliance.setStatus('current')
pethPsePortGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 1)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortAdminEnable"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPairsControlAbility"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPairs"), ("POWER-ETHERNET-MIB", "pethPsePortDetectionStatus"), ("POWER-ETHERNET-MIB", "pethPsePortPowerPriority"), ("POWER-ETHERNET-MIB", "pethPsePortMPSAbsentCounter"), ("POWER-ETHERNET-MIB", "pethPsePortInvalidSignatureCounter"), ("POWER-ETHERNET-MIB", "pethPsePortPowerDeniedCounter"), ("POWER-ETHERNET-MIB", "pethPsePortOverLoadCounter"), ("POWER-ETHERNET-MIB", "pethPsePortShortCounter"), ("POWER-ETHERNET-MIB", "pethPsePortType"), ("POWER-ETHERNET-MIB", "pethPsePortPowerClassifications"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPsePortGroup = pethPsePortGroup.setStatus('current')
pethMainPseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 2)).setObjects(("POWER-ETHERNET-MIB", "pethMainPsePower"), ("POWER-ETHERNET-MIB", "pethMainPseOperStatus"), ("POWER-ETHERNET-MIB", "pethMainPseConsumptionPower"), ("POWER-ETHERNET-MIB", "pethMainPseUsageThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethMainPseGroup = pethMainPseGroup.setStatus('current')
pethNotificationControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 3)).setObjects(("POWER-ETHERNET-MIB", "pethNotificationControlEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethNotificationControlGroup = pethNotificationControlGroup.setStatus('current')
pethPsePortNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 4)).setObjects(("POWER-ETHERNET-MIB", "pethPsePortOnOffNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethPsePortNotificationGroup = pethPsePortNotificationGroup.setStatus('current')
pethMainPowerNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 105, 2, 2, 5)).setObjects(("POWER-ETHERNET-MIB", "pethMainPowerUsageOnNotification"), ("POWER-ETHERNET-MIB", "pethMainPowerUsageOffNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pethMainPowerNotificationGroup = pethMainPowerNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("POWER-ETHERNET-MIB", pethPsePortMPSAbsentCounter=pethPsePortMPSAbsentCounter, pethMainPseEntry=pethMainPseEntry, pethMainPsePower=pethMainPsePower, pethCompliance=pethCompliance, pethNotifications=pethNotifications, pethPsePortAdminEnable=pethPsePortAdminEnable, pethPsePortPowerDeniedCounter=pethPsePortPowerDeniedCounter, pethMainPseGroupIndex=pethMainPseGroupIndex, pethPsePortOnOffNotification=pethPsePortOnOffNotification, pethPsePortGroup=pethPsePortGroup, powerEthernetMIB=powerEthernetMIB, pethPsePortIndex=pethPsePortIndex, PYSNMP_MODULE_ID=powerEthernetMIB, pethMainPseConsumptionPower=pethMainPseConsumptionPower, pethNotificationControlTable=pethNotificationControlTable, pethCompliances=pethCompliances, pethNotificationControlEnable=pethNotificationControlEnable, pethConformance=pethConformance, pethPsePortShortCounter=pethPsePortShortCounter, pethPsePortInvalidSignatureCounter=pethPsePortInvalidSignatureCounter, pethMainPseObjects=pethMainPseObjects, pethPsePortOverLoadCounter=pethPsePortOverLoadCounter, pethMainPseOperStatus=pethMainPseOperStatus, pethPsePortGroupIndex=pethPsePortGroupIndex, pethPsePortTable=pethPsePortTable, pethObjects=pethObjects, pethPsePortPowerClassifications=pethPsePortPowerClassifications, pethPsePortPowerPriority=pethPsePortPowerPriority, pethMainPseUsageThreshold=pethMainPseUsageThreshold, pethMainPowerUsageOffNotification=pethMainPowerUsageOffNotification, pethPsePortPowerPairs=pethPsePortPowerPairs, pethMainPowerNotificationGroup=pethMainPowerNotificationGroup, pethMainPowerUsageOnNotification=pethMainPowerUsageOnNotification, pethMainPseGroup=pethMainPseGroup, pethPsePortDetectionStatus=pethPsePortDetectionStatus, pethPsePortEntry=pethPsePortEntry, pethPsePortPowerPairsControlAbility=pethPsePortPowerPairsControlAbility, pethNotificationControlGroupIndex=pethNotificationControlGroupIndex, pethNotificationControlGroup=pethNotificationControlGroup, pethNotificationControlEntry=pethNotificationControlEntry, pethGroups=pethGroups, pethNotificationControl=pethNotificationControl, pethMainPseTable=pethMainPseTable, pethPsePortType=pethPsePortType, pethPsePortNotificationGroup=pethPsePortNotificationGroup)
