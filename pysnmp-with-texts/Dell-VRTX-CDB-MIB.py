#
# PySNMP MIB module Dell-VRTX-CDB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-VRTX-CDB-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:57:12 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
rnd, = mibBuilder.importSymbols("Dell-VRTX-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, Bits, NotificationType, TimeTicks, Gauge32, ModuleIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Bits", "NotificationType", "TimeTicks", "Gauge32", "ModuleIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "MibIdentifier", "Counter32")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("Dell-VRTX-CDB-MIB", rlManualReboot=rlManualReboot, rlStartupCDBChanged=rlStartupCDBChanged, rlCDB=rlCDB, PYSNMP_MODULE_ID=rlCDB)
