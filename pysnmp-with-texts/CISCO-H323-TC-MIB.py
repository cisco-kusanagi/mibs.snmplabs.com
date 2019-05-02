#
# PySNMP MIB module CISCO-H323-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-H323-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:58:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Integer32, Counter32, Counter64, ModuleIdentity, iso, TimeTicks, Bits, IpAddress, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Integer32", "Counter32", "Counter64", "ModuleIdentity", "iso", "TimeTicks", "Bits", "IpAddress", "ObjectIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoH323TCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 41))
ciscoH323TCMIB.setRevisions(('1998-10-09 12:00', '2000-03-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoH323TCMIB.setRevisionsDescriptions(('The initial version of the mib.', 'Removed CgkUtf8String as it is a duplicate definition of SnmpAdminString.',))
if mibBuilder.loadTexts: ciscoH323TCMIB.setLastUpdated('200003100000Z')
if mibBuilder.loadTexts: ciscoH323TCMIB.setOrganization('Cisco Systems, Inc')
if mibBuilder.loadTexts: ciscoH323TCMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 West Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: h323-support@cisco.com')
if mibBuilder.loadTexts: ciscoH323TCMIB.setDescription('The MIB Module defines a common set of Textual Conventions used in mib modules supporting ITU-T H.323.0 and ITU-T H.225.0 Recommendations.')
class CgkIA5String(TextualConvention, OctetString):
    description = 'Corresponds to an IA5String.'
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkE164String(TextualConvention, OctetString):
    description = "An IA5String limited to the character set '0123456789*#,.' "
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkTAddressTag(TextualConvention, Integer32):
    description = 'A tag to identify the type of the transport address contained in the TAddress data type. The values correlate to the TransportAddress defined in the H.225.0 V2 ITU protocol specification. The tag indicates how to interpret the value of a TAddress data type defined in this specification. All TAddress values are in network byte order TAddress size TAddress contents ipv4 6 octets IPv4 (4 octets), port (2 octets) ipv6 18 IPv6 (16), port (2) ipx 12 net (4), node (6), port (2) nsap 1-20 nsap(1-20) netbios 16 netbios(16) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4))

class CgkNAddressTag(TextualConvention, Integer32):
    description = 'A tag to identify the type of the network address contained in the CgkNAddress textual convention defined in this specification. All CgkNAddress values are in network byte order. NAddress size ipv4 4 octets ipv6 16 ipx 10 net (4), node (6) nsap 1-20 nsap(1-20) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4))

class CgkNAddress(TextualConvention, OctetString):
    description = 'Denotes a network address. An object defined with this syntax must have a corresponding CgkNAddressTag object which identifies the actual size and type.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkGlobalIdentifier(TextualConvention, OctetString):
    reference = 'ITU-T H225.0, Version 2 section 7.6'
    description = 'A 16 octet field containing a unique identifier. The identifier contains the following fields: 60 bit nanosecond time (octets 0-6, low 4 bits of octet 7) 4 bit version (hi 4 bits of octet 7) 3 octet 0 (a variant field) 1 octet hi 2bits 0, low 6bits clock sequence. 6 octet MAC Address See Reference for generation of this value. '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class CgkAliasTag(TextualConvention, Integer32):
    description = 'A tag to identify the type of the Alias address contained in the CgkAliasAddress data type. The values correlate to the AliasAddress defined in the H.225.0 V2 ITU protocol specification. The tag indicates how to interpret the value of an AliasAddress data type defined in that specification. AliasAddress contents other unknown e164 CgkE164String h323Id CgkUtf8String urlId CgkIA5String containing a URL transportId CgkTAddressTag, TAddress emailId CgkIA5String containing e-mail address partyNumber contains PartyNumber (E164String) '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 0), ("e164", 1), ("h323Id", 2), ("urlId", 3), ("transportId", 4), ("emailId", 5), ("partyNumber", 6))

class CgkAliasAddress(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    description = 'A data type corresponding to AliasAddress defined in H.225.0. The value of an object of this type has the syntax and symantics identified by CgkAliasTag. An object defined as CgkAliasAddress must have a corresponding CgkAliasTag object.'
    status = 'current'
    displayHint = '512a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 512)

class CgkEndpointID(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    description = 'A CgkUtf8String corresponding to EndpointIdentifer defined in H.225.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class CgkGatekeeperID(TextualConvention, OctetString):
    reference = 'ITU-T H225.0 Version 2 ANNEX H - H.225.0 Message Syntax (ASN.1)'
    description = 'A CgkUtf8String corresponding to GatekeeperIdentifier defined in H.225.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

mibBuilder.exportSymbols("CISCO-H323-TC-MIB", CgkAliasAddress=CgkAliasAddress, CgkNAddress=CgkNAddress, CgkGatekeeperID=CgkGatekeeperID, CgkEndpointID=CgkEndpointID, CgkE164String=CgkE164String, CgkTAddressTag=CgkTAddressTag, CgkAliasTag=CgkAliasTag, PYSNMP_MODULE_ID=ciscoH323TCMIB, CgkIA5String=CgkIA5String, CgkGlobalIdentifier=CgkGlobalIdentifier, CgkNAddressTag=CgkNAddressTag, ciscoH323TCMIB=ciscoH323TCMIB)
