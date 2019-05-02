#
# PySNMP MIB module Dell-3SW2SWTABLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-3SW2SWTABLES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:55:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, TimeTicks, Counter64, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Counter32, ModuleIdentity, Unsigned32, Gauge32, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "TimeTicks", "Counter64", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Counter32", "ModuleIdentity", "Unsigned32", "Gauge32", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rl3sw2swTables = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 63))
rl3sw2swTables.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rl3sw2swTables.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rl3sw2swTables.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rl3sw2swTables.setOrganization('Dell')
if mibBuilder.loadTexts: rl3sw2swTables.setContactInfo('www.dell.com')
if mibBuilder.loadTexts: rl3sw2swTables.setDescription('This private MIB module defines 3sw 2sw Tables private MIBs.')
rl3sw2swTablesPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 89, 63, 1), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rl3sw2swTablesPollingInterval.setStatus('current')
if mibBuilder.loadTexts: rl3sw2swTablesPollingInterval.setDescription('The polling interval for dynamic 3SW/2SW tables in seconds.')
mibBuilder.exportSymbols("Dell-3SW2SWTABLES-MIB", PYSNMP_MODULE_ID=rl3sw2swTables, rl3sw2swTables=rl3sw2swTables, rl3sw2swTablesPollingInterval=rl3sw2swTablesPollingInterval)
