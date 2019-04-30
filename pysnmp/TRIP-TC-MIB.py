#
# PySNMP MIB module TRIP-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRIP-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, mib_2, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, iso, Counter32, Counter64, Gauge32, ObjectIdentity, TimeTicks, IpAddress, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "mib-2", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "iso", "Counter32", "Counter64", "Gauge32", "ObjectIdentity", "TimeTicks", "IpAddress", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tripTC = ModuleIdentity((1, 3, 6, 1, 2, 1, 115))
tripTC.setRevisions(('2004-09-02 00:00',))
if mibBuilder.loadTexts: tripTC.setLastUpdated('200409020000Z')
if mibBuilder.loadTexts: tripTC.setOrganization('IETF IPTel Working Group. Mailing list: iptel@lists.bell-labs.com')
class TripItad(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TripId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TripAddressFamily(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 255))
    namedValues = NamedValues(("decimal", 1), ("pentadecimal", 2), ("e164", 3), ("other", 255))

class TripAppProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 255))
    namedValues = NamedValues(("sip", 1), ("q931", 2), ("ras", 3), ("annexG", 4), ("other", 255))

class TripCommunityId(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class TripProtocolVersion(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 255)

class TripSendReceiveMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("sendReceive", 1), ("sendOnly", 2), ("receiveOnly", 3))

mibBuilder.exportSymbols("TRIP-TC-MIB", TripAppProtocol=TripAppProtocol, PYSNMP_MODULE_ID=tripTC, TripItad=TripItad, TripAddressFamily=TripAddressFamily, TripCommunityId=TripCommunityId, tripTC=tripTC, TripId=TripId, TripProtocolVersion=TripProtocolVersion, TripSendReceiveMode=TripSendReceiveMode)
