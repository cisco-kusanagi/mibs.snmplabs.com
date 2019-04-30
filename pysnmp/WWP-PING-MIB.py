#
# PySNMP MIB module WWP-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-PING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:31:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, iso, Unsigned32, MibIdentifier, Counter32, IpAddress, Integer32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "iso", "Unsigned32", "MibIdentifier", "Counter32", "IpAddress", "Integer32", "ObjectIdentity")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpPingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 21))
wwpPingMIB.setRevisions(('2001-07-03 12:57',))
if mibBuilder.loadTexts: wwpPingMIB.setLastUpdated('200107031257Z')
if mibBuilder.loadTexts: wwpPingMIB.setOrganization('Organization.')
class PingFailCause(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("unknownHost", 1), ("socketError", 2), ("bindError", 3), ("connectError", 4), ("missingHost", 5), ("asyncError", 6), ("nonBlockError", 7), ("mcastError", 8), ("ttlError", 9), ("mcastTtlError", 10), ("outputError", 11), ("unreachableError", 12), ("isAlive", 13), ("txRx", 14), ("commandCompleted", 15), ("noStatus", 16), ("sendRecvMismatch", 17))

class PingState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("idle", 1), ("pinging", 2), ("pingComplete", 3), ("failed", 4))

wwpPingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1))
wwpPingDelay = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingDelay.setStatus('current')
wwpPingPacketSize = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1464)).clone(56)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingPacketSize.setStatus('current')
wwpPingActivate = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingActivate.setStatus('current')
wwpPingAddress = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingAddress.setStatus('current')
wwpPingPacketCount = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingPacketCount.setStatus('current')
wwpPingPacketTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingPacketTimeout.setStatus('current')
wwpPingSentPackets = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPingSentPackets.setStatus('current')
wwpPingReceivedPackets = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPingReceivedPackets.setStatus('current')
wwpPingFailCause = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 13), PingFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPingFailCause.setStatus('current')
wwpPingState = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 15), PingState().clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPingState.setStatus('current')
wwpPingUntilStopped = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 16), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingUntilStopped.setStatus('current')
mibBuilder.exportSymbols("WWP-PING-MIB", PingState=PingState, wwpPingState=wwpPingState, wwpPingSentPackets=wwpPingSentPackets, wwpPingPacketSize=wwpPingPacketSize, wwpPingPacketCount=wwpPingPacketCount, wwpPingMIBObjects=wwpPingMIBObjects, wwpPingAddress=wwpPingAddress, wwpPingDelay=wwpPingDelay, PingFailCause=PingFailCause, wwpPingFailCause=wwpPingFailCause, PYSNMP_MODULE_ID=wwpPingMIB, wwpPingReceivedPackets=wwpPingReceivedPackets, wwpPingActivate=wwpPingActivate, wwpPingUntilStopped=wwpPingUntilStopped, wwpPingMIB=wwpPingMIB, wwpPingPacketTimeout=wwpPingPacketTimeout)
