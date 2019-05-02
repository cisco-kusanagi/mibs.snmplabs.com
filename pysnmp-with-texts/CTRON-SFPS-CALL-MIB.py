#
# PySNMP MIB module CTRON-SFPS-CALL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-SFPS-CALL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:30:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
sfpsCallTableStats, sfpsSap, sfpsCallByTuple, sfpsSapAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsCallTableStats", "sfpsSap", "sfpsCallByTuple", "sfpsSapAPI")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Bits, iso, IpAddress, Counter32, Integer32, MibIdentifier, ModuleIdentity, NotificationType, TimeTicks, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Bits", "iso", "IpAddress", "Counter32", "Integer32", "MibIdentifier", "ModuleIdentity", "NotificationType", "TimeTicks", "Gauge32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class HexInteger(Integer32):
    pass

sfpsSapTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1), )
if mibBuilder.loadTexts: sfpsSapTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTable.setDescription('This table contains the registered (active) call processors indexed (indirectly) by address and address type supported.')
sfpsSapTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1), ).setIndexNames((0, "CTRON-SFPS-CALL-MIB", "sfpsSapTableTag"), (0, "CTRON-SFPS-CALL-MIB", "sfpsSapTableHash"), (0, "CTRON-SFPS-CALL-MIB", "sfpsSapTableHashIndex"))
if mibBuilder.loadTexts: sfpsSapTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableEntry.setDescription('Each entry contains information pertaining to an active call processor.')
sfpsSapTableTag = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableTag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableTag.setDescription('A type tag used to sort and index the table entries.')
sfpsSapTableHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableHash.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableHash.setDescription('A hash of the sfpsSapTableAddress used to identify the instance.')
sfpsSapTableHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableHashIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableHashIndex.setDescription('A count of the non-unique sfpsSapTableAddress hashes used to identify the instance.')
sfpsSapTableSourceCP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableSourceCP.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableSourceCP.setDescription('The name of the call processor initiating the the SAP attempts for this particular SAP load.')
sfpsSapTableDestCP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableDestCP.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableDestCP.setDescription('The destination call processor that is registered for with this source call processor for the given SAP load.')
sfpsSapTableSAP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableSAP.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableSAP.setDescription('The value of the SAP in 0x format.')
sfpsSapTableOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableOperStatus.setDescription('Displays the Current OperStatus of the SAP entry.')
sfpsSapTableAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableAdminStatus.setDescription('Displays the Current AdminStatus of the SAP entry.')
sfpsSapTableStateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableStateTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableStateTime.setDescription('Total number of SFPSElements stored in NVRAM for persistence.')
sfpsSapTableDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableDescription.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableDescription.setDescription('Text description of the entry.')
sfpsSapTableNumAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableNumAccepted.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableNumAccepted.setDescription('Number accepted by the SAP.')
sfpsSapTableNumDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableNumDropped.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableNumDropped.setDescription('Number dropped by the SAP.')
sfpsSapTableUnicastSap = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapTableUnicastSap.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableUnicastSap.setDescription('')
sfpsSapTableNVStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("unset", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapTableNVStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapTableNVStatus.setDescription('Status in NVRAM for persistence.')
sfpsSapAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("getStatus", 1), ("next", 2), ("first", 3), ("disable", 4), ("disableInNvram", 5), ("enable", 6), ("enableInNvram", 7), ("clearFromNvram", 8), ("clearAllNvram", 9), ("resetStats", 10), ("resetAllStats", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapAPIVerb.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPIVerb.setDescription('1 - getStatus -- The default verb. When the SourceCP, DestCP, and SAP info are entered, this action will get the current AdminStatus, OperStatus, and NvramStatus. (Must perform a mo_get after setting the above info to actually get the status info) 2 - next -- Move to the next Entry in the SAP Table and Get the status. If this operation is successful, the verb will stay next, else it defaults to getStatus. 3 - first -- Jump back to the First Entry in the SAP Table. 4 - disable -- Disable the Current SAP Entry. This does not effect the Status of this Entry in Nvram. 5 - disableInNvram -- Set the Current SAP Entries status to Disabled in Nvram - This does not effect the Current Admin Status for this SAP Entry. 6 - enable -- Enable the Current SAP Entry. This does not effect the Status of this Entry in Nvram. 7 - enableInNvram -- Set the Current SAP Entries status to Enabled in Nvram - This does not effect the Current Admin Status for this SAP Entry. 8 - clearFromNvram -- Clear the Current SAP Entry from Nvram (if set). 9 - clearAllNvram -- Clear all SAP Entries from Nvram. 10 - resetStats -- Resets the Accepted/Dropped Stats for the Current/Entered SAP Entry. 11 - resetAllStats -- Resets the Accepted/Dropped Stats for all SAP Entries.')
sfpsSapAPISourceCP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapAPISourceCP.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPISourceCP.setDescription('The name of the call processor initiating the the SAP attempts for this particular SAP load.')
sfpsSapAPIDestCP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapAPIDestCP.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPIDestCP.setDescription('The destination call processor that is registered for with this source call processor for the given SAP load.')
sfpsSapAPISAP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapAPISAP.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPISAP.setDescription('Enter in the SAP for the desired SAP Entry.')
sfpsSapAPINVStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3), ("unset", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPINVStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPINVStatus.setDescription('Displays the Current Admin Status of this SAP Entry saved in Nvram.')
sfpsSapAPIAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPIAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPIAdminStatus.setDescription('Displays the Current AdminStatus of the SAP Entry.')
sfpsSapAPIOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPIOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPIOperStatus.setDescription('Displays the Current OperStatus of the SAP Entry.')
sfpsSapAPINvSet = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPINvSet.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPINvSet.setDescription('Total number of entries stored in NVRAM for persistence.')
sfpsSapAPINVTotal = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsSapAPINVTotal.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPINVTotal.setDescription('Total number of entries allocated in NVRAM. The switch will always allocate enough space in NVRAM for the number of elements. That is, NvTotal will always be greater than or equal to NvSet.')
sfpsSapAPINumAccept = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPINumAccept.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPINumAccept.setDescription('')
sfpsSapAPINvDiscard = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPINvDiscard.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPINvDiscard.setDescription('')
sfpsSapAPIDefaultStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 2, 2, 2, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disable", 2), ("enable", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsSapAPIDefaultStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsSapAPIDefaultStatus.setDescription('')
sfpsCallByTupleTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1), )
if mibBuilder.loadTexts: sfpsCallByTupleTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleTable.setDescription('This table contains the call tags, and call states indexed (indirectly) by switch tuple (in port, src address, dst address)')
sfpsCallByTupleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1), ).setIndexNames((0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleInPort"), (0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleSrcHash"), (0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleDstHash"), (0, "CTRON-SFPS-CALL-MIB", "sfpsCallByTupleHashIndex"))
if mibBuilder.loadTexts: sfpsCallByTupleEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleEntry.setDescription('Each entry contains information pertaining to a call tag and its state.')
sfpsCallByTupleInPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleInPort.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleInPort.setDescription('Port of the switch on which the packet associated with this call tag was seen.')
sfpsCallByTupleSrcHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleSrcHash.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleSrcHash.setDescription('A hash of sfpsCallByTupleBotSrcAddress used to identify the instance.')
sfpsCallByTupleDstHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleDstHash.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleDstHash.setDescription('A hash of sfpsCallByTupleTopDstAddress used to identify the instance.')
sfpsCallByTupleHashIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleHashIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleHashIndex.setDescription('A count of non-unique sfpsCallByTupleSrcHash and sfpsCallByTupleDstHash pairs used to identify the instance.')
sfpsCallByTupleBotSrcType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleBotSrcType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleBotSrcType.setDescription('The source address type of the lowest known protocol layer.')
sfpsCallByTupleBotSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleBotSrcAddress.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleBotSrcAddress.setDescription('The source address value of the lowest known protocol layer.')
sfpsCallByTupleBotDstType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleBotDstType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleBotDstType.setDescription('The destination address type of the lowest known protocol layer.')
sfpsCallByTupleBotDstAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleBotDstAddress.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleBotDstAddress.setDescription('The destination address value of the lowest known protocol layer.')
sfpsCallByTupleTopSrcType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleTopSrcType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleTopSrcType.setDescription('The source address type of the highest learned protocol layer.')
sfpsCallByTupleTopSrcAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleTopSrcAddress.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleTopSrcAddress.setDescription('The source address value of the highest learned protocol layer.')
sfpsCallByTupleTopDstType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleTopDstType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleTopDstType.setDescription('The destination address type of the highest learned protocol layer.')
sfpsCallByTupleTopDstAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleTopDstAddress.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleTopDstAddress.setDescription('The destination address value of the highest learned protocol layer.')
sfpsCallByTupleCallProcName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleCallProcName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleCallProcName.setDescription('The name of the call processor responsible for all signaling for this packet/call tag.')
sfpsCallByTupleCallTag = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 14), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleCallTag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleCallTag.setDescription('The number used to reference this packet and its associated calls.')
sfpsCallByTupleCallState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleCallState.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleCallState.setDescription('The current state of the packet in the call processor.')
sfpsCallByTupleTimeRemaining = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 5, 1, 1, 16), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallByTupleTimeRemaining.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallByTupleTimeRemaining.setDescription("The number of time ticks remaining before this entry's timer expires and it is removed from the table.")
sfpsCallTableStatsRam = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsRam.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTableStatsRam.setDescription('The number of bytes used by the Call Table.')
sfpsCallTableStatsSize = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsSize.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTableStatsSize.setDescription('The number of entries in the Call Table.')
sfpsCallTableStatsInUse = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsInUse.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTableStatsInUse.setDescription('The current number of calls in use. A call goes into this table only if it is being blocked (waiting for resolve or sent new user).')
sfpsCallTableStatsMax = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsMax.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTableStatsMax.setDescription('The maximum number of calls that the switch maintained.')
sfpsCallTableStatsTotMisses = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsTotMisses.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTableStatsTotMisses.setDescription('The number of times that there were no calls available in the Call Table. This would be the number of calls that had to be dropped.')
sfpsCallTableStatsMissStart = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsMissStart.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTableStatsMissStart.setDescription('Time when last miss occurred')
sfpsCallTableStatsMissStop = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsCallTableStatsMissStop.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTableStatsMissStop.setDescription('Time when missing stopped')
sfpsCallTableStatsLastMiss = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 5, 1, 6, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsCallTableStatsLastMiss.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsCallTableStatsLastMiss.setDescription('Number of calls dropped in last miss, also write 0 to files')
mibBuilder.exportSymbols("CTRON-SFPS-CALL-MIB", sfpsSapTableNumAccepted=sfpsSapTableNumAccepted, sfpsCallByTupleTopSrcAddress=sfpsCallByTupleTopSrcAddress, sfpsSapTableDestCP=sfpsSapTableDestCP, sfpsSapTableOperStatus=sfpsSapTableOperStatus, sfpsSapTableStateTime=sfpsSapTableStateTime, sfpsSapAPINvDiscard=sfpsSapAPINvDiscard, sfpsCallTableStatsMissStart=sfpsCallTableStatsMissStart, sfpsSapTableAdminStatus=sfpsSapTableAdminStatus, sfpsCallByTupleCallState=sfpsCallByTupleCallState, sfpsCallTableStatsSize=sfpsCallTableStatsSize, sfpsSapTableNumDropped=sfpsSapTableNumDropped, sfpsSapTableHashIndex=sfpsSapTableHashIndex, sfpsSapAPINVStatus=sfpsSapAPINVStatus, sfpsCallByTupleBotDstAddress=sfpsCallByTupleBotDstAddress, sfpsSapTable=sfpsSapTable, sfpsCallByTupleEntry=sfpsCallByTupleEntry, sfpsCallTableStatsInUse=sfpsCallTableStatsInUse, sfpsCallByTupleInPort=sfpsCallByTupleInPort, sfpsCallByTupleTopDstType=sfpsCallByTupleTopDstType, sfpsCallByTupleBotSrcAddress=sfpsCallByTupleBotSrcAddress, sfpsSapTableUnicastSap=sfpsSapTableUnicastSap, sfpsSapAPIDefaultStatus=sfpsSapAPIDefaultStatus, sfpsSapTableTag=sfpsSapTableTag, sfpsCallByTupleHashIndex=sfpsCallByTupleHashIndex, sfpsSapTableNVStatus=sfpsSapTableNVStatus, sfpsSapAPIDestCP=sfpsSapAPIDestCP, sfpsCallByTupleTopDstAddress=sfpsCallByTupleTopDstAddress, sfpsCallByTupleCallTag=sfpsCallByTupleCallTag, sfpsCallTableStatsMax=sfpsCallTableStatsMax, sfpsCallTableStatsMissStop=sfpsCallTableStatsMissStop, sfpsSapAPISAP=sfpsSapAPISAP, sfpsSapTableHash=sfpsSapTableHash, sfpsSapTableDescription=sfpsSapTableDescription, sfpsSapAPIVerb=sfpsSapAPIVerb, sfpsSapAPINumAccept=sfpsSapAPINumAccept, sfpsCallTableStatsTotMisses=sfpsCallTableStatsTotMisses, sfpsCallByTupleTable=sfpsCallByTupleTable, sfpsSapAPINVTotal=sfpsSapAPINVTotal, sfpsCallByTupleTopSrcType=sfpsCallByTupleTopSrcType, sfpsSapTableSourceCP=sfpsSapTableSourceCP, sfpsSapTableEntry=sfpsSapTableEntry, sfpsCallByTupleSrcHash=sfpsCallByTupleSrcHash, sfpsCallByTupleCallProcName=sfpsCallByTupleCallProcName, sfpsSapAPIOperStatus=sfpsSapAPIOperStatus, sfpsCallByTupleDstHash=sfpsCallByTupleDstHash, sfpsCallByTupleBotSrcType=sfpsCallByTupleBotSrcType, sfpsSapTableSAP=sfpsSapTableSAP, sfpsSapAPINvSet=sfpsSapAPINvSet, sfpsCallByTupleBotDstType=sfpsCallByTupleBotDstType, sfpsSapAPISourceCP=sfpsSapAPISourceCP, HexInteger=HexInteger, sfpsCallTableStatsLastMiss=sfpsCallTableStatsLastMiss, sfpsCallTableStatsRam=sfpsCallTableStatsRam, sfpsCallByTupleTimeRemaining=sfpsCallByTupleTimeRemaining, sfpsSapAPIAdminStatus=sfpsSapAPIAdminStatus)
