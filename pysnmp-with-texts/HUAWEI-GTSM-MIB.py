#
# PySNMP MIB module HUAWEI-GTSM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-GTSM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:44:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, ObjectIdentity, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, MibIdentifier, Counter32, Counter64, ModuleIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ObjectIdentity", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "MibIdentifier", "Counter32", "Counter64", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hwGTSMModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126))
hwGTSMModule.setRevisions(('2006-09-05 19:38',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwGTSMModule.setRevisionsDescriptions(('The initial revision of this MIB module.',))
if mibBuilder.loadTexts: hwGTSMModule.setLastUpdated('200611131938Z')
if mibBuilder.loadTexts: hwGTSMModule.setOrganization('Huawei Technologies co.,Ltd.')
if mibBuilder.loadTexts: hwGTSMModule.setContactInfo('VRP Team Huawei Technologies co.,Ltd. Huawei Bld.,NO.3 Xinxi Rd., Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.huawei.com Zip:100085 ')
if mibBuilder.loadTexts: hwGTSMModule.setDescription('The HUAWEI-GTSM-MIB contains all the objects that manages GTSM, it mainly contains the following five parts. 1) Default action that is used to deal with the received packets when no GTSM policy matches. 2) Policy table that is used to get or set the GTSM policy. 3) BGP peer group table that is used to get or set the GTSM policy for BGP peer group. 4) Statistics table that is used to compute the number of the packets containing received packets, passing packets and dropped packets. 5) Global configuration clear statistics table that is used to clear all statistics. The table can be used any time when users want to initialize the counter.')
hwGTSM = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1))
hwGTSMDefaultAction = MibScalar((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pass", 1), ("drop", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwGTSMDefaultAction.setStatus('current')
if mibBuilder.loadTexts: hwGTSMDefaultAction.setDescription('The object specifies the default action when no matching policy exists. Default value is pass.')
hwGTSMPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2), )
if mibBuilder.loadTexts: hwGTSMPolicyTable.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicyTable.setDescription('Information about GTSM policies. This object is used to get GTSM policy(policies), create a new policy, modify or delete GTSM policy (policies).')
hwGTSMPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1), ).setIndexNames((0, "HUAWEI-GTSM-MIB", "hwGTSMvrfIndex"), (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyAddressType"), (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyProtocol"), (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicySourceIpAddress"), (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyDestIpAddress"), (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicySourcePort"), (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyDestPort"))
if mibBuilder.loadTexts: hwGTSMPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicyEntry.setDescription('Information about GTSM policies,it used to get gtsm policy(policies),to create a new policy,to modify or to delete gtsm policy(policies).')
hwGTSMvrfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hwGTSMvrfIndex.setStatus('current')
if mibBuilder.loadTexts: hwGTSMvrfIndex.setDescription('The index of VPN Routing and Forwarding table.')
hwGTSMPolicyAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 2), InetAddressType())
if mibBuilder.loadTexts: hwGTSMPolicyAddressType.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicyAddressType.setDescription('The type of Internet address by where the packets received and will go.')
hwGTSMPolicyProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: hwGTSMPolicyProtocol.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicyProtocol.setDescription('The number of protocol.')
hwGTSMPolicySourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 4), InetAddress())
if mibBuilder.loadTexts: hwGTSMPolicySourceIpAddress.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicySourceIpAddress.setDescription('Source IP address in the GTSM policy that will be used to check the matching of source IP address in the received packets.')
hwGTSMPolicyDestIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 5), InetAddress())
if mibBuilder.loadTexts: hwGTSMPolicyDestIpAddress.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicyDestIpAddress.setDescription('Destination IP address in the GTSM policy that will be used to check the matching of destination IP address in the received packets.')
hwGTSMPolicySourcePort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hwGTSMPolicySourcePort.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicySourcePort.setDescription('Source port number in the GTSM policy that will be used to check the matching of source port number in the received packets.')
hwGTSMPolicyDestPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hwGTSMPolicyDestPort.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicyDestPort.setDescription('Destination port number in the GTSM policy that will be used to check the matching of destination port number in the received packets.')
hwGTSMPolicyTTLMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwGTSMPolicyTTLMin.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicyTTLMin.setDescription('The minimum TTL in the policy table. The minimum TTL is compared with the TTL in the packets to check whether the minimum TTL is between the minimum TTL and maximum TTL, and thus check the validity of the received packets.')
hwGTSMPolicyTTLMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGTSMPolicyTTLMax.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicyTTLMax.setDescription('The maximum TTL in policy table that is compared with the TTL in the packets to check whether it is between the minimum TTL and maximum TTL ,and thus check the validity of the received packets. Default value is 255.')
hwGTSMPolicyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 2, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwGTSMPolicyRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicyRowStatus.setDescription('The operating state of the row.')
hwGTSMBgpPeergroupTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3), )
if mibBuilder.loadTexts: hwGTSMBgpPeergroupTable.setStatus('current')
if mibBuilder.loadTexts: hwGTSMBgpPeergroupTable.setDescription('The table of BGP peer group policies. The table contains all the BGP peer group policies.')
hwGTSMBgpPeergroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3, 1), ).setIndexNames((0, "HUAWEI-GTSM-MIB", "hwGTSMvrfIndex"), (0, "HUAWEI-GTSM-MIB", "hwGTSMBgpPeergroupName"))
if mibBuilder.loadTexts: hwGTSMBgpPeergroupEntry.setStatus('current')
if mibBuilder.loadTexts: hwGTSMBgpPeergroupEntry.setDescription('Information about BGP peer group policies. This table is used to get BGP peer group policy (policies), create a policy, modify or delete BGP peer group policy (policies).')
hwGTSMBgpPeergroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 47)))
if mibBuilder.loadTexts: hwGTSMBgpPeergroupName.setStatus('current')
if mibBuilder.loadTexts: hwGTSMBgpPeergroupName.setDescription('Peer group name in the BGP policy table that is compared with the peer group name to decide whether to apply this policy.')
hwGTSMBgpPeergroupTTLMin = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwGTSMBgpPeergroupTTLMin.setStatus('current')
if mibBuilder.loadTexts: hwGTSMBgpPeergroupTTLMin.setDescription('The minimum TTL in policy table that is compared with the TTL in the packets to check whether it is between the minimum TTL and maximum TTL, and thus check the validity of the received packets.')
hwGTSMBgpPeergroupTTLMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGTSMBgpPeergroupTTLMax.setStatus('current')
if mibBuilder.loadTexts: hwGTSMBgpPeergroupTTLMax.setDescription('The maximum TTL in policy table that is compared with the TTL in the packets to check whether it is between the minimum TTL and maximum TTL, and check the validity of the received packets. Default value is 255.')
hwGTSMBgpPeergroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 3, 1, 51), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwGTSMBgpPeergroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwGTSMBgpPeergroupRowStatus.setDescription('The operating state of the row.')
hwGTSMStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4), )
if mibBuilder.loadTexts: hwGTSMStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsTable.setDescription('The table of GTSM Statistics table. The table contains the number of the packets containing received packets, passed packets and discarded packets.')
hwGTSMStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4, 1), ).setIndexNames((0, "HUAWEI-GTSM-MIB", "hwGTSMSlotIndex"))
if mibBuilder.loadTexts: hwGTSMStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsEntry.setDescription('The information of GTSM Statistics,it only can be read.')
hwGTSMSlotIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)))
if mibBuilder.loadTexts: hwGTSMSlotIndex.setStatus('current')
if mibBuilder.loadTexts: hwGTSMSlotIndex.setDescription('The Index of Slot which receives the packets.')
hwGTSMStatisticsRcvPacketNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGTSMStatisticsRcvPacketNumber.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsRcvPacketNumber.setDescription('The total number of received packets of specific slot.')
hwGTSMStatisticsPassPacketNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGTSMStatisticsPassPacketNumber.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsPassPacketNumber.setDescription('The total number of packets that have been transferred to the up layer after packets of specific slot are received.')
hwGTSMStatisticsDropPacketNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 4, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGTSMStatisticsDropPacketNumber.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsDropPacketNumber.setDescription('The total number of packets that do not match the specific GTSM policy when packets of specific slot are received.')
hwGTSMGlobalConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 5), )
if mibBuilder.loadTexts: hwGTSMGlobalConfigTable.setStatus('current')
if mibBuilder.loadTexts: hwGTSMGlobalConfigTable.setDescription('The table of GTSM global configuration table. The table contains all information you have operated to the statistics table.')
hwGTSMGlobalConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 5, 1), ).setIndexNames((0, "HUAWEI-GTSM-MIB", "hwGTSMSlotIndex"))
if mibBuilder.loadTexts: hwGTSMGlobalConfigEntry.setStatus('current')
if mibBuilder.loadTexts: hwGTSMGlobalConfigEntry.setDescription('The information of GTSM global configuration table.The table is used to clear all statistics, you can use this table any time when you want to initialize the counter.')
hwGTSMGlobalConfigClearStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 5, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 255))).clone(namedValues=NamedValues(("reset", 1), ("unused", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwGTSMGlobalConfigClearStatistics.setStatus('current')
if mibBuilder.loadTexts: hwGTSMGlobalConfigClearStatistics.setDescription('It is used to clear the statistics of the GTSM global configuration table.')
hwGTSMGlobalConfigLogDroppedPacket = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 5, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("log", 1), ("nolog", 2))).clone('nolog')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwGTSMGlobalConfigLogDroppedPacket.setStatus('current')
if mibBuilder.loadTexts: hwGTSMGlobalConfigLogDroppedPacket.setDescription('It is used to decide whether to log the dropped packets.')
hwGTSMStatisticsInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6), )
if mibBuilder.loadTexts: hwGTSMStatisticsInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsInfoTable.setDescription('The table of GTSM Statistics Information. The table contains the number of the packets containing received packets, passed packets and discarded packets.')
hwGTSMStatisticsInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6, 1), ).setIndexNames((0, "HUAWEI-GTSM-MIB", "hwGTSMSlotNum"), (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyAddressType"), (0, "HUAWEI-GTSM-MIB", "hwGTSMPolicyProtocol"))
if mibBuilder.loadTexts: hwGTSMStatisticsInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsInfoEntry.setDescription('The information of GTSM Statistics,it only can be read.')
hwGTSMSlotNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)))
if mibBuilder.loadTexts: hwGTSMSlotNum.setStatus('current')
if mibBuilder.loadTexts: hwGTSMSlotNum.setDescription('The Index of Slot which receives the packets.')
hwGTSMStatisticsReceivePacketNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGTSMStatisticsReceivePacketNum.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsReceivePacketNum.setDescription('The total number of received packets of specific slot.')
hwGTSMStatisticsPassPacketNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGTSMStatisticsPassPacketNum.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsPassPacketNum.setDescription('The total number of packets that have been transferred to the up layer after packets of specific slot are received.')
hwGTSMStatisticsDropPacketNum = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 6, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwGTSMStatisticsDropPacketNum.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsDropPacketNum.setDescription('The total number of packets that do not match the specific GTSM policy when packets of specific slot are received.')
hwGTSMGlobalConfigInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 7), )
if mibBuilder.loadTexts: hwGTSMGlobalConfigInfoTable.setStatus('current')
if mibBuilder.loadTexts: hwGTSMGlobalConfigInfoTable.setDescription('The table of GTSM global configuration table. The table contains all information you have operated to the statistics table.')
hwGTSMGlobalConfigInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 7, 1), ).setIndexNames((0, "HUAWEI-GTSM-MIB", "hwGTSMSlotNum"))
if mibBuilder.loadTexts: hwGTSMGlobalConfigInfoEntry.setStatus('current')
if mibBuilder.loadTexts: hwGTSMGlobalConfigInfoEntry.setDescription('The information of GTSM global configuration table.The table is used to clear all statistics, you can use this table any time when you want to initialize the counter.')
hwGTSMGlobalConfigClearStatisticsInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 7, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 255))).clone(namedValues=NamedValues(("reset", 1), ("unused", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwGTSMGlobalConfigClearStatisticsInfo.setStatus('current')
if mibBuilder.loadTexts: hwGTSMGlobalConfigClearStatisticsInfo.setDescription('It is used to clear the statistics of the GTSM global configuration table.')
hwGTSMGlobalConfigLogDroppedPacketInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 1, 7, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("log", 1), ("nolog", 2))).clone('nolog')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwGTSMGlobalConfigLogDroppedPacketInfo.setStatus('current')
if mibBuilder.loadTexts: hwGTSMGlobalConfigLogDroppedPacketInfo.setDescription('It is used to decide whether to log the dropped packets.')
hwGTSMConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2))
hwGTSMCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 1))
hwGTSMCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 1, 1)).setObjects(("HUAWEI-GTSM-MIB", "hwGTSMDefaultActionGroup"), ("HUAWEI-GTSM-MIB", "hwGTSMPolicyGroup"), ("HUAWEI-GTSM-MIB", "hwGTSMBgpPeergroupGroup"), ("HUAWEI-GTSM-MIB", "hwGTSMStatisticsGroup"), ("HUAWEI-GTSM-MIB", "hwGTSMGlobalConfigGroup"), ("HUAWEI-GTSM-MIB", "hwGTSMStatisticsInfoGroup"), ("HUAWEI-GTSM-MIB", "hwGTSMGlobalConfigInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGTSMCompliance = hwGTSMCompliance.setStatus('current')
if mibBuilder.loadTexts: hwGTSMCompliance.setDescription('The compliance statement for systems supporting this module.')
hwGTSMGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2))
hwGTSMDefaultActionGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 1)).setObjects(("HUAWEI-GTSM-MIB", "hwGTSMDefaultAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGTSMDefaultActionGroup = hwGTSMDefaultActionGroup.setStatus('current')
if mibBuilder.loadTexts: hwGTSMDefaultActionGroup.setDescription('The default action group.')
hwGTSMPolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 2)).setObjects(("HUAWEI-GTSM-MIB", "hwGTSMPolicyTTLMin"), ("HUAWEI-GTSM-MIB", "hwGTSMPolicyTTLMax"), ("HUAWEI-GTSM-MIB", "hwGTSMPolicyRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGTSMPolicyGroup = hwGTSMPolicyGroup.setStatus('current')
if mibBuilder.loadTexts: hwGTSMPolicyGroup.setDescription('The GTSM policy group.')
hwGTSMBgpPeergroupGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 3)).setObjects(("HUAWEI-GTSM-MIB", "hwGTSMBgpPeergroupTTLMin"), ("HUAWEI-GTSM-MIB", "hwGTSMBgpPeergroupTTLMax"), ("HUAWEI-GTSM-MIB", "hwGTSMBgpPeergroupRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGTSMBgpPeergroupGroup = hwGTSMBgpPeergroupGroup.setStatus('current')
if mibBuilder.loadTexts: hwGTSMBgpPeergroupGroup.setDescription('The GTSM BGP peer group.')
hwGTSMStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 4)).setObjects(("HUAWEI-GTSM-MIB", "hwGTSMStatisticsRcvPacketNumber"), ("HUAWEI-GTSM-MIB", "hwGTSMStatisticsPassPacketNumber"), ("HUAWEI-GTSM-MIB", "hwGTSMStatisticsDropPacketNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGTSMStatisticsGroup = hwGTSMStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsGroup.setDescription('The GTSM statistics group.')
hwGTSMGlobalConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 5)).setObjects(("HUAWEI-GTSM-MIB", "hwGTSMGlobalConfigClearStatistics"), ("HUAWEI-GTSM-MIB", "hwGTSMGlobalConfigLogDroppedPacket"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGTSMGlobalConfigGroup = hwGTSMGlobalConfigGroup.setStatus('current')
if mibBuilder.loadTexts: hwGTSMGlobalConfigGroup.setDescription('The GTSM global configuration group.')
hwGTSMStatisticsInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 6)).setObjects(("HUAWEI-GTSM-MIB", "hwGTSMStatisticsReceivePacketNum"), ("HUAWEI-GTSM-MIB", "hwGTSMStatisticsPassPacketNum"), ("HUAWEI-GTSM-MIB", "hwGTSMStatisticsDropPacketNum"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGTSMStatisticsInfoGroup = hwGTSMStatisticsInfoGroup.setStatus('current')
if mibBuilder.loadTexts: hwGTSMStatisticsInfoGroup.setDescription('The GTSM statistics group.')
hwGTSMGlobalConfigInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 126, 2, 2, 7)).setObjects(("HUAWEI-GTSM-MIB", "hwGTSMGlobalConfigClearStatisticsInfo"), ("HUAWEI-GTSM-MIB", "hwGTSMGlobalConfigLogDroppedPacketInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwGTSMGlobalConfigInfoGroup = hwGTSMGlobalConfigInfoGroup.setStatus('current')
if mibBuilder.loadTexts: hwGTSMGlobalConfigInfoGroup.setDescription('The GTSM global configuration group.')
mibBuilder.exportSymbols("HUAWEI-GTSM-MIB", hwGTSMPolicyDestPort=hwGTSMPolicyDestPort, hwGTSMStatisticsTable=hwGTSMStatisticsTable, hwGTSMStatisticsReceivePacketNum=hwGTSMStatisticsReceivePacketNum, hwGTSMSlotIndex=hwGTSMSlotIndex, hwGTSM=hwGTSM, hwGTSMStatisticsPassPacketNum=hwGTSMStatisticsPassPacketNum, hwGTSMStatisticsDropPacketNumber=hwGTSMStatisticsDropPacketNumber, hwGTSMPolicyDestIpAddress=hwGTSMPolicyDestIpAddress, hwGTSMCompliance=hwGTSMCompliance, hwGTSMPolicySourcePort=hwGTSMPolicySourcePort, hwGTSMCompliances=hwGTSMCompliances, hwGTSMGlobalConfigInfoGroup=hwGTSMGlobalConfigInfoGroup, hwGTSMSlotNum=hwGTSMSlotNum, hwGTSMStatisticsInfoGroup=hwGTSMStatisticsInfoGroup, hwGTSMModule=hwGTSMModule, hwGTSMPolicyRowStatus=hwGTSMPolicyRowStatus, hwGTSMBgpPeergroupName=hwGTSMBgpPeergroupName, hwGTSMPolicyTTLMin=hwGTSMPolicyTTLMin, hwGTSMBgpPeergroupTable=hwGTSMBgpPeergroupTable, hwGTSMGlobalConfigInfoEntry=hwGTSMGlobalConfigInfoEntry, hwGTSMBgpPeergroupGroup=hwGTSMBgpPeergroupGroup, hwGTSMConformance=hwGTSMConformance, hwGTSMStatisticsPassPacketNumber=hwGTSMStatisticsPassPacketNumber, hwGTSMGlobalConfigClearStatisticsInfo=hwGTSMGlobalConfigClearStatisticsInfo, PYSNMP_MODULE_ID=hwGTSMModule, hwGTSMPolicyAddressType=hwGTSMPolicyAddressType, hwGTSMPolicySourceIpAddress=hwGTSMPolicySourceIpAddress, hwGTSMBgpPeergroupTTLMax=hwGTSMBgpPeergroupTTLMax, hwGTSMStatisticsDropPacketNum=hwGTSMStatisticsDropPacketNum, hwGTSMGlobalConfigInfoTable=hwGTSMGlobalConfigInfoTable, hwGTSMStatisticsRcvPacketNumber=hwGTSMStatisticsRcvPacketNumber, hwGTSMGlobalConfigTable=hwGTSMGlobalConfigTable, hwGTSMGlobalConfigClearStatistics=hwGTSMGlobalConfigClearStatistics, hwGTSMBgpPeergroupEntry=hwGTSMBgpPeergroupEntry, hwGTSMGroups=hwGTSMGroups, hwGTSMDefaultActionGroup=hwGTSMDefaultActionGroup, hwGTSMGlobalConfigLogDroppedPacket=hwGTSMGlobalConfigLogDroppedPacket, hwGTSMGlobalConfigGroup=hwGTSMGlobalConfigGroup, hwGTSMPolicyProtocol=hwGTSMPolicyProtocol, hwGTSMvrfIndex=hwGTSMvrfIndex, hwGTSMBgpPeergroupTTLMin=hwGTSMBgpPeergroupTTLMin, hwGTSMPolicyTTLMax=hwGTSMPolicyTTLMax, hwGTSMStatisticsInfoTable=hwGTSMStatisticsInfoTable, hwGTSMPolicyTable=hwGTSMPolicyTable, hwGTSMPolicyEntry=hwGTSMPolicyEntry, hwGTSMPolicyGroup=hwGTSMPolicyGroup, hwGTSMGlobalConfigLogDroppedPacketInfo=hwGTSMGlobalConfigLogDroppedPacketInfo, hwGTSMGlobalConfigEntry=hwGTSMGlobalConfigEntry, hwGTSMStatisticsGroup=hwGTSMStatisticsGroup, hwGTSMStatisticsInfoEntry=hwGTSMStatisticsInfoEntry, hwGTSMBgpPeergroupRowStatus=hwGTSMBgpPeergroupRowStatus, hwGTSMDefaultAction=hwGTSMDefaultAction, hwGTSMStatisticsEntry=hwGTSMStatisticsEntry)
