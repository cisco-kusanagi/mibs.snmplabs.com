#
# PySNMP MIB module CISCO-RTTMON-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-RTTMON-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:45:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Gauge32, TimeTicks, Unsigned32, IpAddress, ModuleIdentity, Counter32, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "TimeTicks", "Unsigned32", "IpAddress", "ModuleIdentity", "Counter32", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "Counter64", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoRttMonTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 485))
ciscoRttMonTCMIB.setRevisions(('2014-03-19 00:00', '2013-11-26 00:00', '2012-11-02 00:00', '2012-05-25 00:00', '2011-09-15 00:00', '2010-04-26 00:00', '2006-08-11 00:00', '2006-07-17 00:00', '2006-03-02 00:00', '2005-08-09 00:00',))
if mibBuilder.loadTexts: ciscoRttMonTCMIB.setLastUpdated('201403190000Z')
if mibBuilder.loadTexts: ciscoRttMonTCMIB.setOrganization('Cisco Systems, Inc.')
class RttMonScheduleStartType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("pending", 1), ("now", 2), ("random", 3), ("after", 4), ("specific", 5))

class RttReset(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ready", 1), ("reset", 2))

class RttMonOperation(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("notApplicable", 0), ("httpGet", 1), ("httpRaw", 2), ("ftpGet", 3), ("ftpPassive", 4), ("ftpActive", 5), ("voipDTAlertRinging", 6), ("voipDTConnectOK", 7))

class RttResponseSense(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38))
    namedValues = NamedValues(("other", 0), ("ok", 1), ("disconnected", 2), ("overThreshold", 3), ("timeout", 4), ("busy", 5), ("notConnected", 6), ("dropped", 7), ("sequenceError", 8), ("verifyError", 9), ("applicationSpecific", 10), ("dnsServerTimeout", 11), ("tcpConnectTimeout", 12), ("httpTransactionTimeout", 13), ("dnsQueryError", 14), ("httpError", 15), ("error", 16), ("mplsLspEchoTxError", 17), ("mplsLspUnreachable", 18), ("mplsLspMalformedReq", 19), ("mplsLspReachButNotFEC", 20), ("enableOk", 21), ("enableNoConnect", 22), ("enableVersionFail", 23), ("enableInternalError", 24), ("enableAbort", 25), ("enableFail", 26), ("enableAuthFail", 27), ("enableFormatError", 28), ("enablePortInUse", 29), ("statsRetrieveOk", 30), ("statsRetrieveNoConnect", 31), ("statsRetrieveVersionFail", 32), ("statsRetrieveInternalError", 33), ("statsRetrieveAbort", 34), ("statsRetrieveFail", 35), ("statsRetrieveAuthFail", 36), ("statsRetrieveFormatError", 37), ("statsRetrievePortInUse", 38))

class RttMonRttType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26))
    namedValues = NamedValues(("echo", 1), ("pathEcho", 2), ("fileIO", 3), ("script", 4), ("udpEcho", 5), ("tcpConnect", 6), ("http", 7), ("dns", 8), ("jitter", 9), ("dlsw", 10), ("dhcp", 11), ("ftp", 12), ("voip", 13), ("rtp", 14), ("lspGroup", 15), ("icmpjitter", 16), ("lspPing", 17), ("lspTrace", 18), ("ethernetPing", 19), ("ethernetJitter", 20), ("lspPingPseudowire", 21), ("video", 22), ("y1731Delay", 23), ("y1731Loss", 24), ("mcastJitter", 25), ("fabricPathEcho", 26))

class RttMplsVpnMonRttType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("jitter", 1), ("echo", 2), ("pathEcho", 3))

class RttMplsVpnMonLpdFailureSense(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("unknown", 1), ("noPath", 2), ("allPathsBroken", 3), ("allPathsUnexplorable", 4), ("allPathsBrokenOrUnexplorable", 5), ("timeout", 6), ("error", 7))

class RttMplsVpnMonLpdGrpStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("unknown", 1), ("up", 2), ("partial", 3), ("down", 4))

class RttMonProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44))
    namedValues = NamedValues(("notApplicable", 1), ("ipIcmpEcho", 2), ("ipUdpEchoAppl", 3), ("snaRUEcho", 4), ("snaLU0EchoAppl", 5), ("snaLU2EchoAppl", 6), ("snaLU62Echo", 7), ("snaLU62EchoAppl", 8), ("appleTalkEcho", 9), ("appleTalkEchoAppl", 10), ("decNetEcho", 11), ("decNetEchoAppl", 12), ("ipxEcho", 13), ("ipxEchoAppl", 14), ("isoClnsEcho", 15), ("isoClnsEchoAppl", 16), ("vinesEcho", 17), ("vinesEchoAppl", 18), ("xnsEcho", 19), ("xnsEchoAppl", 20), ("apolloEcho", 21), ("apolloEchoAppl", 22), ("netbiosEchoAppl", 23), ("ipTcpConn", 24), ("httpAppl", 25), ("dnsAppl", 26), ("jitterAppl", 27), ("dlswAppl", 28), ("dhcpAppl", 29), ("ftpAppl", 30), ("mplsLspPingAppl", 31), ("voipAppl", 32), ("rtpAppl", 33), ("icmpJitterAppl", 34), ("ethernetPingAppl", 35), ("ethernetJitterAppl", 36), ("videoAppl", 37), ("y1731dmm", 38), ("y17311dm", 39), ("y1731lmm", 40), ("mcastJitterAppl", 41), ("y1731slm", 42), ("y1731dmmv1", 43), ("fabricPathEchoAppl", 44))

class RttMonCodecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("g711ulaw", 1), ("g711alaw", 2), ("g729a", 3))

class RttMonLSPPingReplyMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("replyIpv4Udp", 1), ("replyIpv4UdpRA", 2))

class RttMonTargetAddress(TextualConvention, OctetString):
    status = 'current'

class RttMonReactVar(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49))
    namedValues = NamedValues(("rtt", 1), ("jitterSDAvg", 2), ("jitterDSAvg", 3), ("packetLossSD", 4), ("packetLossDS", 5), ("mos", 6), ("timeout", 7), ("connectionLoss", 8), ("verifyError", 9), ("jitterAvg", 10), ("icpif", 11), ("packetMIA", 12), ("packetLateArrival", 13), ("packetOutOfSequence", 14), ("maxOfPositiveSD", 15), ("maxOfNegativeSD", 16), ("maxOfPositiveDS", 17), ("maxOfNegativeDS", 18), ("iaJitterDS", 19), ("frameLossDS", 20), ("mosLQDS", 21), ("mosCQDS", 22), ("rFactorDS", 23), ("successivePacketLoss", 24), ("maxOfLatencyDS", 25), ("maxOfLatencySD", 26), ("latencyDSAvg", 27), ("latencySDAvg", 28), ("packetLoss", 29), ("iaJitterSD", 30), ("mosCQSD", 31), ("rFactorSD", 32), ("lpdGroup", 33), ("lpdTreeTrace", 34), ("lpdAll", 35), ("unavailSD", 36), ("unavailDS", 37), ("pktLossPctSD", 38), ("pktLossPctDS", 39), ("rttPct", 40), ("maxOfLatencySDPct", 41), ("maxOfLatencyDSPct", 42), ("latencySDAvgPct", 43), ("latencyDSAvgPct", 44), ("jitterSDAvgPct", 45), ("jitterDSAvgPct", 46), ("jitterAvgPct", 47), ("overThreshold", 48), ("protocolSpecificError", 49))

class RttMonIdLst(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class RttMonCtrlIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

mibBuilder.exportSymbols("CISCO-RTTMON-TC-MIB", RttMonCodecType=RttMonCodecType, RttMonLSPPingReplyMode=RttMonLSPPingReplyMode, RttMonIdLst=RttMonIdLst, RttMonReactVar=RttMonReactVar, RttMonProtocol=RttMonProtocol, RttMonCtrlIndex=RttMonCtrlIndex, RttMonScheduleStartType=RttMonScheduleStartType, RttMonOperation=RttMonOperation, RttMonTargetAddress=RttMonTargetAddress, RttResponseSense=RttResponseSense, RttReset=RttReset, RttMonRttType=RttMonRttType, RttMplsVpnMonLpdFailureSense=RttMplsVpnMonLpdFailureSense, PYSNMP_MODULE_ID=ciscoRttMonTCMIB, ciscoRttMonTCMIB=ciscoRttMonTCMIB, RttMplsVpnMonLpdGrpStatus=RttMplsVpnMonLpdGrpStatus, RttMplsVpnMonRttType=RttMplsVpnMonRttType)
