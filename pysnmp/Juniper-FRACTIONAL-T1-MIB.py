#
# PySNMP MIB module Juniper-FRACTIONAL-T1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Juniper-FRACTIONAL-T1-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:51:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
juniMibs, = mibBuilder.importSymbols("Juniper-MIBs", "juniMibs")
JuniNextIfIndex, JuniTimeSlotMap = mibBuilder.importSymbols("Juniper-TC", "JuniNextIfIndex", "JuniTimeSlotMap")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, IpAddress, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, Bits, Gauge32, Unsigned32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "IpAddress", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "Bits", "Gauge32", "Unsigned32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
juniFt1MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6))
juniFt1MIB.setRevisions(('2002-09-16 21:44', '2000-09-26 17:30', '1999-07-14 00:00', '1998-11-13 00:00',))
if mibBuilder.loadTexts: juniFt1MIB.setLastUpdated('200209162144Z')
if mibBuilder.loadTexts: juniFt1MIB.setOrganization('Juniper Networks, Inc.')
juniFt1Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1))
juniFt1NextIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 1), JuniNextIfIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: juniFt1NextIfIndex.setStatus('current')
juniFt1IfTable = MibTable((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2), )
if mibBuilder.loadTexts: juniFt1IfTable.setStatus('current')
juniFt1IfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1), ).setIndexNames((0, "Juniper-FRACTIONAL-T1-MIB", "juniFt1IfIndex"))
if mibBuilder.loadTexts: juniFt1IfEntry.setStatus('current')
juniFt1IfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: juniFt1IfIndex.setStatus('current')
juniFt1IfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniFt1IfRowStatus.setStatus('current')
juniFt1IfLowerIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniFt1IfLowerIfIndex.setStatus('current')
juniFt1IfTimeSlotMap = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 4), JuniTimeSlotMap()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniFt1IfTimeSlotMap.setStatus('current')
juniFt1IfTimeSlotRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("nx56kbps", 0), ("nx64kbps", 1))).clone('nx64kbps')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniFt1IfTimeSlotRate.setStatus('current')
juniFt1IfDataPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("normal", 0), ("inverted", 1))).clone('normal')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniFt1IfDataPolarity.setStatus('obsolete')
juniFt1IfLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noLoop", 0), ("loop", 1))).clone('noLoop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: juniFt1IfLoopbackConfig.setStatus('current')
juniFt1Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4))
juniFt1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1))
juniFt1Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2))
juniFt1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1, 1)).setObjects(("Juniper-FRACTIONAL-T1-MIB", "juniFt1Group"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFt1Compliance = juniFt1Compliance.setStatus('obsolete')
juniFt1Compliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 1, 2)).setObjects(("Juniper-FRACTIONAL-T1-MIB", "juniFt1Group2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFt1Compliance2 = juniFt1Compliance2.setStatus('current')
juniFt1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2, 1)).setObjects(("Juniper-FRACTIONAL-T1-MIB", "juniFt1NextIfIndex"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfRowStatus"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfLowerIfIndex"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfTimeSlotMap"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfTimeSlotRate"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfDataPolarity"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfLoopbackConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFt1Group = juniFt1Group.setStatus('obsolete')
juniFt1Group2 = ObjectGroup((1, 3, 6, 1, 4, 1, 4874, 2, 2, 6, 4, 2, 2)).setObjects(("Juniper-FRACTIONAL-T1-MIB", "juniFt1NextIfIndex"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfRowStatus"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfLowerIfIndex"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfTimeSlotMap"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfTimeSlotRate"), ("Juniper-FRACTIONAL-T1-MIB", "juniFt1IfLoopbackConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    juniFt1Group2 = juniFt1Group2.setStatus('current')
mibBuilder.exportSymbols("Juniper-FRACTIONAL-T1-MIB", juniFt1Group2=juniFt1Group2, juniFt1Compliance2=juniFt1Compliance2, juniFt1Conformance=juniFt1Conformance, juniFt1IfRowStatus=juniFt1IfRowStatus, juniFt1IfTimeSlotMap=juniFt1IfTimeSlotMap, juniFt1IfLoopbackConfig=juniFt1IfLoopbackConfig, juniFt1IfTable=juniFt1IfTable, juniFt1Objects=juniFt1Objects, juniFt1Compliance=juniFt1Compliance, juniFt1NextIfIndex=juniFt1NextIfIndex, juniFt1IfIndex=juniFt1IfIndex, juniFt1IfEntry=juniFt1IfEntry, juniFt1Groups=juniFt1Groups, juniFt1IfDataPolarity=juniFt1IfDataPolarity, juniFt1IfLowerIfIndex=juniFt1IfLowerIfIndex, juniFt1Group=juniFt1Group, PYSNMP_MODULE_ID=juniFt1MIB, juniFt1IfTimeSlotRate=juniFt1IfTimeSlotRate, juniFt1Compliances=juniFt1Compliances, juniFt1MIB=juniFt1MIB)
