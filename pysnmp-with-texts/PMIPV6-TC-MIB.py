#
# PySNMP MIB module PMIPV6-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PMIPV6-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:41:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
mib_2, TimeTicks, Counter32, Integer32, Gauge32, Counter64, ObjectIdentity, iso, ModuleIdentity, NotificationType, IpAddress, MibIdentifier, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "TimeTicks", "Counter32", "Integer32", "Gauge32", "Counter64", "ObjectIdentity", "iso", "ModuleIdentity", "NotificationType", "IpAddress", "MibIdentifier", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pmip6TCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 205))
pmip6TCMIB.setRevisions(('2012-05-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pmip6TCMIB.setRevisionsDescriptions(('The initial version, published as RFC 6475.',))
if mibBuilder.loadTexts: pmip6TCMIB.setLastUpdated('201205070000Z')
if mibBuilder.loadTexts: pmip6TCMIB.setOrganization('IETF NETLMM Working Group')
if mibBuilder.loadTexts: pmip6TCMIB.setContactInfo(' Glenn Mansfield Keeni Postal: Cyber Solutions, Inc. 6-6-3, Minami Yoshinari Aoba-ku, Sendai, Japan 989-3204. Tel: +81-22-303-4012 Fax: +81-22-303-4015 EMail: glenn@cysols.com Sri Gundavelli Postal: Cisco Systems 170 W.Tasman Drive, San Jose, CA 95134 USA Tel: +1-408-527-6109 EMail: sgundave@cisco.com Kazuhide Koide Postal: KDDI Corporation GARDEN AIR TOWER 3-10-10, Iidabashi Chiyoda-ku, Tokyo 102-8460, Japan. Tel: +81-3-6678-3378 EMail: ka-koide@kddi.com Ryuji Wakikawa Postal: TOYOTA InfoTechnology Center, U.S.A., Inc. 465 Bernardo Avenue Mountain View, CA 94043 USA EMail: ryuji@us.toyota-itc.com Support Group EMail: netlmm@ietf.org ')
if mibBuilder.loadTexts: pmip6TCMIB.setDescription("This MIB module provides textual conventions for Proxy Mobile IPv6 Management information. Copyright (c) 2012 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). ")
class Pmip6TimeStamp64(TextualConvention, OctetString):
    reference = 'RFC 5213: Section 8.8'
    description = 'A 64-bit unsigned integer field containing a timestamp. The value indicates the elapsed time since January 1, 1970, 00:00 UTC, by using a fixed-point format. In this format, the integer number of seconds is contained in the first 48 bits of the field, and the remaining 16 bits indicate the number of 1/65536 fractions of a second. '
    status = 'current'
    displayHint = '6d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Pmip6MnIdentifier(TextualConvention, OctetString):
    reference = 'RFC 4283: Section 3'
    description = 'The identity of a mobile node in the Proxy Mobile IPv6 domain. This is the stable identifier of a mobile node that the mobility entities in a Proxy Mobile IPv6 domain can always acquire and use for predictably identifying a mobile node. Various forms of identifiers can be used to identify a mobile node (MN). Two examples are a Network Access Identifier (NAI) and an opaque identifier applicable to a particular application. '
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Pmip6MnLLIdentifier(TextualConvention, OctetString):
    reference = 'RFC 5213: Section 8.6'
    description = 'An identifier that identifies the attached interface of a mobile node. '
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Pmip6MnIndex(TextualConvention, Unsigned32):
    description = "A unique integer value, greater than zero, assigned to each mobile node that is currently attached to the Proxy Mobile IPv6 domain by the management system. It is recommended that the values are assigned in a monotonically increasing order starting from 1. It may wrap after reaching its maximum value. The value for each mobile node must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization. "
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class Pmip6MnLLIndex(TextualConvention, Unsigned32):
    description = "A unique integer value, greater than zero, assigned to each interface of a mobile node that is currently attached to the Proxy Mobile IPv6 domain by the management system. It is recommended that the values are assigned in a monotonically increasing order starting from 1. It may wrap after reaching its maximum value. The value for each interface of a mobile node must remain constant at least from one re-initialization of the entity's network management system to the next re-initialization. "
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class Pmip6MnInterfaceATT(TextualConvention, Integer32):
    reference = 'RFC 5213: Section 8.5, Mobile IPv6 parameters registry on http://www.iana.org/mobility-parameters'
    description = 'The object specifies the access technology that connects the mobile node to the access link on the mobile access gateway. The enumerated values and the corresponding access technology are as follows: reserved (0): Reserved (Not used) logicalNetworkInterface (1): Logical network interface pointToPointInterface (2): Point-to-point interface ethernet (3): Ethernet interface wirelessLan (4): Wireless LAN interface wimax (5): Wimax interface threeGPPGERAN (6): 3GPP GERAN threeGPPUTRAN (7): 3GPP UTRAN threeGPPEUTRAN (8): 3GPP E-UTRAN threeGPP2eHRPD (9): 3GPP2 eHRPD threeGPP2HRPD (10): 3GPP2 HRPD threeGPP21xRTT (11): 3GPP2 1xRTT threeGPP2UMB (12): 3GPP2 UMB '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("reserved", 0), ("logicalNetworkInterface", 1), ("pointToPointInterface", 2), ("ethernet", 3), ("wirelessLan", 4), ("wimax", 5), ("threeGPPGERAN", 6), ("threeGPPUTRAN", 7), ("threeGPPEUTRAN", 8), ("threeGPP2eHRPD", 9), ("threeGPP2HRPD", 10), ("threeGPP21xRTT", 11), ("threeGPP2UMB", 12))

mibBuilder.exportSymbols("PMIPV6-TC-MIB", PYSNMP_MODULE_ID=pmip6TCMIB, Pmip6MnIndex=Pmip6MnIndex, Pmip6MnLLIndex=Pmip6MnLLIndex, Pmip6MnInterfaceATT=Pmip6MnInterfaceATT, Pmip6MnLLIdentifier=Pmip6MnLLIdentifier, Pmip6TimeStamp64=Pmip6TimeStamp64, pmip6TCMIB=pmip6TCMIB, Pmip6MnIdentifier=Pmip6MnIdentifier)
