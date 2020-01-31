#
# PySNMP MIB module A3COM-MLN-R1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/A3COM-MLN-R1-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:29:24 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, MibIdentifier, iso, NotificationType, Counter32, enterprises, ModuleIdentity, Unsigned32, Integer32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "MibIdentifier", "iso", "NotificationType", "Counter32", "enterprises", "ModuleIdentity", "Unsigned32", "Integer32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity")
DisplayString, PhysAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "PhysAddress", "TextualConvention")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComMLN = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 23))
a3mlnStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 23, 10))
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3mlnMaxPorts = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 23, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnMaxPorts.setStatus('mandatory')
a3mlnMaxPhyPorts = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 23, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnMaxPhyPorts.setStatus('mandatory')
a3mlnCCSsaveErr = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 23, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnCCSsaveErr.setStatus('mandatory')
a3mlnCCSdelErr = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 23, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnCCSdelErr.setStatus('mandatory')
a3mlnSetStatus = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 23, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("setNoErr", 1), ("setErr", 2), ("setWarning", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnSetStatus.setStatus('mandatory')
a3mlnSetMsg = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 23, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnSetMsg.setStatus('mandatory')
a3mlnPortTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 23, 7), )
if mibBuilder.loadTexts: a3mlnPortTable.setStatus('mandatory')
a3mlnPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1), ).setIndexNames((0, "A3COM-MLN-R1-MIB", "a3mlnPindex"))
if mibBuilder.loadTexts: a3mlnPortEntry.setStatus('mandatory')
a3mlnPindex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPindex.setStatus('mandatory')
a3mlnPtype = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ppmPort", 1), ("groupPort", 2), ("memberPort", 3), ("primaryPort", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPtype.setStatus('mandatory')
a3mlnPowner = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernet", 1), ("tokenRing", 2), ("fddi", 3), ("otherMedia", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPowner.setStatus('mandatory')
a3mlnPlink = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPlink.setStatus('mandatory')
a3mlnPstState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forwarding", 1), ("blocking", 2), ("ignore", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPstState.setStatus('mandatory')
a3mlnPtbState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("learn", 1), ("noLearn", 2), ("ignore", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPtbState.setStatus('mandatory')
a3mlnPgrpPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPgrpPrimaryPort.setStatus('mandatory')
a3mlnPgrpSrcAdrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPgrpSrcAdrPort.setStatus('mandatory')
a3mlnPgrpSrcAdrMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mediaMAC", 1), ("mediaOther", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPgrpSrcAdrMedia.setStatus('mandatory')
a3mlnPgrpSrcAdrValue = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 10), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPgrpSrcAdrValue.setStatus('mandatory')
a3mlnPgrpDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 7, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPgrpDescription.setStatus('mandatory')
a3mlnGroupTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 23, 8), )
if mibBuilder.loadTexts: a3mlnGroupTable.setStatus('mandatory')
a3mlnGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1), ).setIndexNames((0, "A3COM-MLN-R1-MIB", "a3mlnGrpPort"))
if mibBuilder.loadTexts: a3mlnGroupEntry.setStatus('mandatory')
a3mlnGrpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnGrpPort.setStatus('mandatory')
a3mlnGrpPortType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2))).clone(namedValues=NamedValues(("groupPort", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnGrpPortType.setStatus('mandatory')
a3mlnGrpPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnGrpPortState.setStatus('mandatory')
a3mlnGrpPrimaryPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnGrpPrimaryPort.setStatus('mandatory')
a3mlnGrpOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ethernet", 1), ("tokenRing", 2), ("fddi", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3mlnGrpOwner.setStatus('mandatory')
a3mlnGrpMemberCount = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnGrpMemberCount.setStatus('mandatory')
a3mlnGrpFirstMember = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnGrpFirstMember.setStatus('mandatory')
a3mlnGrpDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 50))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3mlnGrpDescription.setStatus('mandatory')
a3mlnGrpEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 8, 1, 9), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3mlnGrpEntryStatus.setStatus('mandatory')
a3mlnMemberTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 23, 9), )
if mibBuilder.loadTexts: a3mlnMemberTable.setStatus('mandatory')
a3mlnMemberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 23, 9, 1), ).setIndexNames((0, "A3COM-MLN-R1-MIB", "a3mlnMemGrpPort"), (0, "A3COM-MLN-R1-MIB", "a3mlnMemPort"))
if mibBuilder.loadTexts: a3mlnMemberEntry.setStatus('mandatory')
a3mlnMemGrpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 9, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnMemGrpPort.setStatus('mandatory')
a3mlnMemPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 9, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnMemPort.setStatus('mandatory')
a3mlnMemOwner = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("ethernet", 1), ("tokenRing", 2), ("fddi", 3), ("otherMedia", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3mlnMemOwner.setStatus('mandatory')
a3mlnMemEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 9, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3mlnMemEntryStatus.setStatus('mandatory')
a3mlnStatSelGrpPort = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnStatSelGrpPort.setStatus('mandatory')
a3mlnStatSelMacAdr = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnStatSelMacAdr.setStatus('mandatory')
a3mlnPortStatTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3), )
if mibBuilder.loadTexts: a3mlnPortStatTable.setStatus('mandatory')
a3mlnPortStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1), ).setIndexNames((0, "A3COM-MLN-R1-MIB", "a3mlnPStatIndex"))
if mibBuilder.loadTexts: a3mlnPortStatEntry.setStatus('mandatory')
a3mlnPStatIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPStatIndex.setStatus('mandatory')
a3mlnPStatRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPStatRcvd.setStatus('mandatory')
a3mlnPStatXmit = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPStatXmit.setStatus('mandatory')
a3mlnPStatStaMoveFrom = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPStatStaMoveFrom.setStatus('mandatory')
a3mlnPStatStaMoveTo = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPStatStaMoveTo.setStatus('mandatory')
a3mlnPStatSTAchange = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 23, 10, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3mlnPStatSTAchange.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-MLN-R1-MIB", brouterMIB=brouterMIB, a3mlnGrpMemberCount=a3mlnGrpMemberCount, a3mlnPortTable=a3mlnPortTable, a3mlnMemberEntry=a3mlnMemberEntry, a3mlnStatistics=a3mlnStatistics, a3mlnGrpPortState=a3mlnGrpPortState, a3mlnMemberTable=a3mlnMemberTable, a3mlnPStatStaMoveTo=a3mlnPStatStaMoveTo, a3mlnMaxPorts=a3mlnMaxPorts, a3mlnPgrpDescription=a3mlnPgrpDescription, a3mlnPortEntry=a3mlnPortEntry, a3mlnStatSelGrpPort=a3mlnStatSelGrpPort, a3ComMLN=a3ComMLN, a3mlnPortStatTable=a3mlnPortStatTable, a3mlnPstState=a3mlnPstState, a3mlnGroupEntry=a3mlnGroupEntry, a3mlnMemOwner=a3mlnMemOwner, a3mlnPgrpSrcAdrMedia=a3mlnPgrpSrcAdrMedia, a3mlnPgrpSrcAdrPort=a3mlnPgrpSrcAdrPort, a3mlnPgrpSrcAdrValue=a3mlnPgrpSrcAdrValue, a3mlnStatSelMacAdr=a3mlnStatSelMacAdr, a3mlnPStatIndex=a3mlnPStatIndex, a3Com=a3Com, a3mlnPStatXmit=a3mlnPStatXmit, a3mlnPlink=a3mlnPlink, a3mlnSetStatus=a3mlnSetStatus, a3mlnMemGrpPort=a3mlnMemGrpPort, a3mlnCCSdelErr=a3mlnCCSdelErr, a3mlnPtype=a3mlnPtype, RowStatus=RowStatus, a3mlnPowner=a3mlnPowner, a3mlnMaxPhyPorts=a3mlnMaxPhyPorts, a3mlnPortStatEntry=a3mlnPortStatEntry, a3mlnGrpPortType=a3mlnGrpPortType, a3mlnGrpEntryStatus=a3mlnGrpEntryStatus, a3mlnPStatSTAchange=a3mlnPStatSTAchange, a3mlnMemPort=a3mlnMemPort, a3mlnPStatRcvd=a3mlnPStatRcvd, a3mlnMemEntryStatus=a3mlnMemEntryStatus, a3mlnGrpPort=a3mlnGrpPort, a3mlnGrpPrimaryPort=a3mlnGrpPrimaryPort, a3mlnPgrpPrimaryPort=a3mlnPgrpPrimaryPort, a3mlnGrpOwner=a3mlnGrpOwner, a3mlnSetMsg=a3mlnSetMsg, a3mlnGroupTable=a3mlnGroupTable, a3mlnGrpDescription=a3mlnGrpDescription, a3mlnCCSsaveErr=a3mlnCCSsaveErr, a3mlnGrpFirstMember=a3mlnGrpFirstMember, a3mlnPStatStaMoveFrom=a3mlnPStatStaMoveFrom, a3mlnPindex=a3mlnPindex, a3mlnPtbState=a3mlnPtbState)
