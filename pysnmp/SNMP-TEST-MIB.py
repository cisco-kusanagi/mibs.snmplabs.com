#
# PySNMP MIB module SNMP-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-TEST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:00:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rlSnmpTestSimulatedVariables, = mibBuilder.importSymbols("RADLAN-rndApplications", "rlSnmpTestSimulatedVariables")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, TimeTicks, Counter64, Bits, Gauge32, NotificationType, Counter32, ObjectIdentity, Unsigned32, iso, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Counter64", "Bits", "Gauge32", "NotificationType", "Counter32", "ObjectIdentity", "Unsigned32", "iso", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class KeyBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("firstKey", 0), ("secondKey", 1), ("thirdKey", 2), ("fourthKey", 3), ("fifthKey", 4))

class FieldBits(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("firstField", 0), ("secondField", 1), ("thirdField", 2), ("fourthField", 3), ("fifthField", 4))

rlSnmpTestMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpTestMibVersion.setStatus('current')
rlSetsTestTable = MibTable((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2), )
if mibBuilder.loadTexts: rlSetsTestTable.setStatus('current')
rlSetsTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1), ).setIndexNames((0, "SNMP-TEST-MIB", "rlSetsEntryBitsKey"), (0, "SNMP-TEST-MIB", "rlSetsEntryPortListKey"))
if mibBuilder.loadTexts: rlSetsTestEntry.setStatus('current')
rlSetsEntryBitsKey = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 1), KeyBits().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("firstKey", 0), ("secondKey", 1), ("thirdKey", 2), ("fifthKey", 4))))
if mibBuilder.loadTexts: rlSetsEntryBitsKey.setStatus('current')
rlSetsEntryPortListKey = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 2), PortList())
if mibBuilder.loadTexts: rlSetsEntryPortListKey.setStatus('current')
rlSetsEntryBitsField = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 3), FieldBits().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("firstField", 0), ("secondField", 1), ("thirdField", 2), ("fifthField", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSetsEntryBitsField.setStatus('current')
rlSetsEntryPortListField = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSetsEntryPortListField.setStatus('current')
rlSetsEntryCounter64Field = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 5), Counter64()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSetsEntryCounter64Field.setStatus('current')
mibBuilder.exportSymbols("SNMP-TEST-MIB", FieldBits=FieldBits, rlSetsEntryBitsField=rlSetsEntryBitsField, rlSetsEntryPortListKey=rlSetsEntryPortListKey, rlSnmpTestMibVersion=rlSnmpTestMibVersion, rlSetsEntryPortListField=rlSetsEntryPortListField, KeyBits=KeyBits, rlSetsEntryCounter64Field=rlSetsEntryCounter64Field, rlSetsTestEntry=rlSetsTestEntry, rlSetsEntryBitsKey=rlSetsEntryBitsKey, rlSetsTestTable=rlSetsTestTable)
