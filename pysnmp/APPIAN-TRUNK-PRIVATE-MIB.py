#
# PySNMP MIB module APPIAN-TRUNK-PRIVATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APPIAN-TRUNK-PRIVATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:08:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acChassisRingId, acChassisCurrentTime = mibBuilder.importSymbols("APPIAN-CHASSIS-MIB", "acChassisRingId", "acChassisCurrentTime")
AcAdminStatus, AcOpStatus, AcNodeId, acTrunks = mibBuilder.importSymbols("APPIAN-SMI-MIB", "AcAdminStatus", "AcOpStatus", "AcNodeId", "acTrunks")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Unsigned32, Counter64, Gauge32, MibIdentifier, NotificationType, Integer32, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, ObjectIdentity, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "Counter64", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
acTrunksPrivate = ModuleIdentity((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4))
acTrunksPrivate.setRevisions(('1900-03-20 00:00',))
if mibBuilder.loadTexts: acTrunksPrivate.setLastUpdated('0003200000Z')
if mibBuilder.loadTexts: acTrunksPrivate.setOrganization('Appian Communications, Inc.')
acTrunkPrivateTable = MibTable((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1), )
if mibBuilder.loadTexts: acTrunkPrivateTable.setStatus('current')
acTrunkPrivateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1), ).setIndexNames((0, "APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateNodeId"), (0, "APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateIndex"))
if mibBuilder.loadTexts: acTrunkPrivateEntry.setStatus('current')
acTrunkPrivateNodeId = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1, 1), AcNodeId()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: acTrunkPrivateNodeId.setStatus('current')
acTrunkPrivateIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: acTrunkPrivateIndex.setStatus('current')
acTrunkPrivateAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1, 3), AcAdminStatus().clone('inactivate')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acTrunkPrivateAdminStatus.setStatus('current')
acTrunkPrivateOpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1, 4), AcOpStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acTrunkPrivateOpStatus.setStatus('current')
acTrunkPrivateDetailStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 25))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acTrunkPrivateDetailStatus.setStatus('current')
acTrunkPrivateTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 0))
acTrunkUpTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 0, 1)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateNodeId"), ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateIndex"), ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateOpStatus"), ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateDetailStatus"))
if mibBuilder.loadTexts: acTrunkUpTrap.setStatus('current')
acTrunkDownTrap = NotificationType((1, 3, 6, 1, 4, 1, 2785, 2, 6, 4, 0, 2)).setObjects(("APPIAN-CHASSIS-MIB", "acChassisCurrentTime"), ("APPIAN-CHASSIS-MIB", "acChassisRingId"), ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateNodeId"), ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateIndex"), ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateOpStatus"), ("APPIAN-TRUNK-PRIVATE-MIB", "acTrunkPrivateDetailStatus"))
if mibBuilder.loadTexts: acTrunkDownTrap.setStatus('current')
mibBuilder.exportSymbols("APPIAN-TRUNK-PRIVATE-MIB", acTrunkPrivateOpStatus=acTrunkPrivateOpStatus, acTrunkPrivateEntry=acTrunkPrivateEntry, PYSNMP_MODULE_ID=acTrunksPrivate, acTrunkPrivateTraps=acTrunkPrivateTraps, acTrunkPrivateTable=acTrunkPrivateTable, acTrunkDownTrap=acTrunkDownTrap, acTrunkPrivateIndex=acTrunkPrivateIndex, acTrunkPrivateNodeId=acTrunkPrivateNodeId, acTrunkPrivateAdminStatus=acTrunkPrivateAdminStatus, acTrunkPrivateDetailStatus=acTrunkPrivateDetailStatus, acTrunkUpTrap=acTrunkUpTrap, acTrunksPrivate=acTrunksPrivate)