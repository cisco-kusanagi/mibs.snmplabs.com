#
# PySNMP MIB module ZHNFIREWALL (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHNFIREWALL
# Produced by pysmi-0.3.4 at Wed May  1 15:46:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, enterprises, IpAddress, Bits, Gauge32, Counter32, Counter64, NotificationType, ObjectIdentity, MibIdentifier, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "enterprises", "IpAddress", "Bits", "Gauge32", "Counter32", "Counter64", "NotificationType", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "TimeTicks")
TruthValue, RowStatus, DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "MacAddress", "TextualConvention")
lanEthernetIndex, lanDeviceIndex = mibBuilder.importSymbols("ZHNLANDEVICE", "lanEthernetIndex", "lanDeviceIndex")
zhoneWtn, = mibBuilder.importSymbols("Zhone", "zhoneWtn")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
zhnFirewall = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45))
zhnFirewall.setRevisions(('2012-04-18 12:00', '2012-02-03 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: zhnFirewall.setRevisionsDescriptions(('Added https to FirewallMgmtAccessServiceValues', 'First Draft',))
if mibBuilder.loadTexts: zhnFirewall.setLastUpdated('201204181200Z')
if mibBuilder.loadTexts: zhnFirewall.setOrganization('Zhone Technologies, Inc.')
if mibBuilder.loadTexts: zhnFirewall.setContactInfo('Zhone Technologies, Inc. Florida Design Center 8545 126th Avenue North Largo, FL 33773 Toll-Free: +1 877-ZHONE20 (+1 877-946-6320) Tel: +1-510-777-7000 Fax: +1-510-777-7001 E-mail: support@zhone.com')
if mibBuilder.loadTexts: zhnFirewall.setDescription('This file defines the private Enterprise MIB extensions that define LAN Management Access Service Filters and Port Forwarding objects supported by the Zhone CPEs.')
zhnFirewallObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1))
class FirewallMgmtAccessServiceValues(TextualConvention, Integer32):
    description = 'LAN Management Access Services that can be blocked from the CPEs management network.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("http", 1), ("https", 2), ("ping", 3), ("snmp", 4), ("snmpTrap", 5), ("ssh", 6), ("telnet", 7))

class FirewallMgmtAccessServiceActions(TextualConvention, Integer32):
    description = 'LAN Management Access Service actions to perform for the specified service.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("allow", 1), ("deny", 2), ("undefined", 3))

class FirewallPortTypeValues(TextualConvention, Integer32):
    description = 'LAN Port Forwarding actions supported.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("portRange", 1), ("portRemap", 2), ("dmz", 3))

class FirewallPortProtocolValues(TextualConvention, Integer32):
    description = 'LAN Port Forwarding protocols that can be filtered, per port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("tcp", 1), ("udp", 2), ("tcpOrUdp", 3), ("icmp", 4), ("icmpv4", 5), ("none", 6))

firewallMgmtAccessTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1), )
if mibBuilder.loadTexts: firewallMgmtAccessTable.setStatus('current')
if mibBuilder.loadTexts: firewallMgmtAccessTable.setDescription('Table of LAN Management Access Service Filters')
firewallMgmtAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1), ).setIndexNames((0, "ZHNLANDEVICE", "lanDeviceIndex"), (0, "ZHNLANDEVICE", "lanEthernetIndex"), (0, "ZHNFIREWALL", "firewallMgmtServiceIndex"))
if mibBuilder.loadTexts: firewallMgmtAccessEntry.setStatus('current')
if mibBuilder.loadTexts: firewallMgmtAccessEntry.setDescription('Table of entries of LAN Management Access service filters. This table is used to configure management access on the device. It is useful in making the device management network by blocking protocols or services that are highly susceptible to external attacks.')
firewallMgmtServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1, 1), FirewallMgmtAccessServiceValues())
if mibBuilder.loadTexts: firewallMgmtServiceIndex.setStatus('current')
if mibBuilder.loadTexts: firewallMgmtServiceIndex.setDescription('LAN Management Access Services Table index. Enumerated values: Http (1), Https (2), Ping (3), Snmp (4), SnmpTrap (5), Ssh (6), Telnet (7) ')
firewallMgmtService = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firewallMgmtService.setStatus('current')
if mibBuilder.loadTexts: firewallMgmtService.setDescription('LAN Management Access Service description.')
firewallMgmtAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1, 3), FirewallMgmtAccessServiceActions()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallMgmtAction.setStatus('current')
if mibBuilder.loadTexts: firewallMgmtAction.setDescription('LAN Management Access Service filtering action. Enumerated values: Allow (1), Deny (2), Undefined (3) ')
firewallPortForwardingTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2), )
if mibBuilder.loadTexts: firewallPortForwardingTable.setStatus('current')
if mibBuilder.loadTexts: firewallPortForwardingTable.setDescription('Table of LAN Port Forwarding Rules. Note that the rules in this table have no effect until the global firewall object (sysFirewallEnable) is enabled.')
firewallPortForwardingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1), ).setIndexNames((0, "ZHNLANDEVICE", "lanDeviceIndex"), (0, "ZHNLANDEVICE", "lanEthernetIndex"), (0, "ZHNFIREWALL", "firewallPortForwardingIndex"))
if mibBuilder.loadTexts: firewallPortForwardingEntry.setStatus('current')
if mibBuilder.loadTexts: firewallPortForwardingEntry.setDescription('This table is used to configure port forwarding firewall rules for the device.')
firewallPortForwardingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: firewallPortForwardingIndex.setStatus('current')
if mibBuilder.loadTexts: firewallPortForwardingIndex.setDescription('LAN Port Forwarding Rules index.')
firewallPortForwardingName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortForwardingName.setStatus('current')
if mibBuilder.loadTexts: firewallPortForwardingName.setDescription('Descriptive name for a LAN Port Forwarding Rule.')
firewallPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 3), FirewallPortTypeValues()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortType.setStatus('current')
if mibBuilder.loadTexts: firewallPortType.setDescription('Enumerated value of: portRange (1), -- Range indicates that any traffic on those ports will be -- sent to the private IP address. portRemap (2), -- Remap indicates that any traffic on those ports will be -- sent to the private IP address at the private port. dmz (3) -- When DMZ is chosen it is the only rule allowed on that -- interface. A DMZ rule is effectively the same as a Range -- rule with all ports included. Range rules are more secure -- than setting a DMZ rule, because Range rules allow specific -- ports or groups of ports to be opened up. ')
firewallPortProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 4), FirewallPortProtocolValues()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortProtocol.setStatus('current')
if mibBuilder.loadTexts: firewallPortProtocol.setDescription('Enumerated value of: tcp (1), udp (2), tcpOrUdp (3), icmp (4), icmpv4 (5), none (6) ')
firewallPortPublicPortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortPublicPortStart.setStatus('current')
if mibBuilder.loadTexts: firewallPortPublicPortStart.setDescription('Lowest value port number for the range.')
firewallPortPublicPortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortPublicPortEnd.setStatus('current')
if mibBuilder.loadTexts: firewallPortPublicPortEnd.setDescription('Highest value port number for the range. This can be equal to firewallPortPublicPortStart if there is only one port.')
firewallPortPrivatePort = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortPrivatePort.setStatus('current')
if mibBuilder.loadTexts: firewallPortPrivatePort.setDescription('The port number with which to send the traffic.')
firewallPortPrivateIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortPrivateIPAddress.setStatus('current')
if mibBuilder.loadTexts: firewallPortPrivateIPAddress.setDescription('The port IP Address with which to send the traffic.')
firewallPortForwardingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 9), ZhoneRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortForwardingRowStatus.setStatus('current')
if mibBuilder.loadTexts: firewallPortForwardingRowStatus.setDescription('The SNMP RowStatus of the current row. The following objects must be specified upon row creation: firewallPortForwardingName firewallPortPrivateIPAddress ')
zhnFirewallConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3))
zhnFirewallGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 1))
zhnFirewallCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 2))
zhnFirewallCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 2, 1)).setObjects(("ZHNFIREWALL", "zhnFirewallMgmtAccessGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnFirewallCompliance = zhnFirewallCompliance.setStatus('current')
if mibBuilder.loadTexts: zhnFirewallCompliance.setDescription('The Compliance statement for SNMP entities which manage the Zhone CPE LAN Firewall Management Access Services and Port Forwarding Information')
zhnFirewallMgmtAccessGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 1, 1)).setObjects(("ZHNFIREWALL", "firewallMgmtService"), ("ZHNFIREWALL", "firewallMgmtAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnFirewallMgmtAccessGroup = zhnFirewallMgmtAccessGroup.setStatus('current')
if mibBuilder.loadTexts: zhnFirewallMgmtAccessGroup.setDescription('A collection of Zhone IP objects that describe the LAN Management Access Services that can be filtered for a particular LAN interface.')
zhnFirewallPortForwardingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 1, 2)).setObjects(("ZHNFIREWALL", "firewallPortForwardingName"), ("ZHNFIREWALL", "firewallPortType"), ("ZHNFIREWALL", "firewallPortProtocol"), ("ZHNFIREWALL", "firewallPortPublicPortStart"), ("ZHNFIREWALL", "firewallPortPublicPortEnd"), ("ZHNFIREWALL", "firewallPortPrivatePort"), ("ZHNFIREWALL", "firewallPortPrivateIPAddress"), ("ZHNFIREWALL", "firewallPortForwardingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnFirewallPortForwardingGroup = zhnFirewallPortForwardingGroup.setStatus('current')
if mibBuilder.loadTexts: zhnFirewallPortForwardingGroup.setDescription('A collection of Zhone IP objects that describe the LAN Port Forwarding Management rules for filtering protocols and ports for a particular LAN interface.')
mibBuilder.exportSymbols("ZHNFIREWALL", FirewallMgmtAccessServiceActions=FirewallMgmtAccessServiceActions, firewallPortProtocol=firewallPortProtocol, firewallMgmtAccessTable=firewallMgmtAccessTable, zhnFirewall=zhnFirewall, FirewallPortTypeValues=FirewallPortTypeValues, FirewallMgmtAccessServiceValues=FirewallMgmtAccessServiceValues, firewallPortType=firewallPortType, firewallPortForwardingEntry=firewallPortForwardingEntry, firewallPortForwardingTable=firewallPortForwardingTable, firewallMgmtAction=firewallMgmtAction, firewallMgmtService=firewallMgmtService, PYSNMP_MODULE_ID=zhnFirewall, firewallMgmtServiceIndex=firewallMgmtServiceIndex, firewallPortPublicPortStart=firewallPortPublicPortStart, firewallMgmtAccessEntry=firewallMgmtAccessEntry, zhnFirewallPortForwardingGroup=zhnFirewallPortForwardingGroup, firewallPortForwardingRowStatus=firewallPortForwardingRowStatus, firewallPortPrivatePort=firewallPortPrivatePort, zhnFirewallCompliance=zhnFirewallCompliance, firewallPortForwardingName=firewallPortForwardingName, zhnFirewallGroups=zhnFirewallGroups, FirewallPortProtocolValues=FirewallPortProtocolValues, firewallPortPublicPortEnd=firewallPortPublicPortEnd, zhnFirewallMgmtAccessGroup=zhnFirewallMgmtAccessGroup, zhnFirewallObjects=zhnFirewallObjects, firewallPortPrivateIPAddress=firewallPortPrivateIPAddress, zhnFirewallConformance=zhnFirewallConformance, zhnFirewallCompliances=zhnFirewallCompliances, firewallPortForwardingIndex=firewallPortForwardingIndex)
