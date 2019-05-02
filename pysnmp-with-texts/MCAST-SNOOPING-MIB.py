#
# PySNMP MIB module MCAST-SNOOPING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MCAST-SNOOPING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:10:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, TimeTicks, ObjectIdentity, MibIdentifier, IpAddress, Unsigned32, Integer32, Bits, Counter64, NotificationType, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "TimeTicks", "ObjectIdentity", "MibIdentifier", "IpAddress", "Unsigned32", "Integer32", "Bits", "Counter64", "NotificationType", "iso", "Counter32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
swMcastSnoopingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 73))
if mibBuilder.loadTexts: swMcastSnoopingMIB.setLastUpdated('200810240000Z')
if mibBuilder.loadTexts: swMcastSnoopingMIB.setOrganization('D-Link Corp.')
if mibBuilder.loadTexts: swMcastSnoopingMIB.setContactInfo('http://support.dlink.com')
if mibBuilder.loadTexts: swMcastSnoopingMIB.setDescription('The structure of IGMP&MLD snooping for the proprietary enterprise.')
class Ipv6Address(TextualConvention, OctetString):
    description = 'This data type is used to model IPv6 addresses. This is a binary string of 16 octets in network byte-order.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

swMcastSnoopingCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 73, 1))
swMcastSnoopingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 73, 2))
swMcastSnoopingMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 73, 3))
swIGMPSnoopingGlobalState = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 73, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnoopingGlobalState.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingGlobalState.setDescription('This indicates the global state of IGMP snooping.')
swIGMPSnoopingMaxDataDrivenLearningCount = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 73, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnoopingMaxDataDrivenLearningCount.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingMaxDataDrivenLearningCount.setDescription('This indicates the Max Data Driven Learning Count of the IGMP snooping.')
swIGMPSnoopingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1))
swIGMPSnoopingForwardingTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1), )
if mibBuilder.loadTexts: swIGMPSnoopingForwardingTable.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingForwardingTable.setDescription('This contains information about the IGMP snooping forwarding info table.')
swIGMPSnoopingForwardingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1, 1), ).setIndexNames((0, "MCAST-SNOOPING-MIB", "swIGMPSnoopingVlanID"), (0, "MCAST-SNOOPING-MIB", "swIGMPSnpFwdSrcAddr"), (0, "MCAST-SNOOPING-MIB", "swIGMPSnpFwdGrpAddr"))
if mibBuilder.loadTexts: swIGMPSnoopingForwardingEntry.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingForwardingEntry.setDescription('This is an entry of the swIGMPSnoopingForwardingTable.')
swIGMPSnoopingVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnoopingVlanID.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingVlanID.setDescription('This indicates the VLAN ID of the IGMP snooping forwarding entry.')
swIGMPSnpFwdSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpFwdSrcAddr.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpFwdSrcAddr.setDescription('This indicates the source IP Address of the IGMP snooping forwarding entry.')
swIGMPSnpFwdGrpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpFwdGrpAddr.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpFwdGrpAddr.setDescription('This indicates the group IP Address of the IGMP snooping forwarding entry.')
swIGMPSnpFwdMemberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 1, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpFwdMemberPorts.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpFwdMemberPorts.setDescription('This indicates the member port list of the IGMP snooping forwarding entry.')
swIGMPSnoopingGroupTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2), )
if mibBuilder.loadTexts: swIGMPSnoopingGroupTable.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingGroupTable.setDescription('This contains information about the IGMP snooping group info table. This table only shows dynamic groups (including data driven learning groups), to show static groups, the swIGMPSnoopingStaticGroupTable should be used.')
swIGMPSnoopingGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1), ).setIndexNames((0, "MCAST-SNOOPING-MIB", "swIGMPSnoopingVlanID"), (0, "MCAST-SNOOPING-MIB", "swIGMPSnpGrpSrcAddr"), (0, "MCAST-SNOOPING-MIB", "swIGMPSnpGrpGrpAddr"))
if mibBuilder.loadTexts: swIGMPSnoopingGroupEntry.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingGroupEntry.setDescription('This is an entry of the swIGMPSnoopingGroupTable.')
swIGMPSnpGrpSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpGrpSrcAddr.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpGrpSrcAddr.setDescription('This indicates the source IP Address of the IGMP snooping group entry.')
swIGMPSnpGrpGrpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpGrpGrpAddr.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpGrpGrpAddr.setDescription('This indicates the group IP Address of the IGMP snooping group entry.')
swIGMPSnpGrpIncludeMemberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 3), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpGrpIncludeMemberPorts.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpGrpIncludeMemberPorts.setDescription('This indicates the list of member ports in Include mode for the IGMP snooping group entry. For data driven groups, this object should be 0. ')
swIGMPSnpGrpExcludeMemberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpGrpExcludeMemberPorts.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpGrpExcludeMemberPorts.setDescription('This indicates the list of member ports in Exclude mode for the IGMP snooping group entry. For data driven groups, this object should be 0. ')
swIGMPSnpGrpRouterPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 5), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpGrpRouterPorts.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpGrpRouterPorts.setDescription('This indicates the router port list of the IGMP snooping group entry. This is only used for data driven learning groups. For normal groups, this object should be 0.')
swIGMPSnpGrpUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpGrpUpTime.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpGrpUpTime.setDescription('This indicates the time passed since this group was created. ')
swIGMPSnpGrpExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpGrpExpiryTime.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpGrpExpiryTime.setDescription('This indicates the time left until this group will be deleted. ')
swIGMPSnpGrpReportCount = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 1, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpGrpReportCount.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpGrpReportCount.setDescription('This indicates the number of reports received for this group entry. ')
swMLDSnoopingInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2))
swMLDSnoopingForwardingTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1), )
if mibBuilder.loadTexts: swMLDSnoopingForwardingTable.setStatus('current')
if mibBuilder.loadTexts: swMLDSnoopingForwardingTable.setDescription('This contains information about the MLD snooping forwarding info table.')
swMLDSnoopingForwardingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1, 1), ).setIndexNames((0, "MCAST-SNOOPING-MIB", "swMLDSnoopingVlanID"), (0, "MCAST-SNOOPING-MIB", "swMLDSnpFwdSrcAddr"), (0, "MCAST-SNOOPING-MIB", "swMLDSnpFwdGrpAddr"))
if mibBuilder.loadTexts: swMLDSnoopingForwardingEntry.setStatus('current')
if mibBuilder.loadTexts: swMLDSnoopingForwardingEntry.setDescription('This is an entry of the swMLDSnoopingForwardingTable.')
swMLDSnoopingVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMLDSnoopingVlanID.setStatus('current')
if mibBuilder.loadTexts: swMLDSnoopingVlanID.setDescription('This indicates the VLAN ID of the MLD snooping forwarding entry.')
swMLDSnpFwdSrcAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1, 1, 2), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMLDSnpFwdSrcAddr.setStatus('current')
if mibBuilder.loadTexts: swMLDSnpFwdSrcAddr.setDescription('This indicates the source IP Address of the MLD snooping forwarding entry.')
swMLDSnpFwdGrpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1, 1, 3), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMLDSnpFwdGrpAddr.setStatus('current')
if mibBuilder.loadTexts: swMLDSnpFwdGrpAddr.setDescription('This indicates the group IP Address of the MLD snooping forwarding entry.')
swMLDSnpFwdMemberPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 1, 1, 4), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMLDSnpFwdMemberPorts.setStatus('current')
if mibBuilder.loadTexts: swMLDSnpFwdMemberPorts.setDescription('This indicates the member port list of the MLD snooping forwarding entry.')
swMLDSnoopingVlanStatisticCounterTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 3), )
if mibBuilder.loadTexts: swMLDSnoopingVlanStatisticCounterTable.setStatus('current')
if mibBuilder.loadTexts: swMLDSnoopingVlanStatisticCounterTable.setDescription('This contains information about the MLD snooping VLAN statistic counter info table.')
swMLDSnoopingVlanStatisticCounterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 3, 1), ).setIndexNames((0, "MCAST-SNOOPING-MIB", "swMLDSnoopingVlanID"))
if mibBuilder.loadTexts: swMLDSnoopingVlanStatisticCounterEntry.setStatus('current')
if mibBuilder.loadTexts: swMLDSnoopingVlanStatisticCounterEntry.setDescription('This is an entry of the swMLDSnoopingVlanStatisticCounterTable.')
swMLDSnpVlanCounterTotalRxQuery = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 2, 2, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swMLDSnpVlanCounterTotalRxQuery.setStatus('current')
if mibBuilder.loadTexts: swMLDSnpVlanCounterTotalRxQuery.setDescription('This indicates the total count of received MLD Query packets in this VLAN.')
swIGMPSnoopingMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1))
swIGMPSnoopingCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1), )
if mibBuilder.loadTexts: swIGMPSnoopingCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingCtrlTable.setDescription("The table controls the VLAN's IGMP Snooping function.")
swIGMPSnoopingCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1), ).setIndexNames((0, "MCAST-SNOOPING-MIB", "swIGMPSnoopingVlanID"))
if mibBuilder.loadTexts: swIGMPSnoopingCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingCtrlEntry.setDescription('This is an entry of the swIGMPSnoopingCtrlTable.')
swIGMPSnpCtrlQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpCtrlQueryInterval.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlQueryInterval.setDescription('This indicates the Query Interval of the IGMP snooping in this VLAN. The default value is 125.')
swIGMPSnpCtrlMaxResponseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpCtrlMaxResponseTime.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlMaxResponseTime.setDescription('This indicates the Max Response Time of the IGMP snooping in this VLAN. The default value is 10.')
swIGMPSnpCtrlRobustnessValue = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpCtrlRobustnessValue.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlRobustnessValue.setDescription('This indicates the Robustness Value of the IGMP snooping in this VLAN. The default value is 2.')
swIGMPSnpCtrlLastMemberQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpCtrlLastMemberQueryInterval.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlLastMemberQueryInterval.setDescription('This indicates the Last Member Query Interval of the IGMP snooping in this VLAN. The default value is 1.')
swIGMPSnpCtrlQuerierState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpCtrlQuerierState.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlQuerierState.setDescription('This indicates the IGMP snooping state of this VLAN.')
swIGMPSnpCtrlQuerierRole = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 30), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("querier", 1), ("non-querier", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpCtrlQuerierRole.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlQuerierRole.setDescription('This indicates the Querier role of this VLAN.')
swIGMPSnpCtrlQuerierIP = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 35), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpCtrlQuerierIP.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlQuerierIP.setDescription("This indicates the Querier's IP address of the IGMP snooping in this VLAN.")
swIGMPSnpCtrlQuerierExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 40), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpCtrlQuerierExpiryTime.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlQuerierExpiryTime.setDescription('This indicates the Querier Expiry Time of this VLAN.')
swIGMPSnpCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 45), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpCtrlState.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlState.setDescription('This indicates the IGMP Snooping State of this VLAN.')
swIGMPSnpCtrlFastLeaveState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpCtrlFastLeaveState.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlFastLeaveState.setDescription('This indicates the Fast Leave State of this VLAN.')
swIGMPSnpCtrlVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("version-1", 1), ("version-2", 2), ("version-3", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpCtrlVersion.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlVersion.setDescription('This indicates the Version of IGMP Snooping in this VLAN.')
swIGMPSnpCtrlDataDrivenLearningAgedOutState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 1, 1, 70), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpCtrlDataDrivenLearningAgedOutState.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpCtrlDataDrivenLearningAgedOutState.setDescription('This indicates the Data Driven Learning Aged Out State of this VLAN.')
swIGMPSnoopingDataDrivenLearningGroupTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3), )
if mibBuilder.loadTexts: swIGMPSnoopingDataDrivenLearningGroupTable.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingDataDrivenLearningGroupTable.setDescription("The table controls the VLAN's IGMP Snooping data driven learning group function.")
swIGMPSnoopingDataDrivenLearningGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1), ).setIndexNames((0, "MCAST-SNOOPING-MIB", "swIGMPSnoopingVlanID"), (0, "MCAST-SNOOPING-MIB", "swIGMPSnpDataDrivenLearningGrpGrpAddr"))
if mibBuilder.loadTexts: swIGMPSnoopingDataDrivenLearningGroupEntry.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingDataDrivenLearningGroupEntry.setDescription('This is an entry of the swIGMPSnoopingDataDrivenLearningGroupTable.')
swIGMPSnpDataDrivenLearningGrpGrpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpDataDrivenLearningGrpGrpAddr.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpDataDrivenLearningGrpGrpAddr.setDescription('This indicates the group address of the IGMP snooping data driven learning group table.')
swIGMPSnpDataDrivenLearningGrpRouterPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpDataDrivenLearningGrpRouterPorts.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpDataDrivenLearningGrpRouterPorts.setDescription('This indicates the router port list of the IGMP snooping data driven learning group table.')
swIGMPSnpDataDrivenLearningGrpUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpDataDrivenLearningGrpUpTime.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpDataDrivenLearningGrpUpTime.setDescription('This indicates the time passed since this group was created. ')
swIGMPSnpDataDrivenLearningGrpExpiryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpDataDrivenLearningGrpExpiryTime.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpDataDrivenLearningGrpExpiryTime.setDescription('This indicates the time left before this group will be deleted. ')
swIGMPSnpDataDrivenLearningGrpClearGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 3, 1, 100), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("clear", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpDataDrivenLearningGrpClearGrp.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpDataDrivenLearningGrpClearGrp.setDescription('When set to clear, this data driven learning group will be deleted.')
swIGMPSnoopingRouterPortTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 4), )
if mibBuilder.loadTexts: swIGMPSnoopingRouterPortTable.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingRouterPortTable.setDescription("The table controls the VLAN's IGMP Snooping router port list function.")
swIGMPSnoopingRouterPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 4, 1), ).setIndexNames((0, "MCAST-SNOOPING-MIB", "swIGMPSnoopingVlanID"))
if mibBuilder.loadTexts: swIGMPSnoopingRouterPortEntry.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnoopingRouterPortEntry.setDescription('This is an entry of the swIGMPSnoopingRouterPortTable.')
swIGMPSnpStaticRouterPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 4, 1, 5), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpStaticRouterPorts.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpStaticRouterPorts.setDescription('This indicates the static router port list of the IGMP snooping router ports table.')
swIGMPSnpDynamicRouterPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 4, 1, 10), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swIGMPSnpDynamicRouterPorts.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpDynamicRouterPorts.setDescription('This indicates the dynamic router port list of the IGMP snooping router ports table.')
swIGMPSnpForbiddenRouterPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 73, 3, 1, 4, 1, 15), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swIGMPSnpForbiddenRouterPorts.setStatus('current')
if mibBuilder.loadTexts: swIGMPSnpForbiddenRouterPorts.setDescription('This indicates the forbidden router port list of the IGMP snooping router ports table.')
mibBuilder.exportSymbols("MCAST-SNOOPING-MIB", swIGMPSnoopingRouterPortEntry=swIGMPSnoopingRouterPortEntry, swIGMPSnoopingGroupTable=swIGMPSnoopingGroupTable, swMLDSnoopingForwardingTable=swMLDSnoopingForwardingTable, swIGMPSnpDataDrivenLearningGrpClearGrp=swIGMPSnpDataDrivenLearningGrpClearGrp, swIGMPSnpGrpSrcAddr=swIGMPSnpGrpSrcAddr, swIGMPSnoopingMaxDataDrivenLearningCount=swIGMPSnoopingMaxDataDrivenLearningCount, swIGMPSnpGrpExcludeMemberPorts=swIGMPSnpGrpExcludeMemberPorts, swMLDSnoopingVlanID=swMLDSnoopingVlanID, swMLDSnoopingForwardingEntry=swMLDSnoopingForwardingEntry, swIGMPSnpCtrlState=swIGMPSnpCtrlState, swIGMPSnpCtrlVersion=swIGMPSnpCtrlVersion, swMcastSnoopingInfo=swMcastSnoopingInfo, swIGMPSnpCtrlFastLeaveState=swIGMPSnpCtrlFastLeaveState, swIGMPSnpCtrlLastMemberQueryInterval=swIGMPSnpCtrlLastMemberQueryInterval, swMLDSnoopingVlanStatisticCounterEntry=swMLDSnoopingVlanStatisticCounterEntry, swMcastSnoopingMIB=swMcastSnoopingMIB, swIGMPSnoopingInfo=swIGMPSnoopingInfo, swIGMPSnoopingVlanID=swIGMPSnoopingVlanID, swIGMPSnpGrpExpiryTime=swIGMPSnpGrpExpiryTime, swMLDSnoopingInfo=swMLDSnoopingInfo, swIGMPSnoopingCtrlTable=swIGMPSnoopingCtrlTable, swMcastSnoopingMgmt=swMcastSnoopingMgmt, swIGMPSnpGrpGrpAddr=swIGMPSnpGrpGrpAddr, swIGMPSnpGrpUpTime=swIGMPSnpGrpUpTime, swIGMPSnpForbiddenRouterPorts=swIGMPSnpForbiddenRouterPorts, swIGMPSnpCtrlDataDrivenLearningAgedOutState=swIGMPSnpCtrlDataDrivenLearningAgedOutState, swIGMPSnpStaticRouterPorts=swIGMPSnpStaticRouterPorts, swIGMPSnpCtrlQueryInterval=swIGMPSnpCtrlQueryInterval, swIGMPSnoopingGlobalState=swIGMPSnoopingGlobalState, swIGMPSnoopingMgmt=swIGMPSnoopingMgmt, swIGMPSnpGrpReportCount=swIGMPSnpGrpReportCount, swIGMPSnpCtrlQuerierState=swIGMPSnpCtrlQuerierState, swMLDSnoopingVlanStatisticCounterTable=swMLDSnoopingVlanStatisticCounterTable, swIGMPSnoopingForwardingEntry=swIGMPSnoopingForwardingEntry, swIGMPSnpCtrlQuerierIP=swIGMPSnpCtrlQuerierIP, swIGMPSnoopingDataDrivenLearningGroupEntry=swIGMPSnoopingDataDrivenLearningGroupEntry, swIGMPSnpCtrlRobustnessValue=swIGMPSnpCtrlRobustnessValue, swIGMPSnpCtrlQuerierExpiryTime=swIGMPSnpCtrlQuerierExpiryTime, PortList=PortList, swMLDSnpFwdGrpAddr=swMLDSnpFwdGrpAddr, swMLDSnpFwdMemberPorts=swMLDSnpFwdMemberPorts, PYSNMP_MODULE_ID=swMcastSnoopingMIB, swIGMPSnoopingRouterPortTable=swIGMPSnoopingRouterPortTable, swIGMPSnoopingDataDrivenLearningGroupTable=swIGMPSnoopingDataDrivenLearningGroupTable, Ipv6Address=Ipv6Address, swIGMPSnpFwdSrcAddr=swIGMPSnpFwdSrcAddr, swIGMPSnpDynamicRouterPorts=swIGMPSnpDynamicRouterPorts, swIGMPSnoopingGroupEntry=swIGMPSnoopingGroupEntry, swIGMPSnpFwdMemberPorts=swIGMPSnpFwdMemberPorts, swIGMPSnpDataDrivenLearningGrpRouterPorts=swIGMPSnpDataDrivenLearningGrpRouterPorts, swIGMPSnpCtrlMaxResponseTime=swIGMPSnpCtrlMaxResponseTime, swIGMPSnoopingCtrlEntry=swIGMPSnoopingCtrlEntry, swIGMPSnpCtrlQuerierRole=swIGMPSnpCtrlQuerierRole, swIGMPSnpDataDrivenLearningGrpGrpAddr=swIGMPSnpDataDrivenLearningGrpGrpAddr, swIGMPSnpDataDrivenLearningGrpExpiryTime=swIGMPSnpDataDrivenLearningGrpExpiryTime, swIGMPSnpGrpIncludeMemberPorts=swIGMPSnpGrpIncludeMemberPorts, swMcastSnoopingCtrl=swMcastSnoopingCtrl, swMLDSnpVlanCounterTotalRxQuery=swMLDSnpVlanCounterTotalRxQuery, swIGMPSnpDataDrivenLearningGrpUpTime=swIGMPSnpDataDrivenLearningGrpUpTime, swMLDSnpFwdSrcAddr=swMLDSnpFwdSrcAddr, swIGMPSnpGrpRouterPorts=swIGMPSnpGrpRouterPorts, swIGMPSnpFwdGrpAddr=swIGMPSnpFwdGrpAddr, swIGMPSnoopingForwardingTable=swIGMPSnoopingForwardingTable)
