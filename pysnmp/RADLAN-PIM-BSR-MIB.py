#
# PySNMP MIB module RADLAN-PIM-BSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-PIM-BSR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:39:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
IANAipRouteProtocol, = mibBuilder.importSymbols("IANA-RTPROTO-MIB", "IANAipRouteProtocol")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
InetAddressType, InetAddressPrefixLength, InetVersion, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddressPrefixLength", "InetVersion", "InetAddress")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, Bits, iso, Counter32, ObjectIdentity, Unsigned32, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Integer32, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "Bits", "iso", "Counter32", "ObjectIdentity", "Unsigned32", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Integer32", "Counter64", "ModuleIdentity")
TruthValue, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "DisplayString", "TextualConvention")
class AdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("adminStatusUp", 1), ("adminStatusDown", 2))

class OperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5))

rlPimBsrCandidateRPTable = MibTable((1, 3, 6, 1, 4, 1, 89, 220), )
if mibBuilder.loadTexts: rlPimBsrCandidateRPTable.setStatus('current')
rlPimBsrCandidateRPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 220, 1), ).setIndexNames((0, "RADLAN-PIM-BSR-MIB", "rlPimBsrCandidateRPAddressType"), (0, "RADLAN-PIM-BSR-MIB", "rlPimBsrCandidateRPAddress"))
if mibBuilder.loadTexts: rlPimBsrCandidateRPEntry.setStatus('current')
rlPimBsrCandidateRPAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 1), InetAddressType())
if mibBuilder.loadTexts: rlPimBsrCandidateRPAddressType.setStatus('current')
rlPimBsrCandidateRPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: rlPimBsrCandidateRPAddress.setStatus('current')
rlPimBsrCandidateRPGroupPrefixList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPGroupPrefixList.setStatus('current')
rlPimBsrCandidateRPBidir = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPBidir.setStatus('current')
rlPimBsrCandidateRPAdvTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvTimer.setStatus('current')
rlPimBsrCandidateRPPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(192)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPPriority.setStatus('current')
rlPimBsrCandidateRPAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 26214)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvInterval.setStatus('current')
rlPimBsrCandidateRPHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(150)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPHoldtime.setStatus('current')
rlPimBsrCandidateRPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPStatus.setStatus('current')
mibBuilder.exportSymbols("RADLAN-PIM-BSR-MIB", rlPimBsrCandidateRPAddress=rlPimBsrCandidateRPAddress, rlPimBsrCandidateRPGroupPrefixList=rlPimBsrCandidateRPGroupPrefixList, rlPimBsrCandidateRPHoldtime=rlPimBsrCandidateRPHoldtime, AdminStatus=AdminStatus, rlPimBsrCandidateRPPriority=rlPimBsrCandidateRPPriority, rlPimBsrCandidateRPAdvTimer=rlPimBsrCandidateRPAdvTimer, rlPimBsrCandidateRPTable=rlPimBsrCandidateRPTable, rlPimBsrCandidateRPBidir=rlPimBsrCandidateRPBidir, rlPimBsrCandidateRPAdvInterval=rlPimBsrCandidateRPAdvInterval, rlPimBsrCandidateRPStatus=rlPimBsrCandidateRPStatus, rlPimBsrCandidateRPAddressType=rlPimBsrCandidateRPAddressType, OperStatus=OperStatus, rlPimBsrCandidateRPEntry=rlPimBsrCandidateRPEntry)
