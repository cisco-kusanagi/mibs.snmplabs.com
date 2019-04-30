#
# PySNMP MIB module CISCO-SUBSCRIBER-IDENTITY-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SUBSCRIBER-IDENTITY-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Integer32, Counter32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, ObjectIdentity, Bits, Unsigned32, MibIdentifier, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "Counter32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "ObjectIdentity", "Bits", "Unsigned32", "MibIdentifier", "ModuleIdentity", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoSubscriberIdentityTcMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 782))
ciscoSubscriberIdentityTcMIB.setRevisions(('2011-12-23 00:00',))
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setLastUpdated('201112230000Z')
if mibBuilder.loadTexts: ciscoSubscriberIdentityTcMIB.setOrganization('Cisco Systems, Inc.')
class SubSessionIdentity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("other", 1), ("ifIndex", 2), ("subscriberLabel", 3), ("macAddress", 4), ("nativeVrf", 5), ("nativeIpAddress", 6), ("domainVrf", 7), ("domainIpAddress", 8), ("pbhk", 9), ("remoteId", 10), ("circuitId", 11), ("nasPort", 12), ("domain", 13), ("username", 14), ("acctSessionId", 15), ("dnis", 16), ("media", 17), ("mlpNegotiated", 18), ("protocol", 19), ("serviceName", 20), ("dhcpClass", 21), ("tunnelName", 22))

class SubSessionIdentities(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("ifIndex", 0), ("subscriberLabel", 1), ("macAddress", 2), ("nativeVrf", 3), ("nativeIpAddress", 4), ("domainVrf", 5), ("domainIpAddress", 6), ("pbhk", 7), ("remoteId", 8), ("circuitId", 9), ("nasPort", 10), ("domain", 11), ("username", 12), ("acctSessionId", 13), ("dnis", 14), ("media", 15), ("mlpNegotiated", 16), ("protocol", 17), ("serviceName", 18), ("dhcpClass", 19), ("tunnelName", 20))

class SubscriberLabel(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class SubscriberVRF(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberPbhk(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class SubscriberRemoteId(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberCircuitId(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberNasPort(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class SubscriberDomain(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberUsername(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberAcctSessionId(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class SubscriberDnis(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberMediaType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("async", 2), ("atm", 3), ("ethernet", 4), ("ip", 5), ("isdn", 6), ("mpls", 7), ("sync", 8))

class SubscriberProtocolType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("atom", 2), ("ip", 3), ("psdn", 4), ("ppp", 5), ("vpdn", 6))

class SubscriberDhcpClass(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberTunnelName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberLocationName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class SubscriberServiceName(TextualConvention, OctetString):
    reference = "D. Harrington, R. Resuhn, B. Wijnen, 'An Architecture for Describing Simple Network Management Protocol (SNMP) Management Frameworks', RFC-3411, December 2002."
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

mibBuilder.exportSymbols("CISCO-SUBSCRIBER-IDENTITY-TC-MIB", SubscriberMediaType=SubscriberMediaType, SubscriberServiceName=SubscriberServiceName, SubscriberLabel=SubscriberLabel, SubscriberUsername=SubscriberUsername, SubSessionIdentity=SubSessionIdentity, SubscriberCircuitId=SubscriberCircuitId, SubscriberProtocolType=SubscriberProtocolType, SubscriberPbhk=SubscriberPbhk, SubscriberDomain=SubscriberDomain, SubscriberNasPort=SubscriberNasPort, SubscriberDhcpClass=SubscriberDhcpClass, SubscriberLocationName=SubscriberLocationName, SubscriberTunnelName=SubscriberTunnelName, SubSessionIdentities=SubSessionIdentities, PYSNMP_MODULE_ID=ciscoSubscriberIdentityTcMIB, ciscoSubscriberIdentityTcMIB=ciscoSubscriberIdentityTcMIB, SubscriberVRF=SubscriberVRF, SubscriberRemoteId=SubscriberRemoteId, SubscriberDnis=SubscriberDnis, SubscriberAcctSessionId=SubscriberAcctSessionId)
