#
# PySNMP MIB module ARISTA-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-REDUNDANCY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Gauge32, MibIdentifier, TimeTicks, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Counter64, NotificationType, Unsigned32, Bits, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "MibIdentifier", "TimeTicks", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Counter64", "NotificationType", "Unsigned32", "Bits", "iso", "Integer32")
DisplayString, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "TextualConvention")
aristaRedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 8))
aristaRedundancyMIB.setRevisions(('2014-08-15 00:00', '2012-11-10 22:37',))
if mibBuilder.loadTexts: aristaRedundancyMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaRedundancyMIB.setOrganization('Arista Networks, Inc.')
class AristaRedundancyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("standby", 1), ("active", 2), ("disabled", 3))

class AristaRedundancyProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("simplex", 1), ("rpr", 2), ("sso", 3))

aristaRedundancyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0))
aristaRedundancyNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1))
aristaRedundancyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2))
aristaRedundancyStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0))
aristaRedundancyHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 1))
aristaRedundancyProtocolConfig = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 1), AristaRedundancyProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyProtocolConfig.setStatus('current')
aristaRedundancyProtocolOper = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 2), AristaRedundancyProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyProtocolOper.setStatus('current')
aristaRedundancyUnitStateTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3), )
if mibBuilder.loadTexts: aristaRedundancyUnitStateTable.setStatus('current')
aristaRedundancyUnitStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1), ).setIndexNames((0, "ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitId"))
if mibBuilder.loadTexts: aristaRedundancyUnitStateEntry.setStatus('current')
aristaRedundancyUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaRedundancyUnitId.setStatus('current')
aristaRedundancyUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 2), AristaRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyUnitState.setStatus('current')
aristaRedundancyUnitStateEntryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyUnitStateEntryTime.setStatus('current')
aristaRedundancyLastSwOverReason = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyLastSwOverReason.setStatus('current')
aristaRedundancyNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1, 0))
aristaRedundancySwitchOverNotif = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1, 0, 1)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitStateEntryTime"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyLastSwOverReason"))
if mibBuilder.loadTexts: aristaRedundancySwitchOverNotif.setStatus('current')
aristaRedundancyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 1))
aristaRedundancyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2))
aristaRedundancyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 1, 1)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyStatusGroup"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaRedundancyCompliance = aristaRedundancyCompliance.setStatus('current')
aristaRedundancyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2, 1)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyProtocolConfig"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyProtocolOper"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitState"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitStateEntryTime"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyLastSwOverReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaRedundancyStatusGroup = aristaRedundancyStatusGroup.setStatus('current')
aristaRedundancyNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2, 2)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancySwitchOverNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaRedundancyNotificationsGroup = aristaRedundancyNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-REDUNDANCY-MIB", aristaRedundancyLastSwOverReason=aristaRedundancyLastSwOverReason, aristaRedundancyUnitStateEntry=aristaRedundancyUnitStateEntry, aristaRedundancyUnitStateTable=aristaRedundancyUnitStateTable, aristaRedundancyMIB=aristaRedundancyMIB, aristaRedundancyStatus=aristaRedundancyStatus, AristaRedundancyProtocol=AristaRedundancyProtocol, aristaRedundancyUnitStateEntryTime=aristaRedundancyUnitStateEntryTime, aristaRedundancyNotifications=aristaRedundancyNotifications, aristaRedundancyStatusGroup=aristaRedundancyStatusGroup, aristaRedundancyObjects=aristaRedundancyObjects, aristaRedundancyCompliance=aristaRedundancyCompliance, AristaRedundancyState=AristaRedundancyState, aristaRedundancyGroups=aristaRedundancyGroups, aristaRedundancyUnitState=aristaRedundancyUnitState, aristaRedundancyProtocolOper=aristaRedundancyProtocolOper, aristaRedundancyNotificationsGroup=aristaRedundancyNotificationsGroup, aristaRedundancyCompliances=aristaRedundancyCompliances, aristaRedundancyUnitId=aristaRedundancyUnitId, PYSNMP_MODULE_ID=aristaRedundancyMIB, aristaRedundancyConformance=aristaRedundancyConformance, aristaRedundancyProtocolConfig=aristaRedundancyProtocolConfig, aristaRedundancyNotificationPrefix=aristaRedundancyNotificationPrefix, aristaRedundancySwitchOverNotif=aristaRedundancySwitchOverNotif, aristaRedundancyHistory=aristaRedundancyHistory)
