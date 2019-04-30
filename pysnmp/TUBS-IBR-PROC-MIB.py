#
# PySNMP MIB module TUBS-IBR-PROC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-IBR-PROC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, Counter32, iso, IpAddress, TimeTicks, MibIdentifier, NotificationType, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Counter32", "iso", "IpAddress", "TimeTicks", "MibIdentifier", "NotificationType", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ObjectIdentity", "ModuleIdentity")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
ibr, = mibBuilder.importSymbols("TUBS-SMI", "ibr")
procMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 3))
procMIB.setRevisions(('2000-02-09 00:00', '1997-02-14 10:23', '1994-11-15 20:24',))
if mibBuilder.loadTexts: procMIB.setLastUpdated('200002090000Z')
if mibBuilder.loadTexts: procMIB.setOrganization('TU Braunschweig')
procReload = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 3, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: procReload.setStatus('current')
procTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2), )
if mibBuilder.loadTexts: procTable.setStatus('current')
procEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2, 1), ).setIndexNames((0, "TUBS-IBR-PROC-MIB", "procID"))
if mibBuilder.loadTexts: procEntry.setStatus('current')
procID = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: procID.setStatus('current')
procCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: procCmd.setStatus('current')
mibBuilder.exportSymbols("TUBS-IBR-PROC-MIB", PYSNMP_MODULE_ID=procMIB, procMIB=procMIB, procTable=procTable, procEntry=procEntry, procCmd=procCmd, procID=procID, procReload=procReload)
