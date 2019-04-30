#
# PySNMP MIB module DOT3-EPON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DOT3-EPON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:39:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, Integer32, TimeTicks, Bits, Counter64, iso, mib_2, MibIdentifier, ModuleIdentity, NotificationType, Unsigned32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "Integer32", "TimeTicks", "Bits", "Counter64", "iso", "mib-2", "MibIdentifier", "ModuleIdentity", "NotificationType", "Unsigned32", "Counter32", "ObjectIdentity")
TruthValue, DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "MacAddress", "TextualConvention")
dot3EponMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 155))
dot3EponMIB.setRevisions(('2007-03-29 00:00',))
if mibBuilder.loadTexts: dot3EponMIB.setLastUpdated('200703290000Z')
if mibBuilder.loadTexts: dot3EponMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
dot3EponObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 155, 1))
dot3EponConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 155, 2))
dot3EponMpcpObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 155, 1, 1))
dot3MpcpControlTable = MibTable((1, 3, 6, 1, 2, 1, 155, 1, 1, 1), )
if mibBuilder.loadTexts: dot3MpcpControlTable.setStatus('current')
dot3MpcpControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3MpcpControlEntry.setStatus('current')
dot3MpcpOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpOperStatus.setStatus('current')
dot3MpcpAdminState = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3MpcpAdminState.setStatus('current')
dot3MpcpMode = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("olt", 1), ("onu", 2))).clone('olt')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpMode.setStatus('current')
dot3MpcpSyncTime = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 4), Unsigned32()).setUnits('TQ (16nsec)').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpSyncTime.setStatus('current')
dot3MpcpLinkID = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpLinkID.setStatus('current')
dot3MpcpRemoteMACAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpRemoteMACAddress.setStatus('current')
dot3MpcpRegistrationState = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unregistered", 1), ("registering", 2), ("registered", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpRegistrationState.setStatus('current')
dot3MpcpTransmitElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 8), Unsigned32()).setUnits('TQ (16nsec)').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpTransmitElapsed.setStatus('current')
dot3MpcpReceiveElapsed = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 9), Unsigned32()).setUnits('TQ (16nsec)').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpReceiveElapsed.setStatus('current')
dot3MpcpRoundTripTime = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('TQ (16nsec)').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpRoundTripTime.setStatus('current')
dot3MpcpMaximumPendingGrants = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpMaximumPendingGrants.setStatus('current')
dot3MpcpStatTable = MibTable((1, 3, 6, 1, 2, 1, 155, 1, 1, 2), )
if mibBuilder.loadTexts: dot3MpcpStatTable.setStatus('current')
dot3MpcpStatEntry = MibTableRow((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3MpcpStatEntry.setStatus('current')
dot3MpcpMACCtrlFramesTransmitted = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 1), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpMACCtrlFramesTransmitted.setStatus('current')
dot3MpcpMACCtrlFramesReceived = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 2), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpMACCtrlFramesReceived.setStatus('current')
dot3MpcpDiscoveryWindowsSent = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpDiscoveryWindowsSent.setStatus('current')
dot3MpcpDiscoveryTimeout = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpDiscoveryTimeout.setStatus('current')
dot3MpcpTxRegRequest = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 5), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpTxRegRequest.setStatus('current')
dot3MpcpRxRegRequest = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 6), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpRxRegRequest.setStatus('current')
dot3MpcpTxRegAck = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 7), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpTxRegAck.setStatus('current')
dot3MpcpRxRegAck = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 8), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpRxRegAck.setStatus('current')
dot3MpcpTxReport = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 9), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpTxReport.setStatus('current')
dot3MpcpRxReport = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 10), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpRxReport.setStatus('current')
dot3MpcpTxGate = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 11), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpTxGate.setStatus('current')
dot3MpcpRxGate = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 12), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpRxGate.setStatus('current')
dot3MpcpTxRegister = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 13), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpTxRegister.setStatus('current')
dot3MpcpRxRegister = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 1, 2, 1, 14), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3MpcpRxRegister.setStatus('current')
dot3OmpEmulationObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 155, 1, 2))
dot3OmpEmulationTable = MibTable((1, 3, 6, 1, 2, 1, 155, 1, 2, 1), )
if mibBuilder.loadTexts: dot3OmpEmulationTable.setStatus('current')
dot3OmpEmulationEntry = MibTableRow((1, 3, 6, 1, 2, 1, 155, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3OmpEmulationEntry.setStatus('current')
dot3OmpEmulationType = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("olt", 2), ("onu", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationType.setStatus('current')
dot3OmpEmulationStatTable = MibTable((1, 3, 6, 1, 2, 1, 155, 1, 2, 2), )
if mibBuilder.loadTexts: dot3OmpEmulationStatTable.setStatus('current')
dot3OmpEmulationStatEntry = MibTableRow((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3OmpEmulationStatEntry.setStatus('current')
dot3OmpEmulationSLDErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 1), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationSLDErrors.setStatus('current')
dot3OmpEmulationCRC8Errors = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 2), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationCRC8Errors.setStatus('current')
dot3OmpEmulationBadLLID = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 3), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationBadLLID.setStatus('current')
dot3OmpEmulationGoodLLID = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 4), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationGoodLLID.setStatus('current')
dot3OmpEmulationOnuPonCastLLID = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 5), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationOnuPonCastLLID.setStatus('current')
dot3OmpEmulationOltPonCastLLID = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 6), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationOltPonCastLLID.setStatus('current')
dot3OmpEmulationBroadcastBitNotOnuLlid = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 7), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationBroadcastBitNotOnuLlid.setStatus('current')
dot3OmpEmulationOnuLLIDNotBroadcast = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 8), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationOnuLLIDNotBroadcast.setStatus('current')
dot3OmpEmulationBroadcastBitPlusOnuLlid = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 9), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationBroadcastBitPlusOnuLlid.setStatus('current')
dot3OmpEmulationNotBroadcastBitNotOnuLlid = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 2, 2, 1, 10), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3OmpEmulationNotBroadcastBitNotOnuLlid.setStatus('current')
dot3EponFecObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 155, 1, 3))
dot3EponFecTable = MibTable((1, 3, 6, 1, 2, 1, 155, 1, 3, 1), )
if mibBuilder.loadTexts: dot3EponFecTable.setStatus('current')
dot3EponFecEntry = MibTableRow((1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3EponFecEntry.setStatus('current')
dot3EponFecPCSCodingViolation = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 1), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3EponFecPCSCodingViolation.setStatus('current')
dot3EponFecAbility = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("supported", 2), ("unsupported", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3EponFecAbility.setStatus('current')
dot3EponFecMode = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("disabled", 2), ("enabled", 3))).clone('unknown')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3EponFecMode.setStatus('current')
dot3EponFecCorrectedBlocks = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3EponFecCorrectedBlocks.setStatus('current')
dot3EponFecUncorrectableBlocks = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3EponFecUncorrectableBlocks.setStatus('current')
dot3EponFecBufferHeadCodingViolation = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 3, 1, 1, 6), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3EponFecBufferHeadCodingViolation.setStatus('current')
dot3ExtPkgObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 155, 1, 4))
dot3ExtPkgControlObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 155, 1, 4, 1))
dot3ExtPkgControlTable = MibTable((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1), )
if mibBuilder.loadTexts: dot3ExtPkgControlTable.setStatus('current')
dot3ExtPkgControlEntry = MibTableRow((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3ExtPkgControlEntry.setStatus('current')
dot3ExtPkgObjectReset = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("running", 1), ("reset", 2))).clone('running')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgObjectReset.setStatus('current')
dot3ExtPkgObjectPowerDown = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 2), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgObjectPowerDown.setStatus('current')
dot3ExtPkgObjectNumberOfLLIDs = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgObjectNumberOfLLIDs.setStatus('current')
dot3ExtPkgObjectFecEnabled = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noFecEnabled", 1), ("fecTxEnabled", 2), ("fecRxEnabled", 3), ("fecTxRxEnabled", 4))).clone('noFecEnabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgObjectFecEnabled.setStatus('current')
dot3ExtPkgObjectReportMaximumNumQueues = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgObjectReportMaximumNumQueues.setStatus('current')
dot3ExtPkgObjectRegisterAction = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("register", 2), ("deregister", 3), ("reregister", 4))).clone('none')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgObjectRegisterAction.setStatus('current')
dot3ExtPkgQueueTable = MibTable((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2), )
if mibBuilder.loadTexts: dot3ExtPkgQueueTable.setStatus('current')
dot3ExtPkgQueueEntry = MibTableRow((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOT3-EPON-MIB", "dot3QueueIndex"))
if mibBuilder.loadTexts: dot3ExtPkgQueueEntry.setStatus('current')
dot3QueueIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: dot3QueueIndex.setStatus('current')
dot3ExtPkgObjectReportNumThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgObjectReportNumThreshold.setStatus('current')
dot3ExtPkgObjectReportMaximumNumThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgObjectReportMaximumNumThreshold.setStatus('current')
dot3ExtPkgStatTxFramesQueue = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 4), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgStatTxFramesQueue.setStatus('current')
dot3ExtPkgStatRxFramesQueue = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 5), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgStatRxFramesQueue.setStatus('current')
dot3ExtPkgStatDroppedFramesQueue = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 2, 1, 6), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgStatDroppedFramesQueue.setStatus('current')
dot3ExtPkgQueueSetsTable = MibTable((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 3), )
if mibBuilder.loadTexts: dot3ExtPkgQueueSetsTable.setStatus('current')
dot3ExtPkgQueueSetsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOT3-EPON-MIB", "dot3QueueSetQueueIndex"), (0, "DOT3-EPON-MIB", "dot3QueueSetIndex"))
if mibBuilder.loadTexts: dot3ExtPkgQueueSetsEntry.setStatus('current')
dot3QueueSetQueueIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: dot3QueueSetQueueIndex.setStatus('current')
dot3QueueSetIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: dot3QueueSetIndex.setStatus('current')
dot3ExtPkgObjectReportThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 3, 1, 3), Unsigned32()).setUnits('TQ (16nsec)').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgObjectReportThreshold.setStatus('current')
dot3ExtPkgOptIfTable = MibTable((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5), )
if mibBuilder.loadTexts: dot3ExtPkgOptIfTable.setStatus('current')
dot3ExtPkgOptIfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dot3ExtPkgOptIfEntry.setStatus('current')
dot3ExtPkgOptIfSuspectedFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgOptIfSuspectedFlag.setStatus('current')
dot3ExtPkgOptIfInputPower = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 2), Integer32()).setUnits('0.1 dbm').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgOptIfInputPower.setStatus('current')
dot3ExtPkgOptIfLowInputPower = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 3), Integer32()).setUnits('0.1 dbm').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgOptIfLowInputPower.setStatus('current')
dot3ExtPkgOptIfHighInputPower = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 4), Integer32()).setUnits('0.1 dbm').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgOptIfHighInputPower.setStatus('current')
dot3ExtPkgOptIfLowerInputPowerThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 5), Integer32()).setUnits('0.1 dbm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgOptIfLowerInputPowerThreshold.setStatus('current')
dot3ExtPkgOptIfUpperInputPowerThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 6), Integer32()).setUnits('0.1 dbm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgOptIfUpperInputPowerThreshold.setStatus('current')
dot3ExtPkgOptIfOutputPower = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 7), Integer32()).setUnits('0.1 dbm').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgOptIfOutputPower.setStatus('current')
dot3ExtPkgOptIfLowOutputPower = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 8), Integer32()).setUnits('0.1 dbm').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgOptIfLowOutputPower.setStatus('current')
dot3ExtPkgOptIfHighOutputPower = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 9), Integer32()).setUnits('0.1 dbm').setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgOptIfHighOutputPower.setStatus('current')
dot3ExtPkgOptIfLowerOutputPowerThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 10), Integer32()).setUnits('0.1 dbm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgOptIfLowerOutputPowerThreshold.setStatus('current')
dot3ExtPkgOptIfUpperOutputPowerThreshold = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 11), Integer32()).setUnits('0.1 dbm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgOptIfUpperOutputPowerThreshold.setStatus('current')
dot3ExtPkgOptIfSignalDetect = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 12), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgOptIfSignalDetect.setStatus('current')
dot3ExtPkgOptIfTransmitAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 13), TruthValue().clone('false')).setMaxAccess("readonly")
if mibBuilder.loadTexts: dot3ExtPkgOptIfTransmitAlarm.setStatus('current')
dot3ExtPkgOptIfTransmitEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 155, 1, 4, 1, 5, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dot3ExtPkgOptIfTransmitEnable.setStatus('current')
dot3EponGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 155, 2, 1))
dot3MpcpGroupBase = ObjectGroup((1, 3, 6, 1, 2, 1, 155, 2, 1, 1)).setObjects(("DOT3-EPON-MIB", "dot3MpcpOperStatus"), ("DOT3-EPON-MIB", "dot3MpcpAdminState"), ("DOT3-EPON-MIB", "dot3MpcpMode"), ("DOT3-EPON-MIB", "dot3MpcpSyncTime"), ("DOT3-EPON-MIB", "dot3MpcpLinkID"), ("DOT3-EPON-MIB", "dot3MpcpRemoteMACAddress"), ("DOT3-EPON-MIB", "dot3MpcpRegistrationState"), ("DOT3-EPON-MIB", "dot3MpcpMaximumPendingGrants"), ("DOT3-EPON-MIB", "dot3MpcpTransmitElapsed"), ("DOT3-EPON-MIB", "dot3MpcpReceiveElapsed"), ("DOT3-EPON-MIB", "dot3MpcpRoundTripTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3MpcpGroupBase = dot3MpcpGroupBase.setStatus('current')
dot3MpcpGroupStat = ObjectGroup((1, 3, 6, 1, 2, 1, 155, 2, 1, 2)).setObjects(("DOT3-EPON-MIB", "dot3MpcpMACCtrlFramesTransmitted"), ("DOT3-EPON-MIB", "dot3MpcpMACCtrlFramesReceived"), ("DOT3-EPON-MIB", "dot3MpcpDiscoveryWindowsSent"), ("DOT3-EPON-MIB", "dot3MpcpDiscoveryTimeout"), ("DOT3-EPON-MIB", "dot3MpcpTxRegRequest"), ("DOT3-EPON-MIB", "dot3MpcpRxRegRequest"), ("DOT3-EPON-MIB", "dot3MpcpTxRegAck"), ("DOT3-EPON-MIB", "dot3MpcpRxRegAck"), ("DOT3-EPON-MIB", "dot3MpcpTxReport"), ("DOT3-EPON-MIB", "dot3MpcpRxReport"), ("DOT3-EPON-MIB", "dot3MpcpTxGate"), ("DOT3-EPON-MIB", "dot3MpcpRxGate"), ("DOT3-EPON-MIB", "dot3MpcpTxRegister"), ("DOT3-EPON-MIB", "dot3MpcpRxRegister"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3MpcpGroupStat = dot3MpcpGroupStat.setStatus('current')
dot3OmpeGroupID = ObjectGroup((1, 3, 6, 1, 2, 1, 155, 2, 1, 3)).setObjects(("DOT3-EPON-MIB", "dot3OmpEmulationType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OmpeGroupID = dot3OmpeGroupID.setStatus('current')
dot3OmpeGroupStat = ObjectGroup((1, 3, 6, 1, 2, 1, 155, 2, 1, 4)).setObjects(("DOT3-EPON-MIB", "dot3OmpEmulationSLDErrors"), ("DOT3-EPON-MIB", "dot3OmpEmulationCRC8Errors"), ("DOT3-EPON-MIB", "dot3OmpEmulationBadLLID"), ("DOT3-EPON-MIB", "dot3OmpEmulationGoodLLID"), ("DOT3-EPON-MIB", "dot3OmpEmulationOnuPonCastLLID"), ("DOT3-EPON-MIB", "dot3OmpEmulationOltPonCastLLID"), ("DOT3-EPON-MIB", "dot3OmpEmulationBroadcastBitNotOnuLlid"), ("DOT3-EPON-MIB", "dot3OmpEmulationOnuLLIDNotBroadcast"), ("DOT3-EPON-MIB", "dot3OmpEmulationBroadcastBitPlusOnuLlid"), ("DOT3-EPON-MIB", "dot3OmpEmulationNotBroadcastBitNotOnuLlid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OmpeGroupStat = dot3OmpeGroupStat.setStatus('current')
dot3EponFecGroupAll = ObjectGroup((1, 3, 6, 1, 2, 1, 155, 2, 1, 5)).setObjects(("DOT3-EPON-MIB", "dot3EponFecPCSCodingViolation"), ("DOT3-EPON-MIB", "dot3EponFecAbility"), ("DOT3-EPON-MIB", "dot3EponFecMode"), ("DOT3-EPON-MIB", "dot3EponFecCorrectedBlocks"), ("DOT3-EPON-MIB", "dot3EponFecUncorrectableBlocks"), ("DOT3-EPON-MIB", "dot3EponFecBufferHeadCodingViolation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3EponFecGroupAll = dot3EponFecGroupAll.setStatus('current')
dot3ExtPkgGroupControl = ObjectGroup((1, 3, 6, 1, 2, 1, 155, 2, 1, 6)).setObjects(("DOT3-EPON-MIB", "dot3ExtPkgObjectReset"), ("DOT3-EPON-MIB", "dot3ExtPkgObjectPowerDown"), ("DOT3-EPON-MIB", "dot3ExtPkgObjectNumberOfLLIDs"), ("DOT3-EPON-MIB", "dot3ExtPkgObjectFecEnabled"), ("DOT3-EPON-MIB", "dot3ExtPkgObjectReportMaximumNumQueues"), ("DOT3-EPON-MIB", "dot3ExtPkgObjectRegisterAction"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3ExtPkgGroupControl = dot3ExtPkgGroupControl.setStatus('current')
dot3ExtPkgGroupQueue = ObjectGroup((1, 3, 6, 1, 2, 1, 155, 2, 1, 7)).setObjects(("DOT3-EPON-MIB", "dot3ExtPkgObjectReportNumThreshold"), ("DOT3-EPON-MIB", "dot3ExtPkgObjectReportMaximumNumThreshold"), ("DOT3-EPON-MIB", "dot3ExtPkgStatTxFramesQueue"), ("DOT3-EPON-MIB", "dot3ExtPkgStatRxFramesQueue"), ("DOT3-EPON-MIB", "dot3ExtPkgStatDroppedFramesQueue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3ExtPkgGroupQueue = dot3ExtPkgGroupQueue.setStatus('current')
dot3ExtPkgGroupQueueSets = ObjectGroup((1, 3, 6, 1, 2, 1, 155, 2, 1, 8)).setObjects(("DOT3-EPON-MIB", "dot3ExtPkgObjectReportThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3ExtPkgGroupQueueSets = dot3ExtPkgGroupQueueSets.setStatus('current')
dot3ExtPkgGroupOptIf = ObjectGroup((1, 3, 6, 1, 2, 1, 155, 2, 1, 9)).setObjects(("DOT3-EPON-MIB", "dot3ExtPkgOptIfSuspectedFlag"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfInputPower"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfLowInputPower"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfHighInputPower"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfLowerInputPowerThreshold"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfUpperInputPowerThreshold"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfOutputPower"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfLowOutputPower"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfHighOutputPower"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfLowerOutputPowerThreshold"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfUpperOutputPowerThreshold"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfSignalDetect"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfTransmitAlarm"), ("DOT3-EPON-MIB", "dot3ExtPkgOptIfTransmitEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3ExtPkgGroupOptIf = dot3ExtPkgGroupOptIf.setStatus('current')
dot3EponCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 155, 2, 2))
dot3MPCPCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 155, 2, 2, 1)).setObjects(("DOT3-EPON-MIB", "dot3MpcpGroupBase"), ("DOT3-EPON-MIB", "dot3MpcpGroupStat"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3MPCPCompliance = dot3MPCPCompliance.setStatus('current')
dot3OmpeCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 155, 2, 2, 2)).setObjects(("DOT3-EPON-MIB", "dot3OmpeGroupID"), ("DOT3-EPON-MIB", "dot3OmpeGroupStat"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3OmpeCompliance = dot3OmpeCompliance.setStatus('current')
dot3EponFecCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 155, 2, 2, 3)).setObjects(("DOT3-EPON-MIB", "dot3EponFecGroupAll"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3EponFecCompliance = dot3EponFecCompliance.setStatus('current')
dot3ExtPkgCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 155, 2, 2, 4)).setObjects(("DOT3-EPON-MIB", "dot3ExtPkgGroupControl"), ("DOT3-EPON-MIB", "dot3ExtPkgGroupQueue"), ("DOT3-EPON-MIB", "dot3ExtPkgGroupQueueSets"), ("DOT3-EPON-MIB", "dot3ExtPkgGroupOptIf"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dot3ExtPkgCompliance = dot3ExtPkgCompliance.setStatus('current')
mibBuilder.exportSymbols("DOT3-EPON-MIB", dot3QueueSetIndex=dot3QueueSetIndex, dot3OmpEmulationOnuPonCastLLID=dot3OmpEmulationOnuPonCastLLID, dot3MpcpRxGate=dot3MpcpRxGate, dot3ExtPkgQueueSetsTable=dot3ExtPkgQueueSetsTable, dot3MpcpRxRegAck=dot3MpcpRxRegAck, dot3OmpEmulationStatEntry=dot3OmpEmulationStatEntry, dot3OmpeGroupStat=dot3OmpeGroupStat, dot3OmpEmulationStatTable=dot3OmpEmulationStatTable, dot3OmpEmulationBadLLID=dot3OmpEmulationBadLLID, dot3EponFecTable=dot3EponFecTable, dot3OmpeGroupID=dot3OmpeGroupID, dot3QueueIndex=dot3QueueIndex, dot3EponGroups=dot3EponGroups, dot3OmpEmulationEntry=dot3OmpEmulationEntry, dot3OmpEmulationGoodLLID=dot3OmpEmulationGoodLLID, dot3MpcpTxRegAck=dot3MpcpTxRegAck, dot3MpcpRemoteMACAddress=dot3MpcpRemoteMACAddress, dot3MpcpRxRegister=dot3MpcpRxRegister, dot3ExtPkgGroupQueue=dot3ExtPkgGroupQueue, dot3ExtPkgOptIfLowInputPower=dot3ExtPkgOptIfLowInputPower, dot3MpcpTransmitElapsed=dot3MpcpTransmitElapsed, dot3ExtPkgQueueEntry=dot3ExtPkgQueueEntry, dot3ExtPkgStatRxFramesQueue=dot3ExtPkgStatRxFramesQueue, dot3MpcpDiscoveryTimeout=dot3MpcpDiscoveryTimeout, dot3ExtPkgQueueSetsEntry=dot3ExtPkgQueueSetsEntry, dot3MpcpRegistrationState=dot3MpcpRegistrationState, dot3ExtPkgObjectRegisterAction=dot3ExtPkgObjectRegisterAction, dot3MpcpTxReport=dot3MpcpTxReport, dot3EponFecBufferHeadCodingViolation=dot3EponFecBufferHeadCodingViolation, dot3EponCompliances=dot3EponCompliances, dot3MpcpRoundTripTime=dot3MpcpRoundTripTime, dot3ExtPkgObjectReportMaximumNumQueues=dot3ExtPkgObjectReportMaximumNumQueues, dot3ExtPkgControlEntry=dot3ExtPkgControlEntry, dot3ExtPkgCompliance=dot3ExtPkgCompliance, dot3ExtPkgStatTxFramesQueue=dot3ExtPkgStatTxFramesQueue, dot3ExtPkgOptIfHighInputPower=dot3ExtPkgOptIfHighInputPower, dot3MpcpControlEntry=dot3MpcpControlEntry, dot3ExtPkgStatDroppedFramesQueue=dot3ExtPkgStatDroppedFramesQueue, dot3ExtPkgControlObjects=dot3ExtPkgControlObjects, dot3ExtPkgControlTable=dot3ExtPkgControlTable, dot3EponFecAbility=dot3EponFecAbility, dot3MpcpRxReport=dot3MpcpRxReport, dot3EponObjects=dot3EponObjects, dot3MpcpAdminState=dot3MpcpAdminState, dot3EponFecUncorrectableBlocks=dot3EponFecUncorrectableBlocks, dot3ExtPkgObjectReportNumThreshold=dot3ExtPkgObjectReportNumThreshold, dot3ExtPkgOptIfLowerOutputPowerThreshold=dot3ExtPkgOptIfLowerOutputPowerThreshold, dot3ExtPkgObjectReportMaximumNumThreshold=dot3ExtPkgObjectReportMaximumNumThreshold, dot3ExtPkgOptIfOutputPower=dot3ExtPkgOptIfOutputPower, dot3MpcpMACCtrlFramesReceived=dot3MpcpMACCtrlFramesReceived, dot3ExtPkgOptIfTransmitAlarm=dot3ExtPkgOptIfTransmitAlarm, dot3OmpEmulationNotBroadcastBitNotOnuLlid=dot3OmpEmulationNotBroadcastBitNotOnuLlid, dot3MpcpMACCtrlFramesTransmitted=dot3MpcpMACCtrlFramesTransmitted, dot3MpcpMode=dot3MpcpMode, dot3MpcpGroupStat=dot3MpcpGroupStat, dot3MpcpGroupBase=dot3MpcpGroupBase, dot3OmpEmulationType=dot3OmpEmulationType, dot3ExtPkgGroupControl=dot3ExtPkgGroupControl, dot3MpcpTxRegRequest=dot3MpcpTxRegRequest, dot3MPCPCompliance=dot3MPCPCompliance, dot3ExtPkgGroupQueueSets=dot3ExtPkgGroupQueueSets, dot3MpcpSyncTime=dot3MpcpSyncTime, dot3ExtPkgOptIfEntry=dot3ExtPkgOptIfEntry, dot3ExtPkgOptIfUpperOutputPowerThreshold=dot3ExtPkgOptIfUpperOutputPowerThreshold, dot3MpcpMaximumPendingGrants=dot3MpcpMaximumPendingGrants, dot3ExtPkgObjects=dot3ExtPkgObjects, dot3ExtPkgOptIfLowerInputPowerThreshold=dot3ExtPkgOptIfLowerInputPowerThreshold, dot3MpcpTxRegister=dot3MpcpTxRegister, dot3OmpeCompliance=dot3OmpeCompliance, dot3EponConformance=dot3EponConformance, dot3QueueSetQueueIndex=dot3QueueSetQueueIndex, dot3ExtPkgObjectReportThreshold=dot3ExtPkgObjectReportThreshold, dot3ExtPkgObjectPowerDown=dot3ExtPkgObjectPowerDown, dot3MpcpControlTable=dot3MpcpControlTable, dot3OmpEmulationBroadcastBitPlusOnuLlid=dot3OmpEmulationBroadcastBitPlusOnuLlid, dot3OmpEmulationBroadcastBitNotOnuLlid=dot3OmpEmulationBroadcastBitNotOnuLlid, dot3ExtPkgOptIfSuspectedFlag=dot3ExtPkgOptIfSuspectedFlag, dot3ExtPkgOptIfInputPower=dot3ExtPkgOptIfInputPower, dot3EponFecGroupAll=dot3EponFecGroupAll, dot3EponMIB=dot3EponMIB, dot3ExtPkgObjectNumberOfLLIDs=dot3ExtPkgObjectNumberOfLLIDs, dot3EponMpcpObjects=dot3EponMpcpObjects, dot3MpcpDiscoveryWindowsSent=dot3MpcpDiscoveryWindowsSent, dot3EponFecEntry=dot3EponFecEntry, dot3OmpEmulationOnuLLIDNotBroadcast=dot3OmpEmulationOnuLLIDNotBroadcast, dot3EponFecPCSCodingViolation=dot3EponFecPCSCodingViolation, dot3OmpEmulationSLDErrors=dot3OmpEmulationSLDErrors, dot3ExtPkgObjectFecEnabled=dot3ExtPkgObjectFecEnabled, dot3ExtPkgGroupOptIf=dot3ExtPkgGroupOptIf, dot3EponFecObjects=dot3EponFecObjects, dot3ExtPkgOptIfUpperInputPowerThreshold=dot3ExtPkgOptIfUpperInputPowerThreshold, dot3EponFecCorrectedBlocks=dot3EponFecCorrectedBlocks, dot3MpcpReceiveElapsed=dot3MpcpReceiveElapsed, dot3OmpEmulationObjects=dot3OmpEmulationObjects, dot3MpcpRxRegRequest=dot3MpcpRxRegRequest, dot3OmpEmulationTable=dot3OmpEmulationTable, dot3EponFecMode=dot3EponFecMode, PYSNMP_MODULE_ID=dot3EponMIB, dot3MpcpLinkID=dot3MpcpLinkID, dot3ExtPkgQueueTable=dot3ExtPkgQueueTable, dot3ExtPkgOptIfTransmitEnable=dot3ExtPkgOptIfTransmitEnable, dot3ExtPkgOptIfLowOutputPower=dot3ExtPkgOptIfLowOutputPower, dot3EponFecCompliance=dot3EponFecCompliance, dot3ExtPkgObjectReset=dot3ExtPkgObjectReset, dot3MpcpTxGate=dot3MpcpTxGate, dot3OmpEmulationOltPonCastLLID=dot3OmpEmulationOltPonCastLLID, dot3OmpEmulationCRC8Errors=dot3OmpEmulationCRC8Errors, dot3ExtPkgOptIfHighOutputPower=dot3ExtPkgOptIfHighOutputPower, dot3MpcpOperStatus=dot3MpcpOperStatus, dot3MpcpStatTable=dot3MpcpStatTable, dot3ExtPkgOptIfTable=dot3ExtPkgOptIfTable, dot3ExtPkgOptIfSignalDetect=dot3ExtPkgOptIfSignalDetect, dot3MpcpStatEntry=dot3MpcpStatEntry)