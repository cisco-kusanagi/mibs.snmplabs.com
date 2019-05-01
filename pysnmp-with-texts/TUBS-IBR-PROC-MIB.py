#
# PySNMP MIB module TUBS-IBR-PROC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TUBS-IBR-PROC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:27:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Gauge32, Counter32, Bits, iso, ObjectIdentity, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Gauge32", "Counter32", "Bits", "iso", "ObjectIdentity", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
ibr, = mibBuilder.importSymbols("TUBS-SMI", "ibr")
procMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1575, 1, 3))
procMIB.setRevisions(('2000-02-09 00:00', '1997-02-14 10:23', '1994-11-15 20:24',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: procMIB.setRevisionsDescriptions(('Updated IMPORTS and minor stylistic fixes.', 'Various cleanups to make the module conforming to SNMPv2 SMI.', 'The initial revision of this module.',))
if mibBuilder.loadTexts: procMIB.setLastUpdated('200002090000Z')
if mibBuilder.loadTexts: procMIB.setOrganization('TU Braunschweig')
if mibBuilder.loadTexts: procMIB.setContactInfo('Juergen Schoenwaelder TU Braunschweig Bueltenweg 74/75 38106 Braunschweig Germany Tel: +49 531 391 3283 Fax: +49 531 391 5936 E-mail: schoenw@ibr.cs.tu-bs.de')
if mibBuilder.loadTexts: procMIB.setDescription('Experimental MIB module for listing processes.')
procReload = MibScalar((1, 3, 6, 1, 4, 1, 1575, 1, 3, 1), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: procReload.setStatus('current')
if mibBuilder.loadTexts: procReload.setDescription('Any set operation will reload the process table. It contains a time stamp when the proc table was reloaded the last time.')
procTable = MibTable((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2), )
if mibBuilder.loadTexts: procTable.setStatus('current')
if mibBuilder.loadTexts: procTable.setDescription('The process table.')
procEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2, 1), ).setIndexNames((0, "TUBS-IBR-PROC-MIB", "procID"))
if mibBuilder.loadTexts: procEntry.setStatus('current')
if mibBuilder.loadTexts: procEntry.setDescription('An entry for a process in the processes table.')
procID = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: procID.setStatus('current')
if mibBuilder.loadTexts: procID.setDescription('The unique process ID.')
procCmd = MibTableColumn((1, 3, 6, 1, 4, 1, 1575, 1, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: procCmd.setStatus('current')
if mibBuilder.loadTexts: procCmd.setDescription('The command name used to start this process.')
mibBuilder.exportSymbols("TUBS-IBR-PROC-MIB", procTable=procTable, procCmd=procCmd, PYSNMP_MODULE_ID=procMIB, procEntry=procEntry, procMIB=procMIB, procID=procID, procReload=procReload)
