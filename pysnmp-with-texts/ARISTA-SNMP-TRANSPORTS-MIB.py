#
# PySNMP MIB module ARISTA-SNMP-TRANSPORTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-SNMP-TRANSPORTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, Counter64, MibIdentifier, Unsigned32, IpAddress, ObjectIdentity, iso, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "Counter64", "MibIdentifier", "Unsigned32", "IpAddress", "ObjectIdentity", "iso", "Gauge32", "Counter32")
TAddress, DisplayString, TextualConvention, TDomain = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "DisplayString", "TextualConvention", "TDomain")
aristaSnmpTransportMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10))
aristaSnmpTransportMIB.setRevisions(('2014-08-15 00:00', '2012-01-09 13:00', '2012-01-05 18:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaSnmpTransportMIB.setRevisionsDescriptions(('Updated postal and e-mail addresses', 'Updated imports; moved module under aristaMibs', 'Initial version.',))
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaSnmpTransportMIB.setDescription('The Arista Networks specific SNMP transport domains.')
class TransportAddressIPv4NS(TextualConvention, OctetString):
    description = 'Represents a transport address consisting of a namespace string, an IPv4 address and a port number (as used for example by UDP, TCP and SCTP): octets contents encoding 1-4 IPv4 address network-byte order 5-6 port number network-byte order 7-n Namespace string ASCII This textual convention SHOULD NOT be used directly in object definitions since it restricts addresses to a specific format. However, if it is used, it MAY be used either on its own or in conjunction with TransportAddressType or TransportDomain as a pair.'
    status = 'current'
    displayHint = '1d.1d.1d.1d:2d@*1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 255)

class TransportAddressIPv6NS(TextualConvention, OctetString):
    description = 'Represents a transport address consisting of a namespace string, an IPv6 address and a port number (as used for example by UDP, TCP and SCTP): octets contents encoding 1-16 IPv6 address network-byte order 17-18 port number network-byte order 19-n Namespace string ASCII This textual convention SHOULD NOT be used directly in object definitions since it restricts addresses to a specific format. However, if it is used, it MAY be used either on its own or in conjunction with TransportAddressType or TransportDomain as a pair.'
    status = 'current'
    displayHint = '0a[2x:2x:2x:2x:2x:2x:2x:2x]0a:2d@*1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(19, 255)

aristaUDPNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 1))
if mibBuilder.loadTexts: aristaUDPNSDomain.setStatus('current')
if mibBuilder.loadTexts: aristaUDPNSDomain.setDescription('The SNMP over UDP transport domain. The corresponding socket is opened in a specific namespace.')
aristaTCPNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 2))
if mibBuilder.loadTexts: aristaTCPNSDomain.setStatus('current')
if mibBuilder.loadTexts: aristaTCPNSDomain.setDescription('The SNMP over TCP transport domain. The corresponding socket is opened in a specific namespace.')
aristaUDPNS6Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 3))
if mibBuilder.loadTexts: aristaUDPNS6Domain.setStatus('current')
if mibBuilder.loadTexts: aristaUDPNS6Domain.setDescription('The SNMP over UDP6 transport domain. The corresponding socket is opened in a specific namespace.')
aristaTCPNS6Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 10, 4))
if mibBuilder.loadTexts: aristaTCPNS6Domain.setStatus('current')
if mibBuilder.loadTexts: aristaTCPNS6Domain.setDescription('The SNMP over TCP6 transport domain. The corresponding socket is opened in a specific namespace.')
aristaAuthFailTrapObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5))
aristaTransportConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6))
aristaAuthFailTrapTDomain = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5, 1), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaAuthFailTrapTDomain.setStatus('current')
if mibBuilder.loadTexts: aristaAuthFailTrapTDomain.setDescription('Transport Domain of the offending request that caused this trap')
aristaAuthFailTrapSrcTAddress = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 10, 5, 2), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaAuthFailTrapSrcTAddress.setStatus('current')
if mibBuilder.loadTexts: aristaAuthFailTrapSrcTAddress.setDescription('Source Transport Address of the offending request that caused this trap')
aristaAuthFailTrapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 1))
aristaAuthFailCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 2))
aristaAuthFailCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 2, 1)).setObjects(("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaAuthFailCompliance = aristaAuthFailCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaAuthFailCompliance.setDescription('The compliance statement for SNMP entities which implement the ARISTA AuthFailure MIB.')
aristaAuthFailTrapObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 10, 6, 1, 1)).setObjects(("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapTDomain"), ("ARISTA-SNMP-TRANSPORTS-MIB", "aristaAuthFailTrapSrcTAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaAuthFailTrapObjectsGroup = aristaAuthFailTrapObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: aristaAuthFailTrapObjectsGroup.setDescription('Collections of objects for Authentication Failure Trap.')
mibBuilder.exportSymbols("ARISTA-SNMP-TRANSPORTS-MIB", aristaAuthFailTrapSrcTAddress=aristaAuthFailTrapSrcTAddress, aristaTransportConformance=aristaTransportConformance, TransportAddressIPv6NS=TransportAddressIPv6NS, aristaAuthFailTrapGroups=aristaAuthFailTrapGroups, aristaTCPNS6Domain=aristaTCPNS6Domain, aristaAuthFailTrapObjects=aristaAuthFailTrapObjects, PYSNMP_MODULE_ID=aristaSnmpTransportMIB, aristaAuthFailTrapTDomain=aristaAuthFailTrapTDomain, aristaUDPNSDomain=aristaUDPNSDomain, aristaUDPNS6Domain=aristaUDPNS6Domain, aristaAuthFailCompliances=aristaAuthFailCompliances, aristaAuthFailCompliance=aristaAuthFailCompliance, aristaTCPNSDomain=aristaTCPNSDomain, aristaAuthFailTrapObjectsGroup=aristaAuthFailTrapObjectsGroup, aristaSnmpTransportMIB=aristaSnmpTransportMIB, TransportAddressIPv4NS=TransportAddressIPv4NS)
