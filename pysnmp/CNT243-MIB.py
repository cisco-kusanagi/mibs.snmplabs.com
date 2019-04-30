#
# PySNMP MIB module CNT243-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CNT243-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:09:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
cnt2Subagent, = mibBuilder.importSymbols("CNT2-MIB", "cnt2Subagent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, TimeTicks, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, NotificationType, ModuleIdentity, MibIdentifier, enterprises, Counter32, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "TimeTicks", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "NotificationType", "ModuleIdentity", "MibIdentifier", "enterprises", "Counter32", "Integer32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cnt2Atmf = MibIdentifier((1, 3, 6, 1, 4, 1, 333, 2, 4, 3))
cnt2AtmfTable = MibTable((1, 3, 6, 1, 4, 1, 333, 2, 4, 3, 1), )
if mibBuilder.loadTexts: cnt2AtmfTable.setStatus('mandatory')
cnt2AtmfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 333, 2, 4, 3, 1, 1), ).setIndexNames((0, "CNT243-MIB", "cnt2AtmfSlot"), (0, "CNT243-MIB", "cnt2AtmfIndex"))
if mibBuilder.loadTexts: cnt2AtmfEntry.setStatus('mandatory')
cnt2AtmfSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2AtmfSlot.setStatus('mandatory')
cnt2AtmfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2AtmfIndex.setStatus('mandatory')
cnt2AtmfPort = MibTableColumn((1, 3, 6, 1, 4, 1, 333, 2, 4, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cnt2AtmfPort.setStatus('mandatory')
mibBuilder.exportSymbols("CNT243-MIB", cnt2AtmfIndex=cnt2AtmfIndex, cnt2AtmfSlot=cnt2AtmfSlot, cnt2AtmfTable=cnt2AtmfTable, cnt2AtmfPort=cnt2AtmfPort, cnt2AtmfEntry=cnt2AtmfEntry, cnt2Atmf=cnt2Atmf)
