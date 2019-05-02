#
# PySNMP MIB module CTRON-ISDN-CONFIGURATION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-ISDN-CONFIGURATION-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:30:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, iso, Counter32, Unsigned32, enterprises, TimeTicks, ModuleIdentity, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "iso", "Counter32", "Unsigned32", "enterprises", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

cabletron = MibIdentifier((1, 3, 6, 1, 4, 1, 52))
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4))
ctron = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1))
ctDataLink = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2))
ctronWan = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7))
ctISDNconfigMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4))
ctISDNcontrol = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1))
isdnDchTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1), )
if mibBuilder.loadTexts: isdnDchTable.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchTable.setDescription('A list of D channnel interfaces entries. The list consists of a single entry at this time.')
isdnDchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1), ).setIndexNames((0, "CTRON-ISDN-CONFIGURATION-MIB", "isdnDchIndex"))
if mibBuilder.loadTexts: isdnDchEntry.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchEntry.setDescription('A D channnel interface entry containing objects relating to the particular D channel.')
isdnDchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnDchIndex.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchIndex.setDescription('A unique index for this D Channel of this ISDN-Controller.')
isdnDchRateAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("bri1", 2), ("pri1", 3), ("pri2", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnDchRateAccess.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchRateAccess.setDescription('The Rate Access of this ISDN interface.')
isdnDchAllowedCh = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnDchAllowedCh.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchAllowedCh.setDescription('A bit string with bit 1 signifiying time slot 1. A set bit means that a B channel may be allocated on that time slot. A reset bit means the channel is reserved or otherwise out of service.')
isdnDchChInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnDchChInUse.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchChInUse.setDescription('A bit string with bit 1 signifying time slot 1. A set bit means that a B channel has been allocated on that time slot. A reset bit means the channel is available, reserved, or otherwise out of service.')
isdnDchSupportedSwitches = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 5, 10, 16, 17))).clone(namedValues=NamedValues(("bri5ESS", 2), ("bridms100", 5), ("brini1", 10), ("pri4ESS", 16), ("pri5ESS", 17)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnDchSupportedSwitches.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchSupportedSwitches.setDescription('A bit string with each bit position signifying support of a specific switch type as indicated by the list. A set bit means that that switch type is supported.')
isdnDchSwitchType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 5, 10, 16, 17))).clone(namedValues=NamedValues(("bri5ESS", 2), ("bridms100", 5), ("brini1", 10), ("pri4ESS", 16), ("pri5ESS", 17))).clone('brini1')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnDchSwitchType.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchSwitchType.setDescription('Switch type selector as indicated by the list.')
isdnDchSPID1 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 7), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnDchSPID1.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchSPID1.setDescription('The Service profile identifier for BRI channel 1.')
isdnDchSPID2 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 8), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnDchSPID2.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchSPID2.setDescription('The Service profile identifier for BRI channel 2.')
isdnDchDirNum1 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 9), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnDchDirNum1.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchDirNum1.setDescription('The local directory number for BRI channel 1.')
isdnDchDirNum2 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 10), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnDchDirNum2.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchDirNum2.setDescription('The local directory number for BRI channel 2.')
isdnDchOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnDchOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: isdnDchOperStatus.setDescription('The operational status of the signalling channel.')
dialCtlNbrCfgTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2), )
if mibBuilder.loadTexts: dialCtlNbrCfgTable.setStatus('mandatory')
if mibBuilder.loadTexts: dialCtlNbrCfgTable.setDescription('The list of neighbors from which the managed device will accept calls or to which it will place them.')
dialCtlNbrCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1), ).setIndexNames((0, "CTRON-ISDN-CONFIGURATION-MIB", "dialCtlNbrCfgId"), (0, "CTRON-ISDN-CONFIGURATION-MIB", "dialCtlNbrCfgIndex"))
if mibBuilder.loadTexts: dialCtlNbrCfgEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dialCtlNbrCfgEntry.setDescription('A single Neighbor. This entry is effectively permanent, and contains address information describing the neighbor. The value of dialCtlNbrCfgOriginateAddress must be specified before a new row in this table can become active(1). Any writeable parameters in an existing entry can be modified while the entry is active. The modification will take effect when the neighbor in question will be called the next time.')
dialCtlNbrCfgId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlNbrCfgId.setStatus('mandatory')
if mibBuilder.loadTexts: dialCtlNbrCfgId.setDescription('This object defines a single neighbor. There may be several entries in this table for one neighbor, defining different ways of reaching this neighbor. Thus, there may be several entries in this table with the same value of dialCtlNbrCfgId. Multiple entries for one neighbor may be used to support multilink as well as backup lines. A single neighbor will be identified by a unique value of this object. Several entries for one neighbor MUST have the same value of dialCtlNbrCfgId and dialCtlNbrCfgIfIndex but still different ifEntries and thus different values of dialCtlNbrCfgIndex.')
dialCtlNbrCfgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlNbrCfgIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dialCtlNbrCfgIndex.setDescription('The index value which uniquely identifies an entry in this table.')
dialCtlNbrCfgIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlNbrCfgIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: dialCtlNbrCfgIfIndex.setDescription('The ifIndex value of the interface associated with this neighbor.')
dialCtlNbrCfgOriginateAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialCtlNbrCfgOriginateAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dialCtlNbrCfgOriginateAddress.setDescription("Call Address at which the neighbor will be called. Think of this as the set of characters following 'ATDT ' or the 'phone number' included in a D channel call request. The structure of this information will be switch type specific.")
dialCtlNbrCfgAnswerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 2, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialCtlNbrCfgAnswerAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dialCtlNbrCfgAnswerAddress.setDescription('Calling Party Number information element, as for example passed in an ISDN SETUP message by a PBX or switch, for incoming calls. This address can be used to identify the neighbor. If this address is either unknown or identical to dialCtlNbrCfgOriginateAddress, this object will be a zero length string.')
rmtProfileTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3), )
if mibBuilder.loadTexts: rmtProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileTable.setDescription('The list of neighbors from which this device will accept calls or to which it will place them.')
rmtProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1), ).setIndexNames((0, "CTRON-ISDN-CONFIGURATION-MIB", "rmtProfileEntryIndex"))
if mibBuilder.loadTexts: rmtProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntry.setDescription('A single Neighbor. This entry is effectively permanent, and contains information describing the neighbor.')
rmtProfileEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rmtProfileEntryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryIndex.setDescription('The index value which uniquely identifies an entry in this table.')
rmtProfileEntryName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryName.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryName.setDescription('ASCII name of the neighbor.')
rmtProfileEntryMakerName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMakerName.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMakerName.setDescription('ASCII name of the manufacturer of the neighbor. In other words, it is a name by which to uniquely identify the remote access device to which the profile belongs.')
rmtProfileEntryAction = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("idle", 1), ("connect", 2), ("hangup", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryAction.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryAction.setDescription('Desired action for the neighbor interface')
rmtProfileEntryState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("calling", 2), ("ringing", 3), ("connected", 4), ("answering", 5), ("answered", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rmtProfileEntryState.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryState.setDescription('Current state of the neighbor interface')
rmtProfileEntryMaxNeighbor = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 6), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rmtProfileEntryMaxNeighbor.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMaxNeighbor.setDescription('The maximum allowable dialCtlNbrCfgIndex. It is the number of instances of the profile.')
rmtProfileEntryBchInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rmtProfileEntryBchInUse.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryBchInUse.setDescription('A bit string with bit 1 signifiying B channel 1. A set bit means that this channel was assigned for current or last call.')
rmtProfileEntryLinkHead = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rmtProfileEntryLinkHead.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryLinkHead.setDescription('A zero value signifies it is a primary profile. Otherwise, it is an instance profile and the value identifies the primary profile from which it was spawned.')
rmtProfileEntryNextLink = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rmtProfileEntryNextLink.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryNextLink.setDescription('A non-zero value identifies an instance profile. Whereas, a zero value either means it is a primary profile or the last instance of a primary profile.')
rmtProfileEntryMpCapable = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMpCapable.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMpCapable.setDescription('MP option selector. Set to a value of one when MP support is desired otherwise set to a value of two. The default setting is disabled. When enabled the attempt is made to negotiate MP support. Both parties must support MP to be able to successfully negotiate MP.')
rmtProfileEntryMpLineUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(50)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMpLineUtilization.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMpLineUtilization.setDescription('Used to set the Line Utilization Threshold (LUT) % to compare against the linear weighted percentage to determine when more/less bandwidth is to be added/removed. Linear weighting is computed (averaged) over the period of time specified by the rmtProfileEntryMpHistoryTime object. Additional bandwidth is added whenever the linear weighted percentage exceeds the LUT % for a consecutive number of average line utilization reading(s) (computation(s)) as specified by the rmtProfileEntryMpMoreBWSamples object. Conversely, additional possible previously added Bandwidth is removed whenever the linear weighted percentage falls below the LUT % value for a consecutive number of average line utilization reading(s) (computation(s)) as specified by the rmtProfileEntryMpLessBWSamples object.')
rmtProfileEntryMpHistoryTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMpHistoryTime.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMpHistoryTime.setDescription('Used to set the history time value in seconds for the number of line utilization reading(s)/sample(s) desired to compute the average line utilization. It specifies the window size over which to to compute the average line utilization.')
rmtProfileEntryMpMoreBWSamples = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMpMoreBWSamples.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMpMoreBWSamples.setDescription('Used to set the number of consecutive line utilization average computations that must exceed the LUT % value as specified by the rmtProfileEntryMpLineUtilization object before allowing possible more bandwidth to be added.')
rmtProfileEntryMpLessBWSamples = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMpLessBWSamples.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMpLessBWSamples.setDescription('Used to set the number of consecutive line utilization average computations that must fall below the LUT % value as specified by the rmtProfileEntryMpLineUtilization object before removing possible previously added bandwidth.')
rmtProfileEntryMpMaxCallsAllowed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMpMaxCallsAllowed.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMpMaxCallsAllowed.setDescription('Used to set the maxium number of channels an ISDN MP capable call is allowed.')
rmtProfileEntryMpCallsToAdd = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMpCallsToAdd.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMpCallsToAdd.setDescription('Used to set the number of additional channel(s) (call(s)) to increment by whenever the need for more bandwidth is determined.')
rmtProfileEntryMpCallsToRemove = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMpCallsToRemove.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMpCallsToRemove.setDescription('Used to set the number of channel(s) (call(s)) to decrement by whenever the need for possible previously added additional bandwidth is determined to no longer be needed/desired.')
rmtProfileEntryMpAvgPktSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1500)).clone(260)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMpAvgPktSize.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMpAvgPktSize.setDescription('Used to set the average packet size by which to determine when its best to split a packet. This is an attempt to minimize the amount of buffering necessary at the remote device to maintain packet sequentiality.')
rmtProfileEntryMpRmtBwCtrl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 1, 3, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rmtProfileEntryMpRmtBwCtrl.setStatus('mandatory')
if mibBuilder.loadTexts: rmtProfileEntryMpRmtBwCtrl.setDescription('MP remote bandwidth control selector. Set to a one when bandwidth changes are permitted by either side ie by both parties otherwise set to a value of two. The default setting is disabled. That is to say, only the caller is permitted to change (control) the bandwidth.')
callHistory = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2))
callHistoryTableMaxLength = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 1), Integer32().clone(50)).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryTableMaxLength.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryTableMaxLength.setDescription('The upper limit on the number of entries that the callHistoryTable may contain. When this table is full, the oldest entry will be deleted and the new one will be created.')
callHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2), )
if mibBuilder.loadTexts: callHistoryTable.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryTable.setDescription('A table containing information about specific calls to a specific destination.')
callHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1), ).setIndexNames((0, "CTRON-ISDN-CONFIGURATION-MIB", "callHistoryIndex"))
if mibBuilder.loadTexts: callHistoryEntry.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryEntry.setDescription('The information regarding a single Connection.')
callHistorySetupTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistorySetupTime.setStatus('mandatory')
if mibBuilder.loadTexts: callHistorySetupTime.setDescription('The value of system up time when the call associated to this entry was started. This will be useful for an NMS to retrieve all calls after a specific time. Also, this object can be useful in finding large delays between the time the call was started and the time the call was connected. For ISDN media, this will be the time when the setup message was received from or sent to the network.')
callHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryIndex.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryIndex.setDescription('Index variable to access the CallHistoryEntry objects of the callHistoryTable.')
callHistoryPeerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryPeerAddress.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryPeerAddress.setDescription('The number this call is connected to. If the number is not available, then it will have a length of zero.')
callHistoryNeighborId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryNeighborId.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryNeighborId.setDescription('This is the Id value of the neighbor table entry to which this call was made. If a neighbor table entry for this call does not exist, the value of this object will be zero.')
callHistoryLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryLogicalIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryLogicalIfIndex.setDescription('This is the ifIndex value of the logical interface through which this call was made.')
callHistoryDisconnectCause = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 6, 16, 17, 18, 21, 22, 28, 31, 34, 38, 41, 42, 43, 44, 52, 54, 58, 63, 65, 66, 70, 79, 81, 82, 85, 88, 90, 91, 95, 96, 97, 98, 99, 100, 111, 133, 134, 135, 136, 138))).clone(namedValues=NamedValues(("unassignedNumber", 1), ("noRouteToDestination", 2), ("channelUnacceptable", 6), ("normalCallClearing", 16), ("userBusy", 17), ("noUserResponding", 18), ("callRejected", 21), ("numberChangedAddress", 22), ("invalidNumberFormat", 28), ("normalUnspecified", 31), ("noChannelAvailable", 34), ("networkOutOfOrder", 38), ("temporaryFailure", 41), ("switchingEquipmentCongestion", 42), ("userInfoDiscarded", 43), ("requestedChannelNotAvailable", 44), ("outgoingCallsBarred", 52), ("incomingCallsBarred", 54), ("bearerCapabilityNotPresentlyAvail", 58), ("serviceNotAvailable", 63), ("bearerServiceNotImplemented", 65), ("channelTypeNotImplemented", 66), ("onlyRestrictedChannelAvailable", 70), ("serviceOrOptionNotImplemeted", 79), ("invalidCallReferenceValue", 81), ("identifiedChannelDoesNotExist", 82), ("invalidDigitValueForAddress", 85), ("incompatibleDestination", 88), ("destinationAddressMissing", 90), ("transitNetworkDoesNotExist", 91), ("invalidMessageSpecified", 95), ("mandatoryIEmissing", 96), ("messageTypeNonexistentOrNotImplemented", 97), ("messageNotCompatibleWithCallState", 98), ("iEnotImplemented", 99), ("invalidIEcontents", 100), ("protocolError", 111), ("callAlreadyActive", 133), ("lineDisabled", 134), ("badParameter", 135), ("timeoutOccured", 136), ("noCallActive", 138)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryDisconnectCause.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryDisconnectCause.setDescription('The encoded network cause value associated with this call. The value of this object will depend on the interface type as well as on the protocol and protocol version being used on this interface. The more common cause values are indicated in the list.')
callHistoryConnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryConnectTime.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryConnectTime.setDescription('The value of system up time when the call was connected.')
callHistoryDisconnectTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryDisconnectTime.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryDisconnectTime.setDescription('The value of system up time when the call was disconnected.')
callHistoryCallOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("originate", 1), ("answer", 2), ("callback", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryCallOrigin.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryCallOrigin.setDescription('The call origin.')
callHistoryInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryInfoType.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryInfoType.setDescription('The information type for this call.')
callHistoryTransmitPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryTransmitPackets.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryTransmitPackets.setDescription('The number of packets which were transmitted while this call was active.')
callHistoryTransmitBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryTransmitBytes.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryTransmitBytes.setDescription('The number of bytes which were transmitted while this call was active.')
callHistoryReceivePackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryReceivePackets.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryReceivePackets.setDescription('The number of packets which were received while this call was active.')
callHistoryReceiveBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 4, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryReceiveBytes.setStatus('mandatory')
if mibBuilder.loadTexts: callHistoryReceiveBytes.setDescription('The number of bytes which were received while this call was active.')
mibBuilder.exportSymbols("CTRON-ISDN-CONFIGURATION-MIB", callHistoryDisconnectCause=callHistoryDisconnectCause, callHistoryTableMaxLength=callHistoryTableMaxLength, isdnDchSupportedSwitches=isdnDchSupportedSwitches, rmtProfileEntryMpCapable=rmtProfileEntryMpCapable, rmtProfileEntryNextLink=rmtProfileEntryNextLink, callHistoryEntry=callHistoryEntry, cabletron=cabletron, isdnDchEntry=isdnDchEntry, callHistoryReceivePackets=callHistoryReceivePackets, isdnDchDirNum1=isdnDchDirNum1, callHistoryCallOrigin=callHistoryCallOrigin, isdnDchDirNum2=isdnDchDirNum2, ctDataLink=ctDataLink, DisplayString=DisplayString, rmtProfileEntryMpLessBWSamples=rmtProfileEntryMpLessBWSamples, dialCtlNbrCfgOriginateAddress=dialCtlNbrCfgOriginateAddress, isdnDchSPID1=isdnDchSPID1, isdnDchOperStatus=isdnDchOperStatus, callHistoryTable=callHistoryTable, ctron=ctron, isdnDchChInUse=isdnDchChInUse, rmtProfileEntryIndex=rmtProfileEntryIndex, ctISDNcontrol=ctISDNcontrol, dialCtlNbrCfgIfIndex=dialCtlNbrCfgIfIndex, rmtProfileEntryLinkHead=rmtProfileEntryLinkHead, rmtProfileEntryMpRmtBwCtrl=rmtProfileEntryMpRmtBwCtrl, callHistorySetupTime=callHistorySetupTime, dialCtlNbrCfgTable=dialCtlNbrCfgTable, rmtProfileEntryMpMoreBWSamples=rmtProfileEntryMpMoreBWSamples, rmtProfileTable=rmtProfileTable, rmtProfileEntryMpMaxCallsAllowed=rmtProfileEntryMpMaxCallsAllowed, rmtProfileEntryMpAvgPktSize=rmtProfileEntryMpAvgPktSize, rmtProfileEntryAction=rmtProfileEntryAction, rmtProfileEntryMpHistoryTime=rmtProfileEntryMpHistoryTime, dialCtlNbrCfgIndex=dialCtlNbrCfgIndex, callHistoryPeerAddress=callHistoryPeerAddress, callHistoryTransmitBytes=callHistoryTransmitBytes, rmtProfileEntryBchInUse=rmtProfileEntryBchInUse, rmtProfileEntryName=rmtProfileEntryName, isdnDchIndex=isdnDchIndex, rmtProfileEntryMpLineUtilization=rmtProfileEntryMpLineUtilization, mibs=mibs, callHistoryLogicalIfIndex=callHistoryLogicalIfIndex, callHistory=callHistory, rmtProfileEntryMaxNeighbor=rmtProfileEntryMaxNeighbor, callHistoryInfoType=callHistoryInfoType, callHistoryConnectTime=callHistoryConnectTime, rmtProfileEntryMakerName=rmtProfileEntryMakerName, rmtProfileEntryState=rmtProfileEntryState, dialCtlNbrCfgId=dialCtlNbrCfgId, callHistoryNeighborId=callHistoryNeighborId, isdnDchRateAccess=isdnDchRateAccess, callHistoryReceiveBytes=callHistoryReceiveBytes, callHistoryIndex=callHistoryIndex, rmtProfileEntryMpCallsToRemove=rmtProfileEntryMpCallsToRemove, rmtProfileEntry=rmtProfileEntry, isdnDchSwitchType=isdnDchSwitchType, callHistoryTransmitPackets=callHistoryTransmitPackets, ctISDNconfigMib=ctISDNconfigMib, dialCtlNbrCfgEntry=dialCtlNbrCfgEntry, ctronWan=ctronWan, isdnDchSPID2=isdnDchSPID2, rmtProfileEntryMpCallsToAdd=rmtProfileEntryMpCallsToAdd, isdnDchTable=isdnDchTable, isdnDchAllowedCh=isdnDchAllowedCh, dialCtlNbrCfgAnswerAddress=dialCtlNbrCfgAnswerAddress, callHistoryDisconnectTime=callHistoryDisconnectTime)
