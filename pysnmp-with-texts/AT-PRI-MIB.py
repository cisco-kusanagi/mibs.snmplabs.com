#
# PySNMP MIB module AT-PRI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AT-PRI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
DisplayStringUnsized, modules = mibBuilder.importSymbols("AT-SMI-MIB", "DisplayStringUnsized", "modules")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, NotificationType, Counter32, MibIdentifier, ModuleIdentity, iso, Counter64, Unsigned32, ObjectIdentity, IpAddress, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Counter32", "MibIdentifier", "ModuleIdentity", "iso", "Counter64", "Unsigned32", "ObjectIdentity", "IpAddress", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
pri = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42))
pri.setRevisions(('2006-06-28 12:22',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pri.setRevisionsDescriptions(('Initial Revision',))
if mibBuilder.loadTexts: pri.setLastUpdated('200606281222Z')
if mibBuilder.loadTexts: pri.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: pri.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: pri.setDescription('This MIB file contains definitions of managed objects for the PRI module. ')
priIntTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1), )
if mibBuilder.loadTexts: priIntTable.setStatus('current')
if mibBuilder.loadTexts: priIntTable.setDescription('The table of PRI interfaces.')
priIntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1), ).setIndexNames((0, "AT-PRI-MIB", "priIntIndex"))
if mibBuilder.loadTexts: priIntEntry.setStatus('current')
if mibBuilder.loadTexts: priIntEntry.setDescription('A single entry in the PRI interfaces table.')
priIntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntIndex.setStatus('current')
if mibBuilder.loadTexts: priIntIndex.setDescription('The ifIndex of the PRI interface.')
priIntBoardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntBoardIndex.setStatus('current')
if mibBuilder.loadTexts: priIntBoardIndex.setDescription('The index in the arBoardTable of the board on which this PRI interface resides.')
priIntBoardPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntBoardPosition.setStatus('current')
if mibBuilder.loadTexts: priIntBoardPosition.setDescription("The position on this PRI interface's board of this PRI interface.")
priIntMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("isdn", 1), ("tdm", 2), ("mixed", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntMode.setStatus('current')
if mibBuilder.loadTexts: priIntMode.setDescription('The mode of operation of this PRI interface. The value isdn means that the entire interface is operating as an ISDN interface, the value tdm means that the entire interface is operating as TDM groups and the value mixed means that some channels in the interface are dedicated to ISDN and some to TDM groups.')
priIntTdmChannelMap = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntTdmChannelMap.setStatus('current')
if mibBuilder.loadTexts: priIntTdmChannelMap.setDescription('A bit map of the channels in the PRI interface which are dedicated to TDM. PRI channels are numbered from 0 to 31, 0 is unused, 16 (E1) or 24 (T1) is the D channel. The map values are 2 to the power of the channel number.')
priIntIsdnChannelMap = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntIsdnChannelMap.setStatus('current')
if mibBuilder.loadTexts: priIntIsdnChannelMap.setDescription('A bit map of the channels in the PRI interface which are dedicated to ISDN. PRI channels are numbered from 0 to 31, 0 is unused, 16 (E1) or 24 (T1) is the D channel. The map values are 2 to the power of the channel number.')
priIntType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("e1", 1), ("t1", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: priIntType.setStatus('current')
if mibBuilder.loadTexts: priIntType.setDescription('The type of primary rate interface. E1 has 30 B + D channel, T1 has 23 B + D channel. If the value unknown is returned for this object, the exact PRI type has not yet been determined.')
priChanTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2), )
if mibBuilder.loadTexts: priChanTable.setStatus('current')
if mibBuilder.loadTexts: priChanTable.setDescription('The table of channels on PRI interfaces.')
priChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1), ).setIndexNames((0, "AT-PRI-MIB", "priChanIntIndex"), (0, "AT-PRI-MIB", "priChanChannelIndex"))
if mibBuilder.loadTexts: priChanEntry.setStatus('current')
if mibBuilder.loadTexts: priChanEntry.setDescription('A single entry in the PRI channels table.')
priChanIntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: priChanIntIndex.setStatus('current')
if mibBuilder.loadTexts: priChanIntIndex.setDescription('The ifIndex of the PRI interface.')
priChanChannelIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: priChanChannelIndex.setStatus('current')
if mibBuilder.loadTexts: priChanChannelIndex.setDescription('The channel index of the PRI channel. Valid channels have indices from 1 to 31. The D channel on an E1 interface has index 16, the D channel on a T1 interface has index 24.')
priChanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("isdn", 1), ("tdm", 2), ("neither", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: priChanMode.setStatus('current')
if mibBuilder.loadTexts: priChanMode.setDescription('The mode of this PRI channel. The value isdn means that the channel is reserved for use in ISDN calls. The value tdm means that the channel is reserved for use by TDM. For the D channel, this object will usually have the value isdn. An exception is if the interface is running common D channel mode and the D channel is reserved for TDM.')
priChanState = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 42, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inactive", 1), ("active", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: priChanState.setStatus('current')
if mibBuilder.loadTexts: priChanState.setDescription('The state of this PRI channel. The value inactive means that the channel does not currently have an active user, either an ISDN call or an active TDM group. The value active means that the channel is in use, either by an ISDN call or an active TDM group.')
mibBuilder.exportSymbols("AT-PRI-MIB", priIntBoardPosition=priIntBoardPosition, priIntType=priIntType, priChanIntIndex=priChanIntIndex, priChanMode=priChanMode, priIntIndex=priIntIndex, pri=pri, priIntEntry=priIntEntry, priChanTable=priChanTable, priChanChannelIndex=priChanChannelIndex, priIntTdmChannelMap=priIntTdmChannelMap, priIntIsdnChannelMap=priIntIsdnChannelMap, priChanState=priChanState, priIntTable=priIntTable, priChanEntry=priChanEntry, priIntMode=priIntMode, PYSNMP_MODULE_ID=pri, priIntBoardIndex=priIntBoardIndex)
