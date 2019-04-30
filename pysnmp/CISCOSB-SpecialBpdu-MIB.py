#
# PySNMP MIB module CISCOSB-SpecialBpdu-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-SpecialBpdu-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:07:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, Integer32, Counter64, ObjectIdentity, NotificationType, IpAddress, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Integer32", "Counter64", "ObjectIdentity", "NotificationType", "IpAddress", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "Bits", "Gauge32")
TextualConvention, DisplayString, RowStatus, TruthValue, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus", "TruthValue", "MacAddress")
rlSpecialBpdu = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144))
rlSpecialBpdu.setRevisions(('2008-05-03 12:34',))
if mibBuilder.loadTexts: rlSpecialBpdu.setLastUpdated('200805031234Z')
if mibBuilder.loadTexts: rlSpecialBpdu.setOrganization('Cisco Small Business')
class EncapType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("ethernet-v2", 2), ("llc", 3), ("llc-snap", 4))

class Action(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("bridge", 1), ("discard", 2))

class HwAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("forward", 1), ("drop", 2), ("trap", 3))

rlSpecialBpduTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1), )
if mibBuilder.loadTexts: rlSpecialBpduTable.setStatus('current')
rlSpecialBpduEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1), ).setIndexNames((0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"), (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduEncap"), (0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduProtId"))
if mibBuilder.loadTexts: rlSpecialBpduEntry.setStatus('current')
rlSpecialBpduMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 1), MacAddress())
if mibBuilder.loadTexts: rlSpecialBpduMacAddr.setStatus('current')
rlSpecialBpduEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 2), EncapType())
if mibBuilder.loadTexts: rlSpecialBpduEncap.setStatus('current')
rlSpecialBpduProtId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5))
if mibBuilder.loadTexts: rlSpecialBpduProtId.setStatus('current')
rlSpecialBpduAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 4), Action()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSpecialBpduAction.setStatus('current')
rlSpecialBpduRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 1, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSpecialBpduRowStatus.setStatus('current')
rlSpecialBpduHwTable = MibTable((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2), )
if mibBuilder.loadTexts: rlSpecialBpduHwTable.setStatus('current')
rlSpecialBpduHwEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2, 1), ).setIndexNames((0, "CISCOSB-SpecialBpdu-MIB", "rlSpecialBpduMacAddr"))
if mibBuilder.loadTexts: rlSpecialBpduHwEntry.setStatus('current')
rlSpecialBpduHwAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 144, 2, 1, 2), HwAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSpecialBpduHwAction.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-SpecialBpdu-MIB", rlSpecialBpduTable=rlSpecialBpduTable, rlSpecialBpduRowStatus=rlSpecialBpduRowStatus, PYSNMP_MODULE_ID=rlSpecialBpdu, rlSpecialBpduProtId=rlSpecialBpduProtId, Action=Action, rlSpecialBpduHwEntry=rlSpecialBpduHwEntry, rlSpecialBpduHwTable=rlSpecialBpduHwTable, rlSpecialBpduEncap=rlSpecialBpduEncap, rlSpecialBpduMacAddr=rlSpecialBpduMacAddr, EncapType=EncapType, rlSpecialBpduEntry=rlSpecialBpduEntry, HwAction=HwAction, rlSpecialBpduAction=rlSpecialBpduAction, rlSpecialBpdu=rlSpecialBpdu, rlSpecialBpduHwAction=rlSpecialBpduHwAction)
