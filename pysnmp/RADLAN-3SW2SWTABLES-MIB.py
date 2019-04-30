#
# PySNMP MIB module RADLAN-3SW2SWTABLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-3SW2SWTABLES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:36:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, ModuleIdentity, Counter32, Integer32, Bits, Counter64, Gauge32, Unsigned32, IpAddress, TimeTicks, iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Counter32", "Integer32", "Bits", "Counter64", "Gauge32", "Unsigned32", "IpAddress", "TimeTicks", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rl3sw2swTables = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 63))
rl3sw2swTables.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rl3sw2swTables.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rl3sw2swTables.setOrganization('Radlan - a MARVELL company. Marvell Semiconductor, Inc.')
rl3sw2swTablesPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 63, 1), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rl3sw2swTablesPollingInterval.setStatus('current')
mibBuilder.exportSymbols("RADLAN-3SW2SWTABLES-MIB", rl3sw2swTables=rl3sw2swTables, PYSNMP_MODULE_ID=rl3sw2swTables, rl3sw2swTablesPollingInterval=rl3sw2swTablesPollingInterval)
