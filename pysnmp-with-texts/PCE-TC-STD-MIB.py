#
# PySNMP MIB module PCE-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PCE-TC-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:37:53 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
experimental, ModuleIdentity, Counter32, Unsigned32, Gauge32, ObjectIdentity, MibIdentifier, IpAddress, Bits, Counter64, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "experimental", "ModuleIdentity", "Counter32", "Unsigned32", "Gauge32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Bits", "Counter64", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pceTCDraftMIB = ModuleIdentity((1, 3, 6, 1, 3, 9999, 1))
if mibBuilder.loadTexts: pceTCDraftMIB.setLastUpdated('200709250000Z')
if mibBuilder.loadTexts: pceTCDraftMIB.setOrganization('Path Computation Element (PCE) Working Group')
if mibBuilder.loadTexts: pceTCDraftMIB.setContactInfo(' Stephan Emile France Telecom Email: emile.stephan@orange-ftgroup.com Email comments directly to the PCE WG Mailing List at pce@ietf.org WG-URL: http://www.ietf.org/html.charters/pce-charter.html')
if mibBuilder.loadTexts: pceTCDraftMIB.setDescription('This memo defines a portion of the Management Information Base (MIB) for use with network management protocols in the Internet community. In particular, it defines Textual Conventions to represent commonly used Path Computation Element (PCE) management information. The intent is that these TEXTUAL CONVENTIONS (TCs) will be imported and used in PCE related MIB modules to avoid duplicating conventions.')
pceStdMIB = MibIdentifier((1, 3, 6, 1, 3, 9999))
class PcePcepIdentifier(TextualConvention, OctetString):
    description = 'The LDP identifier is a six octet quantity which is used to identify a PCE client.'
    status = 'current'
    displayHint = '1d.1d.1d.1d:1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 6)

class PceRoutingDomainID(TextualConvention, OctetString):
    description = 'A PCE-DOMAINS information element or a A PCE-DEST-DOMAINS information element carries the identifier of a routing domain (area, as) which type depends on both the routing protocol and on the version of Internet protocol in use in this routing domain. This TC defines a common SMI type for the different kinds of routing domain identifiers. A PceRoutingDomainID value is always interpreted within the context of an AddressFamilyNumbers value. Every usage of the PceRoutingDomainID textual convention is required to specify the AddressFamilyNumbers object which provides the context. The value of an PceRoutingDomainID object must always be consistent with the value of the associated AddressFamilyNumbers object. Following is the mapping between AddressFamilyNumbers type and PceRoutingDomainID size: ipV4(1): PceRoutingDomainID is an InetAddressIPv4 corresponding to the name of an OSPF area; ipV6(2): PceRoutingDomainID is an InetAddressIPv6 corresponding to the name of an OSPF area; nsap(3): PceRoutingDomainID type is OCTET STRING (SIZE (0..20)), corresponding to the name of an ISIS area (see RFC 1195); asNumber(18) PceRoutingDomainID type is OCTET STRING (SIZE (2)) corresponding to the name of an Autonomous System. '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

mibBuilder.exportSymbols("PCE-TC-STD-MIB", PceRoutingDomainID=PceRoutingDomainID, pceStdMIB=pceStdMIB, pceTCDraftMIB=pceTCDraftMIB, PYSNMP_MODULE_ID=pceTCDraftMIB, PcePcepIdentifier=PcePcepIdentifier)
