#
# PySNMP MIB module ASCEND-MISC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MISC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:13:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
miscGroup, = mibBuilder.importSymbols("ASCEND-MIB", "miscGroup")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ObjectIdentity, TimeTicks, NotificationType, Counter64, Integer32, Unsigned32, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "TimeTicks", "NotificationType", "Counter64", "Integer32", "Unsigned32", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "IpAddress", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
miscGroupFRTable = MibTable((1, 3, 6, 1, 4, 1, 529, 20, 1), )
if mibBuilder.loadTexts: miscGroupFRTable.setStatus('mandatory')
miscGroupFREntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 20, 1, 1), ).setIndexNames((0, "ASCEND-MISC-MIB", "miscGroupFRLMIIndex"))
if mibBuilder.loadTexts: miscGroupFREntry.setStatus('mandatory')
miscGroupFRLMIIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 20, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: miscGroupFRLMIIndex.setStatus('mandatory')
miscGroupFRLMIDlci = MibTableColumn((1, 3, 6, 1, 4, 1, 529, 20, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dlci-0", 1), ("dlci-1023", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: miscGroupFRLMIDlci.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MISC-MIB", miscGroupFRTable=miscGroupFRTable, miscGroupFRLMIIndex=miscGroupFRLMIIndex, miscGroupFRLMIDlci=miscGroupFRLMIDlci, miscGroupFREntry=miscGroupFREntry)
