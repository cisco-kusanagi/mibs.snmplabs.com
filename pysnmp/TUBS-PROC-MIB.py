#
# PySNMP MIB module TUBS-PROC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-PROC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, enterprises, TimeTicks, Counter32, Unsigned32, Integer32, Counter64, ObjectIdentity, MibIdentifier, iso, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "enterprises", "TimeTicks", "Counter32", "Unsigned32", "Integer32", "Counter64", "ObjectIdentity", "MibIdentifier", "iso", "NotificationType", "IpAddress")
TAddress, RowStatus, TextualConvention, TruthValue, DateAndTime, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "RowStatus", "TextualConvention", "TruthValue", "DateAndTime", "TimeStamp", "DisplayString")
procMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 3))
if mibBuilder.loadTexts: procMIB.setLastUpdated('9411152024Z')
if mibBuilder.loadTexts: procMIB.setOrganization('TU Braunschweig')
procReload = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 3, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: procReload.setStatus('current')
procTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2), )
if mibBuilder.loadTexts: procTable.setStatus('current')
procEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2, 1), ).setIndexNames((0, "TUBS-PROC-MIB", "procID"))
if mibBuilder.loadTexts: procEntry.setStatus('current')
procID = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: procID.setStatus('current')
procCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: procCmd.setStatus('current')
mibBuilder.exportSymbols("TUBS-PROC-MIB", procTable=procTable, procCmd=procCmd, procReload=procReload, procID=procID, PYSNMP_MODULE_ID=procMIB, procMIB=procMIB, procEntry=procEntry)
