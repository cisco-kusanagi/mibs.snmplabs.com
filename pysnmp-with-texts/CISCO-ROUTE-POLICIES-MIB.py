#
# PySNMP MIB module CISCO-ROUTE-POLICIES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ROUTE-POLICIES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:10:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, IpAddress, TimeTicks, Integer32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, NotificationType, Gauge32, Unsigned32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "TimeTicks", "Integer32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "NotificationType", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoRoutePoliciesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578))
ciscoRoutePoliciesMIB.setRevisions(('2006-08-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setRevisionsDescriptions(('Initial version of this MIB module. ',))
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setLastUpdated('200608180000Z')
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setOrganization('Cisco Systems, Inc. ')
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoRoutePoliciesMIB.setDescription("This module provides a subtree to define OIDs so that various routing 'policies' used by Cisco routers can be expressed. This module defines only this 'policy' OID space and doesn't define any other object. As an example, these OIDs are required by at least the following MIB objects: inetCidrRoutePolicy ( IP-FORWARD-MIB, RFC4292 ) and mplsL3VpnVrfRteInetCidrPolicy ( MPLS-L3VPN-STD-MIB RCS4382). Both of these objects are defined as OBJECT IDENTIFIERs without any defined semantics, to differentiate between multiple entries to the same destination in the tables inetCidrRoutePolicyTable and mplsL3VpnVrfRteInetCidrTable. These two objects utilise a generalised notion of 'policy' defined in this module. The table inetCidrRouteTable of IP-FORWARD-MIB may list multiple paths pointing out of (either): * different interfaces with the same next-hop ipv6 route 2003::/64 interface gig0/0 2222::1 ipv6 route 2003::/64 interface gig0/1 2222::1 * different interfaces with no next-hop ipv6 route 2003::/64 interface gig0/0 ipv6 route 2003::/64 interface gig0/1 2003::/64 and 2222::1 represent an IPv6 route-prefix and IPv6 next-hop respectively. If these interfaces were in different zones, then the 'InetAddressIPv6z' type next-hop could distinguish them. If they are in the same zone, then the two interfaces refer to the same link. The indices of inetCidrRouteTable are: inetCidrRouteDestType inetCidrRouteDest inetCidrRoutePfxLen inetCidrRoutePolicy inetCidrRouteNextHopType inetCidrRouteNextHop The inetCidrRoutePolicy object, when instantiated with a value from crpPolicyIfIndex, allows us to distinguish the routing table entries mentioned in the examples above. REFERENCE [1] IP-FORWARD-MIB (RFC4292) [2] MPLS-L3VPN-STD-MIB (RFC4382) [3] ifIndex, IF-MIB [4] RFC 4291 IP Version 6 Addressing Architecture, Section 2.2, Text Representation of Addresses. ")
ciscoRoutePoliciesMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 0))
ciscoRoutePoliciesMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 1))
ciscoRoutePoliciesMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 578, 2))
crpPolicies = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1))
if mibBuilder.loadTexts: crpPolicies.setStatus('current')
if mibBuilder.loadTexts: crpPolicies.setDescription('A subtree to define OIDs so that various routing policies used by Cisco routers can be expressed. Such OIDs may serve as additional indices, e.g., as the values of inetCidrRoutePolicy in inetCidrRouteTable, to delineate between multiple routes to the same destination. ')
crpPolicyIfIndex = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 9, 578, 1, 1, 1))
if mibBuilder.loadTexts: crpPolicyIfIndex.setStatus('current')
if mibBuilder.loadTexts: crpPolicyIfIndex.setDescription('This OID specifies a set of policies, one for each ifIndex value. Specifically, the OID value of crpPolicyIfIndex.i is defined such that each inetCidrRouteTable entry for which the instance of inetCidrRoutePolicy has this value, is associated with ifIndex=i, and thereby is distinct for any inetCidrRouteTable entry associated with ifIndex=j. Note that the value of inetCidrRoutePolicy for the latter would be crpPolicyIfIndex.j. This set of policies is appropriate only if an ifIndex value is sufficient to distinguish between routes. ')
if mibBuilder.loadTexts: crpPolicyIfIndex.setReference('inetCidrRouteTable, IP-FORWARD-MIB, RFC4292. ')
mibBuilder.exportSymbols("CISCO-ROUTE-POLICIES-MIB", crpPolicies=crpPolicies, PYSNMP_MODULE_ID=ciscoRoutePoliciesMIB, ciscoRoutePoliciesMIB=ciscoRoutePoliciesMIB, crpPolicyIfIndex=crpPolicyIfIndex, ciscoRoutePoliciesMIBNotifs=ciscoRoutePoliciesMIBNotifs, ciscoRoutePoliciesMIBObjects=ciscoRoutePoliciesMIBObjects, ciscoRoutePoliciesMIBConform=ciscoRoutePoliciesMIBConform)
