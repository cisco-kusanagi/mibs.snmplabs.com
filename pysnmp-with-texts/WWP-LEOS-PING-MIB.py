#
# PySNMP MIB module WWP-LEOS-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WWP-LEOS-PING-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:38:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
InetAddressType, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, iso, ObjectIdentity, TimeTicks, MibIdentifier, Counter64, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "iso", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Counter64", "Unsigned32", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
wwpModulesLeos, = mibBuilder.importSymbols("WWP-SMI", "wwpModulesLeos")
wwpLeosPingMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19))
wwpLeosPingMIB.setRevisions(('2012-04-02 00:00', '2001-07-03 12:57',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wwpLeosPingMIB.setRevisionsDescriptions(('Add wwpLeosPingInetAddrType to support IP protocol version independent Inet addressing.', 'Initial Creation',))
if mibBuilder.loadTexts: wwpLeosPingMIB.setLastUpdated('201204020000Z')
if mibBuilder.loadTexts: wwpLeosPingMIB.setOrganization('Ciena, Inc')
if mibBuilder.loadTexts: wwpLeosPingMIB.setContactInfo(' Mib Meister 115 North Sullivan Road Spokane Valley, WA 99037 USA Phone: +1 509 242 9000 Email: support@ciena.com')
if mibBuilder.loadTexts: wwpLeosPingMIB.setDescription('The MIB for WWP Ping')
class PingFailCause(TextualConvention, Integer32):
    description = 'The cause of the last ping failure.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17))
    namedValues = NamedValues(("unknownHost", 1), ("socketError", 2), ("bindError", 3), ("connectError", 4), ("missingHost", 5), ("asyncError", 6), ("nonBlockError", 7), ("mcastError", 8), ("ttlError", 9), ("mcastTtlError", 10), ("outputError", 11), ("unreachableError", 12), ("isAlive", 13), ("txRx", 14), ("commandCompleted", 15), ("noStatus", 16), ("sendRecvMismatch", 17))

class PingState(TextualConvention, Integer32):
    description = 'The state of the last ping request.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("idle", 1), ("pinging", 2), ("pingComplete", 3), ("failed", 4))

wwpLeosPingMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1))
wwpLeosPingDelay = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingDelay.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingDelay.setDescription('The object specifies the minimum amount of time to wait before sending the next packet in a sequence after receiving a response or declaring a timeout for a previous packet.')
wwpLeosPingPacketSize = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1464)).clone(56)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingPacketSize.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingPacketSize.setDescription('The size of the ping packets to send to the target.')
wwpLeosPingActivate = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingActivate.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingActivate.setDescription("Ping can be activated by setting this object to true. Once the ping operation is completed, the object is set to 'false'. This object can be set to 'false' by the Management Station to stop the ping.")
wwpLeosPingAddrType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 4), AddressFamilyNumbers()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingAddrType.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingAddrType.setDescription('The address type associated with wwpLeosPingAddr. With the new wwpLeosPingInetAddrType being introduced to support RFC 4001, this OID will only be used when wwpLeosPingAddr is a host name or an IPv4 address. Otherwise, it will be set to other(0).')
wwpLeosPingAddr = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingAddr.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingAddr.setDescription('The host name or IP address of the device to be pinged. wwpLeosPingAddrType determines if address is host name or IP address.')
wwpLeosPingPacketCount = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingPacketCount.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingPacketCount.setDescription('Specifies the number of ICMP requests to send to the target.')
wwpLeosPingPacketTimeout = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingPacketTimeout.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingPacketTimeout.setDescription("Specifies the amount of time to wait for a response to a transmitted packet before declaring the packet 'dropped'.")
wwpLeosPingSentPackets = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingSentPackets.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingSentPackets.setDescription('The number of ping packets that have been sent to the target.')
wwpLeosPingReceivedPackets = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingReceivedPackets.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingReceivedPackets.setDescription('The number of ping packets that have been received from the target.')
wwpLeosPingFailCause = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 10), PingFailCause()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingFailCause.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingFailCause.setDescription('The result of the ping.')
wwpLeosPingState = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 11), PingState().clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingState.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingState.setDescription('The state of the ping process. The possible states include pinging, idle, complete or failed.')
wwpLeosPingUntilStopped = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wwpLeosPingUntilStopped.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingUntilStopped.setDescription("Setting this object to true prior to wwpLeosPingActivate will cause the device to ping the specified host until wwpLeosPingActivate is set to false. The object cannot be modified once the ping is active. The object returns to 'false' once the ping is halted.")
wwpLeosPingInetAddrType = MibScalar((1, 3, 6, 1, 4, 1, 6141, 2, 60, 19, 1, 13), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wwpLeosPingInetAddrType.setStatus('current')
if mibBuilder.loadTexts: wwpLeosPingInetAddrType.setDescription('The Inet address type associated with wwpLeosPingAddr. When set to: ipv4 : wwpLeosPingAddr should be compliant with InetAddressIPv4 from RFC 4001 ipv6 : wwpLeosPingAddr should be compliant with InetAddressIPv6 from RFC 4001.')
mibBuilder.exportSymbols("WWP-LEOS-PING-MIB", wwpLeosPingMIB=wwpLeosPingMIB, wwpLeosPingDelay=wwpLeosPingDelay, wwpLeosPingPacketTimeout=wwpLeosPingPacketTimeout, wwpLeosPingPacketSize=wwpLeosPingPacketSize, wwpLeosPingFailCause=wwpLeosPingFailCause, wwpLeosPingSentPackets=wwpLeosPingSentPackets, PingState=PingState, wwpLeosPingPacketCount=wwpLeosPingPacketCount, wwpLeosPingState=wwpLeosPingState, wwpLeosPingMIBObjects=wwpLeosPingMIBObjects, wwpLeosPingInetAddrType=wwpLeosPingInetAddrType, PingFailCause=PingFailCause, wwpLeosPingReceivedPackets=wwpLeosPingReceivedPackets, PYSNMP_MODULE_ID=wwpLeosPingMIB, wwpLeosPingAddrType=wwpLeosPingAddrType, wwpLeosPingUntilStopped=wwpLeosPingUntilStopped, wwpLeosPingActivate=wwpLeosPingActivate, wwpLeosPingAddr=wwpLeosPingAddr)
