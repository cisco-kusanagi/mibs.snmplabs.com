#
# PySNMP MIB module DLINK-3100-3SW2SWTABLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-3SW2SWTABLES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:32:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, iso, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32, NotificationType, MibIdentifier, ModuleIdentity, Counter64, TimeTicks, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32", "NotificationType", "MibIdentifier", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rl3sw2swTables = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 63))
rl3sw2swTables.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rl3sw2swTables.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rl3sw2swTables.setOrganization('Dlink, Inc. Dlink Semiconductor, Inc.')
rl3sw2swTablesPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 63, 1), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rl3sw2swTablesPollingInterval.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-3SW2SWTABLES-MIB", PYSNMP_MODULE_ID=rl3sw2swTables, rl3sw2swTables=rl3sw2swTables, rl3sw2swTablesPollingInterval=rl3sw2swTablesPollingInterval)
