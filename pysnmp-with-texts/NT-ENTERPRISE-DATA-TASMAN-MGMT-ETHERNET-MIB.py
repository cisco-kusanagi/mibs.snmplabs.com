#
# PySNMP MIB module NT-ENTERPRISE-DATA-TASMAN-MGMT-ETHERNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NT-ENTERPRISE-DATA-TASMAN-MGMT-ETHERNET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:25:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ntEnterpriseDataTasmanInterfaces, = mibBuilder.importSymbols("NT-ENTERPRISE-DATA-MIB", "ntEnterpriseDataTasmanInterfaces")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter32, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, NotificationType, ObjectIdentity, Gauge32, Unsigned32, MibIdentifier, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "NotificationType", "ObjectIdentity", "Gauge32", "Unsigned32", "MibIdentifier", "iso", "ModuleIdentity")
DisplayString, RowStatus, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TruthValue", "TextualConvention")
nnethernetMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4))
nnethernetMib.setRevisions(('1999-07-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: nnethernetMib.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: nnethernetMib.setLastUpdated('9907010000Z')
if mibBuilder.loadTexts: nnethernetMib.setOrganization('Nortel')
if mibBuilder.loadTexts: nnethernetMib.setContactInfo(' ')
if mibBuilder.loadTexts: nnethernetMib.setDescription('Ethernet MIB for defining ethernet parameters')
nnethernetTable = MibTable((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1), )
if mibBuilder.loadTexts: nnethernetTable.setStatus('current')
if mibBuilder.loadTexts: nnethernetTable.setDescription('Ethernet management related parameters are defined in this table.')
nnethernetTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1), ).setIndexNames((0, "NT-ENTERPRISE-DATA-TASMAN-MGMT-ETHERNET-MIB", "nnethernetId"))
if mibBuilder.loadTexts: nnethernetTableEntry.setStatus('current')
if mibBuilder.loadTexts: nnethernetTableEntry.setDescription('Ethernet management parameters are listed in this table.')
nnethernetId = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnethernetId.setStatus('deprecated')
if mibBuilder.loadTexts: nnethernetId.setDescription('ethernetId is the identifier for the ethernet interfaces.')
nnethernetDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 25))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetDescr.setStatus('current')
if mibBuilder.loadTexts: nnethernetDescr.setDescription('Brief description of the ethernet.The maximum length of this parameter is 25 characters.')
nnethernetDhcpRelayServerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 3), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetDhcpRelayServerAddr.setStatus('current')
if mibBuilder.loadTexts: nnethernetDhcpRelayServerAddr.setDescription('The DHCP relay server Ipaddress.')
nnethernetDhcpRelayGatewayAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetDhcpRelayGatewayAddr.setStatus('current')
if mibBuilder.loadTexts: nnethernetDhcpRelayGatewayAddr.setDescription('The DHCP relay gateway address.')
nnethernetFailOverEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetFailOverEnable.setStatus('current')
if mibBuilder.loadTexts: nnethernetFailOverEnable.setDescription('This object toggles the failover enable mode for a particular Ethernet interface. The default mode is failover disabled. At present this is only applicable for data using source forwarding on an Ethernet interface. If failover is enabled on a particular Ethernet interface and the Ethernet interface link goes down, source forwarded traffic will switch over to the other Ethernet interface.')
nnethernetHoldDownTime = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 900)).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetHoldDownTime.setStatus('current')
if mibBuilder.loadTexts: nnethernetHoldDownTime.setDescription('The time, in seconds, that an Ethernet interface should be in holdDown when it receives an up signal. In other words, no source forwarding traffic should be sent on the Ethernet interface during the holdDown time period. The default is 3 seconds and the maximum is 900 seconds (15 minutes). This applies when failover is enabled on the interface and traffic has switched over to the other Ethernet interface .')
nnethernetIcmpRedirectEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetIcmpRedirectEnable.setStatus('current')
if mibBuilder.loadTexts: nnethernetIcmpRedirectEnable.setDescription('This object toggles the ICMP redirect mode for a particular Ethernet interface. The default mode is redirect disabled.')
nnethernetIcmpUnreachableEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 8), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetIcmpUnreachableEnable.setStatus('current')
if mibBuilder.loadTexts: nnethernetIcmpUnreachableEnable.setDescription('This object toggles the ICMP unreachable mode for a particular Ethernet interface. The default mode is unreachable disabled.')
nnethernetIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 9), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetIpAddr.setStatus('current')
if mibBuilder.loadTexts: nnethernetIpAddr.setDescription('The ethernet IP address. The parameters ethernetIpAddr and ethernetSubnetMask have to be set together,giving first IpAddress and then Subnetmask, in a same request. Unless an IpAddress and a Subnet mask are not set the network activity for the specified ethernet interface will not be up for service.')
nnethernetSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetSubnetMask.setStatus('current')
if mibBuilder.loadTexts: nnethernetSubnetMask.setDescription('The ethernet subnet mask. The parameters ethernetIpAddr and ethernetSubnetMask have to be set together,giving first IpAddress and then Subnetmask, in a same request. Unless an IpAddress and a Subnet mask are not set the network activity for the specified ethernet interface will not be up for service.')
nnethernetIpDirectedBroadcastEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 11), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetIpDirectedBroadcastEnable.setStatus('current')
if mibBuilder.loadTexts: nnethernetIpDirectedBroadcastEnable.setDescription('This object toggles the IP directed braodcast mode for a particular Ethernet interface. The default mode is unreachable disabled.')
nnethernetIpMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pass", 1), ("block", 2), ("ospfrip2", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetIpMulticast.setStatus('current')
if mibBuilder.loadTexts: nnethernetIpMulticast.setDescription('Specifies the multicast type.')
nnethernetMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 13), Integer32().clone(1500)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetMtu.setStatus('current')
if mibBuilder.loadTexts: nnethernetMtu.setDescription('Specifies the message transfer size. It has a range of 64-4072. The default value is 1500.')
nnethernetSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("speed-10MBPs", 1), ("speed-100MBPs", 2), ("speed-Auto", 3))).clone(3)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetSpeed.setStatus('current')
if mibBuilder.loadTexts: nnethernetSpeed.setDescription('Specifies the ethernet speed. The values are 10 or 100 or auto.')
nnethernetMode = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("half-duplex", 1), ("full-duplex", 2))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetMode.setStatus('current')
if mibBuilder.loadTexts: nnethernetMode.setDescription('Specifies the ethernet mode to be half-duplex or full-duplex. The default value is half-duplex.')
nnethernetShutdownEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 16), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetShutdownEnable.setStatus('current')
if mibBuilder.loadTexts: nnethernetShutdownEnable.setDescription('This object when enabled shuts down the particular Ehternet interface. Default value is disabled. Both cannot be shutdown at same time. Either of the two Ethernet interfaces, with valid IpAddress, should be up and running for a network activity.')
nnethernetVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4098))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetVlanId.setStatus('current')
if mibBuilder.loadTexts: nnethernetVlanId.setDescription('Vlan Tagging enabled in VLAN forwarding mode for this Id.')
nnethernetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nnethernetRowStatus.setStatus('current')
if mibBuilder.loadTexts: nnethernetRowStatus.setDescription('RowStatus is used to add/delete a row in the table. Adding or deleting a row corresponds to creating or deleting an ethernet entry. In order to add a row to the ethernet table, a set should be done with the value 4 (createAndGo) along with the value of 65535 as an index for both RowStatus and Ethernet Descr. A request to create a row can be completed successfully if and only if a set on the ethernetRowStatus and the ethernetDescr come in the same request with first RowStatus and then Ethernet Description. To delete a row this parameter has to be set with the value 6(destroy).')
nnethernetDropPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 4, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nnethernetDropPackets.setStatus('current')
if mibBuilder.loadTexts: nnethernetDropPackets.setDescription('The total number of drop packet statistics for the LAN interface when the box encounters packet drops like Tunnel encapsulation errors, VLAN packets dropped due to QoS (classification errors, queuing errors),VLAN packets dropped due to RED, Input/Output interface is down with respect to VLAN, VLAN errors such as unrecognized VLAN id, multiple dot1q encapsulations in the packet, system errors from the time box is up. This list is only a subset of the numerous reasons for the packets to be dropped by the agent per interface')
mibBuilder.exportSymbols("NT-ENTERPRISE-DATA-TASMAN-MGMT-ETHERNET-MIB", nnethernetMtu=nnethernetMtu, nnethernetRowStatus=nnethernetRowStatus, nnethernetIpMulticast=nnethernetIpMulticast, nnethernetDhcpRelayServerAddr=nnethernetDhcpRelayServerAddr, nnethernetShutdownEnable=nnethernetShutdownEnable, nnethernetIcmpUnreachableEnable=nnethernetIcmpUnreachableEnable, nnethernetMib=nnethernetMib, nnethernetFailOverEnable=nnethernetFailOverEnable, nnethernetMode=nnethernetMode, nnethernetIpDirectedBroadcastEnable=nnethernetIpDirectedBroadcastEnable, nnethernetDescr=nnethernetDescr, nnethernetDhcpRelayGatewayAddr=nnethernetDhcpRelayGatewayAddr, nnethernetSubnetMask=nnethernetSubnetMask, nnethernetIpAddr=nnethernetIpAddr, nnethernetTableEntry=nnethernetTableEntry, nnethernetSpeed=nnethernetSpeed, PYSNMP_MODULE_ID=nnethernetMib, nnethernetIcmpRedirectEnable=nnethernetIcmpRedirectEnable, nnethernetVlanId=nnethernetVlanId, nnethernetId=nnethernetId, nnethernetTable=nnethernetTable, nnethernetDropPackets=nnethernetDropPackets, nnethernetHoldDownTime=nnethernetHoldDownTime)
