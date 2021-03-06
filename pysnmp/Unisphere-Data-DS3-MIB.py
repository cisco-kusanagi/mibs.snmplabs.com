#
# PySNMP MIB module Unisphere-Data-DS3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-DS3-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ifIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndexOrZero")
PerfIntervalCount, PerfTotalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfTotalCount", "PerfCurrentCount")
dsx3FarEndIntervalEntry, dsx3FarEndTotalEntry, dsx3FarEndCurrentEntry = mibBuilder.importSymbols("RFC1407-MIB", "dsx3FarEndIntervalEntry", "dsx3FarEndTotalEntry", "dsx3FarEndCurrentEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, ObjectIdentity, Gauge32, Counter32, Unsigned32, IpAddress, Bits, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "Gauge32", "Counter32", "Unsigned32", "IpAddress", "Bits", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "TimeTicks", "NotificationType")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdNextIfIndex, = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdNextIfIndex")
usdDs3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4))
usdDs3MIB.setRevisions(('2002-04-04 14:07', '2002-02-22 21:21', '2001-04-27 19:49', '2001-02-05 00:00', '1999-07-27 00:00', '1998-11-13 00:00',))
if mibBuilder.loadTexts: usdDs3MIB.setLastUpdated('200204041407Z')
if mibBuilder.loadTexts: usdDs3MIB.setOrganization('Unisphere Networks, Inc.')
usdDs3Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1))
usdDsx3ConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1), )
if mibBuilder.loadTexts: usdDsx3ConfigTable.setStatus('current')
usdDsx3ConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: usdDsx3ConfigEntry.setStatus('current')
usdDsx3LineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64000))).setUnits('meters').setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3LineLength.setStatus('current')
usdDsx3LineType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 18, 20))).clone(namedValues=NamedValues(("usdDsx3other", 1), ("usdDsx3M23", 2), ("usdDsx3SYNTRAN", 3), ("usdDsx3CbitParity", 4), ("usdDsx3ClearChannel", 5), ("usdE3G832", 6), ("usdE3Framed", 7), ("usdE3Plcp", 8), ("usdDsx3M23Plcp", 18), ("usdDsx3CbitParityPlcp", 20)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3LineType.setStatus('current')
usdDsx3CellScramblerConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("scramblerOn", 1), ("scramblerOff", 2), ("notSupported", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3CellScramblerConfig.setStatus('current')
usdDsx3Channelization = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3Channelization.setStatus('current')
usdDsx3InterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ds3T3", 0), ("ds3E3", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3InterfaceType.setStatus('current')
usdDsx3Application = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ds3FrameOverDs3", 0), ("ds3AtmOverDs3", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3Application.setStatus('current')
usdDsx3Ds3Channel = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 28))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3Ds3Channel.setStatus('current')
usdDsx3LowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 8), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3LowerIfIndex.setStatus('current')
usdDsx3RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3RowStatus.setStatus('current')
usdDsx3Ds3DsuMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4))).clone(namedValues=NamedValues(("ds3DsuModeNone", 0), ("ds3DsuLarsCom", 2), ("ds3DsuDigitalLink", 4))).clone('ds3DsuModeNone')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3Ds3DsuMode.setStatus('current')
usdDsx3Ds3BandwidthLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 44210))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3Ds3BandwidthLimit.setStatus('current')
usdDsx3Ds3DsuScrambleMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("ds3DsuScrambleDisabled", 0), ("ds3DsuScrambleEnable", 1))).clone('ds3DsuScrambleDisabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3Ds3DsuScrambleMode.setStatus('current')
usdDsx3MdlCarrier = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3MdlCarrier.setStatus('current')
usdDsx3MdlTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4, 8))).clone(namedValues=NamedValues(("path", 1), ("idlesignal", 2), ("testsignal", 4), ("none", 8))).clone('none')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3MdlTransmit.setStatus('current')
usdDsx3MdlEic = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3MdlEic.setStatus('current')
usdDsx3MdlLic = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 11))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3MdlLic.setStatus('current')
usdDsx3MdlFic = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3MdlFic.setStatus('current')
usdDsx3MdlUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 18), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 6))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3MdlUnit.setStatus('current')
usdDsx3MdlPfi = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 19), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3MdlPfi.setStatus('current')
usdDsx3MdlPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3MdlPort.setStatus('current')
usdDsx3MdlGenerator = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 1, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 38))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdDsx3MdlGenerator.setStatus('current')
usdDs3NextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 2), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDs3NextIfIndex.setStatus('current')
usdDsx3FarEndCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 3), )
if mibBuilder.loadTexts: usdDsx3FarEndCurrentTable.setStatus('current')
usdDsx3FarEndCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 3, 1), )
dsx3FarEndCurrentEntry.registerAugmentions(("Unisphere-Data-DS3-MIB", "usdDsx3FarEndCurrentEntry"))
usdDsx3FarEndCurrentEntry.setIndexNames(*dsx3FarEndCurrentEntry.getIndexNames())
if mibBuilder.loadTexts: usdDsx3FarEndCurrentEntry.setStatus('current')
usdDsx3FarEndCurrentInvalidSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 3, 1, 1), PerfCurrentCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDsx3FarEndCurrentInvalidSeconds.setStatus('current')
usdDsx3FarEndIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 4), )
if mibBuilder.loadTexts: usdDsx3FarEndIntervalTable.setStatus('current')
usdDsx3FarEndIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 4, 1), )
dsx3FarEndIntervalEntry.registerAugmentions(("Unisphere-Data-DS3-MIB", "usdDsx3FarEndIntervalEntry"))
usdDsx3FarEndIntervalEntry.setIndexNames(*dsx3FarEndIntervalEntry.getIndexNames())
if mibBuilder.loadTexts: usdDsx3FarEndIntervalEntry.setStatus('current')
usdDsx3FarEndIntervalInvalidSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 4, 1, 1), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDsx3FarEndIntervalInvalidSeconds.setStatus('current')
usdDsx3FarEndTotalTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 5), )
if mibBuilder.loadTexts: usdDsx3FarEndTotalTable.setStatus('current')
usdDsx3FarEndTotalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 5, 1), )
dsx3FarEndTotalEntry.registerAugmentions(("Unisphere-Data-DS3-MIB", "usdDsx3FarEndTotalEntry"))
usdDsx3FarEndTotalEntry.setIndexNames(*dsx3FarEndTotalEntry.getIndexNames())
if mibBuilder.loadTexts: usdDsx3FarEndTotalEntry.setStatus('current')
usdDsx3FarEndTotalInvalidSeconds = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 1, 5, 1, 1), PerfTotalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdDsx3FarEndTotalInvalidSeconds.setStatus('current')
usdDs3Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4))
usdDs3Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1))
usdDs3Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2))
usdDs3Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 1)).setObjects(("Unisphere-Data-DS3-MIB", "usdDs3Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3Compliance = usdDs3Compliance.setStatus('obsolete')
usdDs3Compliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 2)).setObjects(("Unisphere-Data-DS3-MIB", "usdDs3Group2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3Compliance2 = usdDs3Compliance2.setStatus('obsolete')
usdDs3Compliance3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 3)).setObjects(("Unisphere-Data-DS3-MIB", "usdDs3Group3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3Compliance3 = usdDs3Compliance3.setStatus('obsolete')
usdDs3Compliance4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 4)).setObjects(("Unisphere-Data-DS3-MIB", "usdDs3Group4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3Compliance4 = usdDs3Compliance4.setStatus('obsolete')
usdDs3Compliance5 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 1, 5)).setObjects(("Unisphere-Data-DS3-MIB", "usdDs3Group5"), ("Unisphere-Data-DS3-MIB", "usdDs3FarEndGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3Compliance5 = usdDs3Compliance5.setStatus('current')
usdDs3Group = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 1)).setObjects(("Unisphere-Data-DS3-MIB", "usdDsx3LineLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3Group = usdDs3Group.setStatus('obsolete')
usdDs3Group2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 2)).setObjects(("Unisphere-Data-DS3-MIB", "usdDsx3LineLength"), ("Unisphere-Data-DS3-MIB", "usdDsx3LineType"), ("Unisphere-Data-DS3-MIB", "usdDsx3CellScramblerConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3Group2 = usdDs3Group2.setStatus('obsolete')
usdDs3Group3 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 3)).setObjects(("Unisphere-Data-DS3-MIB", "usdDsx3LineLength"), ("Unisphere-Data-DS3-MIB", "usdDsx3LineType"), ("Unisphere-Data-DS3-MIB", "usdDsx3CellScramblerConfig"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuMode"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3BandwidthLimit"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuScrambleMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3Group3 = usdDs3Group3.setStatus('obsolete')
usdDs3Group4 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 4)).setObjects(("Unisphere-Data-DS3-MIB", "usdDsx3LineLength"), ("Unisphere-Data-DS3-MIB", "usdDsx3LineType"), ("Unisphere-Data-DS3-MIB", "usdDsx3CellScramblerConfig"), ("Unisphere-Data-DS3-MIB", "usdDsx3Channelization"), ("Unisphere-Data-DS3-MIB", "usdDsx3InterfaceType"), ("Unisphere-Data-DS3-MIB", "usdDsx3Application"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3Channel"), ("Unisphere-Data-DS3-MIB", "usdDsx3LowerIfIndex"), ("Unisphere-Data-DS3-MIB", "usdDsx3RowStatus"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuMode"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3BandwidthLimit"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuScrambleMode"), ("Unisphere-Data-DS3-MIB", "usdDs3NextIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3Group4 = usdDs3Group4.setStatus('obsolete')
usdDs3Group5 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 5)).setObjects(("Unisphere-Data-DS3-MIB", "usdDsx3LineLength"), ("Unisphere-Data-DS3-MIB", "usdDsx3LineType"), ("Unisphere-Data-DS3-MIB", "usdDsx3CellScramblerConfig"), ("Unisphere-Data-DS3-MIB", "usdDsx3Channelization"), ("Unisphere-Data-DS3-MIB", "usdDsx3InterfaceType"), ("Unisphere-Data-DS3-MIB", "usdDsx3Application"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3Channel"), ("Unisphere-Data-DS3-MIB", "usdDsx3LowerIfIndex"), ("Unisphere-Data-DS3-MIB", "usdDsx3RowStatus"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuMode"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3BandwidthLimit"), ("Unisphere-Data-DS3-MIB", "usdDsx3Ds3DsuScrambleMode"), ("Unisphere-Data-DS3-MIB", "usdDsx3MdlCarrier"), ("Unisphere-Data-DS3-MIB", "usdDsx3MdlTransmit"), ("Unisphere-Data-DS3-MIB", "usdDsx3MdlEic"), ("Unisphere-Data-DS3-MIB", "usdDsx3MdlLic"), ("Unisphere-Data-DS3-MIB", "usdDsx3MdlFic"), ("Unisphere-Data-DS3-MIB", "usdDsx3MdlUnit"), ("Unisphere-Data-DS3-MIB", "usdDsx3MdlPfi"), ("Unisphere-Data-DS3-MIB", "usdDsx3MdlPort"), ("Unisphere-Data-DS3-MIB", "usdDsx3MdlGenerator"), ("Unisphere-Data-DS3-MIB", "usdDs3NextIfIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3Group5 = usdDs3Group5.setStatus('current')
usdDs3FarEndGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 4, 4, 2, 6)).setObjects(("Unisphere-Data-DS3-MIB", "usdDsx3FarEndCurrentInvalidSeconds"), ("Unisphere-Data-DS3-MIB", "usdDsx3FarEndIntervalInvalidSeconds"), ("Unisphere-Data-DS3-MIB", "usdDsx3FarEndTotalInvalidSeconds"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdDs3FarEndGroup = usdDs3FarEndGroup.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-DS3-MIB", usdDsx3LineType=usdDsx3LineType, usdDs3Group4=usdDs3Group4, usdDs3Compliance4=usdDs3Compliance4, usdDsx3FarEndCurrentEntry=usdDsx3FarEndCurrentEntry, usdDs3Conformance=usdDs3Conformance, usdDsx3Application=usdDsx3Application, usdDsx3FarEndTotalTable=usdDsx3FarEndTotalTable, usdDs3Group2=usdDs3Group2, usdDsx3MdlTransmit=usdDsx3MdlTransmit, usdDs3Compliance=usdDs3Compliance, usdDsx3ConfigEntry=usdDsx3ConfigEntry, usdDsx3MdlPort=usdDsx3MdlPort, usdDsx3FarEndCurrentInvalidSeconds=usdDsx3FarEndCurrentInvalidSeconds, usdDsx3MdlUnit=usdDsx3MdlUnit, usdDsx3MdlEic=usdDsx3MdlEic, usdDsx3FarEndIntervalTable=usdDsx3FarEndIntervalTable, usdDsx3FarEndCurrentTable=usdDsx3FarEndCurrentTable, usdDsx3LowerIfIndex=usdDsx3LowerIfIndex, usdDs3MIB=usdDs3MIB, usdDs3Compliances=usdDs3Compliances, usdDsx3Ds3BandwidthLimit=usdDsx3Ds3BandwidthLimit, usdDs3Compliance2=usdDs3Compliance2, usdDsx3FarEndIntervalInvalidSeconds=usdDsx3FarEndIntervalInvalidSeconds, usdDs3Objects=usdDs3Objects, usdDs3FarEndGroup=usdDs3FarEndGroup, PYSNMP_MODULE_ID=usdDs3MIB, usdDs3Groups=usdDs3Groups, usdDsx3Ds3DsuMode=usdDsx3Ds3DsuMode, usdDsx3RowStatus=usdDsx3RowStatus, usdDsx3Ds3DsuScrambleMode=usdDsx3Ds3DsuScrambleMode, usdDsx3MdlFic=usdDsx3MdlFic, usdDs3Group=usdDs3Group, usdDs3Compliance3=usdDs3Compliance3, usdDsx3InterfaceType=usdDsx3InterfaceType, usdDs3Group5=usdDs3Group5, usdDs3NextIfIndex=usdDs3NextIfIndex, usdDs3Compliance5=usdDs3Compliance5, usdDsx3CellScramblerConfig=usdDsx3CellScramblerConfig, usdDsx3Ds3Channel=usdDsx3Ds3Channel, usdDsx3FarEndIntervalEntry=usdDsx3FarEndIntervalEntry, usdDsx3FarEndTotalInvalidSeconds=usdDsx3FarEndTotalInvalidSeconds, usdDs3Group3=usdDs3Group3, usdDsx3ConfigTable=usdDsx3ConfigTable, usdDsx3MdlCarrier=usdDsx3MdlCarrier, usdDsx3FarEndTotalEntry=usdDsx3FarEndTotalEntry, usdDsx3MdlLic=usdDsx3MdlLic, usdDsx3MdlPfi=usdDsx3MdlPfi, usdDsx3LineLength=usdDsx3LineLength, usdDsx3MdlGenerator=usdDsx3MdlGenerator, usdDsx3Channelization=usdDsx3Channelization)
