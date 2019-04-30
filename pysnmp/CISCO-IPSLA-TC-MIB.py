#
# PySNMP MIB module CISCO-IPSLA-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSLA-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, Counter32, Bits, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Gauge32, iso, Integer32, IpAddress, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "Counter32", "Bits", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Gauge32", "iso", "Integer32", "IpAddress", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpSlaTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 624))
ciscoIpSlaTCMIB.setRevisions(('2007-03-23 00:00',))
if mibBuilder.loadTexts: ciscoIpSlaTCMIB.setLastUpdated('200703230000Z')
if mibBuilder.loadTexts: ciscoIpSlaTCMIB.setOrganization('Cisco Systems, Inc.')
class IpSlaOperType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("icmpEcho", 1), ("udpEcho", 2), ("tcpConnect", 3), ("udpJitter", 4), ("icmpJitter", 5))

class IpSlaCodecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("g711ulaw", 1), ("g711alaw", 2), ("g729a", 3))

class IpSlaReactVar(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("rtt", 1), ("jitterSDAvg", 2), ("jitterDSAvg", 3), ("packetLossSD", 4), ("packetLossDS", 5), ("mos", 6), ("timeout", 7), ("connectionLoss", 8), ("verifyError", 9), ("jitterAvg", 10), ("icpif", 11), ("packetMIA", 12), ("packetLateArrival", 13), ("packetOutOfSequence", 14), ("maxOfPositiveSD", 15), ("maxOfNegativeSD", 16), ("maxOfPositiveDS", 17), ("maxOfNegativeDS", 18), ("successivePacketLoss", 19), ("maxOfLatencyDS", 20), ("maxOfLatencySD", 21), ("latencyDSAvg", 22), ("latencySDAvg", 23), ("packetLoss", 24))

mibBuilder.exportSymbols("CISCO-IPSLA-TC-MIB", IpSlaReactVar=IpSlaReactVar, ciscoIpSlaTCMIB=ciscoIpSlaTCMIB, PYSNMP_MODULE_ID=ciscoIpSlaTCMIB, IpSlaOperType=IpSlaOperType, IpSlaCodecType=IpSlaCodecType)
