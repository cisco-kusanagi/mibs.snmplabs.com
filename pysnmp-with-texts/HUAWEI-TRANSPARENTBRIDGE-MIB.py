#
# PySNMP MIB module HUAWEI-TRANSPARENTBRIDGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-TRANSPARENTBRIDGE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:49:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
hwBaseTrapProbableCause, hwBaseTrapEventType, hwBaseTrapSeverity = mibBuilder.importSymbols("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause", "hwBaseTrapEventType", "hwBaseTrapSeverity")
hwDatacomm, = mibBuilder.importSymbols("HUAWEI-MIB", "hwDatacomm")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, ModuleIdentity, ObjectIdentity, NotificationType, Unsigned32, TimeTicks, iso, MibIdentifier, Bits, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "ModuleIdentity", "ObjectIdentity", "NotificationType", "Unsigned32", "TimeTicks", "iso", "MibIdentifier", "Bits", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
DisplayString, MacAddress, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "RowStatus", "TextualConvention")
hwTransparentBridgeMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242))
hwTransparentBridge = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1))
hwTransparentBridge.setRevisions(('2015-05-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwTransparentBridge.setRevisionsDescriptions(('Modify the value of the hwTPBridgeId and hwTPBridgeStatBridgeId.',))
if mibBuilder.loadTexts: hwTransparentBridge.setLastUpdated('201505080000Z')
if mibBuilder.loadTexts: hwTransparentBridge.setOrganization('Huawei Technologies Co.,Ltd.')
if mibBuilder.loadTexts: hwTransparentBridge.setContactInfo("Huawei Industrial Base Bantian, Longgang Shenzhen 518129 People's Republic of China Website: http://www.huawei.com Email: support@huawei.com ")
if mibBuilder.loadTexts: hwTransparentBridge.setDescription('The TransparentBridge MIB module is defined to manage TransparentBridge function of Huawei Technologies co.,Ltd.')
hwTPBridgeMngObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1))
hwTPBridgeBase = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1))
hwTPBridgeApply = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2))
hwTPBridgeMIBTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1), )
if mibBuilder.loadTexts: hwTPBridgeMIBTable.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMIBTable.setDescription('The table contains basic information for the bridge. The indexes of this table is hwTPBridgeId.')
hwTPBridgeMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1), ).setIndexNames((0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeId"))
if mibBuilder.loadTexts: hwTPBridgeMIBEntry.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMIBEntry.setDescription('Entries of TransparentBridge MIB table. The indexes of this entry is hwTPBridgeId.')
hwTPBridgeId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwTPBridgeId.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeId.setDescription('The identifier of this bridge.')
hwTPBridgeMacLearn = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 2), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeMacLearn.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMacLearn.setDescription('The value indicates whether the MAC address learning is opened. The value enabled(1) indicates learning is allowed. Default value is enabled(1).')
hwTPBridgeRoutingIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 3), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeRoutingIp.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeRoutingIp.setDescription('The value indicates which routing ip function is opened. The value enabled(1) indicates routing ip is allowed. Default value is disable(2).')
hwTPBridgeBridgingIp = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 4), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeBridgingIp.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeBridgingIp.setDescription('The value indicates which bridging ip function is opened. The value enabled(1) indicates bridging ip is allowed. Default value is enabled(1).')
hwTPBridgeBridgingOther = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 5), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeBridgingOther.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeBridgingOther.setDescription('The value indicates which bridging other protocol function is opened. The value enabled(1) indicates bridging other protocol is allowed. Default value is enabled(1).')
hwTPBridgeAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 6), EnabledStatus().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeAdminStatus.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeAdminStatus.setDescription('Value disable(2) indicates shutdown the bridge; enabled(1) indicates open the bridge.')
hwTPBridgeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 1, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeRowStatus.setDescription('Operation status.')
hwTPBridgeMemberMIBTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2), )
if mibBuilder.loadTexts: hwTPBridgeMemberMIBTable.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberMIBTable.setDescription('The table contains basic information for the bridge membership. The indexes of this table are hwTPBridgeId, hwTPBridgeMemberIfIndex.')
hwTPBridgeMemberMIBEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1), ).setIndexNames((0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeId"), (0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberIfIndex"))
if mibBuilder.loadTexts: hwTPBridgeMemberMIBEntry.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberMIBEntry.setDescription('Entries of TransparentBridge member MIB table. The indexes of this entry are hwTPBridgeId, hwTPBridgeMemberIfIndex.')
hwTPBridgeMemberIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwTPBridgeMemberIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberIfIndex.setDescription('The IfIndex of this bridge member.')
hwTPBridgeMemberVlanTransparent = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1, 2), EnabledStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeMemberVlanTransparent.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberVlanTransparent.setDescription('The value indicates whether the VLAN transparent is opened. The value enabled(1) indicates VLAN transparent is allowed. Default value is disabled(2).')
hwTPBridgeMemberRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hwTPBridgeMemberRowStatus.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberRowStatus.setDescription('Operation status.')
hwTPBridgeStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1), )
if mibBuilder.loadTexts: hwTPBridgeStatTable.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatTable.setDescription('The table contains statistics information for the bridge. The indexes of this table is hwTPBridgeStatBridgeId.')
hwTPBridgeStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1), ).setIndexNames((0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatBridgeId"))
if mibBuilder.loadTexts: hwTPBridgeStatEntry.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatEntry.setDescription('Entries of bridge statistics table. The indexes of this entry is hwTPBridgeStatBridgeId.')
hwTPBridgeStatBridgeId = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hwTPBridgeStatBridgeId.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatBridgeId.setDescription('The bridge-id.')
hwTPBridgeStatInTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatInTotalPkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatInTotalPkts.setDescription('The number of received packets.')
hwTPBridgeStatInBPDUPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatInBPDUPkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatInBPDUPkts.setDescription('The number of BPDU packets received.')
hwTPBridgeStatInUcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatInUcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatInUcastkts.setDescription('The number of unicast packets received.')
hwTPBridgeStatInMcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatInMcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatInMcastkts.setDescription('The number of multicast packets received.')
hwTPBridgeStatInBcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatInBcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatInBcastkts.setDescription('The number of broadcast packets received.')
hwTPBridgeStatOutTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatOutTotalPkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatOutTotalPkts.setDescription('The number of sent packets.')
hwTPBridgeStatOutBPDUPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatOutBPDUPkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatOutBPDUPkts.setDescription('The number of BPDU packets sent.')
hwTPBridgeStatOutUcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatOutUcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatOutUcastkts.setDescription('The number of unicast packets sent.')
hwTPBridgeStatOutMcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatOutMcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatOutMcastkts.setDescription('The number of multicast packets sent.')
hwTPBridgeStatOutBcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeStatOutBcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatOutBcastkts.setDescription('The number of broadcast packets sent.')
hwTPBridgeStatResetFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 1, 1, 12), EnabledStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwTPBridgeStatResetFlag.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeStatResetFlag.setDescription('The flag of reset.')
hwTPBridgeMemberStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2), )
if mibBuilder.loadTexts: hwTPBridgeMemberStatTable.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatTable.setDescription('The table contains statistics information for the member of bridge. The indexes of this table is hwTPBridgeMemberStatIfIndex.')
hwTPBridgeMemberStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1), ).setIndexNames((0, "HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatIfIndex"))
if mibBuilder.loadTexts: hwTPBridgeMemberStatEntry.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatEntry.setDescription('Entries of bridge member statistics table. The indexes of this entry is hwTPBridgeMemberStatIfIndex.')
hwTPBridgeMemberStatIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hwTPBridgeMemberStatIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatIfIndex.setDescription('The IfIndex of this bridge member.')
hwTPBridgeMemberStatInTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatInTotalPkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatInTotalPkts.setDescription('The number of received packets.')
hwTPBridgeMemberStatInBPDUPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatInBPDUPkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatInBPDUPkts.setDescription('The number of BPDU packets received.')
hwTPBridgeMemberStatInUcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatInUcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatInUcastkts.setDescription('The number of unicast packets received.')
hwTPBridgeMemberStatInMcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatInMcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatInMcastkts.setDescription('The number of multicast packets received.')
hwTPBridgeMemberStatInBcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatInBcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatInBcastkts.setDescription('The number of broadcast packets received.')
hwTPBridgeMemberStatOutTotalPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutTotalPkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutTotalPkts.setDescription('The number of sent packets.')
hwTPBridgeMemberStatOutBPDUPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutBPDUPkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutBPDUPkts.setDescription('The number of BPDU packets sent.')
hwTPBridgeMemberStatOutUcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutUcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutUcastkts.setDescription('The number of unicast packets sent.')
hwTPBridgeMemberStatOutMcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutMcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutMcastkts.setDescription('The number of multicast packets sent.')
hwTPBridgeMemberStatOutBcastkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 1, 2, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutBcastkts.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatOutBcastkts.setDescription('The number of broadcast packets sent.')
hwTPBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2))
hwTPBridgeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 1))
hwTPBridgeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2))
hwTPBridgeCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 1, 1)).setObjects(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeGroup"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTPBridgeCompliance = hwTPBridgeCompliance.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeCompliance.setDescription('The core compliance statement for all implementations.')
hwTPBridgeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 1)).setObjects(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMacLearn"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeRoutingIp"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeBridgingIp"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeBridgingOther"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeAdminStatus"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTPBridgeGroup = hwTPBridgeGroup.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeGroup.setDescription(' ')
hwTPBridgeMemberGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 2)).setObjects(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberVlanTransparent"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTPBridgeMemberGroup = hwTPBridgeMemberGroup.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberGroup.setDescription(' ')
hhwTPBridgeStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 3)).setObjects(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInTotalPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInBPDUPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInUcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInMcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatInBcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutTotalPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutBPDUPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutUcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutMcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatOutBcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeStatResetFlag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hhwTPBridgeStatGroup = hhwTPBridgeStatGroup.setStatus('current')
if mibBuilder.loadTexts: hhwTPBridgeStatGroup.setDescription(' ')
hwTPBridgeMemberStatGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 5, 25, 242, 1, 2, 2, 4)).setObjects(("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInTotalPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInBPDUPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInUcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInMcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatInBcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutTotalPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutBPDUPkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutUcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutMcastkts"), ("HUAWEI-TRANSPARENTBRIDGE-MIB", "hwTPBridgeMemberStatOutBcastkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hwTPBridgeMemberStatGroup = hwTPBridgeMemberStatGroup.setStatus('current')
if mibBuilder.loadTexts: hwTPBridgeMemberStatGroup.setDescription(' ')
mibBuilder.exportSymbols("HUAWEI-TRANSPARENTBRIDGE-MIB", hwTransparentBridge=hwTransparentBridge, hwTPBridgeStatOutMcastkts=hwTPBridgeStatOutMcastkts, hwTPBridgeMemberStatOutTotalPkts=hwTPBridgeMemberStatOutTotalPkts, hwTPBridgeMemberStatIfIndex=hwTPBridgeMemberStatIfIndex, hhwTPBridgeStatGroup=hhwTPBridgeStatGroup, hwTPBridgeRoutingIp=hwTPBridgeRoutingIp, hwTransparentBridgeMIB=hwTransparentBridgeMIB, hwTPBridgeStatInTotalPkts=hwTPBridgeStatInTotalPkts, hwTPBridgeStatInBcastkts=hwTPBridgeStatInBcastkts, hwTPBridgeStatInUcastkts=hwTPBridgeStatInUcastkts, hwTPBridgeStatOutUcastkts=hwTPBridgeStatOutUcastkts, hwTPBridgeMemberStatOutBcastkts=hwTPBridgeMemberStatOutBcastkts, hwTPBridgeMemberVlanTransparent=hwTPBridgeMemberVlanTransparent, hwTPBridgeMemberStatGroup=hwTPBridgeMemberStatGroup, hwTPBridgeMacLearn=hwTPBridgeMacLearn, hwTPBridgeApply=hwTPBridgeApply, hwTPBridgeBridgingIp=hwTPBridgeBridgingIp, hwTPBridgeRowStatus=hwTPBridgeRowStatus, hwTPBridgeId=hwTPBridgeId, hwTPBridgeMemberStatInTotalPkts=hwTPBridgeMemberStatInTotalPkts, hwTPBridgeMIBTable=hwTPBridgeMIBTable, hwTPBridgeAdminStatus=hwTPBridgeAdminStatus, PYSNMP_MODULE_ID=hwTransparentBridge, hwTPBridgeMemberStatEntry=hwTPBridgeMemberStatEntry, hwTPBridgeMemberStatInBPDUPkts=hwTPBridgeMemberStatInBPDUPkts, hwTPBridgeStatBridgeId=hwTPBridgeStatBridgeId, hwTPBridgeGroups=hwTPBridgeGroups, hwTPBridgeMIBEntry=hwTPBridgeMIBEntry, hwTPBridgeStatOutTotalPkts=hwTPBridgeStatOutTotalPkts, hwTPBridgeCompliance=hwTPBridgeCompliance, hwTPBridgeMemberStatInMcastkts=hwTPBridgeMemberStatInMcastkts, hwTPBridgeStatOutBcastkts=hwTPBridgeStatOutBcastkts, hwTPBridgeStatInBPDUPkts=hwTPBridgeStatInBPDUPkts, hwTPBridgeConformance=hwTPBridgeConformance, hwTPBridgeMemberStatOutBPDUPkts=hwTPBridgeMemberStatOutBPDUPkts, hwTPBridgeBridgingOther=hwTPBridgeBridgingOther, hwTPBridgeStatOutBPDUPkts=hwTPBridgeStatOutBPDUPkts, hwTPBridgeStatInMcastkts=hwTPBridgeStatInMcastkts, hwTPBridgeStatEntry=hwTPBridgeStatEntry, hwTPBridgeGroup=hwTPBridgeGroup, hwTPBridgeMemberMIBEntry=hwTPBridgeMemberMIBEntry, hwTPBridgeStatResetFlag=hwTPBridgeStatResetFlag, hwTPBridgeMemberIfIndex=hwTPBridgeMemberIfIndex, hwTPBridgeMemberStatInBcastkts=hwTPBridgeMemberStatInBcastkts, hwTPBridgeBase=hwTPBridgeBase, hwTPBridgeMemberStatOutMcastkts=hwTPBridgeMemberStatOutMcastkts, hwTPBridgeMemberGroup=hwTPBridgeMemberGroup, hwTPBridgeMemberStatOutUcastkts=hwTPBridgeMemberStatOutUcastkts, hwTPBridgeStatTable=hwTPBridgeStatTable, hwTPBridgeMemberMIBTable=hwTPBridgeMemberMIBTable, hwTPBridgeMemberStatInUcastkts=hwTPBridgeMemberStatInUcastkts, hwTPBridgeCompliances=hwTPBridgeCompliances, hwTPBridgeMemberStatTable=hwTPBridgeMemberStatTable, hwTPBridgeMngObjects=hwTPBridgeMngObjects, hwTPBridgeMemberRowStatus=hwTPBridgeMemberRowStatus)
