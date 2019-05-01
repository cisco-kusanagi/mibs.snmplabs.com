#
# PySNMP MIB module SNMP-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SNMP-TEST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:08:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
rlSnmpTestSimulatedVariables, = mibBuilder.importSymbols("RADLAN-rndApplications", "rlSnmpTestSimulatedVariables")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, MibIdentifier, Counter64, Bits, TimeTicks, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, Counter32, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "MibIdentifier", "Counter64", "Bits", "TimeTicks", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "Counter32", "Unsigned32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class KeyBits(TextualConvention, Bits):
    description = 'Defined for the sole purpose of allowing syntax refinement'
    status = 'current'
    namedValues = NamedValues(("firstKey", 0), ("secondKey", 1), ("thirdKey", 2), ("fourthKey", 3), ("fifthKey", 4))

class FieldBits(TextualConvention, Bits):
    description = 'Defined for the sole purpose of allowing syntax refinement'
    status = 'current'
    namedValues = NamedValues(("firstField", 0), ("secondField", 1), ("thirdField", 2), ("fourthField", 3), ("fifthField", 4))

rlSnmpTestMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpTestMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlSnmpTestMibVersion.setDescription("MIB's version, the current version is 1.")
rlSetsTestTable = MibTable((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2), )
if mibBuilder.loadTexts: rlSetsTestTable.setStatus('current')
if mibBuilder.loadTexts: rlSetsTestTable.setDescription('This table will allow us to test the PortList and BITS support, both as table keys and fields.')
rlSetsTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1), ).setIndexNames((0, "SNMP-TEST-MIB", "rlSetsEntryBitsKey"), (0, "SNMP-TEST-MIB", "rlSetsEntryPortListKey"))
if mibBuilder.loadTexts: rlSetsTestEntry.setStatus('current')
if mibBuilder.loadTexts: rlSetsTestEntry.setDescription('One entry in the rlSetsTestTable.')
rlSetsEntryBitsKey = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 1), KeyBits().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("firstKey", 0), ("secondKey", 1), ("thirdKey", 2), ("fifthKey", 4))))
if mibBuilder.loadTexts: rlSetsEntryBitsKey.setStatus('current')
if mibBuilder.loadTexts: rlSetsEntryBitsKey.setDescription('BITS key')
rlSetsEntryPortListKey = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 2), PortList())
if mibBuilder.loadTexts: rlSetsEntryPortListKey.setStatus('current')
if mibBuilder.loadTexts: rlSetsEntryPortListKey.setDescription('Port list key')
rlSetsEntryBitsField = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 3), FieldBits().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("firstField", 0), ("secondField", 1), ("thirdField", 2), ("fifthField", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSetsEntryBitsField.setStatus('current')
if mibBuilder.loadTexts: rlSetsEntryBitsField.setDescription('Bits Field')
rlSetsEntryPortListField = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 4), PortList()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSetsEntryPortListField.setStatus('current')
if mibBuilder.loadTexts: rlSetsEntryPortListField.setDescription('Port list field')
rlSetsEntryCounter64Field = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 35, 2, 9, 9, 2, 1, 5), Counter64()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlSetsEntryCounter64Field.setStatus('current')
if mibBuilder.loadTexts: rlSetsEntryCounter64Field.setDescription('Counter64 field')
mibBuilder.exportSymbols("SNMP-TEST-MIB", FieldBits=FieldBits, rlSetsEntryBitsField=rlSetsEntryBitsField, KeyBits=KeyBits, rlSetsEntryPortListField=rlSetsEntryPortListField, rlSnmpTestMibVersion=rlSnmpTestMibVersion, rlSetsTestTable=rlSetsTestTable, rlSetsEntryBitsKey=rlSetsEntryBitsKey, rlSetsTestEntry=rlSetsTestEntry, rlSetsEntryCounter64Field=rlSetsEntryCounter64Field, rlSetsEntryPortListKey=rlSetsEntryPortListKey)
