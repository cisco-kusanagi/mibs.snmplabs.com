#
# PySNMP MIB module CISCO-ENTITY-PROVISIONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ENTITY-PROVISIONING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:39:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, iso, ObjectIdentity, Bits, ModuleIdentity, Integer32, Counter64, TimeTicks, Unsigned32, Counter32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ObjectIdentity", "Bits", "ModuleIdentity", "Integer32", "Counter64", "TimeTicks", "Unsigned32", "Counter32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, AutonomousType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "AutonomousType", "DisplayString")
ciscoEntityProvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 139))
if mibBuilder.loadTexts: ciscoEntityProvMIB.setLastUpdated('9907082052Z')
if mibBuilder.loadTexts: ciscoEntityProvMIB.setOrganization('Cisco Systems, Inc.')
ciscoEntityProvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 1))
ceProvContainerTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1), )
if mibBuilder.loadTexts: ceProvContainerTable.setStatus('current')
ceProvContainerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: ceProvContainerEntry.setStatus('current')
ceProvContainerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unequipped", 1), ("provisioned", 2), ("mismatched", 3), ("invalid", 4), ("equipped", 5), ("failed", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceProvContainerStatus.setStatus('current')
ceProvContainerEquipped = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 2), AutonomousType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ceProvContainerEquipped.setStatus('current')
ceProvContainerDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 139, 1, 1, 1, 3), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ceProvContainerDetected.setStatus('current')
ceProvMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 2))
ceProvMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 2, 0))
ceProvMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3))
ceProvMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1))
ceProvMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2))
ceProvMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 1, 1)).setObjects(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceProvMIBCompliance = ceProvMIBCompliance.setStatus('current')
ceProvContainerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 139, 3, 2, 1)).setObjects(("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerStatus"), ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerEquipped"), ("CISCO-ENTITY-PROVISIONING-MIB", "ceProvContainerDetected"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ceProvContainerGroup = ceProvContainerGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ENTITY-PROVISIONING-MIB", ceProvContainerTable=ceProvContainerTable, ceProvContainerStatus=ceProvContainerStatus, ceProvContainerEquipped=ceProvContainerEquipped, ciscoEntityProvMIBObjects=ciscoEntityProvMIBObjects, PYSNMP_MODULE_ID=ciscoEntityProvMIB, ceProvContainerDetected=ceProvContainerDetected, ceProvMIBConformance=ceProvMIBConformance, ceProvMIBGroups=ceProvMIBGroups, ceProvContainerGroup=ceProvContainerGroup, ceProvContainerEntry=ceProvContainerEntry, ceProvMIBNotifications=ceProvMIBNotifications, ciscoEntityProvMIB=ciscoEntityProvMIB, ceProvMIBCompliances=ceProvMIBCompliances, ceProvMIBCompliance=ceProvMIBCompliance, ceProvMIBNotificationsPrefix=ceProvMIBNotificationsPrefix)
