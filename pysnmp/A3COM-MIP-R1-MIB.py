#
# PySNMP MIB module A3COM-MIP-R1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/tin/Dev/mibs.snmplabs.com/asn1/A3COM-MIP-R1-MIB
# Produced by pysmi-0.3.4 at Fri Jan 31 21:29:23 2020
# On host bier platform Linux version 5.4.0-3-amd64 by user tin
# Using Python version 3.7.6 (default, Jan 19 2020, 22:34:52) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ObjectIdentity, enterprises, iso, Bits, Integer32, MibIdentifier, Counter64, Counter32, NotificationType, IpAddress, TimeTicks, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ObjectIdentity", "enterprises", "iso", "Bits", "Integer32", "MibIdentifier", "Counter64", "Counter32", "NotificationType", "IpAddress", "TimeTicks", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
a3Com = MibIdentifier((1, 3, 6, 1, 4, 1, 43))
brouterMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2))
a3ComMIP = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 27))
a3ComMipSConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 27, 1))
a3ComMipCConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 27, 2))
a3ComMipData = MibIdentifier((1, 3, 6, 1, 4, 1, 43, 2, 27, 3))
class RowStatus(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

a3ComMipControl = MibScalar((1, 3, 6, 1, 4, 1, 43, 2, 27, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComMipControl.setStatus('mandatory')
a3ComMipPortTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1), )
if mibBuilder.loadTexts: a3ComMipPortTable.setStatus('mandatory')
a3ComMipPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1), ).setIndexNames((0, "A3COM-MIP-R1-MIB", "a3ComMipPortIndex"))
if mibBuilder.loadTexts: a3ComMipPortEntry.setStatus('mandatory')
a3ComMipPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComMipPortIndex.setStatus('mandatory')
a3ComMipPortQueryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 5400)).clone(120)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComMipPortQueryInterval.setStatus('mandatory')
a3ComMipPortThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComMipPortThreshold.setStatus('mandatory')
a3ComMipPortQuerier = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("yes", 1), ("no", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComMipPortQuerier.setStatus('mandatory')
a3ComMipPortPaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComMipPortPaceMode.setStatus('mandatory')
a3ComMipLocalGroupTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2), )
if mibBuilder.loadTexts: a3ComMipLocalGroupTable.setStatus('mandatory')
a3ComMipLocalGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2, 1), ).setIndexNames((0, "A3COM-MIP-R1-MIB", "a3ComMipLocalGroupPort"), (0, "A3COM-MIP-R1-MIB", "a3ComMipLocalGroupIpAddr"))
if mibBuilder.loadTexts: a3ComMipLocalGroupEntry.setStatus('mandatory')
a3ComMipLocalGroupPort = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComMipLocalGroupPort.setStatus('mandatory')
a3ComMipLocalGroupIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComMipLocalGroupIpAddr.setStatus('mandatory')
a3ComMipLocalGroupType = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("igmp", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComMipLocalGroupType.setStatus('mandatory')
a3ComMipLocalGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 2, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComMipLocalGroupStatus.setStatus('mandatory')
a3ComMipSmdsGroupTable = MibTable((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 3), )
if mibBuilder.loadTexts: a3ComMipSmdsGroupTable.setStatus('mandatory')
a3ComMipSmdsGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 3, 1), ).setIndexNames((0, "A3COM-MIP-R1-MIB", "a3ComMipSmdsGroupIpAddr"))
if mibBuilder.loadTexts: a3ComMipSmdsGroupEntry.setStatus('mandatory')
a3ComMipSmdsGroupIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: a3ComMipSmdsGroupIpAddr.setStatus('mandatory')
a3ComMipSmdsGroupMediaAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComMipSmdsGroupMediaAddr.setStatus('mandatory')
a3ComMipSmdsGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 2, 27, 2, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: a3ComMipSmdsGroupStatus.setStatus('mandatory')
mibBuilder.exportSymbols("A3COM-MIP-R1-MIB", RowStatus=RowStatus, a3ComMipSmdsGroupStatus=a3ComMipSmdsGroupStatus, a3ComMipCConfig=a3ComMipCConfig, a3ComMipControl=a3ComMipControl, a3ComMipPortQuerier=a3ComMipPortQuerier, a3ComMipLocalGroupTable=a3ComMipLocalGroupTable, a3ComMipLocalGroupStatus=a3ComMipLocalGroupStatus, a3ComMipData=a3ComMipData, a3Com=a3Com, a3ComMipSmdsGroupMediaAddr=a3ComMipSmdsGroupMediaAddr, a3ComMipSmdsGroupTable=a3ComMipSmdsGroupTable, brouterMIB=brouterMIB, a3ComMipPortPaceMode=a3ComMipPortPaceMode, a3ComMipLocalGroupIpAddr=a3ComMipLocalGroupIpAddr, a3ComMipSmdsGroupIpAddr=a3ComMipSmdsGroupIpAddr, a3ComMIP=a3ComMIP, a3ComMipPortThreshold=a3ComMipPortThreshold, a3ComMipLocalGroupPort=a3ComMipLocalGroupPort, a3ComMipSmdsGroupEntry=a3ComMipSmdsGroupEntry, a3ComMipPortQueryInterval=a3ComMipPortQueryInterval, a3ComMipLocalGroupEntry=a3ComMipLocalGroupEntry, a3ComMipPortEntry=a3ComMipPortEntry, a3ComMipPortIndex=a3ComMipPortIndex, a3ComMipLocalGroupType=a3ComMipLocalGroupType, a3ComMipSConfig=a3ComMipSConfig, a3ComMipPortTable=a3ComMipPortTable)
