#
# PySNMP MIB module Unisphere-Data-FRACTIONAL-T1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Unisphere-Data-FRACTIONAL-T1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:23:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Unsigned32, Counter32, IpAddress, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Gauge32, Counter64, iso, Bits, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Counter32", "IpAddress", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Gauge32", "Counter64", "iso", "Bits", "Integer32", "MibIdentifier")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
usDataMibs, = mibBuilder.importSymbols("Unisphere-Data-MIBs", "usDataMibs")
UsdNextIfIndex, UsdTimeSlotMap = mibBuilder.importSymbols("Unisphere-Data-TC", "UsdNextIfIndex", "UsdTimeSlotMap")
usdFt1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6))
usdFt1MIB.setRevisions(('2000-09-26 17:30', '1999-07-14 00:00', '1998-11-13 00:00',))
if mibBuilder.loadTexts: usdFt1MIB.setLastUpdated('200009261730Z')
if mibBuilder.loadTexts: usdFt1MIB.setOrganization('Unisphere Networks, Inc.')
usdFt1Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1))
usdFt1NextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 1), UsdNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usdFt1NextIfIndex.setStatus('current')
usdFt1IfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2), )
if mibBuilder.loadTexts: usdFt1IfTable.setStatus('current')
usdFt1IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1), ).setIndexNames((0, "Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfIndex"))
if mibBuilder.loadTexts: usdFt1IfEntry.setStatus('current')
usdFt1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: usdFt1IfIndex.setStatus('current')
usdFt1IfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfRowStatus.setStatus('current')
usdFt1IfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfLowerIfIndex.setStatus('current')
usdFt1IfTimeSlotMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 4), UsdTimeSlotMap()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfTimeSlotMap.setStatus('current')
usdFt1IfTimeSlotRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nx56kbps", 0), ("nx64kbps", 1))).clone('nx64kbps')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfTimeSlotRate.setStatus('current')
usdFt1IfDataPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("inverted", 1))).clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfDataPolarity.setStatus('obsolete')
usdFt1IfLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noLoop", 0), ("loop", 1))).clone('noLoop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usdFt1IfLoopbackConfig.setStatus('current')
usdFt1Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4))
usdFt1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1))
usdFt1Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2))
usdFt1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1, 1)).setObjects(("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFt1Compliance = usdFt1Compliance.setStatus('obsolete')
usdFt1Compliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1, 2)).setObjects(("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1Group2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFt1Compliance2 = usdFt1Compliance2.setStatus('current')
usdFt1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2, 1)).setObjects(("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1NextIfIndex"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfRowStatus"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLowerIfIndex"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotMap"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotRate"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfDataPolarity"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLoopbackConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFt1Group = usdFt1Group.setStatus('obsolete')
usdFt1Group2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2, 2)).setObjects(("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1NextIfIndex"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfRowStatus"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLowerIfIndex"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotMap"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfTimeSlotRate"), ("Unisphere-Data-FRACTIONAL-T1-MIB", "usdFt1IfLoopbackConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usdFt1Group2 = usdFt1Group2.setStatus('current')
mibBuilder.exportSymbols("Unisphere-Data-FRACTIONAL-T1-MIB", usdFt1Group2=usdFt1Group2, usdFt1IfLoopbackConfig=usdFt1IfLoopbackConfig, usdFt1NextIfIndex=usdFt1NextIfIndex, usdFt1Groups=usdFt1Groups, usdFt1IfTimeSlotRate=usdFt1IfTimeSlotRate, usdFt1IfTable=usdFt1IfTable, usdFt1IfRowStatus=usdFt1IfRowStatus, PYSNMP_MODULE_ID=usdFt1MIB, usdFt1Compliances=usdFt1Compliances, usdFt1MIB=usdFt1MIB, usdFt1Compliance2=usdFt1Compliance2, usdFt1IfLowerIfIndex=usdFt1IfLowerIfIndex, usdFt1Group=usdFt1Group, usdFt1IfEntry=usdFt1IfEntry, usdFt1Objects=usdFt1Objects, usdFt1IfIndex=usdFt1IfIndex, usdFt1Compliance=usdFt1Compliance, usdFt1IfDataPolarity=usdFt1IfDataPolarity, usdFt1IfTimeSlotMap=usdFt1IfTimeSlotMap, usdFt1Conformance=usdFt1Conformance)
