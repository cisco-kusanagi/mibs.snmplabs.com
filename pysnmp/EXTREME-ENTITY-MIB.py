#
# PySNMP MIB module EXTREME-ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:53:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
extremeAgent, = mibBuilder.importSymbols("EXTREME-BASE-MIB", "extremeAgent")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Bits, MibIdentifier, ModuleIdentity, Counter64, Counter32, NotificationType, Integer32, IpAddress, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Bits", "MibIdentifier", "ModuleIdentity", "Counter64", "Counter32", "NotificationType", "Integer32", "IpAddress", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extremeEntity = ModuleIdentity((1, 3, 6, 1, 4, 1, 1916, 1, 31))
if mibBuilder.loadTexts: extremeEntity.setLastUpdated('0409170000Z')
if mibBuilder.loadTexts: extremeEntity.setOrganization('Extreme Networks, Inc.')
extremeEntityFRUTable = MibTable((1, 3, 6, 1, 4, 1, 1916, 1, 31, 1), )
if mibBuilder.loadTexts: extremeEntityFRUTable.setStatus('current')
extremeEntityFRUEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: extremeEntityFRUEntry.setStatus('current')
extremeEntityFRUStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEntityFRUStartTime.setStatus('current')
extremeEntityFRUOdometer = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEntityFRUOdometer.setStatus('current')
extremeEntityFRUOdometerUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 1916, 1, 31, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("days", 1), ("seconds", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extremeEntityFRUOdometerUnit.setStatus('current')
mibBuilder.exportSymbols("EXTREME-ENTITY-MIB", extremeEntityFRUStartTime=extremeEntityFRUStartTime, extremeEntityFRUOdometerUnit=extremeEntityFRUOdometerUnit, extremeEntityFRUTable=extremeEntityFRUTable, extremeEntity=extremeEntity, extremeEntityFRUOdometer=extremeEntityFRUOdometer, PYSNMP_MODULE_ID=extremeEntity, extremeEntityFRUEntry=extremeEntityFRUEntry)
