#
# PySNMP MIB module ZIPLOCK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZIPLOCK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:41:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ctResource, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctResource")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, TimeTicks, Bits, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Unsigned32, Counter64, iso, IpAddress, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "TimeTicks", "Bits", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Unsigned32", "Counter64", "iso", "IpAddress", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctZiplock = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3))
ctZiplockTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1), )
if mibBuilder.loadTexts: ctZiplockTable.setStatus('mandatory')
ctZiplockEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1), ).setIndexNames((0, "ZIPLOCK-MIB", "ctZiplockNumber"))
if mibBuilder.loadTexts: ctZiplockEntry.setStatus('mandatory')
ctZiplockNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctZiplockNumber.setStatus('mandatory')
ctZiplockPresence = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctZiplockPresence.setStatus('mandatory')
ctZiplockRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctZiplockRevision.setStatus('mandatory')
ctZiplockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12, 3, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctZiplockStatus.setStatus('mandatory')
mibBuilder.exportSymbols("ZIPLOCK-MIB", ctZiplockPresence=ctZiplockPresence, ctZiplockStatus=ctZiplockStatus, ctZiplock=ctZiplock, ctZiplockNumber=ctZiplockNumber, ctZiplockRevision=ctZiplockRevision, ctZiplockEntry=ctZiplockEntry, ctZiplockTable=ctZiplockTable)
