#
# PySNMP MIB module CXViewing-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXViewing-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:18:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
cxViewing, = mibBuilder.importSymbols("CXProduct-SMI", "cxViewing")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType, ObjectIdentity, Unsigned32, ModuleIdentity, IpAddress, TimeTicks, Counter64, iso, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter64", "iso", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cxViewTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 1), )
if mibBuilder.loadTexts: cxViewTable.setStatus('mandatory')
cxViewEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 1, 1), ).setIndexNames((0, "CXViewing-MIB", "cxViewConsoleAddress"))
if mibBuilder.loadTexts: cxViewEntry.setStatus('mandatory')
cxViewConsoleAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxViewConsoleAddress.setStatus('mandatory')
cxViewCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: cxViewCurrent.setStatus('mandatory')
cxViewNMEStatus = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cxViewNMEStatus.setStatus('mandatory')
cxViewNMEMode = MibScalar((1, 3, 6, 1, 4, 1, 495, 2, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("slave", 1), ("master", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cxViewNMEMode.setStatus('mandatory')
mibBuilder.exportSymbols("CXViewing-MIB", cxViewEntry=cxViewEntry, cxViewConsoleAddress=cxViewConsoleAddress, cxViewNMEStatus=cxViewNMEStatus, cxViewNMEMode=cxViewNMEMode, cxViewTable=cxViewTable, cxViewCurrent=cxViewCurrent)
