#
# PySNMP MIB module CXTokenBus-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXTokenBus-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:33:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
SapIndex, Alias, cxTokenBus = mibBuilder.importSymbols("CXProduct-SMI", "SapIndex", "Alias", "cxTokenBus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, TimeTicks, Counter64, NotificationType, iso, MibIdentifier, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "TimeTicks", "Counter64", "NotificationType", "iso", "MibIdentifier", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tbSapTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1), )
if mibBuilder.loadTexts: tbSapTable.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapTable.setDescription('A table containing configuration information about each LLC service access point.')
tbSapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1), ).setIndexNames((0, "CXTokenBus-MIB", "tbSapNumber"))
if mibBuilder.loadTexts: tbSapEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapEntry.setDescription('The parameters for a particular frame relay module service access point.')
tbSapNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 1), SapIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbSapNumber.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapNumber.setDescription('This object serves to identify the service access point by a numerical value.')
tbSapRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("invalid", 1), ("valid", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbSapRowStatus.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapRowStatus.setDescription("Indicates whether the particular service access point is configured within the MIB. Service access point entries (rows) may be created by setting this object value to 'valid', or deleted by changing this object value to 'invalid'. Options: invalid (1) valid (2)")
tbSapAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 3), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbSapAlias.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapAlias.setDescription('Identifies the service access point by a textual name. Names are unique per service access point.')
tbSapCompanionAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 4), Alias().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbSapCompanionAlias.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapCompanionAlias.setDescription('Identifies the remote service access point that will communicate with this service access point by a textual name. Names are unique per service access point.')
tbSapType = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2))).clone(namedValues=NamedValues(("upper", 2))).clone('upper')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbSapType.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapType.setDescription("This object serves to identify the service access point by type: 'lower' or 'upper'. In our case, only upper is relevent but this object is kept for uniformity with the other Sap definition in the system")
tbSapStatGathering = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbSapStatGathering.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapStatGathering.setDescription('This object specifies if the SAP statistics will be updated. If disabled, the counter will always be zero.')
tbSapStatRxUnitDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbSapStatRxUnitDataFrames.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapStatRxUnitDataFrames.setDescription('Indicates the number of data frames received from the upper layer which requested no acknowledgment from the destination token bus module.')
tbSapStatRxUnitDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbSapStatRxUnitDataOctets.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapStatRxUnitDataOctets.setDescription('Indicates the number of data octets received from the upper layer which requested no acknowledgment from the destination token bus module.')
tbSapStatRxDataAckFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbSapStatRxDataAckFrames.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapStatRxDataAckFrames.setDescription('Indicates the number of data frames received from the upper layer which requested an acknowledgment from the destination token bus module.')
tbSapStatRxDataAckOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbSapStatRxDataAckOctets.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapStatRxDataAckOctets.setDescription('Indicates the number of data octets received from the upper layer which requested an acknowledgment from the destination token bus module.')
tbSapStatTxUnitDataFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbSapStatTxUnitDataFrames.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapStatTxUnitDataFrames.setDescription('Indicates the number of data frames sent to the upper layer where the originating card did not request an acknowledgment.')
tbSapStatTxUnitDataOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbSapStatTxUnitDataOctets.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapStatTxUnitDataOctets.setDescription('Indicates the number of data octets sent to the upper layer where the originating card did not request an acknowledgment.')
tbSapStatTxDataAckFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbSapStatTxDataAckFrames.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapStatTxDataAckFrames.setDescription('Indicates the number of data frames sent to the upper layer where the originating card requested an acknowledgment.')
tbSapStatTxDataAckOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbSapStatTxDataAckOctets.setStatus('mandatory')
if mibBuilder.loadTexts: tbSapStatTxDataAckOctets.setDescription('Indicates the number of data octets sent to the upper layer where the originating card requested an acknowledgment.')
tbDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2))
tbDevPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 1), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbDevPollingInterval.setStatus('mandatory')
if mibBuilder.loadTexts: tbDevPollingInterval.setDescription('This determine how often the Token Bus Device will be polled for transmission completion and frame reception. This value is in millisecond. If this value is 0, the token bus module is waiting for an external polling message. This is the case in special test software only.')
tbRxFrameDescriptors = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 2), Integer32().clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbRxFrameDescriptors.setStatus('mandatory')
if mibBuilder.loadTexts: tbRxFrameDescriptors.setDescription('Number of frame descriptors allocated to the token bus device (MC68824) to perform the receive process.')
tbRxBufferDescriptors = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 3), Integer32().clone(320)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbRxBufferDescriptors.setStatus('mandatory')
if mibBuilder.loadTexts: tbRxBufferDescriptors.setDescription('Number of buffer descriptors allocated to the token bus device (MC68824) to perform the receive process.')
tbTxFrameDescriptors = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 4), Integer32().clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbTxFrameDescriptors.setStatus('mandatory')
if mibBuilder.loadTexts: tbTxFrameDescriptors.setDescription('Number of frame descriptors allocated to the token bus device (MC68824) to perform the transmission process.')
tbTxBufferDescriptors = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 5), Integer32().clone(160)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbTxBufferDescriptors.setStatus('mandatory')
if mibBuilder.loadTexts: tbTxBufferDescriptors.setDescription('Number of buffer descriptors allocated to the token bus device (MC68824) to perform the transmission process.')
tbMaxFrameSizeClass6 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbMaxFrameSizeClass6.setStatus('mandatory')
if mibBuilder.loadTexts: tbMaxFrameSizeClass6.setDescription('Maximum frame size permit to be transmitted at the access class 6. This maximum must be enforced to guaranty the maximum token rotation time specified above.')
tbMaxFrameSizeClass4 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbMaxFrameSizeClass4.setStatus('mandatory')
if mibBuilder.loadTexts: tbMaxFrameSizeClass4.setDescription('Maximum frame size permit to be transmitted at the access class 4.')
tbMaxFrameSizeClass2 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbMaxFrameSizeClass2.setStatus('mandatory')
if mibBuilder.loadTexts: tbMaxFrameSizeClass2.setDescription('Maximum frame size permit to be transmitted at the access class 2.')
tbMaxFrameSizeClass0 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbMaxFrameSizeClass0.setStatus('mandatory')
if mibBuilder.loadTexts: tbMaxFrameSizeClass0.setDescription('Maximum frame size permit to be transmitted at the access class 0.')
tbHiPriorityTokenHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)).clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbHiPriorityTokenHoldTime.setStatus('mandatory')
if mibBuilder.loadTexts: tbHiPriorityTokenHoldTime.setDescription('Maximum time a station can hold the token to transmit frame at the highest priority (access class 6). The value to configure may be calculated with this formula: tbHiPriorityTokenHoldTime=(target rotation time(sec)) * Bus Clock frequency ------------------------------------------------- number of card * 64')
tbTargetRotationTimeClass4 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767)).clone(480)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbTargetRotationTimeClass4.setStatus('mandatory')
if mibBuilder.loadTexts: tbTargetRotationTimeClass4.setDescription('This parameter defines the target rotation time for the access class 4. The value to configure may be calculated with this formula: tbTargetRotationTimeClass4=(target rotation time(sec)) * Bus Clock frequency ------------------------------------------------- 64')
tbTargetRotationTimeClass2 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767)).clone(384)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbTargetRotationTimeClass2.setStatus('mandatory')
if mibBuilder.loadTexts: tbTargetRotationTimeClass2.setDescription('This parameter defines the target rotation time for the access class 2. The value to configure may be calculated with this formula: tbTargetRotationTimeClass2=(target rotation time(sec)) * Bus Clock frequency ------------------------------------------------ 64')
tbTargetRotationTimeClass0 = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767)).clone(288)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbTargetRotationTimeClass0.setStatus('mandatory')
if mibBuilder.loadTexts: tbTargetRotationTimeClass0.setDescription('This parameter defines the target rotation time for the access class 0. The value to configure may be calculated with this formula: tbTargetRotationTimeClass0=(target rotation time(sec)) * Bus Clock frequency ------------------------------------------------- 64')
tbTargetRotationForMaintenance = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32767)).clone(288)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbTargetRotationForMaintenance.setStatus('mandatory')
if mibBuilder.loadTexts: tbTargetRotationForMaintenance.setDescription('This parameter defines the target rotation time for the ring maintenance. The value to configure may be calculated with this formula: tbTargetRotationorMaintenance = target rotation time(sec)) * Bus Clock frequency ------------------------------------------------ 64')
tbMaxInterSolicitCount = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(16, 255)).clone(32)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbMaxInterSolicitCount.setStatus('mandatory')
if mibBuilder.loadTexts: tbMaxInterSolicitCount.setDescription('This parameter defines the target rotation time for the ring maintenance. The value to configure may be calculated with this formula: tbTimeForMaintenance = (target rotation time(sec)) * Bus Clock frequency ------------------------------------------------- 64')
tbNonRwrMaxRetryLimit = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbNonRwrMaxRetryLimit.setStatus('mandatory')
if mibBuilder.loadTexts: tbNonRwrMaxRetryLimit.setDescription('This parameter specifies how many times the MC68824 chip set will try to retransmit a request with no response (RWNR) frame on which it detected a transmission failure.')
tbRwrMaxRetryLimit = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbRwrMaxRetryLimit.setStatus('mandatory')
if mibBuilder.loadTexts: tbRwrMaxRetryLimit.setDescription('This parameter specifies how many time the MC68824 chip set will try to retransmit a request with response (RWR) frame on which it detected a transmission failure through a lack of response.')
tbSlotTime = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 8191)).clone(256)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tbSlotTime.setStatus('mandatory')
if mibBuilder.loadTexts: tbSlotTime.setDescription('This parameter specifies how much time the MC68824 chip set will wait for a response on a transmission a request with response (RWR) frame. This parameter must be specified in octet time.')
tbTxNonRwrFailures = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbTxNonRwrFailures.setStatus('mandatory')
if mibBuilder.loadTexts: tbTxNonRwrFailures.setDescription('Number of transmission failures related to the request with no response frames.')
tbTxRwrFailures = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbTxRwrFailures.setStatus('mandatory')
if mibBuilder.loadTexts: tbTxRwrFailures.setDescription('Number of transmission failure related to the request with response frames.')
tbUnexpectedFrame6s = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbUnexpectedFrame6s.setStatus('mandatory')
if mibBuilder.loadTexts: tbUnexpectedFrame6s.setDescription('This counter incrementes when the TBC hears an unexpected frame when expecting a response to a transmitted request with response frame. An unexpected frame in this case is any valid frame which is not a response frame addressed to this station. Upon detecting this event, the TBC increment this counter and goes to the IDLE without passing the token.')
tbUnexpectedFrame10s = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbUnexpectedFrame10s.setStatus('mandatory')
if mibBuilder.loadTexts: tbUnexpectedFrame10s.setDescription("The TBC module incremented this counter when it executes the 'unexpected frame 10' transition the IEEE 802.4 access control machine (ACM). It occurs when the TBC attempted to solicit a new successor and while waiting for a response, heard either a data frame not sent by itself. When this event occurs, it indicates a protocol error, possibly a duplicate token situation. After this event, The TBC will go to the IDLE without passing the token.")
tbNbUnderruns = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbNbUnderruns.setStatus('mandatory')
if mibBuilder.loadTexts: tbNbUnderruns.setDescription('This statistic represents the number of times the TBC detected a FIFO underrun during transmission.')
tbRxRetryRwrFrames = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbRxRetryRwrFrames.setStatus('mandatory')
if mibBuilder.loadTexts: tbRxRetryRwrFrames.setDescription('Number of detected retransmitted request with response frame. This event mostly occurs when the RWR frame or its response is lost.')
tbRxNullLsduRwrFrames = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbRxNullLsduRwrFrames.setStatus('mandatory')
if mibBuilder.loadTexts: tbRxNullLsduRwrFrames.setDescription('Number of received request with response frame which did not contain any LLC service data unit (LDSU).')
tbNbPassedTokens = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbNbPassedTokens.setStatus('mandatory')
if mibBuilder.loadTexts: tbNbPassedTokens.setDescription('Number of time this station thinks it has sucessfully passed the token. It can be used to calculate the average token rotation time.')
tbNbHeardTokens = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbNbHeardTokens.setStatus('mandatory')
if mibBuilder.loadTexts: tbNbHeardTokens.setDescription('Number of time this station heard a token where Destination Address (DA) or Source Address (SA) are not equal to This Station (TS) address. This number can be used to determine how many stations there is on the logical ring.')
tbNbNoSuccessor8Passes = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbNbNoSuccessor8Passes.setStatus('mandatory')
if mibBuilder.loadTexts: tbNbNoSuccessor8Passes.setDescription("This statistic indicates the number of times this station has gone through the no successor 8 arc in the state machine. This happens when the TBC fails to pass the token and does not succeed in finding a new successor station. The counter is incremented only if the TBC thinks it is not the only active station in the network. A significantly large value in this counter may indicate a 'faulty' transmitter condition in this station.")
tbNbWhoFollowsFrames = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbNbWhoFollowsFrames.setStatus('mandatory')
if mibBuilder.loadTexts: tbNbWhoFollowsFrames.setDescription("This statistic is the number of times this station has had to look for a new next station to pass the token to. This frame is sent as part of the TBC's effort to pass the token to its former successor's successor if the original successor station does not respond to the token. This counter is incremented by two every time a failure occurs.")
tbNbTokenPassFailures = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbNbTokenPassFailures.setStatus('mandatory')
if mibBuilder.loadTexts: tbNbTokenPassFailures.setDescription('This statistic indicates the number of token pass failed transitions when pass state is equal to pass token. Upon failing to pass the token, the TBC tries to send a second token (pass state equals repeat pass token). If this effort fails too, this counter is not incremented again; but the TBC will then send a who follows frame and the who follows query counter will be incremented.')
tbRxPeriodNonSilences = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbRxPeriodNonSilences.setStatus('mandatory')
if mibBuilder.loadTexts: tbRxPeriodNonSilences.setDescription('This statistic is the number of received periods of non-silence.')
tbRxBadCrcFrames = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbRxBadCrcFrames.setStatus('mandatory')
if mibBuilder.loadTexts: tbRxBadCrcFrames.setDescription('This statistic tracks the number of received frames with FCS (or CRC) errors and the E-bit reset.')
tbRxEBitSetFrames = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbRxEBitSetFrames.setStatus('mandatory')
if mibBuilder.loadTexts: tbRxEBitSetFrames.setDescription('This statistic counts the number of received frames with the E-bit set in the end delimiter. The E bit, or error bit, is set by the regenerative repeater (headend remodulator), when the headend detects a FCS error on the forward channel.')
tbRxFrameFragments = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbRxFrameFragments.setStatus('mandatory')
if mibBuilder.loadTexts: tbRxFrameFragments.setDescription('This statistic represents the number of frame fragments (start delimiter (SD) not followed by a valid end delimiter (ED)). A valid frame consists of only data (zero or one MAC symbols) between the SD and the ED. If an SD is detected and then, before a valid ED, the TBC detects either silence, non data (not part of the aligned ED), or bad signal, then this counter is incremented. Note that this includes abort sequences.')
tbRxFrameTooLongs = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbRxFrameTooLongs.setStatus('mandatory')
if mibBuilder.loadTexts: tbRxFrameTooLongs.setDescription('This statistic is the number of received frames tart are too long (>8 KBytes).')
tbNbNoFdBdErrors = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbNbNoFdBdErrors.setStatus('mandatory')
if mibBuilder.loadTexts: tbNbNoFdBdErrors.setDescription('This statistic counts the number of frames that were not received because there were not enough frame descriptors or there were not enough buffers.')
tbNbOverruns = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 5, 9, 2, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tbNbOverruns.setStatus('mandatory')
if mibBuilder.loadTexts: tbNbOverruns.setDescription('This statistic represents the number of times the TBC detected a FIFO overrun during receive.')
mibBuilder.exportSymbols("CXTokenBus-MIB", tbTxNonRwrFailures=tbTxNonRwrFailures, tbRxFrameDescriptors=tbRxFrameDescriptors, tbSlotTime=tbSlotTime, tbNbHeardTokens=tbNbHeardTokens, tbNonRwrMaxRetryLimit=tbNonRwrMaxRetryLimit, tbNbWhoFollowsFrames=tbNbWhoFollowsFrames, tbNbUnderruns=tbNbUnderruns, tbSapStatGathering=tbSapStatGathering, tbRxFrameFragments=tbRxFrameFragments, tbHiPriorityTokenHoldTime=tbHiPriorityTokenHoldTime, tbDevice=tbDevice, tbSapRowStatus=tbSapRowStatus, tbTargetRotationTimeClass0=tbTargetRotationTimeClass0, tbTxRwrFailures=tbTxRwrFailures, tbSapStatTxUnitDataFrames=tbSapStatTxUnitDataFrames, tbRxRetryRwrFrames=tbRxRetryRwrFrames, tbNbPassedTokens=tbNbPassedTokens, tbNbTokenPassFailures=tbNbTokenPassFailures, tbSapStatTxDataAckFrames=tbSapStatTxDataAckFrames, tbTargetRotationForMaintenance=tbTargetRotationForMaintenance, tbRxBufferDescriptors=tbRxBufferDescriptors, tbMaxInterSolicitCount=tbMaxInterSolicitCount, tbUnexpectedFrame10s=tbUnexpectedFrame10s, tbSapTable=tbSapTable, tbDevPollingInterval=tbDevPollingInterval, tbTargetRotationTimeClass2=tbTargetRotationTimeClass2, tbSapType=tbSapType, tbSapStatRxDataAckOctets=tbSapStatRxDataAckOctets, tbMaxFrameSizeClass6=tbMaxFrameSizeClass6, tbMaxFrameSizeClass0=tbMaxFrameSizeClass0, tbRxPeriodNonSilences=tbRxPeriodNonSilences, tbSapAlias=tbSapAlias, tbTargetRotationTimeClass4=tbTargetRotationTimeClass4, tbNbOverruns=tbNbOverruns, tbSapStatTxUnitDataOctets=tbSapStatTxUnitDataOctets, tbSapNumber=tbSapNumber, tbNbNoFdBdErrors=tbNbNoFdBdErrors, tbRxEBitSetFrames=tbRxEBitSetFrames, tbSapStatRxDataAckFrames=tbSapStatRxDataAckFrames, tbNbNoSuccessor8Passes=tbNbNoSuccessor8Passes, tbRxFrameTooLongs=tbRxFrameTooLongs, tbSapEntry=tbSapEntry, tbTxBufferDescriptors=tbTxBufferDescriptors, tbSapStatRxUnitDataOctets=tbSapStatRxUnitDataOctets, tbSapCompanionAlias=tbSapCompanionAlias, tbRxBadCrcFrames=tbRxBadCrcFrames, tbSapStatRxUnitDataFrames=tbSapStatRxUnitDataFrames, tbRxNullLsduRwrFrames=tbRxNullLsduRwrFrames, tbMaxFrameSizeClass2=tbMaxFrameSizeClass2, tbMaxFrameSizeClass4=tbMaxFrameSizeClass4, tbRwrMaxRetryLimit=tbRwrMaxRetryLimit, tbSapStatTxDataAckOctets=tbSapStatTxDataAckOctets, tbUnexpectedFrame6s=tbUnexpectedFrame6s, tbTxFrameDescriptors=tbTxFrameDescriptors)
