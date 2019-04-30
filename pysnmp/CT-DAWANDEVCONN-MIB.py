#
# PySNMP MIB module CT-DAWANDEVCONN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CT-DAWANDEVCONN-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:12:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, MibIdentifier, Integer32, Bits, Unsigned32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter32, ModuleIdentity, Gauge32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "MibIdentifier", "Integer32", "Bits", "Unsigned32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter32", "ModuleIdentity", "Gauge32", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctSSA = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497))
daWanDevConn = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4497, 23))
daWanDevConnTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1), )
if mibBuilder.loadTexts: daWanDevConnTable.setStatus('mandatory')
daWanDevConnEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1), ).setIndexNames((0, "CT-DAWANDEVCONN-MIB", "daWanDeviceIndex"), (0, "CT-DAWANDEVCONN-MIB", "daWanConnectionIndex"))
if mibBuilder.loadTexts: daWanDevConnEntry.setStatus('mandatory')
daWanDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanDeviceIndex.setStatus('mandatory')
daWanConnectionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4497, 23, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: daWanConnectionIndex.setStatus('mandatory')
mibBuilder.exportSymbols("CT-DAWANDEVCONN-MIB", daWanDevConnEntry=daWanDevConnEntry, ctSSA=ctSSA, daWanDevConnTable=daWanDevConnTable, daWanConnectionIndex=daWanConnectionIndex, daWanDevConn=daWanDevConn, daWanDeviceIndex=daWanDeviceIndex)
