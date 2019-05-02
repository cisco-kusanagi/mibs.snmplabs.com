#
# PySNMP MIB module CISCO-TM (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-TM
# Produced by pysmi-0.3.4 at Wed May  1 12:14:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoDomains, = mibBuilder.importSymbols("CISCO-SMI", "ciscoDomains")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, iso, MibIdentifier, Counter64, Gauge32, TimeTicks, Bits, ObjectIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "MibIdentifier", "Counter64", "Gauge32", "TimeTicks", "Bits", "ObjectIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoTransportMappings = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1))
ciscoTransportMappings.setRevisions(('2001-08-23 16:00', '2000-06-21 16:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoTransportMappings.setRevisionsDescriptions(('Added Cisco Networking Services (CNS) Transport domain and identifier.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoTransportMappings.setLastUpdated('200108231600Z')
if mibBuilder.loadTexts: ciscoTransportMappings.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoTransportMappings.setContactInfo(' Cisco Systems Customer Service Postal: 170 W. Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoTransportMappings.setDescription('Extension of SNMPv2-TM MIB')
snmpUDPVPNDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 1))
if mibBuilder.loadTexts: snmpUDPVPNDomain.setStatus('current')
if mibBuilder.loadTexts: snmpUDPVPNDomain.setDescription("This transport domain is used to specify that particular SNMP messages are to be sent/received over a particular Virtual Private Network (VPN), implemented using MPLS (Multiprotocol Label Switching). The corresponding transport address is of type SnmpUDPVPNAddress. A VPN is defined as a set of sites with a common community of interest. Sites within an MPLS-based VPN often have private addresses which aren't accessible from outside of the VPN, and may be duplicates of private addresses used in other VPNs. To uniquely identify such a private address, it must be associated with a particular VPN routing/forwarding instance, also known as a VRF (VPN Routing and Forwarding table).")
if mibBuilder.loadTexts: snmpUDPVPNDomain.setReference('RFC 2547: BGP/MPLS VPNs')
class SnmpUDPVPNAddress(TextualConvention, OctetString):
    description = 'Represents a UDP VPN address: octets contents encoding 1-4 IP-address network-byte order 5-6 UDP-port network-byte order 7..38 VRF name string of (up to 32) octets IP address and port numbers should be represented in binary format. String must contain printable characters.'
    status = 'current'
    displayHint = '1d.1d.1d.1d/2d/32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 38)

snmpAAL5Domain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 2))
if mibBuilder.loadTexts: snmpAAL5Domain.setStatus('current')
if mibBuilder.loadTexts: snmpAAL5Domain.setDescription('This transport domain is used to specify that particular SNMP messages are to be sent/received over AAL5 transport. The corresponding transport address is of type SnmpAAL5VCIdentifier. An ATM VCC referenced by a SnmpAAL5VCIdentifier must be used only for SNMP packets, and not for any other kind of packets. Care must be taken with the use of this domain because its associated transport address, SnmpAAL5VCIdentifier, contains identifiers which only have local and temporal uniqueness: ifIndex, VPI, VCI. Use of this transport mapping is not recommended, except in circumstances where an IP address is not available and thus a mapping over UDP, such as snmpUDPDomain, can not be used.')
class SnmpAAL5VCIdentifier(TextualConvention, OctetString):
    description = 'Represents a AAL5 VCC: octets contents encoding 1-4 ifIndex network_byte order 5-8 vpi network-byte order 9-12 vci network-byte order ifIndex, vpi and vci should be represented in binary format. ifIndex specifies the value of the ifIndex object associated with the interface supporting the VCC. vpi specifies the value of the VPI (Virtual Path Identifier) associated with the VCC. vci specifies the value of the VCI (Virtual Channel Identifier) associated with the VCC.'
    status = 'current'
    displayHint = '4d/4d/4d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(12, 12)
    fixedLength = 12

snmpCNSDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 9, 19, 1, 3))
if mibBuilder.loadTexts: snmpCNSDomain.setStatus('current')
if mibBuilder.loadTexts: snmpCNSDomain.setDescription('This transport domain is used for transporting SNMP messages over the CNS Event Service. The corresponding transport addresses are of type SnmpCNSIdentifier. CNS Event service is an event based transport mechanism. Events are published by producers on particular subjects. Consumers listening for these subjects receive the events. Point to point communication is provided on the CNS Event Service by the use of Name Space Mapper Service that uses the device-id, appended at the end of the subject, to locate a specific target. An Event Agent subject used by a SnmpCNSIdentifier must be used only for SNMP events, and not for any other kind of events. Use of this transport mapping is not recommended, except in circumstances where an IP address is not available and thus a mapping over UDP, such as snmpUDPDomain, can not be used.')
class SnmpCNSIdentifier(TextualConvention, OctetString):
    description = "Represents the address that identifies targets in the CNS Event Service Transport mapping. octets contents encoding 1-19 service-field string of (19) octets 20-274 device-id string of (upto 255) octets service-field specifies the type of service (request, response or notifications) and has a fixed length of 19 octets. It also serves the purpose of distinguishing SNMP Message events from other CNS Events. device-id uniquely identifies devices subscribed to the CNS Event Service Bus. device-id may be same as the hostname for the device. The device-id must be separated from the service-field by a '.'. If the device-id is omitted, SnmpCNSIdentifier would contain just the fixed-length (19 octets) service-field. Thus target addresses are CNS Event subjects of the form: <service-field>.<device-id>"
    status = 'current'
    displayHint = '19a.255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(19, 274)

mibBuilder.exportSymbols("CISCO-TM", snmpAAL5Domain=snmpAAL5Domain, SnmpUDPVPNAddress=SnmpUDPVPNAddress, snmpCNSDomain=snmpCNSDomain, ciscoTransportMappings=ciscoTransportMappings, SnmpCNSIdentifier=SnmpCNSIdentifier, PYSNMP_MODULE_ID=ciscoTransportMappings, SnmpAAL5VCIdentifier=SnmpAAL5VCIdentifier, snmpUDPVPNDomain=snmpUDPVPNDomain)
