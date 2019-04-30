#
# PySNMP MIB module ZHNFIREWALL (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZHNFIREWALL
# Produced by pysmi-0.3.4 at Mon Apr 29 21:40:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
enterprises, IpAddress, ModuleIdentity, Gauge32, Counter64, Integer32, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Counter32, TimeTicks, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "IpAddress", "ModuleIdentity", "Gauge32", "Counter64", "Integer32", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Counter32", "TimeTicks", "NotificationType", "Bits")
TruthValue, RowStatus, TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "MacAddress", "DisplayString")
lanEthernetIndex, lanDeviceIndex = mibBuilder.importSymbols("ZHNLANDEVICE", "lanEthernetIndex", "lanDeviceIndex")
zhoneWtn, = mibBuilder.importSymbols("Zhone", "zhoneWtn")
ZhoneRowStatus, = mibBuilder.importSymbols("Zhone-TC", "ZhoneRowStatus")
zhnFirewall = ModuleIdentity((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45))
zhnFirewall.setRevisions(('2012-04-18 12:00', '2012-02-03 12:00',))
if mibBuilder.loadTexts: zhnFirewall.setLastUpdated('201204181200Z')
if mibBuilder.loadTexts: zhnFirewall.setOrganization('Zhone Technologies, Inc.')
zhnFirewallObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1))
class FirewallMgmtAccessServiceValues(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("http", 1), ("https", 2), ("ping", 3), ("snmp", 4), ("snmpTrap", 5), ("ssh", 6), ("telnet", 7))

class FirewallMgmtAccessServiceActions(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("allow", 1), ("deny", 2), ("undefined", 3))

class FirewallPortTypeValues(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("portRange", 1), ("portRemap", 2), ("dmz", 3))

class FirewallPortProtocolValues(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("tcp", 1), ("udp", 2), ("tcpOrUdp", 3), ("icmp", 4), ("icmpv4", 5), ("none", 6))

firewallMgmtAccessTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1), )
if mibBuilder.loadTexts: firewallMgmtAccessTable.setStatus('current')
firewallMgmtAccessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1), ).setIndexNames((0, "ZHNLANDEVICE", "lanDeviceIndex"), (0, "ZHNLANDEVICE", "lanEthernetIndex"), (0, "ZHNFIREWALL", "firewallMgmtServiceIndex"))
if mibBuilder.loadTexts: firewallMgmtAccessEntry.setStatus('current')
firewallMgmtServiceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1, 1), FirewallMgmtAccessServiceValues())
if mibBuilder.loadTexts: firewallMgmtServiceIndex.setStatus('current')
firewallMgmtService = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: firewallMgmtService.setStatus('current')
firewallMgmtAction = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 1, 1, 3), FirewallMgmtAccessServiceActions()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallMgmtAction.setStatus('current')
firewallPortForwardingTable = MibTable((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2), )
if mibBuilder.loadTexts: firewallPortForwardingTable.setStatus('current')
firewallPortForwardingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1), ).setIndexNames((0, "ZHNLANDEVICE", "lanDeviceIndex"), (0, "ZHNLANDEVICE", "lanEthernetIndex"), (0, "ZHNFIREWALL", "firewallPortForwardingIndex"))
if mibBuilder.loadTexts: firewallPortForwardingEntry.setStatus('current')
firewallPortForwardingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: firewallPortForwardingIndex.setStatus('current')
firewallPortForwardingName = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortForwardingName.setStatus('current')
firewallPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 3), FirewallPortTypeValues()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortType.setStatus('current')
firewallPortProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 4), FirewallPortProtocolValues()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortProtocol.setStatus('current')
firewallPortPublicPortStart = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortPublicPortStart.setStatus('current')
firewallPortPublicPortEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortPublicPortEnd.setStatus('current')
firewallPortPrivatePort = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortPrivatePort.setStatus('current')
firewallPortPrivateIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortPrivateIPAddress.setStatus('current')
firewallPortForwardingRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 1, 2, 1, 9), ZhoneRowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firewallPortForwardingRowStatus.setStatus('current')
zhnFirewallConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3))
zhnFirewallGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 1))
zhnFirewallCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 2))
zhnFirewallCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 2, 1)).setObjects(("ZHNFIREWALL", "zhnFirewallMgmtAccessGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnFirewallCompliance = zhnFirewallCompliance.setStatus('current')
zhnFirewallMgmtAccessGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 1, 1)).setObjects(("ZHNFIREWALL", "firewallMgmtService"), ("ZHNFIREWALL", "firewallMgmtAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnFirewallMgmtAccessGroup = zhnFirewallMgmtAccessGroup.setStatus('current')
zhnFirewallPortForwardingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5504, 2, 5, 45, 3, 1, 2)).setObjects(("ZHNFIREWALL", "firewallPortForwardingName"), ("ZHNFIREWALL", "firewallPortType"), ("ZHNFIREWALL", "firewallPortProtocol"), ("ZHNFIREWALL", "firewallPortPublicPortStart"), ("ZHNFIREWALL", "firewallPortPublicPortEnd"), ("ZHNFIREWALL", "firewallPortPrivatePort"), ("ZHNFIREWALL", "firewallPortPrivateIPAddress"), ("ZHNFIREWALL", "firewallPortForwardingRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    zhnFirewallPortForwardingGroup = zhnFirewallPortForwardingGroup.setStatus('current')
mibBuilder.exportSymbols("ZHNFIREWALL", FirewallPortTypeValues=FirewallPortTypeValues, zhnFirewall=zhnFirewall, firewallMgmtAction=firewallMgmtAction, firewallMgmtService=firewallMgmtService, firewallPortProtocol=firewallPortProtocol, PYSNMP_MODULE_ID=zhnFirewall, zhnFirewallMgmtAccessGroup=zhnFirewallMgmtAccessGroup, firewallPortType=firewallPortType, zhnFirewallCompliances=zhnFirewallCompliances, firewallPortForwardingTable=firewallPortForwardingTable, zhnFirewallGroups=zhnFirewallGroups, firewallMgmtAccessEntry=firewallMgmtAccessEntry, firewallPortForwardingName=firewallPortForwardingName, firewallMgmtAccessTable=firewallMgmtAccessTable, firewallPortPublicPortStart=firewallPortPublicPortStart, firewallPortPublicPortEnd=firewallPortPublicPortEnd, FirewallMgmtAccessServiceActions=FirewallMgmtAccessServiceActions, firewallPortForwardingEntry=firewallPortForwardingEntry, zhnFirewallPortForwardingGroup=zhnFirewallPortForwardingGroup, zhnFirewallObjects=zhnFirewallObjects, FirewallPortProtocolValues=FirewallPortProtocolValues, zhnFirewallConformance=zhnFirewallConformance, firewallPortPrivateIPAddress=firewallPortPrivateIPAddress, FirewallMgmtAccessServiceValues=FirewallMgmtAccessServiceValues, firewallPortPrivatePort=firewallPortPrivatePort, firewallPortForwardingRowStatus=firewallPortForwardingRowStatus, zhnFirewallCompliance=zhnFirewallCompliance, firewallMgmtServiceIndex=firewallMgmtServiceIndex, firewallPortForwardingIndex=firewallPortForwardingIndex)
