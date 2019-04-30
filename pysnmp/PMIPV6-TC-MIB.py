#
# PySNMP MIB module PMIPV6-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PMIPV6-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:32:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, mib_2, Counter32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, IpAddress, ModuleIdentity, iso, NotificationType, MibIdentifier, Integer32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "mib-2", "Counter32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "iso", "NotificationType", "MibIdentifier", "Integer32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pmip6TCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 205))
pmip6TCMIB.setRevisions(('2012-05-07 00:00',))
if mibBuilder.loadTexts: pmip6TCMIB.setLastUpdated('201205070000Z')
if mibBuilder.loadTexts: pmip6TCMIB.setOrganization('IETF NETLMM Working Group')
class Pmip6TimeStamp64(TextualConvention, OctetString):
    reference = 'RFC 5213: Section 8.8'
    status = 'current'
    displayHint = '6d:2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Pmip6MnIdentifier(TextualConvention, OctetString):
    reference = 'RFC 4283: Section 3'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Pmip6MnLLIdentifier(TextualConvention, OctetString):
    reference = 'RFC 5213: Section 8.6'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class Pmip6MnIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class Pmip6MnLLIndex(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class Pmip6MnInterfaceATT(TextualConvention, Integer32):
    reference = 'RFC 5213: Section 8.5, Mobile IPv6 parameters registry on http://www.iana.org/mobility-parameters'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("reserved", 0), ("logicalNetworkInterface", 1), ("pointToPointInterface", 2), ("ethernet", 3), ("wirelessLan", 4), ("wimax", 5), ("threeGPPGERAN", 6), ("threeGPPUTRAN", 7), ("threeGPPEUTRAN", 8), ("threeGPP2eHRPD", 9), ("threeGPP2HRPD", 10), ("threeGPP21xRTT", 11), ("threeGPP2UMB", 12))

mibBuilder.exportSymbols("PMIPV6-TC-MIB", Pmip6MnLLIdentifier=Pmip6MnLLIdentifier, Pmip6MnLLIndex=Pmip6MnLLIndex, Pmip6MnInterfaceATT=Pmip6MnInterfaceATT, Pmip6MnIndex=Pmip6MnIndex, pmip6TCMIB=pmip6TCMIB, PYSNMP_MODULE_ID=pmip6TCMIB, Pmip6MnIdentifier=Pmip6MnIdentifier, Pmip6TimeStamp64=Pmip6TimeStamp64)
