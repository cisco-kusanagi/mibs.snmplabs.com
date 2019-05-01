#
# PySNMP MIB module IPV6-UDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IPV6-UDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:56:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
Ipv6IfIndexOrZero, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6IfIndexOrZero", "Ipv6Address")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, MibIdentifier, iso, Bits, Gauge32, experimental, ObjectIdentity, Unsigned32, mib_2, ModuleIdentity, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "MibIdentifier", "iso", "Bits", "Gauge32", "experimental", "ObjectIdentity", "Unsigned32", "mib-2", "ModuleIdentity", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ipv6UdpMIB = ModuleIdentity((1, 3, 6, 1, 3, 87))
ipv6UdpMIB.setRevisions(('2017-02-22 00:00', '1998-01-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ipv6UdpMIB.setRevisionsDescriptions(('Obsoleting this MIB module; it has been replaced by the revised UDP-MIB (RFC 4113).', 'First revision, published as RFC 2454',))
if mibBuilder.loadTexts: ipv6UdpMIB.setLastUpdated('201702220000Z')
if mibBuilder.loadTexts: ipv6UdpMIB.setOrganization('IETF IPv6 MIB Working Group')
if mibBuilder.loadTexts: ipv6UdpMIB.setContactInfo(' Mike Daniele Postal: Compaq Computer Corporation 110 Spitbrook Rd Nashua, NH 03062. US Phone: +1 603 884 1423 Email: daniele@zk3.dec.com')
if mibBuilder.loadTexts: ipv6UdpMIB.setDescription("The obsolete MIB module for entities implementing UDP over IPv6. Use the UDP-MIB instead. Copyright (c) 2017 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")
udp = MibIdentifier((1, 3, 6, 1, 2, 1, 7))
ipv6UdpTable = MibTable((1, 3, 6, 1, 2, 1, 7, 6), )
if mibBuilder.loadTexts: ipv6UdpTable.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpTable.setDescription('A table containing UDP listener information for UDP/IPv6 endpoints. This table is obsoleted by UDP-MIB::udpEndpointTable.')
ipv6UdpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 7, 6, 1), ).setIndexNames((0, "IPV6-UDP-MIB", "ipv6UdpLocalAddress"), (0, "IPV6-UDP-MIB", "ipv6UdpLocalPort"), (0, "IPV6-UDP-MIB", "ipv6UdpIfIndex"))
if mibBuilder.loadTexts: ipv6UdpEntry.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpEntry.setDescription('Information about a particular current UDP listener. Note that conceptual rows in this table require an additional index object compared to udpTable, since IPv6 addresses are not guaranteed to be unique on the managed node. This entry is obsoleted by UDP-MIB::udpEndpointTable.')
ipv6UdpLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6UdpLocalAddress.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpLocalAddress.setDescription('The local IPv6 address for this UDP listener. In the case of a UDP listener which is willing to accept datagrams for any IPv6 address associated with the managed node, the value ::0 is used. This object is obsoleted by UDP-MIB::udpEndpointLocalAddress.')
ipv6UdpLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: ipv6UdpLocalPort.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpLocalPort.setDescription('The local port number for this UDP listener. This object is obsoleted by UDP-MIB::udpEndpointLocalPort.')
ipv6UdpIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 7, 6, 1, 3), Ipv6IfIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6UdpIfIndex.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpIfIndex.setDescription('An index object used to disambiguate conceptual rows in the table, since the ipv6UdpLocalAddress/ipv6UdpLocalPort pair may not be unique. This object identifies the local interface that is associated with ipv6UdpLocalAddress for this UDP listener. If such a local interface cannot be determined, this object should take on the value 0. (A possible example of this would be if the value of ipv6UdpLocalAddress is ::0.) The interface identified by a particular non-0 value of this index is the same interface as identified by the same value of ipv6IfIndex. The value of this object must remain constant during the life of this UDP endpoint. This object is obsoleted by the zone identifier in an InetAddressIPv6z address in UDP-MIB::udpEndpointLocalAddress.')
ipv6UdpConformance = MibIdentifier((1, 3, 6, 1, 3, 87, 2))
ipv6UdpCompliances = MibIdentifier((1, 3, 6, 1, 3, 87, 2, 1))
ipv6UdpGroups = MibIdentifier((1, 3, 6, 1, 3, 87, 2, 2))
ipv6UdpCompliance = ModuleCompliance((1, 3, 6, 1, 3, 87, 2, 1, 1)).setObjects(("IPV6-UDP-MIB", "ipv6UdpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6UdpCompliance = ipv6UdpCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpCompliance.setDescription('The compliance statement for SNMPv2 entities which implement UDP over IPv6. This object is obsoleted by UDP-MIB::udpMIBCompliance2.')
ipv6UdpGroup = ObjectGroup((1, 3, 6, 1, 3, 87, 2, 2, 1)).setObjects(("IPV6-UDP-MIB", "ipv6UdpIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6UdpGroup = ipv6UdpGroup.setStatus('obsolete')
if mibBuilder.loadTexts: ipv6UdpGroup.setDescription('The group of objects providing management of UDP over IPv6. This group is obsoleted by several groups in UDP-MIB.')
mibBuilder.exportSymbols("IPV6-UDP-MIB", ipv6UdpGroup=ipv6UdpGroup, ipv6UdpEntry=ipv6UdpEntry, ipv6UdpLocalAddress=ipv6UdpLocalAddress, ipv6UdpLocalPort=ipv6UdpLocalPort, ipv6UdpMIB=ipv6UdpMIB, udp=udp, ipv6UdpCompliances=ipv6UdpCompliances, PYSNMP_MODULE_ID=ipv6UdpMIB, ipv6UdpIfIndex=ipv6UdpIfIndex, ipv6UdpCompliance=ipv6UdpCompliance, ipv6UdpConformance=ipv6UdpConformance, ipv6UdpTable=ipv6UdpTable, ipv6UdpGroups=ipv6UdpGroups)
