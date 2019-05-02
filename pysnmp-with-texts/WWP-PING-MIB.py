#
# PySNMP MIB module WWP-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-PING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter64, IpAddress, Gauge32, MibIdentifier, ObjectIdentity, Integer32, TimeTicks, Counter32, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "IpAddress", "Gauge32", "MibIdentifier", "ObjectIdentity", "Integer32", "TimeTicks", "Counter32", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
wwpModules, = mibBuilder.importSymbols("WWP-SMI", "wwpModules")
wwpPingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 21))
wwpPingMIB.setRevisions(('2001-07-03 12:57',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpPingMIB.setRevisionsDescriptions(('Initial Creation',))
if mibBuilder.loadTexts: wwpPingMIB.setLastUpdated('200107031257Z')
if mibBuilder.loadTexts: wwpPingMIB.setOrganization('Organization.')
if mibBuilder.loadTexts: wwpPingMIB.setContactInfo(' Mib Meister Postal: World Wide Packets P.O. Box 950 Veradale, WA 99037 USA Phone: +1 509 242 9000 Email: mib.meister@worldwidepackets.com')
if mibBuilder.loadTexts: wwpPingMIB.setDescription('The MIB for WWP Ping')
class PingFailCause(TextualConvention, Integer32):
    description = 'Description.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("unknownHost", 1), ("socketError", 2), ("bindError", 3), ("connectError", 4), ("missingHost", 5), ("asyncError", 6), ("nonBlockError", 7), ("mcastError", 8), ("ttlError", 9), ("mcastTtlError", 10), ("outputError", 11), ("unreachableError", 12), ("isAlive", 13), ("txRx", 14), ("commandCompleted", 15), ("noStatus", 16), ("sendRecvMismatch", 17))

class PingState(TextualConvention, Integer32):
    description = 'Description.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("idle", 1), ("pinging", 2), ("pingComplete", 3), ("failed", 4))

wwpPingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1))
wwpPingDelay = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingDelay.setStatus('current')
if mibBuilder.loadTexts: wwpPingDelay.setDescription('The object specifies the minimum amount of time to wait before sending the next packet in a sequence after receiving a response or declaring a timeout for a previous packet.')
wwpPingPacketSize = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1464)).clone(56)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingPacketSize.setStatus('current')
if mibBuilder.loadTexts: wwpPingPacketSize.setDescription('The size of the ping packets to send to the target.')
wwpPingActivate = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingActivate.setStatus('current')
if mibBuilder.loadTexts: wwpPingActivate.setDescription("Ping can be activated by setting this object to true. Once the ping operation is completed , the object is set to 'false'. This object can be set to 'false' by the Management Station to stop the ping.")
wwpPingAddress = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingAddress.setStatus('current')
if mibBuilder.loadTexts: wwpPingAddress.setDescription('The address of the device to be pinged. The default value should be of the loopback address.')
wwpPingPacketCount = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingPacketCount.setStatus('current')
if mibBuilder.loadTexts: wwpPingPacketCount.setDescription('Specifies the number of icmp requests to send to the target.')
wwpPingPacketTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingPacketTimeout.setStatus('current')
if mibBuilder.loadTexts: wwpPingPacketTimeout.setDescription("Specifies the amount of time to wait for a response to a transmitted packet before declaring the packet 'dropped'.")
wwpPingSentPackets = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPingSentPackets.setStatus('current')
if mibBuilder.loadTexts: wwpPingSentPackets.setDescription('The number of ping packets that have been sent to the target.')
wwpPingReceivedPackets = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPingReceivedPackets.setStatus('current')
if mibBuilder.loadTexts: wwpPingReceivedPackets.setDescription('The number of ping packets that have been reveived from the target.')
wwpPingFailCause = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 13), PingFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPingFailCause.setStatus('current')
if mibBuilder.loadTexts: wwpPingFailCause.setDescription('The result of the ping.')
wwpPingState = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 15), PingState().clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpPingState.setStatus('current')
if mibBuilder.loadTexts: wwpPingState.setDescription('The state of the ping process.The state be pinging, idle, complete or failed.')
wwpPingUntilStopped = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 21, 1, 16), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpPingUntilStopped.setStatus('current')
if mibBuilder.loadTexts: wwpPingUntilStopped.setDescription("setting this object to true prior to wwpPingActivate will cause the device to ping the specified host until wwpPingActivate is set to false. The object can't be modified once the ping is active. The object returns to 'false' once the ping is halted.")
mibBuilder.exportSymbols("WWP-PING-MIB", wwpPingUntilStopped=wwpPingUntilStopped, wwpPingAddress=wwpPingAddress, wwpPingPacketTimeout=wwpPingPacketTimeout, wwpPingPacketCount=wwpPingPacketCount, PYSNMP_MODULE_ID=wwpPingMIB, PingState=PingState, wwpPingMIBObjects=wwpPingMIBObjects, wwpPingMIB=wwpPingMIB, wwpPingSentPackets=wwpPingSentPackets, wwpPingActivate=wwpPingActivate, wwpPingFailCause=wwpPingFailCause, wwpPingState=wwpPingState, wwpPingDelay=wwpPingDelay, wwpPingReceivedPackets=wwpPingReceivedPackets, PingFailCause=PingFailCause, wwpPingPacketSize=wwpPingPacketSize)
