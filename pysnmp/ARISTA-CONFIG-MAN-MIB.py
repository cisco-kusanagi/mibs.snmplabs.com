#
# PySNMP MIB module ARISTA-CONFIG-MAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-CONFIG-MAN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, Bits, IpAddress, ObjectIdentity, Gauge32, Counter32, TimeTicks, ModuleIdentity, Integer32, Counter64, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "IpAddress", "ObjectIdentity", "Gauge32", "Counter32", "TimeTicks", "ModuleIdentity", "Integer32", "Counter64", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaConfigManMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 9))
aristaConfigManMIB.setRevisions(('2014-08-15 00:00', '2014-05-06 13:00', '2012-08-23 13:00',))
if mibBuilder.loadTexts: aristaConfigManMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaConfigManMIB.setOrganization('Arista Networks, Inc.')
class ConfigHistoryEventMedium(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 0), ("erase", 1), ("commandSource", 2), ("running", 3), ("startup", 4), ("url", 5), ("session", 6))

aristaConfigManMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1))
aristaConfigManMibConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2))
aristaCmdHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1))
aristaCmdHistoryRunningLastChanged = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryRunningLastChanged.setStatus('current')
aristaCmdHistoryEventTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2), )
if mibBuilder.loadTexts: aristaCmdHistoryEventTable.setStatus('current')
aristaCmdHistoryEventEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1), ).setIndexNames((0, "ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventIndex"))
if mibBuilder.loadTexts: aristaCmdHistoryEventEntry.setStatus('current')
aristaCmdHistoryEventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaCmdHistoryEventIndex.setStatus('current')
aristaCmdHistoryEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventTime.setStatus('current')
aristaCmdHistoryEventCommandSource = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("commandLine", 0), ("snmp", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventCommandSource.setStatus('current')
aristaCmdHistoryEventConfigSource = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 4), ConfigHistoryEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventConfigSource.setStatus('current')
aristaCmdHistoryEventConfigDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 5), ConfigHistoryEventMedium()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventConfigDestination.setStatus('current')
aristaCmdHistoryEventConfigSourceURLScheme = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventConfigSourceURLScheme.setStatus('current')
aristaCmdHistoryEventConfigDestURLScheme = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 9, 1, 1, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaCmdHistoryEventConfigDestURLScheme.setStatus('current')
aristaConfigManMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 3))
aristaConfigManMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 3, 0))
aristaConfigManEvent = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 9, 3, 0, 1)).setObjects(("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventCommandSource"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSource"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestination"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSourceURLScheme"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestURLScheme"))
if mibBuilder.loadTexts: aristaConfigManEvent.setStatus('current')
aristaConfigManMibCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1))
aristaConfigManMibGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 2))
aristaConfigManMibCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 1)).setObjects(("ARISTA-CONFIG-MAN-MIB", "aristaConfigEventDetailGroup"), ("ARISTA-CONFIG-MAN-MIB", "aristaConfigManMibNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigManMibCompliance = aristaConfigManMibCompliance.setStatus('current')
aristaConfigEventDetailGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 2, 1)).setObjects(("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryRunningLastChanged"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventTime"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventCommandSource"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSource"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestination"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigSourceURLScheme"), ("ARISTA-CONFIG-MAN-MIB", "aristaCmdHistoryEventConfigDestURLScheme"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigEventDetailGroup = aristaConfigEventDetailGroup.setStatus('current')
aristaConfigManMibNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 9, 2, 1, 2, 2)).setObjects(("ARISTA-CONFIG-MAN-MIB", "aristaConfigManEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaConfigManMibNotificationsGroup = aristaConfigManMibNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-CONFIG-MAN-MIB", aristaCmdHistoryEventConfigSourceURLScheme=aristaCmdHistoryEventConfigSourceURLScheme, aristaCmdHistoryEventTable=aristaCmdHistoryEventTable, aristaConfigEventDetailGroup=aristaConfigEventDetailGroup, aristaCmdHistory=aristaCmdHistory, aristaCmdHistoryEventConfigSource=aristaCmdHistoryEventConfigSource, aristaConfigManMibNotificationsGroup=aristaConfigManMibNotificationsGroup, ConfigHistoryEventMedium=ConfigHistoryEventMedium, aristaConfigManMibCompliances=aristaConfigManMibCompliances, PYSNMP_MODULE_ID=aristaConfigManMIB, aristaCmdHistoryEventEntry=aristaCmdHistoryEventEntry, aristaConfigManMibGroups=aristaConfigManMibGroups, aristaConfigManMibCompliance=aristaConfigManMibCompliance, aristaConfigManMIBObjects=aristaConfigManMIBObjects, aristaConfigManMIBNotificationPrefix=aristaConfigManMIBNotificationPrefix, aristaCmdHistoryEventIndex=aristaCmdHistoryEventIndex, aristaCmdHistoryEventConfigDestination=aristaCmdHistoryEventConfigDestination, aristaConfigManMIBNotifications=aristaConfigManMIBNotifications, aristaConfigManMIB=aristaConfigManMIB, aristaCmdHistoryEventCommandSource=aristaCmdHistoryEventCommandSource, aristaCmdHistoryRunningLastChanged=aristaCmdHistoryRunningLastChanged, aristaConfigManEvent=aristaConfigManEvent, aristaConfigManMibConformance=aristaConfigManMibConformance, aristaCmdHistoryEventConfigDestURLScheme=aristaCmdHistoryEventConfigDestURLScheme, aristaCmdHistoryEventTime=aristaCmdHistoryEventTime)
