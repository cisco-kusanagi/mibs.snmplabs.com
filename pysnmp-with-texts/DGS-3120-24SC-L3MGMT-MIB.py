#
# PySNMP MIB module DGS-3120-24SC-L3MGMT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DGS-3120-24SC-L3MGMT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:43:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, iso, TimeTicks, NotificationType, Gauge32, MibIdentifier, Bits, IpAddress, Counter64, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "iso", "TimeTicks", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "IpAddress", "Counter64", "ModuleIdentity", "Integer32")
DisplayString, TextualConvention, PhysAddress, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress", "TruthValue", "RowStatus")
dlink_Dgs3120Proj_Dgs3120_24SC, = mibBuilder.importSymbols("SWDGS3120PRIMGMT-MIB", "dlink-Dgs3120Proj-Dgs3120-24SC")
swL3MgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3))
if mibBuilder.loadTexts: swL3MgmtMIB.setLastUpdated('1211160000Z')
if mibBuilder.loadTexts: swL3MgmtMIB.setOrganization(' ')
if mibBuilder.loadTexts: swL3MgmtMIB.setContactInfo(' ')
if mibBuilder.loadTexts: swL3MgmtMIB.setDescription('The Structure of Layer 3 Network Management Information for the proprietary enterprise.')
class NodeAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class NetAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

swL3IpMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2))
swL3IpCtrlMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1))
swL3IpFdbMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 2))
swL3IpCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3), )
if mibBuilder.loadTexts: swL3IpCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlTable.setDescription('This table contain IP interface information.')
swL3IpCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1), ).setIndexNames((0, "DGS-3120-24SC-L3MGMT-MIB", "swL3IpCtrlInterfaceName"))
if mibBuilder.loadTexts: swL3IpCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlEntry.setDescription('A list of information about a specific IP interface.')
swL3IpCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlInterfaceName.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlInterfaceName.setDescription('This object indicates the name of the IP interface.')
swL3IpCtrlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIfIndex.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIfIndex.setDescription('This object uniquely identifies the IP interface number in the swL3IpCtrlTable.')
swL3IpCtrlIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpAddr.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpAddr.setDescription('The IP address of the interface. This object only can take the value of the unicast IP address.')
swL3IpCtrlIpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpSubnetMask.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpSubnetMask.setDescription('The IP net mask for this interface.')
swL3IpCtrlVlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlVlanName.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlVlanName.setDescription("This object indicates the IP control entry's VLAN name. The VLAN name in each entry must be unique in the IP Control Table.")
swL3IpCtrlProxyArp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlProxyArp.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlProxyArp.setDescription('This object indicates enable/disable of the proxy ARP function for IPv4.')
swL3IpCtrlSecondary = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 7), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlSecondary.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlSecondary.setDescription('When this is true(1), the IP address is the secondary IP. When false(2), the IP address is the primary IP.')
swL3IpCtrlMode = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("bootp", 3), ("dhcp", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlMode.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlMode.setDescription('This object indicates the IP operation mode. other(1) - This entry is currently in use but the conditions under which it will remain are determined by each of the following values. bootp(3) - The IP address will be set automatically from a BOOTP server. dhcp(4) - The IP address will be set automatically from a DHCP server.')
swL3IpCtrlAdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlAdminState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlAdminState.setDescription('The state of the IP interface.')
swL3IpCtrlIpv4AdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpv4AdminState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv4AdminState.setDescription('The IPv4 admin state of the IP interface. The default state is determined by project. This state will only be effective when the swL3IpCtrlAdminState is enabled.')
swL3IpCtrlIpv6AdminState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpv6AdminState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv6AdminState.setDescription('The IPv6 admin state of the IP interface. The default state is determined by project. This state will only be effective when the swL3IpCtrlAdminState is enabled.')
swL3IpCtrlIpv6LinkLocalAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 14), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAddress.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAddress.setDescription('The IPv6 link local address for this interface.')
swL3IpCtrlIpv6LinkLocalPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalPrefixLen.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalPrefixLen.setDescription('The IPv6 prefix length for this IPv6 link local address.')
swL3IpCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpCtrlState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlState.setDescription('This variable displays the status of the entry. The status is used for creating, modifying, and deleting instances of the objects in this table.')
swL3IpCtrlIpv6LinkLocalAutoState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAutoState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpv6LinkLocalAutoState.setDescription('The state of the IPv6 link local auto.')
swL3IpCtrlLocalProxyArp = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlLocalProxyArp.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlLocalProxyArp.setDescription('This object indicates enable/disable of the local proxy ARP function for IPv4.')
swL3IpCtrlDhcpv6ClientState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlDhcpv6ClientState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlDhcpv6ClientState.setDescription('The state of the Dhcpv6 Client.')
swL3IpCtrlIpDhcpOption12State = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12State.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12State.setDescription('Enable or disable insertion of option 12 in the DHCPDISCOVER and DHCPREQUEST message.')
swL3IpCtrlIpDhcpOption12HostName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 3, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12HostName.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlIpDhcpOption12HostName.setDescription('Specify the host name to be inserted in the DHCPDISCOVER and DHCPREQUEST message. The specified host name must start with a letter, end with a letter or digit, and have only letters, digits, and hyphen as interior characters; the maximal length is 63. By default, the host name is empty. When set an empty host name, means to clear the host name setting and use the default value to encode option 12.')
swL3Ipv6CtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 4), )
if mibBuilder.loadTexts: swL3Ipv6CtrlTable.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlTable.setDescription('This table contains IPv6 information of an IP interface.')
swL3Ipv6CtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 4, 1), ).setIndexNames((0, "DGS-3120-24SC-L3MGMT-MIB", "swL3Ipv6CtrlInterfaceName"))
if mibBuilder.loadTexts: swL3Ipv6CtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlEntry.setDescription('A list of IPv6 information about a specific IP interface.')
swL3Ipv6CtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 4, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6CtrlInterfaceName.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlInterfaceName.setDescription('This object indicates the name of the IP interface.')
swL3Ipv6CtrlMaxReassmblySize = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6CtrlMaxReassmblySize.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlMaxReassmblySize.setDescription('Maximum Reassembly Size of the IP interface.')
swL3Ipv6CtrlNsRetransTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3Ipv6CtrlNsRetransTimer.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6CtrlNsRetransTimer.setDescription("Neighbor solicitation's retransmit timer. The unit is set in milliseconds.")
swL3Ipv6AddressCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 5), )
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlTable.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlTable.setDescription('This table contain IPv6 address information for each IP interface.')
swL3Ipv6AddressCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 5, 1), ).setIndexNames((0, "DGS-3120-24SC-L3MGMT-MIB", "swL3Ipv6AddressCtrlInterfaceName"), (0, "DGS-3120-24SC-L3MGMT-MIB", "swL3Ipv6Address"), (0, "DGS-3120-24SC-L3MGMT-MIB", "swL3Ipv6AddressCtrlPrefixLen"))
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlEntry.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlEntry.setDescription('A list of information about a specific IPv6 address.')
swL3Ipv6AddressCtrlInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 5, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlInterfaceName.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlInterfaceName.setDescription('This object indicates the name of the IP interface. ')
swL3Ipv6Address = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 5, 1, 2), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6Address.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6Address.setDescription('Specify the IPv6 address.')
swL3Ipv6AddressCtrlPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlPrefixLen.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlPrefixLen.setDescription('Indicates the prefix length of this IPv6 address.')
swL3Ipv6AddressCtrlState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlState.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlState.setDescription('This variable displays the status of the entry. The status is used for creating, modifying, and deleting instances of the objects in this table.')
swL3Ipv6AddressCtrlAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("manual", 1), ("dhcpv6", 2), ("stateless", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlAddressType.setStatus('current')
if mibBuilder.loadTexts: swL3Ipv6AddressCtrlAddressType.setDescription('This object indicates the type of the IPv6 address. manual(1): the IPv6 address is configured by user. dhcpv6(2): the IPv6 address is assigned by DHCPv6 server. stateless(3): the IPv6 address is assigned by router advertisement.')
swL3IpCtrlAllIpIfState = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("enabled", 2), ("disabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpCtrlAllIpIfState.setStatus('current')
if mibBuilder.loadTexts: swL3IpCtrlAllIpIfState.setDescription('This object indicates all interface function state of the device.')
swL3IpFdbInfoTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 2, 1), )
if mibBuilder.loadTexts: swL3IpFdbInfoTable.setStatus('current')
if mibBuilder.loadTexts: swL3IpFdbInfoTable.setDescription('A table that contains forwarding and/or filtering information. This information is used by the switch in determining how to propagate the received IP packets.')
swL3IpFdbInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 2, 1, 1), ).setIndexNames((0, "DGS-3120-24SC-L3MGMT-MIB", "swL3IpFdbInfoIpAddr"))
if mibBuilder.loadTexts: swL3IpFdbInfoEntry.setStatus('current')
if mibBuilder.loadTexts: swL3IpFdbInfoEntry.setDescription('Information about a specific IP address for which the bridge has some forwarding and/or filtering information.')
swL3IpFdbInfoIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFdbInfoIpAddr.setStatus('current')
if mibBuilder.loadTexts: swL3IpFdbInfoIpAddr.setDescription('A IP address for which switch has forwarding and/or filtering information.')
swL3IpFdbInfoIpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 2, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFdbInfoIpSubnetMask.setStatus('current')
if mibBuilder.loadTexts: swL3IpFdbInfoIpSubnetMask.setDescription('A IP net mask for this interface for which the switch has forwarding and/or filtering information.')
swL3IpFdbInfoPort = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFdbInfoPort.setStatus('current')
if mibBuilder.loadTexts: swL3IpFdbInfoPort.setDescription("Either the value '0', or the port number of the port on which packets having an IP address equal to the value of the corresponding instance of swL3IpFdbInfoIpAddr has been seen. A value of '0' indicates that the port number has not been learned but that switch does have some forwarding/filtering information about this address.")
swL3IpFdbInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("dynamic", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpFdbInfoType.setStatus('current')
if mibBuilder.loadTexts: swL3IpFdbInfoType.setDescription('The status of this entry.')
swL3IpArpAgingTime = MibScalar((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: swL3IpArpAgingTime.setStatus('current')
if mibBuilder.loadTexts: swL3IpArpAgingTime.setDescription('The timeout period in minutes for aging out dynamically learned arp information.')
swL3IpStaticRouteTable = MibTable((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 5), )
if mibBuilder.loadTexts: swL3IpStaticRouteTable.setStatus('current')
if mibBuilder.loadTexts: swL3IpStaticRouteTable.setDescription("This entity's IP static Routing table.")
swL3IpStaticRouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 5, 1), ).setIndexNames((0, "DGS-3120-24SC-L3MGMT-MIB", "swL3IpStaticRouteDest"), (0, "DGS-3120-24SC-L3MGMT-MIB", "swL3IpStaticRouteMask"), (0, "DGS-3120-24SC-L3MGMT-MIB", "swL3IpStaticRouteNextHop"))
if mibBuilder.loadTexts: swL3IpStaticRouteEntry.setStatus('current')
if mibBuilder.loadTexts: swL3IpStaticRouteEntry.setDescription("A particular route to a particular destination, under a particular policy. Once an entry be built,it shouldn't be modified.That is,it just support create and delete action.")
swL3IpStaticRouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpStaticRouteDest.setStatus('current')
if mibBuilder.loadTexts: swL3IpStaticRouteDest.setDescription('The destination IP address of this route. This object may not take a Multicast (Class D) address value. Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical-AND of x with the value of the corresponding instance of the swL3IpStaticRouteMask object is not equal to x.')
swL3IpStaticRouteMask = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpStaticRouteMask.setStatus('current')
if mibBuilder.loadTexts: swL3IpStaticRouteMask.setDescription('Indicate the mask to be logical-ANDed with the destination address before being compared to the value in the swL3IpStaticRouteDest field. For those systems that do not support arbitrary subnet masks, an agent constructs the value of the swL3IpStaticRouteMask by reference to the IP Address Class. Any assignment (implicit or otherwise) of an instance of this object to a value x must be rejected if the bitwise logical-AND of x with the value of the corresponding instance of the swL3IpStaticRouteDest object is not equal to swL3IpStaticRouteDest.')
swL3IpStaticRouteBkupState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("primary", 1), ("backup", 2), ("none", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpStaticRouteBkupState.setStatus('current')
if mibBuilder.loadTexts: swL3IpStaticRouteBkupState.setDescription('The routing state for this route.The value SHOULD be primary(1) or backup(2).')
swL3IpStaticRouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 5, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpStaticRouteNextHop.setStatus('current')
if mibBuilder.loadTexts: swL3IpStaticRouteNextHop.setDescription('On remote routes, the address of the next sys- tem en route; Otherwise, 0.0.0.0.')
swL3IpStaticRouteMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 5, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpStaticRouteMetric.setStatus('current')
if mibBuilder.loadTexts: swL3IpStaticRouteMetric.setDescription('The routing metric for this route.')
swL3IpStaticRouteStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 5, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("valid", 3), ("active", 4), ("inActive", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpStaticRouteStatus.setStatus('current')
if mibBuilder.loadTexts: swL3IpStaticRouteStatus.setDescription('This object indicates the status of this entry. other(1) - this entry is currently in use but the conditions under which it will remain so are different from each of the following values. invalid(2) - writing this value to the object, and then the corresponding entry will be removed from the table. valid(3) - this entry is reside in the table. active(4) - the nextHop of this entry exists in the ARP table. inActive(5) - the next hop of this entry does not exist in the ARP table.')
swL3IpStaticRouteWeight = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: swL3IpStaticRouteWeight.setStatus('current')
if mibBuilder.loadTexts: swL3IpStaticRouteWeight.setDescription('Specifies the weight value. Used for the weighted multipath.')
swL3IpStaticRouteInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 11, 117, 1, 3, 3, 2, 5, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: swL3IpStaticRouteInterfaceName.setStatus('current')
if mibBuilder.loadTexts: swL3IpStaticRouteInterfaceName.setDescription('Specifies the name of the IP interface.')
mibBuilder.exportSymbols("DGS-3120-24SC-L3MGMT-MIB", swL3IpCtrlLocalProxyArp=swL3IpCtrlLocalProxyArp, swL3Ipv6CtrlInterfaceName=swL3Ipv6CtrlInterfaceName, swL3MgmtMIB=swL3MgmtMIB, swL3IpStaticRouteMetric=swL3IpStaticRouteMetric, swL3IpFdbInfoPort=swL3IpFdbInfoPort, swL3IpCtrlIpDhcpOption12State=swL3IpCtrlIpDhcpOption12State, swL3IpCtrlTable=swL3IpCtrlTable, swL3IpStaticRouteDest=swL3IpStaticRouteDest, swL3IpCtrlState=swL3IpCtrlState, swL3IpCtrlVlanName=swL3IpCtrlVlanName, swL3Ipv6CtrlMaxReassmblySize=swL3Ipv6CtrlMaxReassmblySize, swL3IpCtrlSecondary=swL3IpCtrlSecondary, swL3Ipv6Address=swL3Ipv6Address, swL3IpFdbInfoIpSubnetMask=swL3IpFdbInfoIpSubnetMask, swL3IpFdbInfoType=swL3IpFdbInfoType, swL3IpStaticRouteMask=swL3IpStaticRouteMask, swL3IpCtrlMgmt=swL3IpCtrlMgmt, swL3Ipv6AddressCtrlState=swL3Ipv6AddressCtrlState, swL3IpArpAgingTime=swL3IpArpAgingTime, swL3IpCtrlIpSubnetMask=swL3IpCtrlIpSubnetMask, swL3IpCtrlAllIpIfState=swL3IpCtrlAllIpIfState, swL3IpCtrlMode=swL3IpCtrlMode, swL3Ipv6CtrlNsRetransTimer=swL3Ipv6CtrlNsRetransTimer, swL3IpCtrlIpv6AdminState=swL3IpCtrlIpv6AdminState, swL3IpMgmt=swL3IpMgmt, swL3IpCtrlAdminState=swL3IpCtrlAdminState, swL3Ipv6AddressCtrlInterfaceName=swL3Ipv6AddressCtrlInterfaceName, swL3IpStaticRouteEntry=swL3IpStaticRouteEntry, swL3IpFdbInfoEntry=swL3IpFdbInfoEntry, NetAddress=NetAddress, swL3IpFdbInfoTable=swL3IpFdbInfoTable, swL3Ipv6CtrlEntry=swL3Ipv6CtrlEntry, swL3IpCtrlDhcpv6ClientState=swL3IpCtrlDhcpv6ClientState, swL3IpCtrlIpAddr=swL3IpCtrlIpAddr, swL3IpStaticRouteBkupState=swL3IpStaticRouteBkupState, swL3IpCtrlIpv6LinkLocalPrefixLen=swL3IpCtrlIpv6LinkLocalPrefixLen, swL3IpStaticRouteStatus=swL3IpStaticRouteStatus, swL3IpStaticRouteNextHop=swL3IpStaticRouteNextHop, swL3Ipv6AddressCtrlPrefixLen=swL3Ipv6AddressCtrlPrefixLen, PYSNMP_MODULE_ID=swL3MgmtMIB, swL3IpCtrlProxyArp=swL3IpCtrlProxyArp, swL3Ipv6AddressCtrlTable=swL3Ipv6AddressCtrlTable, swL3IpCtrlEntry=swL3IpCtrlEntry, NodeAddress=NodeAddress, swL3IpCtrlInterfaceName=swL3IpCtrlInterfaceName, swL3IpStaticRouteTable=swL3IpStaticRouteTable, swL3IpCtrlIpDhcpOption12HostName=swL3IpCtrlIpDhcpOption12HostName, swL3Ipv6CtrlTable=swL3Ipv6CtrlTable, swL3IpCtrlIfIndex=swL3IpCtrlIfIndex, swL3IpCtrlIpv4AdminState=swL3IpCtrlIpv4AdminState, swL3IpStaticRouteWeight=swL3IpStaticRouteWeight, swL3IpFdbMgmt=swL3IpFdbMgmt, swL3IpStaticRouteInterfaceName=swL3IpStaticRouteInterfaceName, swL3IpFdbInfoIpAddr=swL3IpFdbInfoIpAddr, swL3Ipv6AddressCtrlAddressType=swL3Ipv6AddressCtrlAddressType, swL3IpCtrlIpv6LinkLocalAutoState=swL3IpCtrlIpv6LinkLocalAutoState, swL3Ipv6AddressCtrlEntry=swL3Ipv6AddressCtrlEntry, swL3IpCtrlIpv6LinkLocalAddress=swL3IpCtrlIpv6LinkLocalAddress)