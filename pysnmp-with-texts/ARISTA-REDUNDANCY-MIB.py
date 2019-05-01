#
# PySNMP MIB module ARISTA-REDUNDANCY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-REDUNDANCY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity, iso, Bits, Counter32, NotificationType, IpAddress, Unsigned32, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity", "iso", "Bits", "Counter32", "NotificationType", "IpAddress", "Unsigned32", "TimeTicks", "MibIdentifier")
TimeStamp, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "TextualConvention")
aristaRedundancyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 8))
aristaRedundancyMIB.setRevisions(('2014-08-15 00:00', '2012-11-10 22:37',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaRedundancyMIB.setRevisionsDescriptions(('Updated postal and e-mail addresses.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: aristaRedundancyMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaRedundancyMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaRedundancyMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaRedundancyMIB.setDescription("This MIB module provides configuration and status information pertaining to high availability or redundancy infrastructure on Arista devices. As such, this MIB module is aimed at providing relevant information on 'Modular Systems' which support dual supervisors for control plane redundancy. Each of the dual supervisors are referred to as 'unit' in the module.")
class AristaRedundancyState(TextualConvention, Integer32):
    description = 'The status of the unit. unknown - The redundancy status is unknown. standby - The unit is initialized, and is in the standby state. active - The unit is currently in active mode. The SNMP agent runs only on the active unit. disabled - The unit is currently disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("unknown", 0), ("standby", 1), ("active", 2), ("disabled", 3))

class AristaRedundancyProtocol(TextualConvention, Integer32):
    description = 'The redundancy protocol. unknown - The protocol is unknown. simplex - The peer unit will remain disabled with this protocol. rpr - Route Processor Redundancy. This protocol allows the startup configuration files to be synchronized between the units but not the active operational state. sso - Stateful Switchover. This protocol allows the peer units to synchronize not only configuration but also operational state so when the active unit fails, the peer can take over control plane responsibilities.'
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
if mibBuilder.loadTexts: aristaRedundancyProtocolConfig.setDescription('Indicates the configured redundancy protocol in the system.')
aristaRedundancyProtocolOper = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 2), AristaRedundancyProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyProtocolOper.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancyProtocolOper.setDescription('Indicates the operational redundancy protocol in the system.')
aristaRedundancyUnitStateTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3), )
if mibBuilder.loadTexts: aristaRedundancyUnitStateTable.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancyUnitStateTable.setDescription('This table contains the current redundancy state information for the units in the system.')
aristaRedundancyUnitStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1), ).setIndexNames((0, "ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitId"))
if mibBuilder.loadTexts: aristaRedundancyUnitStateEntry.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancyUnitStateEntry.setDescription('An entry containing redundancy state information for a unit.')
aristaRedundancyUnitId = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: aristaRedundancyUnitId.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancyUnitId.setDescription('A unique identifier representing a unit. Usually it is the slot number of the inserted unit on the given modular system.')
aristaRedundancyUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 2), AristaRedundancyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyUnitState.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancyUnitState.setDescription('The current state of the given unit.')
aristaRedundancyUnitStateEntryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyUnitStateEntryTime.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancyUnitStateEntryTime.setDescription('The value of sysUpTime when the unit entered the given state.')
aristaRedundancyLastSwOverReason = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 8, 0, 0, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaRedundancyLastSwOverReason.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancyLastSwOverReason.setDescription('The reason for the last switchover in the system.')
aristaRedundancyNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1, 0))
aristaRedundancySwitchOverNotif = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 8, 1, 0, 1)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitStateEntryTime"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyLastSwOverReason"))
if mibBuilder.loadTexts: aristaRedundancySwitchOverNotif.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancySwitchOverNotif.setDescription('A switchover notification is generated whenever a unit becomes active and it has taken over the control plane duties.')
aristaRedundancyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 1))
aristaRedundancyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2))
aristaRedundancyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 1, 1)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyStatusGroup"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaRedundancyCompliance = aristaRedundancyCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancyCompliance.setDescription('The compliance statement for Arista switches that support Redundancy MIB.')
aristaRedundancyStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2, 1)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancyProtocolConfig"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyProtocolOper"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitState"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyUnitStateEntryTime"), ("ARISTA-REDUNDANCY-MIB", "aristaRedundancyLastSwOverReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaRedundancyStatusGroup = aristaRedundancyStatusGroup.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancyStatusGroup.setDescription('The collection of objects that represent the redundancy status of the system.')
aristaRedundancyNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 8, 2, 2, 2)).setObjects(("ARISTA-REDUNDANCY-MIB", "aristaRedundancySwitchOverNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaRedundancyNotificationsGroup = aristaRedundancyNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: aristaRedundancyNotificationsGroup.setDescription('The collection of notifications generated by the system on redundancy change events.')
mibBuilder.exportSymbols("ARISTA-REDUNDANCY-MIB", PYSNMP_MODULE_ID=aristaRedundancyMIB, aristaRedundancyNotificationsGroup=aristaRedundancyNotificationsGroup, aristaRedundancyProtocolConfig=aristaRedundancyProtocolConfig, aristaRedundancyUnitState=aristaRedundancyUnitState, AristaRedundancyState=AristaRedundancyState, aristaRedundancyCompliance=aristaRedundancyCompliance, aristaRedundancyMIB=aristaRedundancyMIB, aristaRedundancyUnitStateEntry=aristaRedundancyUnitStateEntry, aristaRedundancyStatus=aristaRedundancyStatus, aristaRedundancyUnitId=aristaRedundancyUnitId, aristaRedundancyConformance=aristaRedundancyConformance, aristaRedundancyUnitStateTable=aristaRedundancyUnitStateTable, aristaRedundancyHistory=aristaRedundancyHistory, aristaRedundancyObjects=aristaRedundancyObjects, aristaRedundancyStatusGroup=aristaRedundancyStatusGroup, aristaRedundancyGroups=aristaRedundancyGroups, aristaRedundancyLastSwOverReason=aristaRedundancyLastSwOverReason, AristaRedundancyProtocol=AristaRedundancyProtocol, aristaRedundancyProtocolOper=aristaRedundancyProtocolOper, aristaRedundancyUnitStateEntryTime=aristaRedundancyUnitStateEntryTime, aristaRedundancyCompliances=aristaRedundancyCompliances, aristaRedundancyNotifications=aristaRedundancyNotifications, aristaRedundancyNotificationPrefix=aristaRedundancyNotificationPrefix, aristaRedundancySwitchOverNotif=aristaRedundancySwitchOverNotif)
