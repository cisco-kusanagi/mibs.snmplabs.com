#
# PySNMP MIB module TR-STNASSIGN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TR-STNASSIGN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:19:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ctTRStnAssign, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctTRStnAssign")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, Counter32, iso, Unsigned32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, ObjectIdentity, TimeTicks, NotificationType, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "Counter32", "iso", "Unsigned32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "NotificationType", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnInterfaceCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnInterfaceCount.setStatus('mandatory')
stnAssignTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 2), )
if mibBuilder.loadTexts: stnAssignTable.setStatus('mandatory')
stnAssignTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 2, 1), ).setIndexNames((0, "TR-STNASSIGN-MIB", "stnAssignIndex"))
if mibBuilder.loadTexts: stnAssignTableEntry.setStatus('mandatory')
stnAssignIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAssignIndex.setStatus('mandatory')
stnAssignPortAssociation = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: stnAssignPortAssociation.setStatus('mandatory')
stnAssignPortRing = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: stnAssignPortRing.setStatus('mandatory')
mibBuilder.exportSymbols("TR-STNASSIGN-MIB", stnAssignIndex=stnAssignIndex, stnAssignTable=stnAssignTable, stnInterfaceCount=stnInterfaceCount, stnAssignPortRing=stnAssignPortRing, stnAssignTableEntry=stnAssignTableEntry, stnAssignPortAssociation=stnAssignPortAssociation)
