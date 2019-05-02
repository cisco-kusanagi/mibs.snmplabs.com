#
# PySNMP MIB module H3C-IF-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-IF-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:22:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
h3cCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cCommon")
ifIndex, ifDescr = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifDescr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Bits, Counter64, ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, TimeTicks, MibIdentifier, Integer32, Counter32, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Counter64", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "TimeTicks", "MibIdentifier", "Integer32", "Counter32", "Unsigned32", "IpAddress")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
h3cIfExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40))
h3cIfExt.setRevisions(('2009-05-06 19:36', '2004-11-13 19:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cIfExt.setRevisionsDescriptions(('Update this MIB module.', 'The initial revision of this MIB module.',))
if mibBuilder.loadTexts: h3cIfExt.setLastUpdated('200905061936Z')
if mibBuilder.loadTexts: h3cIfExt.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cIfExt.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip: 100085')
if mibBuilder.loadTexts: h3cIfExt.setDescription('This MIB is an extension of interface MIBs such as IF-MIB. This MIB is applicable to routers, switches and other products. Some objects in this may be used only for some specific products, so users should refer to the related documents to acquire more detail information. ')
h3cIfExtScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 1))
h3cIfStatGlobalFlowInterval = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 1, 1), Integer32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIfStatGlobalFlowInterval.setStatus('current')
if mibBuilder.loadTexts: h3cIfStatGlobalFlowInterval.setDescription('Sampling interval for in/out flow of all interfaces. Setting zero indicates closing the statistic function.')
h3cIfExtGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2))
h3cIfStat = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1))
h3cIfStatScalarGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 1))
h3cIfStatTable = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2))
h3cIfFlowStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1), )
if mibBuilder.loadTexts: h3cIfFlowStatTable.setStatus('current')
if mibBuilder.loadTexts: h3cIfFlowStatTable.setDescription('This table contains objects to get statistic information of interfaces on a device.')
h3cIfStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cIfStatEntry.setStatus('current')
if mibBuilder.loadTexts: h3cIfStatEntry.setDescription('Entry items')
h3cIfStatFlowInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 1), Integer32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIfStatFlowInterval.setStatus('current')
if mibBuilder.loadTexts: h3cIfStatFlowInterval.setDescription('Sampling interval for in/out flow of interface. Setting zero indicates closing this statistic function and objects in this table should return 0.')
h3cIfStatFlowInBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfStatFlowInBits.setStatus('current')
if mibBuilder.loadTexts: h3cIfStatFlowInBits.setDescription('In bits in the specific interval.')
h3cIfStatFlowOutBits = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfStatFlowOutBits.setStatus('current')
if mibBuilder.loadTexts: h3cIfStatFlowOutBits.setDescription('Out bits in specific interval.')
h3cIfStatFlowInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfStatFlowInPkts.setStatus('current')
if mibBuilder.loadTexts: h3cIfStatFlowInPkts.setDescription('In Packets in the specific interval.')
h3cIfStatFlowOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfStatFlowOutPkts.setStatus('current')
if mibBuilder.loadTexts: h3cIfStatFlowOutPkts.setDescription('Out packets in the specific interval.')
h3cIfStatFlowInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfStatFlowInBytes.setStatus('current')
if mibBuilder.loadTexts: h3cIfStatFlowInBytes.setDescription('In bytes in the specific interval.')
h3cIfStatFlowOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfStatFlowOutBytes.setStatus('current')
if mibBuilder.loadTexts: h3cIfStatFlowOutBytes.setDescription('Out bytes in the specific interval.')
h3cIfSpeedStatTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2), )
if mibBuilder.loadTexts: h3cIfSpeedStatTable.setStatus('current')
if mibBuilder.loadTexts: h3cIfSpeedStatTable.setDescription('This table contains objects to get average speed information in the specific interval of interfaces on a device.')
h3cIfSpeedStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cIfSpeedStatEntry.setStatus('current')
if mibBuilder.loadTexts: h3cIfSpeedStatEntry.setDescription('Entry items')
h3cIfSpeedStatInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 1), Integer32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIfSpeedStatInterval.setStatus('current')
if mibBuilder.loadTexts: h3cIfSpeedStatInterval.setDescription('Sampling interval for in/out flow of interface. Setting zero indicates closing this statistic function and objects in this table should return 0.')
h3cIfSpeedStatInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfSpeedStatInPkts.setStatus('current')
if mibBuilder.loadTexts: h3cIfSpeedStatInPkts.setDescription('Average of input packets per second in the specific interval by h3cIfSpeedStatInterval.')
h3cIfSpeedStatOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfSpeedStatOutPkts.setStatus('current')
if mibBuilder.loadTexts: h3cIfSpeedStatOutPkts.setDescription('Average of output packets per second in the specific interval by h3cIfSpeedStatInterval.')
h3cIfSpeedStatInBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfSpeedStatInBytes.setStatus('current')
if mibBuilder.loadTexts: h3cIfSpeedStatInBytes.setDescription('Average of input bytes per second in the specific interval by h3cIfSpeedStatInterval.')
h3cIfSpeedStatOutBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 1, 2, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfSpeedStatOutBytes.setStatus('current')
if mibBuilder.loadTexts: h3cIfSpeedStatOutBytes.setDescription('Average of output bytes per second in the specific interval by h3cIfSpeedStatInterval.')
h3cIfControl = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2))
h3cRTParentIfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1), )
if mibBuilder.loadTexts: h3cRTParentIfTable.setStatus('current')
if mibBuilder.loadTexts: h3cRTParentIfTable.setDescription('This table contains all interfaces that can create sub interface.')
h3cRTParentIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1), ).setIndexNames((0, "H3C-IF-EXT-MIB", "h3cRTParentIfIndex"))
if mibBuilder.loadTexts: h3cRTParentIfEntry.setStatus('current')
if mibBuilder.loadTexts: h3cRTParentIfEntry.setDescription('This entry describes a interface that can create sub interface.')
h3cRTParentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cRTParentIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cRTParentIfIndex.setDescription('The index of interface that can creat sub interface. The value is the same as ifIndex value for this interface.')
h3cRTMinSubIfOrdinal = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRTMinSubIfOrdinal.setStatus('current')
if mibBuilder.loadTexts: h3cRTMinSubIfOrdinal.setDescription('The minimum ordinal of the sub interface can be created.')
h3cRTMaxSubIfOrdinal = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRTMaxSubIfOrdinal.setStatus('current')
if mibBuilder.loadTexts: h3cRTMaxSubIfOrdinal.setDescription('The max ordinal of the sub interface can be created.')
h3cRTSubIfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2), )
if mibBuilder.loadTexts: h3cRTSubIfTable.setStatus('current')
if mibBuilder.loadTexts: h3cRTSubIfTable.setDescription('This table contains objects to create or delete sub interfaces. To create a sub interface, a valid parent interface must be specified by h3cRTSubIfParentIfIndex and the h3cRTSubIfOrdinal must be in the range between h3cRTMinSubIfOrdinal and h3cRTMaxSubIfOrdinal of the parent interface from h3cRTParentIfTable. Sub interfaces are logical virtual interfaces configured on a main interface. The main interface can be either a physical interface (such as a Layer 3 Ethernet interface) or a logical interface (such as an MFR interface). The subinterfaces on a main interface share the physical layer parameters of the main interface but can have link layer and network layer parameters of their own. Disabling or enabling a subinterface does not affect the main interface, but the main interface status change affects the subinterfaces. The subinterfaces cannot operate normally unless the main interface is connected. A single physical interface containing multiple subinterfaces enables you to network in a more flexible way. You can create subinterfaces for the following physical interfaces: Ethernet interface. An Ethernet subinterface associated with no VLAN supports only IPX, while an Ethernet subinterface associated with a VLAN supports both IP and IPX. WAN interfaces with their data link layer protocols being frame relay, whose subinterfaces support IP and IPX. WAN interfaces with their data link layer protocols being X.25, whose subinterfaces support IP and IPX. ATM interface, whose subinterfaces support only IP.')
h3cRTSubIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1), ).setIndexNames((0, "H3C-IF-EXT-MIB", "h3cRTSubIfParentIfIndex"), (0, "H3C-IF-EXT-MIB", "h3cRTSubIfOrdinal"))
if mibBuilder.loadTexts: h3cRTSubIfEntry.setStatus('current')
if mibBuilder.loadTexts: h3cRTSubIfEntry.setDescription('The h3cRTSubIfTable entry items')
h3cRTSubIfParentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cRTSubIfParentIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cRTSubIfParentIfIndex.setDescription('The parent interface index. The value should be the same as the h3cRTParentIfIndex.')
h3cRTSubIfOrdinal = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: h3cRTSubIfOrdinal.setStatus('current')
if mibBuilder.loadTexts: h3cRTSubIfOrdinal.setDescription('The ordinal of sub interface. It should between h3cRTMinSubIfOrdinal and h3cRTMaxSubIfOrdinal of the parent interface.')
h3cRTSubIfSubIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRTSubIfSubIfIndex.setStatus('current')
if mibBuilder.loadTexts: h3cRTSubIfSubIfIndex.setDescription('The ifIndex value of the sub interface')
h3cRTSubIfSubIfDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cRTSubIfSubIfDesc.setStatus('current')
if mibBuilder.loadTexts: h3cRTSubIfSubIfDesc.setDescription('The name of the interface')
h3cRTSubIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: h3cRTSubIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: h3cRTSubIfRowStatus.setDescription('Operation status.')
h3cIfLinkModeTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3), )
if mibBuilder.loadTexts: h3cIfLinkModeTable.setStatus('current')
if mibBuilder.loadTexts: h3cIfLinkModeTable.setDescription('This table contains objects to get or set the link mode of an interface. According to the layer at which the device processes received data packets, Ethernet interfaces can operate in bridge or route mode.')
h3cIfLinkModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1), ).setIndexNames((0, "H3C-IF-EXT-MIB", "h3cIfLinkModeIndex"))
if mibBuilder.loadTexts: h3cIfLinkModeEntry.setStatus('current')
if mibBuilder.loadTexts: h3cIfLinkModeEntry.setDescription('The interface link mode table entry')
h3cIfLinkModeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: h3cIfLinkModeIndex.setStatus('current')
if mibBuilder.loadTexts: h3cIfLinkModeIndex.setDescription('The value is same as ifIndex.')
h3cIfLinkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bridgeMode", 1), ("routeMode", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIfLinkMode.setStatus('current')
if mibBuilder.loadTexts: h3cIfLinkMode.setDescription('The current link mode of the interface If h3cIfLinkModeSwitchSupport is true, writing to the object can change the link mode of the interface.')
h3cIfLinkModeSwitchSupport = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 2, 3, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfLinkModeSwitchSupport.setStatus('current')
if mibBuilder.loadTexts: h3cIfLinkModeSwitchSupport.setDescription('Whether the interface supports link mode switching. If this object is true, the interface can operate in either bridge mode or route mode. Otherwise the interfaces can operate only in bridge or route mode.')
h3cIfInterfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3))
h3cIfPhysicalNumber = MibScalar((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfPhysicalNumber.setStatus('current')
if mibBuilder.loadTexts: h3cIfPhysicalNumber.setDescription('Represents the number of physical interfaces in the device.')
h3cIfTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2), )
if mibBuilder.loadTexts: h3cIfTable.setStatus('current')
if mibBuilder.loadTexts: h3cIfTable.setDescription('A list of interface entries. The number of entries is given by the value of IfNumber.')
h3cIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cIfEntry.setStatus('current')
if mibBuilder.loadTexts: h3cIfEntry.setDescription('An entry containing management information applicable to a particular interface.')
h3cIfUpDownTimes = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfUpDownTimes.setStatus('current')
if mibBuilder.loadTexts: h3cIfUpDownTimes.setDescription("The interface's up/down times, since the device was initialized.")
h3cIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIfMtu.setStatus('current')
if mibBuilder.loadTexts: h3cIfMtu.setDescription('The size of the largest datagram which can be sent/received on the interface, specified in octets. For interfaces that are used for transmitting network datagram, this is the size of the largest network datagram that can be sent on the interface.')
h3cIfBandwidthRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfBandwidthRate.setStatus('current')
if mibBuilder.loadTexts: h3cIfBandwidthRate.setDescription('The rate of the bandwidth for an interface.')
h3cIfDiscardPktRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfDiscardPktRate.setStatus('current')
if mibBuilder.loadTexts: h3cIfDiscardPktRate.setDescription('The rate of the discarded packets for an interface.')
h3cIfStatusKeepTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfStatusKeepTime.setStatus('current')
if mibBuilder.loadTexts: h3cIfStatusKeepTime.setDescription('The time since the interface entered its current operational state.')
h3cIfInNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfInNUcastPkts.setStatus('current')
if mibBuilder.loadTexts: h3cIfInNUcastPkts.setDescription('The number of non-unicast (i.e., subnetwork- broadcast or subnetwork-multicast) packets delivered to a higher-layer protocol.')
h3cIfOutNUcastPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 2, 3, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cIfOutNUcastPkts.setStatus('current')
if mibBuilder.loadTexts: h3cIfOutNUcastPkts.setDescription('The total number of packets that higher-level protocols requested be transmitted to a non- unicast (i.e., a subnetwork-broadcast or subnetwork-multicast) address.')
h3cIfExtTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3))
h3cIfExtTrapPrex = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0))
h3cIfBandwidthUsageHigh = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 1)).setObjects(("IF-MIB", "ifDescr"), ("H3C-IF-EXT-MIB", "h3cIfBandwidthRate"), ("H3C-IF-EXT-MIB", "h3cIfBandwidthUpperLimit"))
if mibBuilder.loadTexts: h3cIfBandwidthUsageHigh.setStatus('current')
if mibBuilder.loadTexts: h3cIfBandwidthUsageHigh.setDescription('The notification is generated when the rate of the bandwidth for the interface exceeds the upper limit.')
h3cIfDiscardPktRateHigh = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 0, 2)).setObjects(("IF-MIB", "ifDescr"), ("H3C-IF-EXT-MIB", "h3cIfDiscardPktRate"), ("H3C-IF-EXT-MIB", "h3cIfDiscardPktRateUpperLimit"))
if mibBuilder.loadTexts: h3cIfDiscardPktRateHigh.setStatus('current')
if mibBuilder.loadTexts: h3cIfDiscardPktRateHigh.setDescription('The notification is generated when the rate of the discarded packets for the interface exceeds the upper limit.')
h3cIfExtTrapObject = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1))
h3cIfExtTrapCfgTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1), )
if mibBuilder.loadTexts: h3cIfExtTrapCfgTable.setStatus('current')
if mibBuilder.loadTexts: h3cIfExtTrapCfgTable.setDescription('The trap configuration table.')
h3cIfExtTrapCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: h3cIfExtTrapCfgEntry.setStatus('current')
if mibBuilder.loadTexts: h3cIfExtTrapCfgEntry.setDescription('An entry for this table.')
h3cIfBandwidthUpperLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIfBandwidthUpperLimit.setStatus('current')
if mibBuilder.loadTexts: h3cIfBandwidthUpperLimit.setDescription('The rate of the bandwidth upper limit for an interface.')
h3cIfDiscardPktRateUpperLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 40, 3, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: h3cIfDiscardPktRateUpperLimit.setStatus('current')
if mibBuilder.loadTexts: h3cIfDiscardPktRateUpperLimit.setDescription('The rate of the discarded packets upper limit for an interface.')
mibBuilder.exportSymbols("H3C-IF-EXT-MIB", h3cIfLinkModeTable=h3cIfLinkModeTable, h3cIfStatEntry=h3cIfStatEntry, PYSNMP_MODULE_ID=h3cIfExt, h3cIfDiscardPktRate=h3cIfDiscardPktRate, h3cIfStatFlowOutBytes=h3cIfStatFlowOutBytes, h3cIfSpeedStatInterval=h3cIfSpeedStatInterval, h3cIfMtu=h3cIfMtu, h3cIfExtGroup=h3cIfExtGroup, h3cIfStatFlowInBits=h3cIfStatFlowInBits, h3cIfStatScalarGroup=h3cIfStatScalarGroup, h3cIfStatTable=h3cIfStatTable, h3cRTParentIfTable=h3cRTParentIfTable, h3cIfLinkModeIndex=h3cIfLinkModeIndex, h3cIfInNUcastPkts=h3cIfInNUcastPkts, h3cIfBandwidthUpperLimit=h3cIfBandwidthUpperLimit, h3cIfStatGlobalFlowInterval=h3cIfStatGlobalFlowInterval, h3cIfFlowStatTable=h3cIfFlowStatTable, h3cRTSubIfParentIfIndex=h3cRTSubIfParentIfIndex, h3cIfExtTrapPrex=h3cIfExtTrapPrex, h3cIfStatFlowInterval=h3cIfStatFlowInterval, h3cRTMaxSubIfOrdinal=h3cRTMaxSubIfOrdinal, h3cRTParentIfEntry=h3cRTParentIfEntry, h3cIfStatFlowOutBits=h3cIfStatFlowOutBits, h3cIfEntry=h3cIfEntry, h3cIfSpeedStatEntry=h3cIfSpeedStatEntry, h3cRTSubIfTable=h3cRTSubIfTable, h3cRTSubIfRowStatus=h3cRTSubIfRowStatus, h3cIfBandwidthUsageHigh=h3cIfBandwidthUsageHigh, h3cIfLinkModeSwitchSupport=h3cIfLinkModeSwitchSupport, h3cIfExtTrapCfgEntry=h3cIfExtTrapCfgEntry, h3cRTMinSubIfOrdinal=h3cRTMinSubIfOrdinal, h3cIfExtTrap=h3cIfExtTrap, h3cIfControl=h3cIfControl, h3cIfStatFlowInBytes=h3cIfStatFlowInBytes, h3cIfExtTrapCfgTable=h3cIfExtTrapCfgTable, h3cIfStatusKeepTime=h3cIfStatusKeepTime, h3cRTParentIfIndex=h3cRTParentIfIndex, h3cIfLinkMode=h3cIfLinkMode, h3cIfSpeedStatOutBytes=h3cIfSpeedStatOutBytes, h3cRTSubIfSubIfDesc=h3cRTSubIfSubIfDesc, h3cIfExtTrapObject=h3cIfExtTrapObject, h3cIfDiscardPktRateUpperLimit=h3cIfDiscardPktRateUpperLimit, h3cIfLinkModeEntry=h3cIfLinkModeEntry, h3cIfStatFlowInPkts=h3cIfStatFlowInPkts, h3cIfInterfaces=h3cIfInterfaces, h3cRTSubIfEntry=h3cRTSubIfEntry, h3cIfPhysicalNumber=h3cIfPhysicalNumber, h3cIfStat=h3cIfStat, h3cIfSpeedStatTable=h3cIfSpeedStatTable, h3cIfSpeedStatInPkts=h3cIfSpeedStatInPkts, h3cRTSubIfSubIfIndex=h3cRTSubIfSubIfIndex, h3cRTSubIfOrdinal=h3cRTSubIfOrdinal, h3cIfDiscardPktRateHigh=h3cIfDiscardPktRateHigh, h3cIfSpeedStatOutPkts=h3cIfSpeedStatOutPkts, h3cIfStatFlowOutPkts=h3cIfStatFlowOutPkts, h3cIfExt=h3cIfExt, h3cIfSpeedStatInBytes=h3cIfSpeedStatInBytes, h3cIfTable=h3cIfTable, h3cIfExtScalarGroup=h3cIfExtScalarGroup, h3cIfBandwidthRate=h3cIfBandwidthRate, h3cIfOutNUcastPkts=h3cIfOutNUcastPkts, h3cIfUpDownTimes=h3cIfUpDownTimes)
