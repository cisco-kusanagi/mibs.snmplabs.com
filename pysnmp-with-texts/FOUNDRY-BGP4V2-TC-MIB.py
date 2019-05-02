#
# PySNMP MIB module FOUNDRY-BGP4V2-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FOUNDRY-BGP4V2-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:14:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
bgp4V2Root, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "bgp4V2Root")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, mib_2, Counter64, iso, NotificationType, Counter32, MibIdentifier, Integer32, ModuleIdentity, Bits, Gauge32, TimeTicks, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "mib-2", "Counter64", "iso", "NotificationType", "Counter32", "MibIdentifier", "Integer32", "ModuleIdentity", "Bits", "Gauge32", "TimeTicks", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bgp4V2TC = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 3, 5, 1))
bgp4V2TC.setRevisions(('2014-01-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bgp4V2TC.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: bgp4V2TC.setLastUpdated('201401230000Z')
if mibBuilder.loadTexts: bgp4V2TC.setOrganization('IETF IDR Working Group')
if mibBuilder.loadTexts: bgp4V2TC.setContactInfo('E-mail: idr@ietf.org')
if mibBuilder.loadTexts: bgp4V2TC.setDescription('Textual conventions for BGP-4. Copyright (C) The IETF Trust (2014). This version of this MIB module is part of RFC XXX; see the RFC itself for full legal notices.')
class Bgp4V2IdentifierTC(TextualConvention, OctetString):
    reference = 'RFC 4273, Section 4.2'
    description = 'The representation of a BGP Identifier. BGP Identifiers are presented in the received network byte order. The BGP Identifier is displayed as if it is an IP address, even if it would be an illegal one.'
    status = 'current'
    displayHint = '1d.'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class Bgp4V2AddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3'
    description = 'The representation of a BGP AFI. The value of this object should be restricted to be between the values of 0 and 65535.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class Bgp4V2SubsequentAddressFamilyIdentifierTC(TextualConvention, Integer32):
    reference = 'RFC 4760, Section 3. The value of this object should be restricted to be between the values of 0 and 255.'
    description = 'The representation of a BGP SAFI'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 4))
    namedValues = NamedValues(("unicast", 1), ("multicast", 2), ("mpls", 4))

mibBuilder.exportSymbols("FOUNDRY-BGP4V2-TC-MIB", Bgp4V2AddressFamilyIdentifierTC=Bgp4V2AddressFamilyIdentifierTC, Bgp4V2SubsequentAddressFamilyIdentifierTC=Bgp4V2SubsequentAddressFamilyIdentifierTC, bgp4V2TC=bgp4V2TC, PYSNMP_MODULE_ID=bgp4V2TC, Bgp4V2IdentifierTC=Bgp4V2IdentifierTC)
