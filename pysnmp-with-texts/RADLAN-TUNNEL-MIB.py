#
# PySNMP MIB module RADLAN-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-TUNNEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:50:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
DnsName, = mibBuilder.importSymbols("DNS-SERVER-MIB", "DnsName")
IANAtunnelType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAtunnelType")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, Counter32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, NotificationType, ModuleIdentity, IpAddress, iso, Unsigned32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "Counter32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "NotificationType", "ModuleIdentity", "IpAddress", "iso", "Unsigned32", "TimeTicks", "Bits")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
tunnelIfEntry, = mibBuilder.importSymbols("TUNNEL-MIB", "tunnelIfEntry")
rlTunnel = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 122))
rlTunnel.setRevisions(('2012-05-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlTunnel.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlTunnel.setLastUpdated('201109120000Z')
if mibBuilder.loadTexts: rlTunnel.setOrganization('Marvell Semiconductor, Inc.')
if mibBuilder.loadTexts: rlTunnel.setContactInfo('www.marvell.com')
if mibBuilder.loadTexts: rlTunnel.setDescription('The private MIB module definition for Tunneling.')
rlTunnelIsatapStatus = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapStatus.setStatus('deprecated')
if mibBuilder.loadTexts: rlTunnelIsatapStatus.setDescription('The ISATAP status.')
rlTunnelIsatapRobustness = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapRobustness.setStatus('deprecated')
if mibBuilder.loadTexts: rlTunnelIsatapRobustness.setDescription('specifies how many DNS Querys and Router Solicitations should be sent to get the corresponding reply.')
rlTunnelIsatapDnsHostName = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 3), DnsName()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapDnsHostName.setStatus('deprecated')
if mibBuilder.loadTexts: rlTunnelIsatapDnsHostName.setDescription('The domain name for ISATAP.')
rlTunnelIsatapQueryInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapQueryInterval.setStatus('deprecated')
if mibBuilder.loadTexts: rlTunnelIsatapQueryInterval.setDescription('specifies the time interval between sending of DNS Queries before receiving the first reply from the DNS Server.')
rlTunnelIsatapRSInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapRSInterval.setStatus('deprecated')
if mibBuilder.loadTexts: rlTunnelIsatapRSInterval.setDescription('specifies the time interval between sending of Router Solicitations before receiving the first reply from the ISATAP Router.')
rlTunnelIsatapMinQueryInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapMinQueryInterval.setStatus('deprecated')
if mibBuilder.loadTexts: rlTunnelIsatapMinQueryInterval.setDescription('specifies the minimum time interval between between successive queries of same advertising ISATAP interface.')
rlTunnelIsatapMinRSInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapMinRSInterval.setStatus('deprecated')
if mibBuilder.loadTexts: rlTunnelIsatapMinRSInterval.setDescription('specifies the minimum time between successive solicitations of the same advertising ISATAP interface.')
rlTunnelIsatapRouterAddress = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapRouterAddress.setStatus('deprecated')
if mibBuilder.loadTexts: rlTunnelIsatapRouterAddress.setDescription('specifies the IPv4 address of ISATAP Router.')
rlTunnelIsatapLocalIPv4Address = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapLocalIPv4Address.setStatus('deprecated')
if mibBuilder.loadTexts: rlTunnelIsatapLocalIPv4Address.setDescription('specifies the IPv4 address currently used as IPv4 source address for ISATAP Tunnel.')
rlTunnelGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 122, 11))
rlTunnelIfTable = MibTable((1, 3, 6, 1, 4, 1, 89, 122, 11, 1), )
if mibBuilder.loadTexts: rlTunnelIfTable.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIfTable.setDescription('This table is parallel to tunnelIfTable, and is used to add/delete tunnel entries to/from that table. In addition it contains private objects.')
rlTunnelIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 122, 11, 1, 1), )
tunnelIfEntry.registerAugmentions(("RADLAN-TUNNEL-MIB", "rlTunnelIfEntry"))
rlTunnelIfEntry.setIndexNames(*tunnelIfEntry.getIndexNames())
if mibBuilder.loadTexts: rlTunnelIfEntry.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIfEntry.setDescription('Additional configuration parameters for a tunnel interface.')
rlTunnelIfEncapsMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 11, 1, 1, 1), IANAtunnelType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIfEncapsMethod.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIfEncapsMethod.setDescription('The encapsulation method used by the tunnel. This field added since it is read-only in standard MIB.')
rlTunnelIfLocalAddressSource = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 11, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("configured", 1), ("auto", 2), ("interface", 3))).clone('configured')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIfLocalAddressSource.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIfLocalAddressSource.setDescription('Defines the method of obtaining Local address for the tunnel interface. Configured - configured by user. Automatic - minimum IP address of the device. Interface - minimum IP address on user specified interface.')
rlTunnelIfLocalAddressInterfaceId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 11, 1, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIfLocalAddressInterfaceId.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIfLocalAddressInterfaceId.setDescription('Interface ID, used to determine Local address for tunnel interface if rlTunnelIfLocalAddressSource set to interface.')
rlTunnelIfLocalIPv4Address = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 11, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIfLocalIPv4Address.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIfLocalIPv4Address.setDescription('Specifies the IPv4 address currently used as IPv4 Local address for IPv6 over IPv4 Tunnel.')
rlTunnelIfStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 11, 1, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIfStatus.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIfStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table.')
rlTunnelTypeSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 122, 12))
rlTunnelIsatap = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 122, 12, 1))
rlTunnelIsatapConfTable = MibTable((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 1), )
if mibBuilder.loadTexts: rlTunnelIsatapConfTable.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapConfTable.setDescription('This table contains ISATAP-specific configuration.')
rlTunnelIsatapConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlTunnelIsatapConfEntry.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapConfEntry.setDescription('Additional configuration parameters for a tunnel interface.')
rlTunnelIsatapConfDnsName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 1, 1, 1), OctetString().clone('ISATAP')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapConfDnsName.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapConfDnsName.setDescription('DNS name.')
rlTunnelIsatapConfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 1, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapConfRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapConfRowStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table.')
rlTunnelIsatapPrlTable = MibTable((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 2), )
if mibBuilder.loadTexts: rlTunnelIsatapPrlTable.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapPrlTable.setDescription('This table contains ISATAP-specific configuration.')
rlTunnelIsatapPrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 2, 1), ).setIndexNames((0, "RADLAN-TUNNEL-MIB", "rlTunnelIsatapPrlIfIndex"), (0, "RADLAN-TUNNEL-MIB", "rlTunnelIsatapPrlPriority"))
if mibBuilder.loadTexts: rlTunnelIsatapPrlEntry.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapPrlEntry.setDescription('Additional configuration parameters for a tunnel interface.')
rlTunnelIsatapPrlIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapPrlIfIndex.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapPrlIfIndex.setDescription('The index of the interface to which this PRL entry belongs.')
rlTunnelIsatapPrlPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapPrlPriority.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapPrlPriority.setDescription('The priority of the entry. Lower value - higher priority.')
rlTunnelIsatapPrlAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapPrlAddress.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapPrlAddress.setDescription('IPv4 address of the potential router.')
rlTunnelIsatapPrlIsActive = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlTunnelIsatapPrlIsActive.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapPrlIsActive.setDescription('Whether the PRL entry is active (meaning it has an up to date RA).')
rlTunnelIsatapConfRSInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(10, 3600)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapConfRSInterval.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapConfRSInterval.setDescription('Specifies the time interval between Router Solicitations prior to receiving the first reply from the ISATAP router.')
rlTunnelIsatapConfRobustness = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 12, 1, 12), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 20)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIsatapConfRobustness.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIsatapConfRobustness.setDescription('After a Router Advertisement was received, Router Solicitation messages are sent every Lifetime / (1 + Robustness) seconds, where Lifetime is the Lifetime advertised in the RA.')
rlTunnelIPv6EndConfig = MibScalar((1, 3, 6, 1, 4, 1, 89, 122, 12, 2), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTunnelIPv6EndConfig.setStatus('current')
if mibBuilder.loadTexts: rlTunnelIPv6EndConfig.setDescription('Used to indicate end of snmp configuration for IPv6. Can be removed, if mechanism for indicating end config per mib is added to SNMP.')
mibBuilder.exportSymbols("RADLAN-TUNNEL-MIB", rlTunnelIfEntry=rlTunnelIfEntry, PYSNMP_MODULE_ID=rlTunnel, rlTunnelIsatapQueryInterval=rlTunnelIsatapQueryInterval, rlTunnelIsatap=rlTunnelIsatap, rlTunnelIsatapPrlIfIndex=rlTunnelIsatapPrlIfIndex, rlTunnelIsatapRouterAddress=rlTunnelIsatapRouterAddress, rlTunnelIfLocalIPv4Address=rlTunnelIfLocalIPv4Address, rlTunnelIsatapPrlEntry=rlTunnelIsatapPrlEntry, rlTunnelIsatapRobustness=rlTunnelIsatapRobustness, rlTunnelIsatapConfDnsName=rlTunnelIsatapConfDnsName, rlTunnelIfStatus=rlTunnelIfStatus, rlTunnelIsatapConfRobustness=rlTunnelIsatapConfRobustness, rlTunnelIfLocalAddressSource=rlTunnelIfLocalAddressSource, rlTunnelIsatapStatus=rlTunnelIsatapStatus, rlTunnelIsatapLocalIPv4Address=rlTunnelIsatapLocalIPv4Address, rlTunnelIPv6EndConfig=rlTunnelIPv6EndConfig, rlTunnel=rlTunnel, rlTunnelIsatapRSInterval=rlTunnelIsatapRSInterval, rlTunnelIsatapMinRSInterval=rlTunnelIsatapMinRSInterval, rlTunnelIsatapDnsHostName=rlTunnelIsatapDnsHostName, rlTunnelIfLocalAddressInterfaceId=rlTunnelIfLocalAddressInterfaceId, rlTunnelGeneral=rlTunnelGeneral, rlTunnelIsatapPrlPriority=rlTunnelIsatapPrlPriority, rlTunnelIsatapPrlIsActive=rlTunnelIsatapPrlIsActive, rlTunnelIsatapMinQueryInterval=rlTunnelIsatapMinQueryInterval, rlTunnelIfTable=rlTunnelIfTable, rlTunnelIsatapConfEntry=rlTunnelIsatapConfEntry, rlTunnelIsatapPrlAddress=rlTunnelIsatapPrlAddress, rlTunnelIsatapConfRSInterval=rlTunnelIsatapConfRSInterval, rlTunnelIfEncapsMethod=rlTunnelIfEncapsMethod, rlTunnelIsatapConfRowStatus=rlTunnelIsatapConfRowStatus, rlTunnelTypeSpecific=rlTunnelTypeSpecific, rlTunnelIsatapConfTable=rlTunnelIsatapConfTable, rlTunnelIsatapPrlTable=rlTunnelIsatapPrlTable)
