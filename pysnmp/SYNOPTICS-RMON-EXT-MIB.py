#
# PySNMP MIB module SYNOPTICS-RMON-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SYNOPTICS-RMON-EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:06:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Bits, TimeTicks, ObjectIdentity, Counter64, Gauge32, Counter32, IpAddress, NotificationType, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Bits", "TimeTicks", "ObjectIdentity", "Counter64", "Gauge32", "Counter32", "IpAddress", "NotificationType", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
products, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "products")
snpxRmonExt = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 8))
snpxRmonGetTabExt = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 8, 6))
getTable = MibIdentifier((1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1))
getTableTable = MibTable((1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1, 1), )
if mibBuilder.loadTexts: getTableTable.setStatus('mandatory')
getTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1, 1, 1), ).setIndexNames((0, "SYNOPTICS-RMON-EXT-MIB", "getTableSource"), (0, "SYNOPTICS-RMON-EXT-MIB", "getTableIndex"))
if mibBuilder.loadTexts: getTableEntry.setStatus('mandatory')
getTableSource = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: getTableSource.setStatus('mandatory')
getTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1, 1, 1, 2), ObjectIdentifier())
if mibBuilder.loadTexts: getTableIndex.setStatus('mandatory')
getTableData = MibTableColumn((1, 3, 6, 1, 4, 1, 45, 1, 8, 6, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: getTableData.setStatus('mandatory')
mibBuilder.exportSymbols("SYNOPTICS-RMON-EXT-MIB", getTableData=getTableData, getTableEntry=getTableEntry, getTableSource=getTableSource, getTableIndex=getTableIndex, getTable=getTable, getTableTable=getTableTable, snpxRmonExt=snpxRmonExt, snpxRmonGetTabExt=snpxRmonGetTabExt)
