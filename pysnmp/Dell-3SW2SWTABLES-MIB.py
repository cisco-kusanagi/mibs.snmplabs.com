#
# PySNMP MIB module Dell-3SW2SWTABLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-3SW2SWTABLES-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:40:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Counter64, Unsigned32, Gauge32, MibIdentifier, Bits, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, ModuleIdentity, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "Unsigned32", "Gauge32", "MibIdentifier", "Bits", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "ModuleIdentity", "Integer32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rl3sw2swTables = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 63))
rl3sw2swTables.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rl3sw2swTables.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rl3sw2swTables.setOrganization('Dell')
rl3sw2swTablesPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 63, 1), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rl3sw2swTablesPollingInterval.setStatus('current')
mibBuilder.exportSymbols("Dell-3SW2SWTABLES-MIB", rl3sw2swTables=rl3sw2swTables, rl3sw2swTablesPollingInterval=rl3sw2swTablesPollingInterval, PYSNMP_MODULE_ID=rl3sw2swTables)
