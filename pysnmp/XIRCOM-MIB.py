#
# PySNMP MIB module XIRCOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XIRCOM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:37:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Bits, Integer32, NotificationType, ModuleIdentity, Counter32, ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Gauge32, IpAddress, MibIdentifier, enterprises, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Bits", "Integer32", "NotificationType", "ModuleIdentity", "Counter32", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "enterprises", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xircom = MibIdentifier((1, 3, 6, 1, 4, 1, 588))
printers = MibIdentifier((1, 3, 6, 1, 4, 1, 588, 1))
printerStatus = MibScalar((1, 3, 6, 1, 4, 1, 588, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: printerStatus.setStatus('mandatory')
acceptPrintJobs = MibScalar((1, 3, 6, 1, 4, 1, 588, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acceptPrintJobs.setStatus('mandatory')
queuedJobs = MibScalar((1, 3, 6, 1, 4, 1, 588, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: queuedJobs.setStatus('mandatory')
sendTrap = MibScalar((1, 3, 6, 1, 4, 1, 588, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sendTrap.setStatus('mandatory')
printerTrap = NotificationType((1, 3, 6, 1, 4, 1, 588, 1) + (0,0)).setObjects(("XIRCOM-MIB", "printerStatus"))
mibBuilder.exportSymbols("XIRCOM-MIB", printers=printers, printerStatus=printerStatus, sendTrap=sendTrap, printerTrap=printerTrap, xircom=xircom, acceptPrintJobs=acceptPrintJobs, queuedJobs=queuedJobs)
