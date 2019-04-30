#
# PySNMP MIB module MULTI-MEDIA-REG-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MULTI-MEDIA-REG-TC
# Produced by pysmi-0.3.4 at Mon Apr 29 20:06:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter64, Counter32, MibIdentifier, Bits, ObjectIdentity, Gauge32, IpAddress, ModuleIdentity, NotificationType, Unsigned32, experimental = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter64", "Counter32", "MibIdentifier", "Bits", "ObjectIdentity", "Gauge32", "IpAddress", "ModuleIdentity", "NotificationType", "Unsigned32", "experimental")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
multimediaRegMib = ModuleIdentity((1, 3, 6, 1, 3, 323))
multimediaRegMib.setRevisions(('1998-05-29 12:00',))
if mibBuilder.loadTexts: multimediaRegMib.setLastUpdated('9805291200Z')
if mibBuilder.loadTexts: multimediaRegMib.setOrganization('Cisco Systems, Inc.')
class MmUtf8String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class MmE164String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '128a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class MmTAddressTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 0), ("ipv4", 1), ("ipv6", 2), ("ipx", 3), ("nsap", 4), ("netbios", 5))

class MmGlobalIdentifier(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    status = 'current'
    displayHint = '8d-9,3x,1d,2x:2x:2x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class MmAliasTag(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 0), ("e164", 1), ("h323Id", 2), ("urlId", 3), ("transportId", 4), ("emailId", 5), ("partyNumber", 6))

class MmAliasAddress(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    status = 'current'
    displayHint = '512a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 512)

class MmEndpointID(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class MmGatekeeperID(TextualConvention, OctetString):
    reference = 'ITU H225.0 Version 2'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 128)

class MmH225Crv(TextualConvention, Integer32):
    reference = 'ITU H225.0 Version 2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

mmRtpRoot = ObjectIdentity((1, 3, 6, 1, 3, 323, 1))
if mibBuilder.loadTexts: mmRtpRoot.setStatus('current')
mmH323Root = ObjectIdentity((1, 3, 6, 1, 3, 323, 2))
if mibBuilder.loadTexts: mmH323Root.setStatus('current')
mmH320Root = ObjectIdentity((1, 3, 6, 1, 3, 323, 3))
if mibBuilder.loadTexts: mmH320Root.setStatus('current')
mmH245Root = ObjectIdentity((1, 3, 6, 1, 3, 323, 4))
if mibBuilder.loadTexts: mmH245Root.setStatus('current')
mibBuilder.exportSymbols("MULTI-MEDIA-REG-TC", MmH225Crv=MmH225Crv, mmH320Root=mmH320Root, multimediaRegMib=multimediaRegMib, MmAliasAddress=MmAliasAddress, PYSNMP_MODULE_ID=multimediaRegMib, mmRtpRoot=mmRtpRoot, mmH245Root=mmH245Root, MmAliasTag=MmAliasTag, MmTAddressTag=MmTAddressTag, MmUtf8String=MmUtf8String, MmGatekeeperID=MmGatekeeperID, mmH323Root=mmH323Root, MmEndpointID=MmEndpointID, MmGlobalIdentifier=MmGlobalIdentifier, MmE164String=MmE164String)
