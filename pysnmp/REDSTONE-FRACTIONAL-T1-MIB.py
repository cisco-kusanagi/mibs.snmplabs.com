#
# PySNMP MIB module REDSTONE-FRACTIONAL-T1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDSTONE-FRACTIONAL-T1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:47:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
rsMgmt, = mibBuilder.importSymbols("REDSTONE-SMI", "rsMgmt")
RsNextIfIndex, RsTimeSlotMap = mibBuilder.importSymbols("REDSTONE-TC", "RsNextIfIndex", "RsTimeSlotMap")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Integer32, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity, iso, Unsigned32, IpAddress, TimeTicks, Counter32, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity", "iso", "Unsigned32", "IpAddress", "TimeTicks", "Counter32", "Gauge32", "Counter64")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
rsFt1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2773, 2, 6))
rsFt1MIB.setRevisions(('1999-07-14 00:00', '1998-01-01 00:00',))
if mibBuilder.loadTexts: rsFt1MIB.setLastUpdated('9907140000Z')
if mibBuilder.loadTexts: rsFt1MIB.setOrganization('Redstone Communications, Inc.')
rsFt1Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1))
rsFt1NextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 1), RsNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsFt1NextIfIndex.setStatus('current')
rsFt1IfTable = MibTable((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2), )
if mibBuilder.loadTexts: rsFt1IfTable.setStatus('current')
rsFt1IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1), ).setIndexNames((0, "REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfIndex"))
if mibBuilder.loadTexts: rsFt1IfEntry.setStatus('current')
rsFt1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rsFt1IfIndex.setStatus('current')
rsFt1IfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsFt1IfRowStatus.setStatus('current')
rsFt1IfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsFt1IfLowerIfIndex.setStatus('current')
rsFt1IfTimeSlotMap = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 4), RsTimeSlotMap()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsFt1IfTimeSlotMap.setStatus('current')
rsFt1IfTimeSlotRate = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nx56kbps", 0), ("nx64kbps", 1))).clone('nx64kbps')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsFt1IfTimeSlotRate.setStatus('current')
rsFt1IfDataPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("inverted", 1))).clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsFt1IfDataPolarity.setStatus('obsolete')
rsFt1IfLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 2773, 2, 6, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noLoop", 0), ("loop", 1))).clone('noLoop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rsFt1IfLoopbackConfig.setStatus('current')
rsFt1Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 6, 4))
rsFt1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 1))
rsFt1Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 2))
rsFt1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 1, 1)).setObjects(("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsFt1Compliance = rsFt1Compliance.setStatus('obsolete')
rsFt1Compliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 1, 2)).setObjects(("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1Group2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsFt1Compliance2 = rsFt1Compliance2.setStatus('current')
rsFt1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 2, 1)).setObjects(("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1NextIfIndex"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfRowStatus"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfLowerIfIndex"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfTimeSlotMap"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfTimeSlotRate"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfDataPolarity"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfLoopbackConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsFt1Group = rsFt1Group.setStatus('obsolete')
rsFt1Group2 = ObjectGroup((1, 3, 6, 1, 4, 1, 2773, 2, 6, 4, 2, 2)).setObjects(("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1NextIfIndex"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfRowStatus"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfLowerIfIndex"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfTimeSlotMap"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfTimeSlotRate"), ("REDSTONE-FRACTIONAL-T1-MIB", "rsFt1IfLoopbackConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    rsFt1Group2 = rsFt1Group2.setStatus('current')
mibBuilder.exportSymbols("REDSTONE-FRACTIONAL-T1-MIB", rsFt1Compliances=rsFt1Compliances, rsFt1Groups=rsFt1Groups, rsFt1IfTimeSlotMap=rsFt1IfTimeSlotMap, rsFt1Compliance2=rsFt1Compliance2, rsFt1Conformance=rsFt1Conformance, rsFt1Group=rsFt1Group, rsFt1IfDataPolarity=rsFt1IfDataPolarity, rsFt1Compliance=rsFt1Compliance, rsFt1NextIfIndex=rsFt1NextIfIndex, rsFt1IfLowerIfIndex=rsFt1IfLowerIfIndex, rsFt1Group2=rsFt1Group2, rsFt1IfEntry=rsFt1IfEntry, rsFt1IfTable=rsFt1IfTable, PYSNMP_MODULE_ID=rsFt1MIB, rsFt1MIB=rsFt1MIB, rsFt1IfRowStatus=rsFt1IfRowStatus, rsFt1IfIndex=rsFt1IfIndex, rsFt1IfLoopbackConfig=rsFt1IfLoopbackConfig, rsFt1Objects=rsFt1Objects, rsFt1IfTimeSlotRate=rsFt1IfTimeSlotRate)
