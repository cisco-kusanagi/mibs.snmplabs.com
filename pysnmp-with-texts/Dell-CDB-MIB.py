#
# PySNMP MIB module Dell-CDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-CDB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:55:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("Dell-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, iso, Counter32, NotificationType, Integer32, Bits, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, MibIdentifier, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "iso", "Counter32", "NotificationType", "Integer32", "Bits", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "MibIdentifier", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
rlCDB = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 94))
rlCDB.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlCDB.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlCDB.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlCDB.setOrganization('Dell')
if mibBuilder.loadTexts: rlCDB.setContactInfo('www.dell.com')
if mibBuilder.loadTexts: rlCDB.setDescription('This private MIB module defines CDB private MIBs.')
rlStartupCDBChanged = MibScalar((1, 3, 6, 1, 4, 1, 89, 94, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBChanged.setStatus('current')
if mibBuilder.loadTexts: rlStartupCDBChanged.setDescription("Indicates whether the startup CDB has changed between the router's last two reboots")
rlManualReboot = MibScalar((1, 3, 6, 1, 4, 1, 89, 94, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlManualReboot.setStatus('current')
if mibBuilder.loadTexts: rlManualReboot.setDescription('Indicates whether the device was shutdown orderly before reboot or not (i.e. power failure)')
rlStartupCDBEmpty = MibScalar((1, 3, 6, 1, 4, 1, 89, 94, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlStartupCDBEmpty.setStatus('current')
if mibBuilder.loadTexts: rlStartupCDBEmpty.setDescription('Indicates whether the startup-cdb is empty, meaning: does not include any user configuration.')
mibBuilder.exportSymbols("Dell-CDB-MIB", rlManualReboot=rlManualReboot, rlCDB=rlCDB, PYSNMP_MODULE_ID=rlCDB, rlStartupCDBChanged=rlStartupCDBChanged, rlStartupCDBEmpty=rlStartupCDBEmpty)
