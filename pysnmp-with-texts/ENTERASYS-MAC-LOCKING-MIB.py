#
# PySNMP MIB module ENTERASYS-MAC-LOCKING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-MAC-LOCKING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:03:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Counter64, Counter32, Gauge32, Bits, NotificationType, Integer32, ModuleIdentity, ObjectIdentity, Unsigned32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Counter64", "Counter32", "Gauge32", "Bits", "NotificationType", "Integer32", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "IpAddress", "TimeTicks")
RowStatus, DisplayString, MacAddress, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "MacAddress", "TextualConvention", "TruthValue")
etsysMACLockingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21))
etsysMACLockingMIB.setRevisions(('2011-03-08 19:47', '2007-05-21 13:04', '2007-05-17 12:55', '2007-05-09 19:24', '2007-04-16 15:26', '2003-07-30 15:45', '2003-01-17 21:14', '2002-08-05 20:30', '2002-08-01 14:45',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: etsysMACLockingMIB.setRevisionsDescriptions(('Added the etsysMACLockingThresholdEnable leaf and etsysMACLockingMACThresholdNotification notification so that an administrator can take appropriate action upon the MAC address table threshold (etsysMACLockingFirstArrivalStationsAllocated) being reached.', 'Added the etsysMACLockingViolationSyslogEnable leaf to control the sending of syslog messages for violating MAC addresses.', 'Clarify that only static MAC lock entries that are in the active(1) state, should be represented in the etsysMACLockingStationTable.', 'Added the etsysMACLockingRemoveStation object to allow for the removal of any current locked MAC address. Added the agingFirstArrival enumeration to represent first arrival entries that are aging.', 'Added the etsysMACLockingFirstArrivalAging object to control the aging of first arrival entries on a per-port basis.', 'Updated the description clause for the etsysMACLockingMoveFirstArrivalToStatic object.', 'Added objects to support the transition of dynamically locked MAC addresses to statically locked addresses.', 'Added more descriptive text and corrected two range issues in the description of the allocated objects.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: etsysMACLockingMIB.setLastUpdated('201103081947Z')
if mibBuilder.loadTexts: etsysMACLockingMIB.setOrganization('Enterasys Networks, Inc')
if mibBuilder.loadTexts: etsysMACLockingMIB.setContactInfo('Postal: Enterasys Networks 50 Minuteman Rd. Andover, MA 01810-1008 USA Phone: +1 978 684 1000 E-mail: support@enterasys.com WWW: http://www.enterasys.com')
if mibBuilder.loadTexts: etsysMACLockingMIB.setDescription("This MIB module defines the portion of the SNMP enterprise MIBs under Enterasys Networks' enterprise OID pertaining to MAC Locking. This MIB is designed to provide configuration and status objects pertaining to per port MAC Locking.")
etsysMACLockingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1))
etsysMACLockingSystemBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 1))
etsysMACLockingPortConfigBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2))
etsysMACLockingStaticStationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3))
etsysMACLockingStationBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4))
etsysMACLockingTrapBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 0))
etsysMACLockingSystemEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 1, 1), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingSystemEnable.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingSystemEnable.setDescription('This object is a configuration convenience. While disabled(2), all per port configuration is ignored, but changeable. When set to enabled(1), the per port configuration becomes active.')
etsysMACLockingPortTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1), )
if mibBuilder.loadTexts: etsysMACLockingPortTable.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingPortTable.setDescription('A table that provides for the configuration of MAC Locking for each port. Regardless of the value of etsysMACLockingSystemEnable, this table is automatically populated with one row per supported port. MAC Locking is not supported on media types whose addresses cannot be adequately represented by the MacAddress convention')
etsysMACLockingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1), ).setIndexNames((0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPort"))
if mibBuilder.loadTexts: etsysMACLockingPortEntry.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingPortEntry.setDescription('Each conceptual row allows control over whether MAC locking is enabled for the port corresponding to the row. Similarly, each row provides control over whether violation traps are sent. Information in this table is persistent.')
etsysMACLockingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: etsysMACLockingPort.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingPort.setDescription('The interface number for this row.')
etsysMACLockingEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingEnable.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingEnable.setDescription('When set to enabled(1) any static entries currently created on this port become active and the first n MACs which are received on this port are locked, where n is equal to etsysMACLockingFirstArrivalStationsAllocated. When set to disabled(2), all entries in the etsysMACLockingStationTable are cleared, and the port forwards without regard to MAC locking.')
etsysMACLockingViolationEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingViolationEnable.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingViolationEnable.setDescription('When set to enabled(1), the agent issues violation traps for violations detected by the agent. Arrival of violation traps at the management station is not guaranteed and the trap generation rate is not required to match the violation detection rate. A best effort delivery is acceptable. When disabled(2), no traps are sent.')
etsysMACLockingLastViolationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMACLockingLastViolationAddress.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingLastViolationAddress.setDescription('The last source MAC received on this port which was a violation. A violation is defined to be when the maximum number of firstArrival entries exists for this port in the etsysMACLockingStationTable and the source MAC address of the received packet differs from all entries found for this port in the etsysMACLockingStationTable.')
etsysMACLockingFirstArrivalStationsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMACLockingFirstArrivalStationsAllowed.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingFirstArrivalStationsAllowed.setDescription('The agent sets this number for the benefit of management to use when determining the permissible range of values for the etsysMACLockingFirstArrivalStationsAllocated object. The default value of this object is device dependent.')
etsysMACLockingFirstArrivalStationsAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingFirstArrivalStationsAllocated.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingFirstArrivalStationsAllocated.setDescription('Management sets this number in the range of 0 to etsysMACLockingFirstArrivalStationsAllowed. This number limits the number of locked MACs on this port using the first arrival method. The default value of this object SHOULD be the same as the default value of etsysMACLockingFirstArrivalStationsAllowed.')
etsysMACLockingStaticStationsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMACLockingStaticStationsAllowed.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingStaticStationsAllowed.setDescription('The agent sets this number for the benefit of management to use when determining the permissible range of values for the etsysMACLockingStaticStationsAllocated object. The default value of this object is device dependent.')
etsysMACLockingStaticStationsAllocated = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingStaticStationsAllocated.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingStaticStationsAllocated.setDescription('Management sets this number in the range of 0 to etsysMACLockingStaticStationsAllowed. This limits the number of statically provisioned, locked MACs on this port. The default value of this object SHOULD be the same as the default value of etsysMACLockingStaticStationsAllowed.')
etsysMACLockingMoveFirstArrivalToStatic = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingMoveFirstArrivalToStatic.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingMoveFirstArrivalToStatic.setDescription('When set to true(1), moves First Arrival MACs locked on the port, in lexicographical order, into Statically Locked MACs on the port. The move continues until all First Arrival MACs are moved or until the number of allowable static entries (etsysMACLockingStaticStationsAllocated) has been exhausted. If there is an insufficient number Static entries available to accommodate all the First Arrival MACs, then only the First Arrival MACs already moved to statically locked MACs will be static entries, the remaining First Arrival MACs will remain as First Arrival entries and a MIB_ERROR is returned. When read this object will always return false(2).')
etsysMACLockingStaticStationsCount = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMACLockingStaticStationsCount.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingStaticStationsCount.setDescription('Returns the number of Statically Locked MACs currently locked on the port.')
etsysMACLockingClearStaticStations = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 11), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingClearStaticStations.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingClearStaticStations.setDescription('When set to true(1), clears out all the Statically Locked MACs on this port. When read this object will always return false(2).')
etsysMACLockingFirstArrivalAging = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingFirstArrivalAging.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingFirstArrivalAging.setDescription('When set to true(1), firstArrival MACs that have aged out of the forwarding database will be removed for the associated port lock')
etsysMACLockingViolationSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 13), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingViolationSyslogEnable.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingViolationSyslogEnable.setDescription('When set to enabled(1), the agent issues syslog messages for violations detected by the agent. Arrival of violation syslog messages at the management station is not guaranteed and the messages generation rate is not required to match the violation detection rate. A best effort delivery is acceptable. When disabled(2), no syslog messages are sent as a result of MAC locking violations.')
etsysMACLockingThresholdEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 14), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingThresholdEnable.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingThresholdEnable.setDescription('When set to enabled(1), the agent issues a trap when the MAC address threshold as defined in the etsysMACLockingFirstArrivalStationsAllocated object has been reached. Arrival of these traps at the management station is not guaranteed and the trap generation rate is not required to match the detection rate. A best effort delivery is acceptable. When disabled(2), no traps are sent as a result of the threshold being reached.')
etsysMACLockingThresholdSyslogEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 2, 1, 1, 15), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingThresholdSyslogEnable.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingThresholdSyslogEnable.setDescription('When set to enabled(1), the agent issues a syslog message when the MAC address threshold as defined in the etsysMACLockingFirstArrivalStationsAllocated object has been reached. Arrival of these messages is not guaranteed and the message generation rate is not required to match the detection rate. A best effort delivery is acceptable. When disabled(2), no messages are sent as a result of the threshold being reached.')
etsysMACLockingStaticStationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1), )
if mibBuilder.loadTexts: etsysMACLockingStaticStationTable.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingStaticStationTable.setDescription('This table lists all statically locked MAC addresses for each port. When MAC locking is enabled on a port, all active rows in this table will appear in the etsysMACLockingStationTable with the object etsysMACLockingLockedEntryCause set to static(2). Rows in this table are persistent between resets.')
etsysMACLockingStaticStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1, 1), ).setIndexNames((0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPort"), (0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedAddress"))
if mibBuilder.loadTexts: etsysMACLockingStaticStationEntry.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingStaticStationEntry.setDescription('Each conceptual row contains a user specified locked MAC address.')
etsysMACLockingLockedAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: etsysMACLockingLockedAddress.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingLockedAddress.setDescription('The MAC that has been locked to this port.')
etsysMACLockingStaticEntryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 3, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysMACLockingStaticEntryRowStatus.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingStaticEntryRowStatus.setDescription("The status column has six defined values: - 'active', which indicates that a row shall also exist or be created in etsysMACLockingStationTable with the same index and the object etsysMACLockingLockedEntryCause in that row shall be static(1); - 'notInService', which indicates the existence or causes the creation of a row in this table. However, no corresponding row shall exist or be created in etsysMACLockingStationTable; - 'notReady', will never be read in any row of this table since existence is the only requirement for this tables rows; - 'createAndGo', which causes a new row to be created in both this table and in the etsysMACLockingStationTable with the same index and the object etsysMACLockingLockedEntryCause shall have the value static(1); - 'createAndWait', which causes a new row to be created in this table. However, no corresponding row shall be created in etsysMACLockingStationTable; and, - 'destroy', which causes the agent to remove this tables row along with the corresponding row in etsysMACLockingStationTable.")
etsysMACLockingStationTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1), )
if mibBuilder.loadTexts: etsysMACLockingStationTable.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingStationTable.setDescription('This table lists any locked MAC address for each port along with their entry types. On each port in the system, MACs can be locked. For each MAC locked to a port, a row appears in this table. When MAC locking is enabled on a port, the first n packets received by the port has its source MAC locked to the port and the locked cause displays firstArrival(2) The value n is equal to the etsysMACLockingFirstArrivalStationsAllocated object. Additionally, management may explicitly lock a MAC to a port by using the etsysMACLockingStationStaticTable. For each entry in the static table that is active(1), a corresponding entry appears in this table with its etsysMACLockingLockedEntryCause object set to static(1).')
etsysMACLockingStationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1, 1), ).setIndexNames((0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPort"), (0, "ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedAddress"))
if mibBuilder.loadTexts: etsysMACLockingStationEntry.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingStationEntry.setDescription('Each conceptual row contains a locked cause which describes how the MAC was locked on the port. If etsysMACLockingSystemEnable is disabled(2), then this table will be empty. This table contains entries for those ports which have MAC locking enabled and have locked MACs.')
etsysMACLockingLockedEntryCause = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("static", 1), ("firstArrival", 2), ("agingFirstArrival", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysMACLockingLockedEntryCause.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingLockedEntryCause.setDescription('When management statically provisions a MAC onto this port, then this object is returns static(1). If this MAC was dynamically locked, then this object returns firstArrival(2). If first arrival aging is enabled on the port and the MAC address is dynamically locked, then this object returns agingFirstArrival(3).')
etsysMACLockingRemoveStation = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 4, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysMACLockingRemoveStation.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingRemoveStation.setDescription('When this is object is set to true(1) the MAC address specified by the indexing will be removed from etsysMACLockingStationTable. If the etsysMACLockingLockedEntryCause leaf for this table entry is of type static(1), then the associated entry will also be removed from the etsysMACLockingStaticStationTable. A set to false(2) will have no effect. This object will always return false(2).')
etsysMACLockingMACViolation = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 0, 1)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLastViolationAddress"))
if mibBuilder.loadTexts: etsysMACLockingMACViolation.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingMACViolation.setDescription('If MAC Locking is globally enabled and specifically enabled for this port, then this trap is sent when a packet is received with a source MAC that differs from all the currently locked MACs for the port specified in this instance of the notification.')
etsysMACLockingMACThreshold = NotificationType((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 1, 0, 2)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalStationsAllocated"))
if mibBuilder.loadTexts: etsysMACLockingMACThreshold.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingMACThreshold.setDescription('MAC database threshold notification. The device will send this notification when the MAC address threshold configured in the etsysMACLockingFirstArrivalStationsAllocated object has been reached so that the administrator can take appropriate action.')
etsysMACLockingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2))
etsysMACLockingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1))
etsysMACLockingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2))
etsysMACLockingSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 1)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingSystemEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingSystemGroup = etsysMACLockingSystemGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingSystemGroup.setDescription('A collection of objects providing global configuration for the MAC Locking feature.')
etsysMACLockingPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 2)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingEnable"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingViolationEnable"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLastViolationAddress"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalStationsAllowed"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalStationsAllocated"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticStationsAllowed"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticStationsAllocated"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingMoveFirstArrivalToStatic"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticStationsCount"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingClearStaticStations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingPortGroup = etsysMACLockingPortGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingPortGroup.setDescription('A collection of objects providing port based configuration and status of MAC Locking.')
etsysMACLockingStationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 3)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedEntryCause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingStationGroup = etsysMACLockingStationGroup.setStatus('deprecated')
if mibBuilder.loadTexts: etsysMACLockingStationGroup.setDescription('********* THIS GROUP IS DEPRECATED ********** A list of currently locked MACs.')
etsysMACLockingStaticStationGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 4)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingStaticStationGroup = etsysMACLockingStaticStationGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingStaticStationGroup.setDescription('A list of statically provisioned locked MACs. This group is mandatory if static MAC locking is supported, otherwise it is optional.')
etsysMACLockingPortFirstArrivalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 5)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingFirstArrivalAging"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingPortFirstArrivalGroup = etsysMACLockingPortFirstArrivalGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingPortFirstArrivalGroup.setDescription('A collection of objects providing port based configuration of firstArrival MAC Locking.')
etsysMACLockingStationGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 6)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingLockedEntryCause"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingRemoveStation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingStationGroup2 = etsysMACLockingStationGroup2.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingStationGroup2.setDescription('A collection of objects providing status and configuration of all currently locked MAC addresses.')
etsysMACLockingNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 7)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingMACViolation"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingMACThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingNotificationGroup = etsysMACLockingNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingNotificationGroup.setDescription('The MAC Locking notifications.')
etsysMACLockingPortMessageGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 1, 8)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingViolationSyslogEnable"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingThresholdEnable"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingThresholdSyslogEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingPortMessageGroup = etsysMACLockingPortMessageGroup.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingPortMessageGroup.setDescription('A collection of objects providing port based configuration and status for MAC Locking syslog messages and notifications.')
etsysMACLockingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 1)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingSystemGroup"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPortGroup"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingCompliance = etsysMACLockingCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: etsysMACLockingCompliance.setDescription('******** THIS COMPLIANCE IS DEPRECATED ******** The compliance statement for devices that support MAC Locking.')
etsysMACLockingPortFirstArrivalCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 2)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPortFirstArrivalGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingPortFirstArrivalCompliance = etsysMACLockingPortFirstArrivalCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingPortFirstArrivalCompliance.setDescription('The compliance statement for all devices that support aging first arrival mac lock entries on a per port basis.')
etsysMACLockingCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 3)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingSystemGroup"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPortGroup"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingStationGroup2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingCompliance2 = etsysMACLockingCompliance2.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingCompliance2.setDescription('The compliance statement for devices that support MAC Locking.')
etsysMACLockingNotificationCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 21, 2, 2, 1, 4)).setObjects(("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingNotificationGroup"), ("ENTERASYS-MAC-LOCKING-MIB", "etsysMACLockingPortMessageGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysMACLockingNotificationCompliance = etsysMACLockingNotificationCompliance.setStatus('current')
if mibBuilder.loadTexts: etsysMACLockingNotificationCompliance.setDescription('The compliance statement for all devices that support notifications and syslog messages for MAC Locking events.')
mibBuilder.exportSymbols("ENTERASYS-MAC-LOCKING-MIB", etsysMACLockingThresholdEnable=etsysMACLockingThresholdEnable, etsysMACLockingStationBranch=etsysMACLockingStationBranch, etsysMACLockingGroups=etsysMACLockingGroups, etsysMACLockingStationGroup=etsysMACLockingStationGroup, etsysMACLockingStaticStationsAllowed=etsysMACLockingStaticStationsAllowed, etsysMACLockingLockedAddress=etsysMACLockingLockedAddress, etsysMACLockingMIB=etsysMACLockingMIB, etsysMACLockingConformance=etsysMACLockingConformance, etsysMACLockingStaticStationsAllocated=etsysMACLockingStaticStationsAllocated, etsysMACLockingStationEntry=etsysMACLockingStationEntry, etsysMACLockingPortMessageGroup=etsysMACLockingPortMessageGroup, etsysMACLockingStationGroup2=etsysMACLockingStationGroup2, etsysMACLockingStaticStationEntry=etsysMACLockingStaticStationEntry, etsysMACLockingNotificationGroup=etsysMACLockingNotificationGroup, etsysMACLockingEnable=etsysMACLockingEnable, etsysMACLockingObjects=etsysMACLockingObjects, etsysMACLockingClearStaticStations=etsysMACLockingClearStaticStations, etsysMACLockingStaticStationTable=etsysMACLockingStaticStationTable, etsysMACLockingNotificationCompliance=etsysMACLockingNotificationCompliance, etsysMACLockingThresholdSyslogEnable=etsysMACLockingThresholdSyslogEnable, etsysMACLockingCompliances=etsysMACLockingCompliances, etsysMACLockingPortGroup=etsysMACLockingPortGroup, etsysMACLockingStaticStationGroup=etsysMACLockingStaticStationGroup, etsysMACLockingRemoveStation=etsysMACLockingRemoveStation, etsysMACLockingTrapBranch=etsysMACLockingTrapBranch, etsysMACLockingMoveFirstArrivalToStatic=etsysMACLockingMoveFirstArrivalToStatic, etsysMACLockingLockedEntryCause=etsysMACLockingLockedEntryCause, etsysMACLockingStaticStationBranch=etsysMACLockingStaticStationBranch, etsysMACLockingSystemEnable=etsysMACLockingSystemEnable, etsysMACLockingStaticEntryRowStatus=etsysMACLockingStaticEntryRowStatus, etsysMACLockingPortTable=etsysMACLockingPortTable, etsysMACLockingLastViolationAddress=etsysMACLockingLastViolationAddress, etsysMACLockingPortFirstArrivalCompliance=etsysMACLockingPortFirstArrivalCompliance, etsysMACLockingStationTable=etsysMACLockingStationTable, etsysMACLockingPort=etsysMACLockingPort, etsysMACLockingFirstArrivalStationsAllowed=etsysMACLockingFirstArrivalStationsAllowed, etsysMACLockingFirstArrivalAging=etsysMACLockingFirstArrivalAging, etsysMACLockingCompliance=etsysMACLockingCompliance, PYSNMP_MODULE_ID=etsysMACLockingMIB, etsysMACLockingPortEntry=etsysMACLockingPortEntry, etsysMACLockingFirstArrivalStationsAllocated=etsysMACLockingFirstArrivalStationsAllocated, etsysMACLockingViolationSyslogEnable=etsysMACLockingViolationSyslogEnable, etsysMACLockingSystemGroup=etsysMACLockingSystemGroup, etsysMACLockingStaticStationsCount=etsysMACLockingStaticStationsCount, etsysMACLockingMACViolation=etsysMACLockingMACViolation, etsysMACLockingCompliance2=etsysMACLockingCompliance2, etsysMACLockingPortConfigBranch=etsysMACLockingPortConfigBranch, etsysMACLockingMACThreshold=etsysMACLockingMACThreshold, etsysMACLockingPortFirstArrivalGroup=etsysMACLockingPortFirstArrivalGroup, etsysMACLockingViolationEnable=etsysMACLockingViolationEnable, etsysMACLockingSystemBranch=etsysMACLockingSystemBranch)
