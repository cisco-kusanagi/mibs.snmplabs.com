#
# PySNMP MIB module Fore-If-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-If-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
foreIfExtension, = mibBuilder.importSymbols("Fore-Common-MIB", "foreIfExtension")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Gauge32, Counter64, Bits, Unsigned32, Integer32, ModuleIdentity, IpAddress, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Counter64", "Bits", "Unsigned32", "Integer32", "ModuleIdentity", "IpAddress", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
foreIfModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 1, 15, 1))
if mibBuilder.loadTexts: foreIfModule.setLastUpdated('9709081030-0400')
if mibBuilder.loadTexts: foreIfModule.setOrganization('FORE')
foreIfGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 326, 1, 15, 2))
foreIfTable = MibTable((1, 3, 6, 1, 4, 1, 326, 1, 15, 2, 1), )
if mibBuilder.loadTexts: foreIfTable.setStatus('current')
foreIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 1, 15, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: foreIfEntry.setStatus('current')
foreIfMtu = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 1, 15, 2, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: foreIfMtu.setStatus('current')
mibBuilder.exportSymbols("Fore-If-MIB", foreIfModule=foreIfModule, foreIfTable=foreIfTable, PYSNMP_MODULE_ID=foreIfModule, foreIfEntry=foreIfEntry, foreIfMtu=foreIfMtu, foreIfGroup=foreIfGroup)
