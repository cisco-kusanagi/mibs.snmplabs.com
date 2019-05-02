#
# PySNMP MIB module ASCEND-MISC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MISC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:29:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
miscGroup, = mibBuilder.importSymbols("ASCEND-MIB", "miscGroup")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, TimeTicks, ModuleIdentity, Unsigned32, Counter64, MibIdentifier, iso, Counter32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "TimeTicks", "ModuleIdentity", "Unsigned32", "Counter64", "MibIdentifier", "iso", "Counter32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
miscGroupFRTable = MibTable((1, 3, 6, 1, 4, 1, 529, 20, 1), )
if mibBuilder.loadTexts: miscGroupFRTable.setStatus('mandatory')
if mibBuilder.loadTexts: miscGroupFRTable.setDescription('Variables in Frame Relay profile.')
miscGroupFREntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 20, 1, 1), ).setIndexNames((0, "ASCEND-MISC-MIB", "miscGroupFRLMIIndex"))
if mibBuilder.loadTexts: miscGroupFREntry.setStatus('mandatory')
if mibBuilder.loadTexts: miscGroupFREntry.setDescription('An entry containing object variables for Frame Relay profile.')
miscGroupFRLMIIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 20, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: miscGroupFRLMIIndex.setStatus('mandatory')
if mibBuilder.loadTexts: miscGroupFRLMIIndex.setDescription('The index in to Frame Relay profile variables.')
miscGroupFRLMIDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dlci-0", 1), ("dlci-1023", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: miscGroupFRLMIDlci.setStatus('mandatory')
if mibBuilder.loadTexts: miscGroupFRLMIDlci.setDescription('The value of Link Management DLCI.')
mibBuilder.exportSymbols("ASCEND-MISC-MIB", miscGroupFRLMIIndex=miscGroupFRLMIIndex, miscGroupFREntry=miscGroupFREntry, miscGroupFRLMIDlci=miscGroupFRLMIDlci, miscGroupFRTable=miscGroupFRTable)
