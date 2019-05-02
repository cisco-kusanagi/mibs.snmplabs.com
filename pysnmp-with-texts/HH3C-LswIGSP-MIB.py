#
# PySNMP MIB module HH3C-LswIGSP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LswIGSP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:28:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
hh3clswCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3clswCommon")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, Bits, NotificationType, Unsigned32, MibIdentifier, ObjectIdentity, Gauge32, Counter32, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "Bits", "NotificationType", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Gauge32", "Counter32", "iso", "Counter64")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
hh3cLswIgmpsnoopingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7))
hh3cLswIgmpsnoopingMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cLswIgmpsnoopingMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hh3cLswIgmpsnoopingMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hh3cLswIgmpsnoopingMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cLswIgmpsnoopingMib.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cLswIgmpsnoopingMib.setDescription('')
class EnabledStatus(TextualConvention, Integer32):
    description = 'A simple status value for the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

hh3cLswIgmpsnoopingMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1))
hh3cIgmpSnoopingStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 1), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIgmpSnoopingStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingStatus.setDescription('Configure to enable IGMP Snooping.')
hh3cIgmpSnoopingRouterPortAge = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000)).clone(105)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIgmpSnoopingRouterPortAge.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingRouterPortAge.setDescription('Configure the aging time of the router port.')
hh3cIgmpSnoopingResponseTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 25)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIgmpSnoopingResponseTime.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingResponseTime.setDescription('Configure the maximum query response time.')
hh3cIgmpSnoopingHostTime = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(200, 1000)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIgmpSnoopingHostTime.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingHostTime.setDescription('Configure the aging time of the multicast group port.')
hh3cIgmpSnoopingGroupLimitTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 5), )
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupLimitTable.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupLimitTable.setDescription('The table lists the maximum group number that one interface could do IGMP Snooping.')
hh3cIgmpSnoopingGroupLimitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 5, 1), ).setIndexNames((0, "HH3C-LswIGSP-MIB", "hh3cIgmpSnoopingGroupIfIndex"))
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupLimitEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupLimitEntry.setDescription('An entry (conceptual row) representing the maximum group number on an interface which IGMP Snooping operation is enabled.')
hh3cIgmpSnoopingGroupIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 5, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupIfIndex.setDescription('The ifIndex value of the port on which IGMP snooping is enabled.')
hh3cIgmpSnoopingGroupLimitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 5, 1, 2), Unsigned32().clone(4294967295)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupLimitNumber.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupLimitNumber.setDescription('The maxmum group number of IGMP Snooping on a port.')
hh3cIgmpSnoopingFastLeaveTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 6), )
if mibBuilder.loadTexts: hh3cIgmpSnoopingFastLeaveTable.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingFastLeaveTable.setDescription('The table specifies the fast leave status on those ports that do IGMP Snooping.')
hh3cIgmpSnoopingFastLeaveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 6, 1), ).setIndexNames((0, "HH3C-LswIGSP-MIB", "hh3cIgmpSnoopingFastLeaveIfIndex"))
if mibBuilder.loadTexts: hh3cIgmpSnoopingFastLeaveEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingFastLeaveEntry.setDescription('An entry specifies the fast leave status on those ports that do IGMP Snooping.')
hh3cIgmpSnoopingFastLeaveIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 6, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hh3cIgmpSnoopingFastLeaveIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingFastLeaveIfIndex.setDescription('The ifIndex value of the port on which IGMP snooping is enabled.')
hh3cIgmpSnoopingFastLeaveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 6, 1, 2), EnabledStatus().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIgmpSnoopingFastLeaveStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingFastLeaveStatus.setDescription('The fast leave status of the port on which IGMP Snooping is enabled.')
hh3cIgmpSnoopingGroupPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7), )
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyTable.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyTable.setDescription('This is a table specifies the group policy parameter and Vlan ID of the IGMP Snooping port.')
hh3cIgmpSnoopingGroupPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7, 1), ).setIndexNames((0, "HH3C-LswIGSP-MIB", "hh3cIgmpSnoopingGroupPolicyIfIndex"), (0, "HH3C-LswIGSP-MIB", "hh3cIgmpSnoopingGroupPolicyVlanID"))
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyEntry.setDescription('An entry representing the group policy parameter and Vlan ID of a port on which IGMP Snooping operation is enabled.')
hh3cIgmpSnoopingGroupPolicyIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyIfIndex.setDescription('The ifIndex value of the port on which IGMP Snooping is enabled.')
hh3cIgmpSnoopingGroupPolicyVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyVlanID.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyVlanID.setDescription('The Vlan ID which the IGMP Snooping port is attached to.')
hh3cIgmpSnoopingGroupPolicyParameter = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2000, 2999))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyParameter.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyParameter.setDescription('The ACL Number which is used as the group policy parameter of the IGMP Snooping port.')
hh3cIgmpSnoopingGroupPolicyStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 7, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingGroupPolicyStatus.setDescription('This object is used to create or delete a row and represent the current status of this row. Now support three state:CreateAndGo,Active,Destroy.')
hh3cIgmpSnoopingNonFloodingStatus = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 8), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIgmpSnoopingNonFloodingStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingNonFloodingStatus.setDescription('Configure to disable multicast flooding when no member exists in the destinated group. To use this function,IGMP snooping must be enabled.')
hh3cIgmpSnoopingVlanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 9), )
if mibBuilder.loadTexts: hh3cIgmpSnoopingVlanStatusTable.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingVlanStatusTable.setDescription('The table used to enable or disable IGMP snooping on the specified VLAN.')
hh3cIgmpSnoopingVlanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 9, 1), ).setIndexNames((0, "HH3C-LswIGSP-MIB", "hh3cIgmpSnoopingVlanID"))
if mibBuilder.loadTexts: hh3cIgmpSnoopingVlanStatusEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingVlanStatusEntry.setDescription('An entry representing the IGMP snooping status on the specified VLAN.')
hh3cIgmpSnoopingVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094)))
if mibBuilder.loadTexts: hh3cIgmpSnoopingVlanID.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingVlanID.setDescription('An index uniquely identifies on which VLAN IGMP snooping is enabled or disabled. ')
hh3cIgmpSnoopingVlanEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 9, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIgmpSnoopingVlanEnabled.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingVlanEnabled.setDescription('Indicating whether IGMP snooping is enabled on this VLAN.')
hh3cIgmpSnoopingStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10))
hh3cRecvIGMPGQueryNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRecvIGMPGQueryNum.setStatus('current')
if mibBuilder.loadTexts: hh3cRecvIGMPGQueryNum.setDescription('The statistics of IGMP general query packets received on the device.')
hh3cRecvIGMPSQueryNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRecvIGMPSQueryNum.setStatus('current')
if mibBuilder.loadTexts: hh3cRecvIGMPSQueryNum.setDescription('The statistics of IGMP specific query packets received on the device.')
hh3cRecvIGMPV1ReportNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRecvIGMPV1ReportNum.setStatus('current')
if mibBuilder.loadTexts: hh3cRecvIGMPV1ReportNum.setDescription('The statistics of IGMP V1 report packets received on the device.')
hh3cRecvIGMPV2ReportNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRecvIGMPV2ReportNum.setStatus('current')
if mibBuilder.loadTexts: hh3cRecvIGMPV2ReportNum.setDescription('The statistics of IGMP V2 report packets received on the device.')
hh3cRecvIGMPLeaveNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRecvIGMPLeaveNum.setStatus('current')
if mibBuilder.loadTexts: hh3cRecvIGMPLeaveNum.setDescription('The statistics of IGMP leave packets received on the device.')
hh3cRecvErrorIGMPPacketNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cRecvErrorIGMPPacketNum.setStatus('current')
if mibBuilder.loadTexts: hh3cRecvErrorIGMPPacketNum.setDescription('The statistics of error IGMP packets received on the device.')
hh3cSentIGMPSQueryNum = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cSentIGMPSQueryNum.setStatus('current')
if mibBuilder.loadTexts: hh3cSentIGMPSQueryNum.setDescription('The statistics of IGMP specific query packets sent from the device.')
hh3cIgmpSnoopingClearStats = MibScalar((1, 3, 6, 1, 4, 1, 25506, 8, 35, 7, 1, 10, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("clear", 1), ("counting", 2))).clone('counting')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cIgmpSnoopingClearStats.setStatus('current')
if mibBuilder.loadTexts: hh3cIgmpSnoopingClearStats.setDescription('The configuration to clear the statistics of IGMP packets.')
mibBuilder.exportSymbols("HH3C-LswIGSP-MIB", hh3cIgmpSnoopingGroupPolicyEntry=hh3cIgmpSnoopingGroupPolicyEntry, hh3cIgmpSnoopingGroupPolicyParameter=hh3cIgmpSnoopingGroupPolicyParameter, hh3cIgmpSnoopingFastLeaveStatus=hh3cIgmpSnoopingFastLeaveStatus, hh3cIgmpSnoopingGroupPolicyIfIndex=hh3cIgmpSnoopingGroupPolicyIfIndex, hh3cIgmpSnoopingResponseTime=hh3cIgmpSnoopingResponseTime, hh3cRecvIGMPV2ReportNum=hh3cRecvIGMPV2ReportNum, hh3cIgmpSnoopingGroupLimitNumber=hh3cIgmpSnoopingGroupLimitNumber, PYSNMP_MODULE_ID=hh3cLswIgmpsnoopingMib, EnabledStatus=EnabledStatus, hh3cRecvIGMPSQueryNum=hh3cRecvIGMPSQueryNum, hh3cIgmpSnoopingGroupLimitTable=hh3cIgmpSnoopingGroupLimitTable, hh3cIgmpSnoopingFastLeaveEntry=hh3cIgmpSnoopingFastLeaveEntry, hh3cIgmpSnoopingVlanStatusTable=hh3cIgmpSnoopingVlanStatusTable, hh3cIgmpSnoopingNonFloodingStatus=hh3cIgmpSnoopingNonFloodingStatus, hh3cIgmpSnoopingVlanID=hh3cIgmpSnoopingVlanID, hh3cIgmpSnoopingStatus=hh3cIgmpSnoopingStatus, hh3cIgmpSnoopingVlanStatusEntry=hh3cIgmpSnoopingVlanStatusEntry, hh3cIgmpSnoopingFastLeaveTable=hh3cIgmpSnoopingFastLeaveTable, hh3cIgmpSnoopingGroupPolicyVlanID=hh3cIgmpSnoopingGroupPolicyVlanID, hh3cIgmpSnoopingGroupPolicyStatus=hh3cIgmpSnoopingGroupPolicyStatus, hh3cIgmpSnoopingGroupPolicyTable=hh3cIgmpSnoopingGroupPolicyTable, hh3cRecvIGMPGQueryNum=hh3cRecvIGMPGQueryNum, hh3cSentIGMPSQueryNum=hh3cSentIGMPSQueryNum, hh3cRecvIGMPV1ReportNum=hh3cRecvIGMPV1ReportNum, hh3cIgmpSnoopingVlanEnabled=hh3cIgmpSnoopingVlanEnabled, hh3cRecvIGMPLeaveNum=hh3cRecvIGMPLeaveNum, hh3cIgmpSnoopingHostTime=hh3cIgmpSnoopingHostTime, hh3cLswIgmpsnoopingMibObject=hh3cLswIgmpsnoopingMibObject, hh3cIgmpSnoopingClearStats=hh3cIgmpSnoopingClearStats, hh3cLswIgmpsnoopingMib=hh3cLswIgmpsnoopingMib, hh3cIgmpSnoopingFastLeaveIfIndex=hh3cIgmpSnoopingFastLeaveIfIndex, hh3cIgmpSnoopingGroupIfIndex=hh3cIgmpSnoopingGroupIfIndex, hh3cIgmpSnoopingGroupLimitEntry=hh3cIgmpSnoopingGroupLimitEntry, hh3cRecvErrorIGMPPacketNum=hh3cRecvErrorIGMPPacketNum, hh3cIgmpSnoopingStatsObjects=hh3cIgmpSnoopingStatsObjects, hh3cIgmpSnoopingRouterPortAge=hh3cIgmpSnoopingRouterPortAge)
