#
# PySNMP MIB module HM2-PLATFORM-MSRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HM2-PLATFORM-MSRP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:19:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
BridgeId, = mibBuilder.importSymbols("BRIDGE-MIB", "BridgeId")
hm2AgentDot1qMrpMxrp, = mibBuilder.importSymbols("HM2-PLATFORM-MRP-MIB", "hm2AgentDot1qMrpMxrp")
VlanId, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "VlanId")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, Integer32, NotificationType, ModuleIdentity, iso, MibIdentifier, ObjectIdentity, Unsigned32, Gauge32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "Integer32", "NotificationType", "ModuleIdentity", "iso", "MibIdentifier", "ObjectIdentity", "Unsigned32", "Gauge32", "Bits")
TextualConvention, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "MacAddress")
hm2PlatformMSRP = ModuleIdentity((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3))
hm2PlatformMSRP.setRevisions(('2013-04-10 00:00',))
if mibBuilder.loadTexts: hm2PlatformMSRP.setLastUpdated('201304100000Z')
if mibBuilder.loadTexts: hm2PlatformMSRP.setOrganization('Hirschmann Automation and Control GmbH')
class Hm2AgentDot1qPriorityValue(TextualConvention, Unsigned32):
    reference = '12.13.3.3'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class Hm2AgentDot1qMsrpStreamRankValue(TextualConvention, Integer32):
    reference = '35.2.2.8.5b'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("emergency", 0), ("nonEmergency", 1))

class Hm2AgentDot1qMsrpStreamIdValue(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:1x:1x:1x:1x:1x.1x:1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class Hm2AgentDot1qMsrpReservationDirectionValue(TextualConvention, Integer32):
    reference = '35.2.1.2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("talkerRegistrations", 0), ("listenerRegistrations", 1))

class Hm2AgentDot1qMsrpReservationDeclarationTypeValue(TextualConvention, Integer32):
    reference = '35.2.1.3'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("talkerAdvertise", 0), ("talkerFailed", 1), ("listenerAskingFailed", 2), ("listenerReady", 3), ("listenerReadyFailed", 4))

class Hm2AgentDot1qMsrpReservationFailureCodeValue(TextualConvention, Integer32):
    reference = '35.2.2.8.7'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("noFailure", 0), ("insufficientBandwidth", 1), ("insufficientResources", 2), ("insufficientTrafficClassBandwidth", 3), ("streamIDInUse", 4), ("streamDestinationAddressInUse", 5), ("streamPreemptedByHigherRank", 6), ("latencyHasChanged", 7), ("egressPortNotAVBCapable", 8), ("useDifferentDestinationAddress", 9), ("outOfMSRPResources", 10), ("outOfMMRPResources", 11), ("cannotStoreDestinationAddress", 12), ("priorityIsNoAnSRCLass", 13), ("maxFrameSizeTooLarge", 14), ("maxFanInPortsLimitReached", 15), ("firstValueChangedForStreamID", 16), ("vlanBlockedOnEgress", 17), ("vlanTaggingDisabledOnEgress", 18), ("srClassPriorityMismatch", 19))

class Hm2AgentDot1qFqtssTrafficClassValue(TextualConvention, Unsigned32):
    reference = '12.21'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class Hm2AgentDot1qFqtssDeltaBandwidthValue(TextualConvention, Unsigned32):
    reference = '12.21, 34.4'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100000000)

class Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue(TextualConvention, Unsigned32):
    reference = '8.6.8, 12.21'
    status = 'current'
    displayHint = 'd'

hm2AgentDot1qMsrp = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1))
hm2AgentDot1qMrpMsrpStats = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2))
hm2AgentDot1qFqtss = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3))
hm2AgentDot1qPortMsrpTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1), )
if mibBuilder.loadTexts: hm2AgentDot1qPortMsrpTable.setStatus('current')
hm2AgentDot1qPortMsrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1), ).setIndexNames((0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpPort"))
if mibBuilder.loadTexts: hm2AgentDot1qPortMsrpEntry.setStatus('current')
hm2AgentDot1qMsrpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hm2AgentDot1qMsrpPort.setStatus('current')
hm2AgentDot1qPortMsrpEnabledStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qPortMsrpEnabledStatus.setStatus('current')
hm2AgentDot1qPortMsrpFailedRegistrations = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1, 3), Counter64()).setUnits('failed MSRP registrations').setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qPortMsrpFailedRegistrations.setStatus('current')
hm2AgentDot1qPortMsrpLastPduOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qPortMsrpLastPduOrigin.setStatus('current')
hm2AgentDot1qPortMsrpPvid = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 1, 1, 5), VlanId().clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qPortMsrpPvid.setStatus('current')
hm2AgentDot1qBridgeMsrpEnabledStatus = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qBridgeMsrpEnabledStatus.setStatus('current')
hm2AgentDot1qBridgeMsrpTalkerPruning = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qBridgeMsrpTalkerPruning.setStatus('current')
hm2AgentDot1qBridgeMsrpMaxFanInPorts = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 4), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qBridgeMsrpMaxFanInPorts.setStatus('current')
hm2AgentDot1qBridgeMsrpBoundaryPropagate = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qBridgeMsrpBoundaryPropagate.setStatus('current')
hm2AgentDot1qMsrpStreamTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7), )
if mibBuilder.loadTexts: hm2AgentDot1qMsrpStreamTable.setStatus('current')
hm2AgentDot1qMsrpStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1), ).setIndexNames((0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpStreamIndex"))
if mibBuilder.loadTexts: hm2AgentDot1qMsrpStreamEntry.setStatus('current')
hm2AgentDot1qMsrpStreamIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: hm2AgentDot1qMsrpStreamIndex.setStatus('current')
hm2AgentDot1qMsrpStreamID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 2), Hm2AgentDot1qMsrpStreamIdValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpStreamID.setStatus('current')
hm2AgentDot1qMsrpStreamDestMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpStreamDestMacAddr.setStatus('current')
hm2AgentDot1qMsrpStreamVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpStreamVlanId.setStatus('current')
hm2AgentDot1qMsrpStreamTspecMaxFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpStreamTspecMaxFrameSize.setStatus('current')
hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames.setStatus('current')
hm2AgentDot1qMsrpStreamDataFramePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 7), Hm2AgentDot1qPriorityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpStreamDataFramePriority.setStatus('current')
hm2AgentDot1qMsrpStreamRank = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 7, 1, 8), Hm2AgentDot1qMsrpStreamRankValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpStreamRank.setStatus('current')
hm2AgentDot1qMsrpReservationTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8), )
if mibBuilder.loadTexts: hm2AgentDot1qMsrpReservationTable.setStatus('current')
hm2AgentDot1qMsrpReservationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1), ).setIndexNames((0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpReservationStreamId"), (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpReservationDirection"), (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpPort"))
if mibBuilder.loadTexts: hm2AgentDot1qMsrpReservationEntry.setStatus('current')
hm2AgentDot1qMsrpReservationStreamId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 1), Hm2AgentDot1qMsrpStreamIdValue())
if mibBuilder.loadTexts: hm2AgentDot1qMsrpReservationStreamId.setStatus('current')
hm2AgentDot1qMsrpReservationDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 2), Hm2AgentDot1qMsrpReservationDirectionValue())
if mibBuilder.loadTexts: hm2AgentDot1qMsrpReservationDirection.setStatus('current')
hm2AgentDot1qMsrpReservationDeclarationType = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 3), Hm2AgentDot1qMsrpReservationDeclarationTypeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpReservationDeclarationType.setStatus('current')
hm2AgentDot1qMsrpReservationAccumulatedLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 4), Unsigned32()).setUnits('nano-seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpReservationAccumulatedLatency.setStatus('current')
hm2AgentDot1qMsrpReservationFailureBridgeId = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 5), BridgeId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpReservationFailureBridgeId.setStatus('current')
hm2AgentDot1qMsrpReservationFailureCode = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 6), Hm2AgentDot1qMsrpReservationFailureCodeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpReservationFailureCode.setStatus('current')
hm2AgentDot1qMsrpReservationDroppedStreamFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 7), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpReservationDroppedStreamFrames.setStatus('current')
hm2AgentDot1qMsrpReservationStreamAge = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 1, 8, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMsrpReservationStreamAge.setStatus('current')
hm2AgentDot1qMrpMsrpPktTx = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPktTx.setStatus('current')
hm2AgentDot1qMrpMsrpPktRx = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPktRx.setStatus('current')
hm2AgentDot1qMrpMsrpPktRxBadHeader = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPktRxBadHeader.setStatus('current')
hm2AgentDot1qMrpMsrpPktRxBadFormat = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPktRxBadFormat.setStatus('current')
hm2AgentDot1qMrpMsrpPktTxFailure = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPktTxFailure.setStatus('current')
hm2AgentDot1qMrpMsrpStatsTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6), )
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpStatsTable.setStatus('current')
hm2AgentDot1qMrpMsrpStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1), ).setIndexNames((0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMrpMsrpIntf"))
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpStatsEntry.setStatus('current')
hm2AgentDot1qMrpMsrpIntf = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpIntf.setStatus('current')
hm2AgentDot1qMrpMsrpPortPktTx = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPortPktTx.setStatus('current')
hm2AgentDot1qMrpMsrpPortPktRx = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPortPktRx.setStatus('current')
hm2AgentDot1qMrpMsrpPortPktRxBadHeader = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPortPktRxBadHeader.setStatus('current')
hm2AgentDot1qMrpMsrpPortPktRxBadFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPortPktRxBadFormat.setStatus('current')
hm2AgentDot1qMrpMsrpPortPktTxFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPortPktTxFailure.setStatus('current')
hm2AgentDot1qMrpMsrpPortPktRegFailure = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPortPktRegFailure.setStatus('current')
hm2AgentDot1qMrpMsrpPktMessageFailure = MibScalar((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 2, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qMrpMsrpPktMessageFailure.setStatus('current')
hm2AgentDot1qFqtssNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 0))
hm2AgentDot1qFqtssObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 1))
hm2AgentDot1qFqtssConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 2))
hm2AgentDot1qFqtssBap = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3))
hm2AgentDot1qFqtssMappings = MibIdentifier((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4))
hm2AgentDot1qFqtssBapTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1), )
if mibBuilder.loadTexts: hm2AgentDot1qFqtssBapTable.setStatus('current')
hm2AgentDot1qFqtssBapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1), ).setIndexNames((0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpPort"), (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qFqtssTrafficClass"))
if mibBuilder.loadTexts: hm2AgentDot1qFqtssBapEntry.setStatus('current')
hm2AgentDot1qFqtssTrafficClass = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 1), Hm2AgentDot1qFqtssTrafficClassValue())
if mibBuilder.loadTexts: hm2AgentDot1qFqtssTrafficClass.setStatus('current')
hm2AgentDot1qFqtssDeltaBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 2), Hm2AgentDot1qFqtssDeltaBandwidthValue()).setUnits('percent').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qFqtssDeltaBandwidth.setStatus('current')
hm2AgentDot1qFqtssOperIdleSlopeMs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 3), Unsigned32()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qFqtssOperIdleSlopeMs.setStatus('current')
hm2AgentDot1qFqtssOperIdleSlopeLs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 4), Unsigned32()).setUnits('bits per second').setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qFqtssOperIdleSlopeLs.setStatus('current')
hm2AgentDot1qFqtssAdminIdleSlopeMs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 5), Unsigned32()).setUnits('bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qFqtssAdminIdleSlopeMs.setStatus('current')
hm2AgentDot1qFqtssAdminIdleSlopeLs = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 3, 1, 1, 6), Unsigned32()).setUnits('bits per second').setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qFqtssAdminIdleSlopeLs.setStatus('current')
hm2AgentDot1qFqtssTxSelectionAlgorithmTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 1), )
if mibBuilder.loadTexts: hm2AgentDot1qFqtssTxSelectionAlgorithmTable.setStatus('current')
hm2AgentDot1qFqtssTxSelectionAlgorithmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 1, 1), ).setIndexNames((0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpPort"), (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qFqtssTrafficClass"))
if mibBuilder.loadTexts: hm2AgentDot1qFqtssTxSelectionAlgorithmEntry.setStatus('current')
hm2AgentDot1qFqtssTxSelectionAlgorithmID = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 1, 1, 1), Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qFqtssTxSelectionAlgorithmID.setStatus('current')
hm2AgentDot1qFqtssSrpRegenOverrideTable = MibTable((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 2), )
if mibBuilder.loadTexts: hm2AgentDot1qFqtssSrpRegenOverrideTable.setStatus('current')
hm2AgentDot1qFqtssSrpRegenOverrideEntry = MibTableRow((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 2, 1), ).setIndexNames((0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qMsrpPort"), (0, "HM2-PLATFORM-MSRP-MIB", "hm2AgentDot1qFqtssTrafficClass"))
if mibBuilder.loadTexts: hm2AgentDot1qFqtssSrpRegenOverrideEntry.setStatus('current')
hm2AgentDot1qFqtssSrClassPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 2, 1, 1), Hm2AgentDot1qPriorityValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qFqtssSrClassPriority.setStatus('current')
hm2AgentDot1qFqtssPriorityRegenOverride = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 2, 1, 2), Hm2AgentDot1qPriorityValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hm2AgentDot1qFqtssPriorityRegenOverride.setStatus('current')
hm2AgentDot1qFqtssSrpBoundaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 248, 12, 60, 2, 3, 3, 4, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hm2AgentDot1qFqtssSrpBoundaryPort.setStatus('current')
mibBuilder.exportSymbols("HM2-PLATFORM-MSRP-MIB", hm2AgentDot1qMrpMsrpPktRx=hm2AgentDot1qMrpMsrpPktRx, hm2AgentDot1qMsrpStreamRank=hm2AgentDot1qMsrpStreamRank, hm2PlatformMSRP=hm2PlatformMSRP, hm2AgentDot1qMrpMsrpStats=hm2AgentDot1qMrpMsrpStats, hm2AgentDot1qPortMsrpLastPduOrigin=hm2AgentDot1qPortMsrpLastPduOrigin, hm2AgentDot1qBridgeMsrpTalkerPruning=hm2AgentDot1qBridgeMsrpTalkerPruning, Hm2AgentDot1qMsrpStreamIdValue=Hm2AgentDot1qMsrpStreamIdValue, hm2AgentDot1qPortMsrpEnabledStatus=hm2AgentDot1qPortMsrpEnabledStatus, hm2AgentDot1qMsrpReservationFailureBridgeId=hm2AgentDot1qMsrpReservationFailureBridgeId, hm2AgentDot1qPortMsrpTable=hm2AgentDot1qPortMsrpTable, hm2AgentDot1qFqtssBap=hm2AgentDot1qFqtssBap, hm2AgentDot1qMsrpStreamTable=hm2AgentDot1qMsrpStreamTable, hm2AgentDot1qBridgeMsrpBoundaryPropagate=hm2AgentDot1qBridgeMsrpBoundaryPropagate, Hm2AgentDot1qMsrpStreamRankValue=Hm2AgentDot1qMsrpStreamRankValue, hm2AgentDot1qBridgeMsrpMaxFanInPorts=hm2AgentDot1qBridgeMsrpMaxFanInPorts, hm2AgentDot1qMrpMsrpPortPktTx=hm2AgentDot1qMrpMsrpPortPktTx, hm2AgentDot1qFqtssTrafficClass=hm2AgentDot1qFqtssTrafficClass, hm2AgentDot1qFqtssSrpRegenOverrideTable=hm2AgentDot1qFqtssSrpRegenOverrideTable, hm2AgentDot1qMsrpReservationAccumulatedLatency=hm2AgentDot1qMsrpReservationAccumulatedLatency, hm2AgentDot1qFqtssOperIdleSlopeMs=hm2AgentDot1qFqtssOperIdleSlopeMs, hm2AgentDot1qMsrpReservationStreamAge=hm2AgentDot1qMsrpReservationStreamAge, hm2AgentDot1qFqtssPriorityRegenOverride=hm2AgentDot1qFqtssPriorityRegenOverride, hm2AgentDot1qMrpMsrpPktTxFailure=hm2AgentDot1qMrpMsrpPktTxFailure, hm2AgentDot1qBridgeMsrpEnabledStatus=hm2AgentDot1qBridgeMsrpEnabledStatus, hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames=hm2AgentDot1qMsrpStreamTspecMaxIntervalFrames, hm2AgentDot1qFqtssConformance=hm2AgentDot1qFqtssConformance, hm2AgentDot1qFqtss=hm2AgentDot1qFqtss, hm2AgentDot1qMsrpPort=hm2AgentDot1qMsrpPort, hm2AgentDot1qMsrpStreamTspecMaxFrameSize=hm2AgentDot1qMsrpStreamTspecMaxFrameSize, hm2AgentDot1qMsrpReservationFailureCode=hm2AgentDot1qMsrpReservationFailureCode, Hm2AgentDot1qMsrpReservationDirectionValue=Hm2AgentDot1qMsrpReservationDirectionValue, hm2AgentDot1qMsrpStreamVlanId=hm2AgentDot1qMsrpStreamVlanId, hm2AgentDot1qFqtssSrpRegenOverrideEntry=hm2AgentDot1qFqtssSrpRegenOverrideEntry, hm2AgentDot1qPortMsrpEntry=hm2AgentDot1qPortMsrpEntry, hm2AgentDot1qFqtssOperIdleSlopeLs=hm2AgentDot1qFqtssOperIdleSlopeLs, hm2AgentDot1qMsrpReservationStreamId=hm2AgentDot1qMsrpReservationStreamId, Hm2AgentDot1qMsrpReservationFailureCodeValue=Hm2AgentDot1qMsrpReservationFailureCodeValue, hm2AgentDot1qMsrpStreamDataFramePriority=hm2AgentDot1qMsrpStreamDataFramePriority, hm2AgentDot1qFqtssSrClassPriority=hm2AgentDot1qFqtssSrClassPriority, hm2AgentDot1qFqtssBapTable=hm2AgentDot1qFqtssBapTable, hm2AgentDot1qMsrpStreamEntry=hm2AgentDot1qMsrpStreamEntry, hm2AgentDot1qFqtssAdminIdleSlopeMs=hm2AgentDot1qFqtssAdminIdleSlopeMs, hm2AgentDot1qMsrpStreamID=hm2AgentDot1qMsrpStreamID, hm2AgentDot1qFqtssMappings=hm2AgentDot1qFqtssMappings, hm2AgentDot1qMrpMsrpPktTx=hm2AgentDot1qMrpMsrpPktTx, Hm2AgentDot1qFqtssDeltaBandwidthValue=Hm2AgentDot1qFqtssDeltaBandwidthValue, hm2AgentDot1qFqtssBapEntry=hm2AgentDot1qFqtssBapEntry, hm2AgentDot1qFqtssDeltaBandwidth=hm2AgentDot1qFqtssDeltaBandwidth, hm2AgentDot1qFqtssTxSelectionAlgorithmEntry=hm2AgentDot1qFqtssTxSelectionAlgorithmEntry, hm2AgentDot1qMsrpReservationEntry=hm2AgentDot1qMsrpReservationEntry, hm2AgentDot1qFqtssNotifications=hm2AgentDot1qFqtssNotifications, hm2AgentDot1qMrpMsrpStatsEntry=hm2AgentDot1qMrpMsrpStatsEntry, hm2AgentDot1qMrpMsrpStatsTable=hm2AgentDot1qMrpMsrpStatsTable, hm2AgentDot1qFqtssObjects=hm2AgentDot1qFqtssObjects, hm2AgentDot1qMrpMsrpPktRxBadFormat=hm2AgentDot1qMrpMsrpPktRxBadFormat, hm2AgentDot1qFqtssTxSelectionAlgorithmTable=hm2AgentDot1qFqtssTxSelectionAlgorithmTable, hm2AgentDot1qMsrp=hm2AgentDot1qMsrp, hm2AgentDot1qMrpMsrpPktRxBadHeader=hm2AgentDot1qMrpMsrpPktRxBadHeader, hm2AgentDot1qMsrpReservationTable=hm2AgentDot1qMsrpReservationTable, hm2AgentDot1qMrpMsrpPortPktTxFailure=hm2AgentDot1qMrpMsrpPortPktTxFailure, hm2AgentDot1qMrpMsrpPortPktRxBadHeader=hm2AgentDot1qMrpMsrpPortPktRxBadHeader, hm2AgentDot1qMrpMsrpIntf=hm2AgentDot1qMrpMsrpIntf, hm2AgentDot1qMsrpReservationDeclarationType=hm2AgentDot1qMsrpReservationDeclarationType, hm2AgentDot1qMsrpReservationDroppedStreamFrames=hm2AgentDot1qMsrpReservationDroppedStreamFrames, hm2AgentDot1qMrpMsrpPortPktRx=hm2AgentDot1qMrpMsrpPortPktRx, hm2AgentDot1qFqtssAdminIdleSlopeLs=hm2AgentDot1qFqtssAdminIdleSlopeLs, hm2AgentDot1qMrpMsrpPortPktRegFailure=hm2AgentDot1qMrpMsrpPortPktRegFailure, hm2AgentDot1qFqtssSrpBoundaryPort=hm2AgentDot1qFqtssSrpBoundaryPort, Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue=Hm2AgentDot1qFtqssTxSelectionAlgorithmIDValue, hm2AgentDot1qMrpMsrpPortPktRxBadFormat=hm2AgentDot1qMrpMsrpPortPktRxBadFormat, hm2AgentDot1qMsrpStreamDestMacAddr=hm2AgentDot1qMsrpStreamDestMacAddr, hm2AgentDot1qMrpMsrpPktMessageFailure=hm2AgentDot1qMrpMsrpPktMessageFailure, hm2AgentDot1qMsrpReservationDirection=hm2AgentDot1qMsrpReservationDirection, Hm2AgentDot1qPriorityValue=Hm2AgentDot1qPriorityValue, Hm2AgentDot1qFqtssTrafficClassValue=Hm2AgentDot1qFqtssTrafficClassValue, PYSNMP_MODULE_ID=hm2PlatformMSRP, Hm2AgentDot1qMsrpReservationDeclarationTypeValue=Hm2AgentDot1qMsrpReservationDeclarationTypeValue, hm2AgentDot1qPortMsrpPvid=hm2AgentDot1qPortMsrpPvid, hm2AgentDot1qPortMsrpFailedRegistrations=hm2AgentDot1qPortMsrpFailedRegistrations, hm2AgentDot1qFqtssTxSelectionAlgorithmID=hm2AgentDot1qFqtssTxSelectionAlgorithmID, hm2AgentDot1qMsrpStreamIndex=hm2AgentDot1qMsrpStreamIndex)
