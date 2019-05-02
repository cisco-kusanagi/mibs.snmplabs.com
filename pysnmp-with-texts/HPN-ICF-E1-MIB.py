#
# PySNMP MIB module HPN-ICF-E1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-E1-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:38:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, Counter32, iso, MibIdentifier, Bits, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, Gauge32, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Counter32", "iso", "MibIdentifier", "Bits", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "Gauge32", "Unsigned32", "TimeTicks")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
hpnicfE1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28))
hpnicfE1.setRevisions(('2012-07-16 17:41', '2010-04-08 18:55', '2009-06-08 17:41', '2004-12-01 14:36',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfE1.setRevisionsDescriptions(('To fix bugs in the MIB file.', 'To fix bugs in the MIB file.', 'To fix bugs in the MIB file.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: hpnicfE1.setLastUpdated('201207161741Z')
if mibBuilder.loadTexts: hpnicfE1.setOrganization('')
if mibBuilder.loadTexts: hpnicfE1.setContactInfo('')
if mibBuilder.loadTexts: hpnicfE1.setDescription('This MIB provides E1 interface information that are excluded by RFC 1213 and RFC 2233')
hpnicfe1InterfaceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1), )
if mibBuilder.loadTexts: hpnicfe1InterfaceStatusTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceStatusTable.setDescription('This table contains E1 interface packet statistics ')
hpnicfe1InterfaceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfe1InterfaceStatusEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceStatusEntry.setDescription('This entry contains E1 interface packet statistics. The index of this Entry is ifIndex defined in ifTable of RFC1213-MIB')
hpnicfe1InterfaceInErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceInErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceInErrs.setDescription('The total number of error received on this interface')
hpnicfe1InterfaceInRuntsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceInRuntsErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceInRuntsErrs.setDescription('The number of Runts Error(too short packet) received on this interface')
hpnicfe1InterfaceInGiantsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceInGiantsErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceInGiantsErrs.setDescription('The number of Giants Error(too long packet) received on this interface')
hpnicfe1InterfaceInCrcErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceInCrcErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceInCrcErrs.setDescription('The number of CRC Error received on this interface')
hpnicfe1InterfaceInAlignErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceInAlignErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceInAlignErrs.setDescription('The number of Align Error received on this interface')
hpnicfe1InterfaceInOverRunsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceInOverRunsErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceInOverRunsErrs.setDescription('The number of Over Runs Error received on this interface')
hpnicfe1InterfaceInDribblesErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceInDribblesErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceInDribblesErrs.setDescription('The number of dribble packets received')
hpnicfe1InterfaceInAbortedSeqErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceInAbortedSeqErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceInAbortedSeqErrs.setDescription('The number of AbortedSeq Error received on this interface')
hpnicfe1InterfaceInNoBufferErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceInNoBufferErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceInNoBufferErrs.setDescription('The number of Error (no buffer available)')
hpnicfe1InterfaceInFramingErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceInFramingErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceInFramingErrs.setDescription('The number of framing Errors')
hpnicfe1InterfaceOutputErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceOutputErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceOutputErrs.setDescription('The number of total Error transmited on this interface')
hpnicfe1InterfaceOutUnderRunErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceOutUnderRunErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceOutUnderRunErrs.setDescription('The number of UnderRun Error transmited on this interface')
hpnicfe1InterfaceOutCollisonsErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceOutCollisonsErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceOutCollisonsErrs.setDescription('The number of Collisions Error transmited on this interface')
hpnicfe1InterfaceOutDeferedErrs = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1InterfaceOutDeferedErrs.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceOutDeferedErrs.setDescription('The number of Deferred Error transmited on this interface')
hpnicfe1Table = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2), )
if mibBuilder.loadTexts: hpnicfe1Table.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1Table.setDescription('A list of E1 interface entries.')
hpnicfe1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfe1Entry.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1Entry.setDescription('This entry contains E1 interface management information.')
class HpnicfE1TimeSlot(TextualConvention, OctetString):
    description = "Each octet within this value specifies a set of time slots, with the first octet specifying time slot 1 through 8, the second octet specifying time slots 9 through 16, etc. Within each octet, the most significant bit represents the highest numbered time slot, and the least significant bit represents the lowest numbered time slot. Thus, each time slot of the E1 is represented by a single bit within the value of this object. If that bit has a value of '1' then that time slot is included in the set of time slots; the time slot is not included if its bit has a value of '0'."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

hpnicfe1Type = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 1), Bits().clone(namedValues=NamedValues(("voice", 0), ("pos", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1Type.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1Type.setDescription('Specifies the type of the E1 interface. Now it supports types as follow: voice voice type pos POS type')
hpnicfe1Clock = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("slave", 1), ("master", 2), ("internal", 3), ("line", 4), ("linePri", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfe1Clock.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1Clock.setDescription('Specifies the clock type used on the E1 interface.')
hpnicfe1FrameFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("crc4", 1), ("nocrc4", 2))).clone('crc4')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfe1FrameFormat.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1FrameFormat.setDescription('Specifies the frame format used on the E1 interface.')
hpnicfe1LineCode = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("ami", 1), ("hdb3", 3))).clone('hdb3')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfe1LineCode.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1LineCode.setDescription('Specifies the line code type used on the E1 interface.')
hpnicfe1PriSetTimeSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 5), HpnicfE1TimeSlot()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfe1PriSetTimeSlot.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1PriSetTimeSlot.setDescription('This is a bit-map of PRI time slots used on the E1 interface. It needs to administratively shut down the D channel of the E1 interface before cancelling PRI time slots.')
hpnicfe1DChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1DChannelIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1DChannelIndex.setDescription('This is the ifIndex of the D channel of the E1 interface.')
hpnicfe1SubScribLineChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1SubScribLineChannelIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1SubScribLineChannelIndex.setDescription('This is the ifIndex of the subscriber-line channel of the E1 interface.')
hpnicfe1FcmChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1FcmChannelIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1FcmChannelIndex.setDescription('This is the ifIndex of the FCM (Fast Connection Modem) channel of the E1 interface.')
hpnicfe1InterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 3), )
if mibBuilder.loadTexts: hpnicfe1InterfaceTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceTable.setDescription('A list of channels of E1 interface entries. Including D channels and subscriber-line channels.')
hpnicfe1InterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfe1InterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1InterfaceEntry.setDescription('This entry contains channels of E1 interface management information. Including D channels and subscriber-line channels.')
hpnicfe1ControllerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfe1ControllerIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1ControllerIndex.setDescription('Which E1 interface is this channel belonged to.')
hpnicfe1TimeSlotSetTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4), )
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetTable.setDescription('A list of time slot set information of E1 interface entries.')
hpnicfe1TimeSlotSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetEntry.setDescription('This entry contains time slot set information of E1 interface.')
hpnicfe1TimeSlotSetGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 30))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetGroupId.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetGroupId.setDescription('Group ID.')
hpnicfe1TimeSlotSetSignalType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unkown", 1), ("em-delay", 2), ("em-immediate", 3), ("em-wink", 4), ("fxo-ground", 5), ("fxo-loop", 6), ("fxs-ground", 7), ("fxs-loop", 8), ("r2", 9)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetSignalType.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetSignalType.setDescription('Signal type. Now it supports types as follow: unkown, unkown em-delay E&M Delay Dial em-immediate E&M Immediate Start em-wink E&M Wink Start fxo-ground FXO Ground Start fxo-loop FXO Loop Start fxs-ground FXS Ground Start fxs-loop FXS Loop Start r2 R2 ITU Q421')
hpnicfe1TimeSlotSetList = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4, 1, 3), HpnicfE1TimeSlot()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetList.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetList.setDescription('Time slot bit map.')
hpnicfe1TimeSlotSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 28, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfe1TimeSlotSetRowStatus.setDescription('Operation status.')
mibBuilder.exportSymbols("HPN-ICF-E1-MIB", hpnicfe1InterfaceTable=hpnicfe1InterfaceTable, hpnicfe1InterfaceInGiantsErrs=hpnicfe1InterfaceInGiantsErrs, HpnicfE1TimeSlot=HpnicfE1TimeSlot, hpnicfe1Table=hpnicfe1Table, hpnicfe1InterfaceInErrs=hpnicfe1InterfaceInErrs, hpnicfe1InterfaceStatusEntry=hpnicfe1InterfaceStatusEntry, hpnicfe1InterfaceInOverRunsErrs=hpnicfe1InterfaceInOverRunsErrs, hpnicfe1InterfaceStatusTable=hpnicfe1InterfaceStatusTable, hpnicfe1InterfaceInFramingErrs=hpnicfe1InterfaceInFramingErrs, hpnicfe1TimeSlotSetGroupId=hpnicfe1TimeSlotSetGroupId, hpnicfe1TimeSlotSetList=hpnicfe1TimeSlotSetList, hpnicfe1DChannelIndex=hpnicfe1DChannelIndex, hpnicfe1PriSetTimeSlot=hpnicfe1PriSetTimeSlot, hpnicfe1FrameFormat=hpnicfe1FrameFormat, PYSNMP_MODULE_ID=hpnicfE1, hpnicfe1InterfaceOutDeferedErrs=hpnicfe1InterfaceOutDeferedErrs, hpnicfe1Type=hpnicfe1Type, hpnicfe1InterfaceInDribblesErrs=hpnicfe1InterfaceInDribblesErrs, hpnicfe1InterfaceInRuntsErrs=hpnicfe1InterfaceInRuntsErrs, hpnicfe1InterfaceOutUnderRunErrs=hpnicfe1InterfaceOutUnderRunErrs, hpnicfe1InterfaceInAbortedSeqErrs=hpnicfe1InterfaceInAbortedSeqErrs, hpnicfe1InterfaceInNoBufferErrs=hpnicfe1InterfaceInNoBufferErrs, hpnicfE1=hpnicfE1, hpnicfe1Entry=hpnicfe1Entry, hpnicfe1InterfaceEntry=hpnicfe1InterfaceEntry, hpnicfe1InterfaceOutputErrs=hpnicfe1InterfaceOutputErrs, hpnicfe1TimeSlotSetRowStatus=hpnicfe1TimeSlotSetRowStatus, hpnicfe1InterfaceOutCollisonsErrs=hpnicfe1InterfaceOutCollisonsErrs, hpnicfe1TimeSlotSetTable=hpnicfe1TimeSlotSetTable, hpnicfe1SubScribLineChannelIndex=hpnicfe1SubScribLineChannelIndex, hpnicfe1InterfaceInAlignErrs=hpnicfe1InterfaceInAlignErrs, hpnicfe1FcmChannelIndex=hpnicfe1FcmChannelIndex, hpnicfe1LineCode=hpnicfe1LineCode, hpnicfe1ControllerIndex=hpnicfe1ControllerIndex, hpnicfe1TimeSlotSetEntry=hpnicfe1TimeSlotSetEntry, hpnicfe1TimeSlotSetSignalType=hpnicfe1TimeSlotSetSignalType, hpnicfe1InterfaceInCrcErrs=hpnicfe1InterfaceInCrcErrs, hpnicfe1Clock=hpnicfe1Clock)
