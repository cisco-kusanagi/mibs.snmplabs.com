#
# PySNMP MIB module HP-ICF-SMART-LINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-SMART-LINK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:35:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
VlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
IpAddress, iso, Integer32, Gauge32, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, Counter64, MibIdentifier, Bits, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "Integer32", "Gauge32", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "Counter64", "MibIdentifier", "Bits", "Unsigned32", "Counter32")
DisplayString, TextualConvention, MacAddress, DateAndTime, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress", "DateAndTime", "TruthValue", "RowStatus")
hpicfSmartLinkMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96))
hpicfSmartLinkMIB.setRevisions(('2013-03-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpicfSmartLinkMIB.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: hpicfSmartLinkMIB.setLastUpdated('201303200000Z')
if mibBuilder.loadTexts: hpicfSmartLinkMIB.setOrganization('HP Networking')
if mibBuilder.loadTexts: hpicfSmartLinkMIB.setContactInfo('Hewlett-Packard Company 8000 Foothills Blvd. Roseville, CA 95747')
if mibBuilder.loadTexts: hpicfSmartLinkMIB.setDescription('This MIB module provides information about Smart link feature. Smart link group is a pair of Layer 2 interfaces, where one of the interfaces is configured as master and other acts as slave. The feature provides an alternative solution to the Spanning Tree Protocol (STP). Smart link is typically configured in service provider or enterprise networks where users do not want to run STP on the device.')
hpicfSmartLinkNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 0))
hpicfSmartLinkObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1))
hpicfSmartLinkConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2))
hpicfSmartLinkFlushStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1))
hpicfSmartLinkLastFlushTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1, 1), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkLastFlushTime.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkLastFlushTime.setDescription('Time when last flush packet was received. An empty string indicates that flush packets are not received. This object will be set to empty string when hpicfSmartLinkResetFlushStatistics is set to true (1).')
hpicfSmartLinkTotalFlushPktsRx = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkTotalFlushPktsRx.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkTotalFlushPktsRx.setDescription('Total number of flush packets received.')
hpicfSmartLinkLastFlushPort = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkLastFlushPort.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkLastFlushPort.setDescription('Port on which last flush packet was received. A value of 0 (zero) indicates that flush packets are not received. This object will be set to 0 (zero) when hpicfSmartLinkResetFlushStatistics is set to true (1).')
hpicfSmartLinkLastFlushDeviceId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkLastFlushDeviceId.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkLastFlushDeviceId.setDescription('Device ID from last received flush packet. An empty string indicates that flush packets are not received. This object will be set to empty string when hpicfSmartLinkResetFlushStatistics is set to true (1).')
hpicfSmartLinkLastFlushVlan = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 1, 5), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkLastFlushVlan.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkLastFlushVlan.setDescription('The control VLAN of the last received flush packet. A value of 0 (zero) indicates that flush packets are not received. This object will be set to 0(zero) when hpicfSmartLinkResetFlushStatistics is set to true (1).')
hpicfSmartLinkResetFlushStatistics = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfSmartLinkResetFlushStatistics.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkResetFlushStatistics.setDescription('Set this to true(1) to reset the flush packet statistics. This MIB object will always return false(2) upon read.')
hpicfSmartLinkGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3), )
if mibBuilder.loadTexts: hpicfSmartLinkGroupTable.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupTable.setDescription('This table allows user to configure Smart link groups.')
hpicfSmartLinkGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1), ).setIndexNames((0, "HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupIndex"))
if mibBuilder.loadTexts: hpicfSmartLinkGroupEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupEntry.setDescription('An entry containing information about a Smart link group.')
hpicfSmartLinkGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpicfSmartLinkGroupIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupIndex.setDescription('The Object which uniquely identifies the Smart link group.')
hpicfSmartLinkGroupMasterPort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupMasterPort.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupMasterPort.setDescription('This object is used to configure master port of this group. The value of 0 (zero) indicates that master port is not configured for this group.')
hpicfSmartLinkGroupSlavePort = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupSlavePort.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupSlavePort.setDescription('This object is used to configure slave port of this group. The value of 0 (zero) indicates that slave port is not configured for this group.')
hpicfSmartLinkGroupSendControlVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 4), VlanIndex().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupSendControlVlan.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupSendControlVlan.setDescription('The object indicates the VLAN on which the flush packets are sent for this group.')
hpicfSmartLinkGroupPreemptionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("role", 2))).clone('off')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupPreemptionMode.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupPreemptionMode.setDescription('The object specifies the preemption mechanism for this group. off(1) - No preemption happens from master to slave. role(2) - The master always preempts to slave after the time specified in hpicfSmartLinkGroupPreemptionDelay.')
hpicfSmartLinkGroupPreemptionDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupPreemptionDelay.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupPreemptionDelay.setDescription('The delay time, in seconds, until standby preempts active on this group.')
hpicfSmartLinkGroupProtectedVlan1k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupProtectedVlan1k.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupProtectedVlan1k.setDescription('A string of octets containing one bit per protected VLAN from VLAN IDs 1 to 1024. The first octet corresponds to VLAN IDs 1 through 8, the second octet to VLAN IDs 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered VLAN ID, and the least significant bit represents the highest numbered VLAN ID.')
hpicfSmartLinkGroupProtectedVlan2k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupProtectedVlan2k.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupProtectedVlan2k.setDescription('A string of octets containing one bit per protected VLAN from VLAN IDs 1025 to 2048. The first octet corresponds to VLAN IDs 1025 through 1032, the second octet to VLAN IDs 1033 through 1040, etc. Within each octet, the most significant bit represents the lowest numbered VLAN ID, and the least significant bit represents the highest numbered VLAN ID.')
hpicfSmartLinkGroupProtectedVlan3k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupProtectedVlan3k.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupProtectedVlan3k.setDescription('A string of octets containing one bit per protected VLAN from VLAN IDs 2049 to 3072. The first octet corresponds to VLAN IDs 2049 through 2056, the second octet to VLAN IDs 2057 through 2064, etc. Within each octet, the most significant bit represents the lowest numbered VLAN ID, and the least significant bit represents the highest numbered VLAN ID.')
hpicfSmartLinkGroupProtectedVlan4k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupProtectedVlan4k.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupProtectedVlan4k.setDescription('A string of octets containing one bit per protected VLAN from VLAN IDs 3073 to 4094. The first octet corresponds to VLAN IDs 3073 through 3080, the second octet to VLAN IDs 3081 through 3088, etc. Within each octet, the most significant bit represents the lowest numbered VLAN ID, and the least significant bit represents the highest numbered VLAN ID.')
hpicfSmartLinkGroupTrapControl = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupTrapControl.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupTrapControl.setDescription('Setting this object to the value of true(1) allows the system to send hpicfSmartLinkPortRoleChangeNotification trap whenever standby link takes over active link.')
hpicfSmartLinkGroupClearStats = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 12), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupClearStats.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupClearStats.setDescription('Setting this object to the value of true(1) clears the group statistics. This object will always return false(2).')
hpicfSmartLinkGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 3, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupRowStatus.setDescription("Status of the row in hpicfSmartLinkGroupTable. This object must be set to 'creatAndGo' to create an entry and set to 'destroy' to delete an entry. The columns can be modified only when the RowStatus is 'active'.")
hpicfSmartLinkExtendedGroupTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4), )
if mibBuilder.loadTexts: hpicfSmartLinkExtendedGroupTable.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkExtendedGroupTable.setDescription('This table contains information of Smart link groups.')
hpicfSmartLinkExtendedGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1), )
hpicfSmartLinkGroupEntry.registerAugmentions(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkExtendedGroupEntry"))
hpicfSmartLinkExtendedGroupEntry.setIndexNames(*hpicfSmartLinkGroupEntry.getIndexNames())
if mibBuilder.loadTexts: hpicfSmartLinkExtendedGroupEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkExtendedGroupEntry.setDescription('An entry containing information about a Smart link group.')
hpicfSmartLinkGroupMasterPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("uninitialized", 1), ("active", 2), ("standby", 3), ("down", 4))).clone('uninitialized')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkGroupMasterPortState.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupMasterPortState.setDescription("The status of an interface participating in Smart link operation. uninitialized (1) - A value of 'uninitialized' indicates that, the interface is not configured. active(2) - A value of 'active' indicates that, the interface is actively forwarding traffic. standby(3) - A value of 'standby' indicates that, the interface is ready to forward traffic if the active interface goes down. down(4) - A value of 'down' indicates that, the interface is physically down. ")
hpicfSmartLinkGroupSlavePortState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("uninitialized", 1), ("active", 2), ("standby", 3), ("down", 4))).clone('uninitialized')).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkGroupSlavePortState.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupSlavePortState.setDescription("The status of an interface participating in Smart link operation. uninitialized (1) - A value of ' uninitialized ' indicates that, the interface is not configured. active(2) - A value of 'active' indicates that, the interface is actively forwarding traffic. standby(3) - A value of 'standby' indicates that, the interface is ready to forward traffic if the active interface goes down. down(4) - A value of 'down' indicates that, the interface is physically down.")
hpicfSmartLinkMasterFlushPktTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkMasterFlushPktTx.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkMasterFlushPktTx.setDescription('Number of flush packets sent on master port.')
hpicfSmartLinkMasterFlushPktLastUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkMasterFlushPktLastUpdate.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkMasterFlushPktLastUpdate.setDescription('This MIB object indicates the time at which the last flush packet was sent on master port.')
hpicfSmartLinkSlaveFlushPktTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkSlaveFlushPktTx.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkSlaveFlushPktTx.setDescription('Number of flush packets sent on slave port.')
hpicfSmartLinkSlaveFlushPktLastUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 4, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfSmartLinkSlaveFlushPktLastUpdate.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkSlaveFlushPktLastUpdate.setDescription('This MIB object indicates the time at which the last flush packet was sent on slave port.')
hpicfSmartLinkPortTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5), )
if mibBuilder.loadTexts: hpicfSmartLinkPortTable.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkPortTable.setDescription('This table allows user to configure Smart link port attributes.')
hpicfSmartLinkPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1), ).setIndexNames((0, "HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkPortIndex"))
if mibBuilder.loadTexts: hpicfSmartLinkPortEntry.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkPortEntry.setDescription('An entry, containing configuration information of a Smart link port. An entry will be created when receive control VLANs are configured for this port.')
hpicfSmartLinkPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpicfSmartLinkPortIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkPortIndex.setDescription('The port which uniquely identifies a row in this entry')
hpicfSmartLinkRecvControlVlans1k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkRecvControlVlans1k.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkRecvControlVlans1k.setDescription('A string of octets containing one bit per protected VLAN from VLAN IDs 1 to 1024. The first octet corresponds to VLAN IDs 1 through 8, the second octet to VLAN IDs 9 through 16, etc. Within each octet, the most significant bit represents the lowest numbered VLAN ID, and the least significant bit represents the highest numbered VLAN ID.')
hpicfSmartLinkRecvControlVlans2k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkRecvControlVlans2k.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkRecvControlVlans2k.setDescription('A string of octets containing one bit per protected VLAN from VLAN IDs 1025 to 2048. The first octet corresponds to VLAN IDs 1025 through 1032, the second octet to VLAN IDs 1033 through 1040, etc. Within each octet, the most significant bit represents the lowest numbered VLAN ID, and the least significant bit represents the highest numbered VLAN ID.')
hpicfSmartLinkRecvControlVlans3k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkRecvControlVlans3k.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkRecvControlVlans3k.setDescription('A string of octets containing one bit per protected VLAN from VLAN IDs 2049 to 3072. The first octet corresponds to VLAN IDs 2049 through 2056, the second octet to VLAN IDs 2057 through 2064, etc. Within each octet, the most significant bit represents the lowest numbered VLAN ID, and the least significant bit represents the highest numbered VLAN ID.')
hpicfSmartLinkRecvControlVlans4k = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkRecvControlVlans4k.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkRecvControlVlans4k.setDescription('A string of octets containing one bit per protected VLAN from VLAN IDs 3073 to 4094. The first octet corresponds to VLAN IDs 3073 through 3080, the second octet to VLAN IDs 3081 through 3088, etc. Within each octet, the most significant bit represents the lowest numbered VLAN ID, and the least significant bit represents the highest numbered VLAN ID.')
hpicfSmartLinkPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 1, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfSmartLinkPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkPortRowStatus.setDescription("Status of the row in hpicfSmartLinkPortTable. This object must be set to 'creatAndGo' to create an entry and set to 'destroy' to delete an entry. The columns can be modified only when the rowstatus is 'active'.")
hpicfSmartLinkNotifyGroupIndex = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 0, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfSmartLinkNotifyGroupIndex.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkNotifyGroupIndex.setDescription('The object which uniquely identifies the Smart link group.')
hpicfSmartLinkPortStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 0, 2)).setObjects(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkNotifyGroupIndex"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupMasterPortState"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupSlavePortState"))
if mibBuilder.loadTexts: hpicfSmartLinkPortStateChangeNotification.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkPortStateChangeNotification.setDescription('A hpicfSmartLinkPortStateChangeNotification is generated when standby port transits to active state.')
hpicfSmartLinkConformanceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1))
hpicfSmartLinkCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 2))
hpicfSmartLinkCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 2, 1)).setObjects(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGlobalGroup"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupsGroup"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkPortGroup"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkNotificationGroup"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkNotificationObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSmartLinkCompliance1 = hpicfSmartLinkCompliance1.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkCompliance1.setDescription('The compliance statement')
hpicfSmartLinkGlobalGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1, 1)).setObjects(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkTotalFlushPktsRx"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkLastFlushPort"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkLastFlushTime"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkLastFlushDeviceId"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkLastFlushVlan"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkResetFlushStatistics"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSmartLinkGlobalGroup = hpicfSmartLinkGlobalGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGlobalGroup.setDescription('These objects contains Smart link global statistics.')
hpicfSmartLinkGroupsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1, 2)).setObjects(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupMasterPort"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupSlavePort"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupSendControlVlan"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupPreemptionMode"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupPreemptionDelay"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupProtectedVlan1k"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupProtectedVlan2k"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupProtectedVlan3k"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupProtectedVlan4k"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupTrapControl"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupClearStats"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupMasterPortState"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupSlavePortState"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkMasterFlushPktTx"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkMasterFlushPktLastUpdate"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkSlaveFlushPktTx"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkSlaveFlushPktLastUpdate"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkGroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSmartLinkGroupsGroup = hpicfSmartLinkGroupsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkGroupsGroup.setDescription('These objects are used for managing and monitoring Smart link groups.')
hpicfSmartLinkPortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1, 3)).setObjects(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkRecvControlVlans1k"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkRecvControlVlans2k"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkRecvControlVlans3k"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkRecvControlVlans4k"), ("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkPortRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSmartLinkPortGroup = hpicfSmartLinkPortGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkPortGroup.setDescription('These objects are used for managing and monitoring Smart link interfaces.')
hpicfSmartLinkNotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1, 4)).setObjects(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkNotifyGroupIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSmartLinkNotificationObjectsGroup = hpicfSmartLinkNotificationObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkNotificationObjectsGroup.setDescription('Group of objects required to control traps for Smart link interfaces.')
hpicfSmartLinkNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 96, 2, 1, 5)).setObjects(("HP-ICF-SMART-LINK-MIB", "hpicfSmartLinkPortStateChangeNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfSmartLinkNotificationGroup = hpicfSmartLinkNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: hpicfSmartLinkNotificationGroup.setDescription('Group of notifications for Smart link interfaces.')
mibBuilder.exportSymbols("HP-ICF-SMART-LINK-MIB", hpicfSmartLinkConformance=hpicfSmartLinkConformance, hpicfSmartLinkRecvControlVlans1k=hpicfSmartLinkRecvControlVlans1k, hpicfSmartLinkExtendedGroupTable=hpicfSmartLinkExtendedGroupTable, hpicfSmartLinkPortStateChangeNotification=hpicfSmartLinkPortStateChangeNotification, hpicfSmartLinkGroupProtectedVlan4k=hpicfSmartLinkGroupProtectedVlan4k, hpicfSmartLinkNotifications=hpicfSmartLinkNotifications, hpicfSmartLinkTotalFlushPktsRx=hpicfSmartLinkTotalFlushPktsRx, hpicfSmartLinkGroupSlavePort=hpicfSmartLinkGroupSlavePort, hpicfSmartLinkGroupTable=hpicfSmartLinkGroupTable, hpicfSmartLinkGroupPreemptionDelay=hpicfSmartLinkGroupPreemptionDelay, hpicfSmartLinkGroupMasterPortState=hpicfSmartLinkGroupMasterPortState, hpicfSmartLinkResetFlushStatistics=hpicfSmartLinkResetFlushStatistics, hpicfSmartLinkNotifyGroupIndex=hpicfSmartLinkNotifyGroupIndex, hpicfSmartLinkRecvControlVlans3k=hpicfSmartLinkRecvControlVlans3k, hpicfSmartLinkPortEntry=hpicfSmartLinkPortEntry, hpicfSmartLinkGroupEntry=hpicfSmartLinkGroupEntry, hpicfSmartLinkMasterFlushPktLastUpdate=hpicfSmartLinkMasterFlushPktLastUpdate, hpicfSmartLinkGroupTrapControl=hpicfSmartLinkGroupTrapControl, hpicfSmartLinkGroupIndex=hpicfSmartLinkGroupIndex, hpicfSmartLinkLastFlushDeviceId=hpicfSmartLinkLastFlushDeviceId, hpicfSmartLinkRecvControlVlans4k=hpicfSmartLinkRecvControlVlans4k, hpicfSmartLinkLastFlushVlan=hpicfSmartLinkLastFlushVlan, hpicfSmartLinkGroupSlavePortState=hpicfSmartLinkGroupSlavePortState, hpicfSmartLinkGlobalGroup=hpicfSmartLinkGlobalGroup, hpicfSmartLinkNotificationGroup=hpicfSmartLinkNotificationGroup, hpicfSmartLinkGroupClearStats=hpicfSmartLinkGroupClearStats, hpicfSmartLinkGroupProtectedVlan3k=hpicfSmartLinkGroupProtectedVlan3k, hpicfSmartLinkSlaveFlushPktLastUpdate=hpicfSmartLinkSlaveFlushPktLastUpdate, PYSNMP_MODULE_ID=hpicfSmartLinkMIB, hpicfSmartLinkPortTable=hpicfSmartLinkPortTable, hpicfSmartLinkPortIndex=hpicfSmartLinkPortIndex, hpicfSmartLinkNotificationObjectsGroup=hpicfSmartLinkNotificationObjectsGroup, hpicfSmartLinkConformanceGroups=hpicfSmartLinkConformanceGroups, hpicfSmartLinkGroupPreemptionMode=hpicfSmartLinkGroupPreemptionMode, hpicfSmartLinkGroupsGroup=hpicfSmartLinkGroupsGroup, hpicfSmartLinkPortGroup=hpicfSmartLinkPortGroup, hpicfSmartLinkGroupMasterPort=hpicfSmartLinkGroupMasterPort, hpicfSmartLinkGroupProtectedVlan2k=hpicfSmartLinkGroupProtectedVlan2k, hpicfSmartLinkSlaveFlushPktTx=hpicfSmartLinkSlaveFlushPktTx, hpicfSmartLinkGroupRowStatus=hpicfSmartLinkGroupRowStatus, hpicfSmartLinkCompliances=hpicfSmartLinkCompliances, hpicfSmartLinkRecvControlVlans2k=hpicfSmartLinkRecvControlVlans2k, hpicfSmartLinkFlushStatistics=hpicfSmartLinkFlushStatistics, hpicfSmartLinkGroupSendControlVlan=hpicfSmartLinkGroupSendControlVlan, hpicfSmartLinkExtendedGroupEntry=hpicfSmartLinkExtendedGroupEntry, hpicfSmartLinkLastFlushTime=hpicfSmartLinkLastFlushTime, hpicfSmartLinkMIB=hpicfSmartLinkMIB, hpicfSmartLinkLastFlushPort=hpicfSmartLinkLastFlushPort, hpicfSmartLinkObjects=hpicfSmartLinkObjects, hpicfSmartLinkMasterFlushPktTx=hpicfSmartLinkMasterFlushPktTx, hpicfSmartLinkPortRowStatus=hpicfSmartLinkPortRowStatus, hpicfSmartLinkCompliance1=hpicfSmartLinkCompliance1, hpicfSmartLinkGroupProtectedVlan1k=hpicfSmartLinkGroupProtectedVlan1k)
