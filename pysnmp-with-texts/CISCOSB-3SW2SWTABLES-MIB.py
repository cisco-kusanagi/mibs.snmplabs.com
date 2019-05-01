#
# PySNMP MIB module CISCOSB-3SW2SWTABLES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOSB-3SW2SWTABLES-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:21:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Gauge32, NotificationType, Integer32, ModuleIdentity, TimeTicks, IpAddress, iso, Bits, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Gauge32", "NotificationType", "Integer32", "ModuleIdentity", "TimeTicks", "IpAddress", "iso", "Bits", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rl3sw2swTables = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 63))
rl3sw2swTables.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rl3sw2swTables.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rl3sw2swTables.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rl3sw2swTables.setOrganization('Cisco Small Business')
if mibBuilder.loadTexts: rl3sw2swTables.setContactInfo('Postal: 170 West Tasman Drive San Jose , CA 95134-1706 USA Website: Cisco Small Business Home http://www.cisco.com/smb>;, Cisco Small Business Support Community <http://www.cisco.com/go/smallbizsupport>')
if mibBuilder.loadTexts: rl3sw2swTables.setDescription('This private MIB module defines 3sw 2sw Tables private MIBs.')
rl3sw2swTablesPollingInterval = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 63, 1), Integer32().clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rl3sw2swTablesPollingInterval.setStatus('current')
if mibBuilder.loadTexts: rl3sw2swTablesPollingInterval.setDescription('The polling interval for dynamic 3SW/2SW tables in seconds.')
mibBuilder.exportSymbols("CISCOSB-3SW2SWTABLES-MIB", rl3sw2swTablesPollingInterval=rl3sw2swTablesPollingInterval, rl3sw2swTables=rl3sw2swTables, PYSNMP_MODULE_ID=rl3sw2swTables)
