#
# PySNMP MIB module DLINK-3100-CLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-CLI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:48:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, TimeTicks, Gauge32, ObjectIdentity, Unsigned32, MibIdentifier, iso, Integer32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "TimeTicks", "Gauge32", "ObjectIdentity", "Unsigned32", "MibIdentifier", "iso", "Integer32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Bits")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
rlCli = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52))
rlCli.setRevisions(('2007-01-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlCli.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlCli.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlCli.setOrganization('Dlink, Inc. Dlink Semiconductor, Inc.')
if mibBuilder.loadTexts: rlCli.setContactInfo('www.dlink.com')
if mibBuilder.loadTexts: rlCli.setDescription('This private MIB module defines CLI private MIBs.')
rlCliMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCliMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlCliMibVersion.setDescription("MIB's version, the current version is 1.")
rlCliPassword = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCliPassword.setStatus('current')
if mibBuilder.loadTexts: rlCliPassword.setDescription('CLI Password')
rlCliTimer = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCliTimer.setStatus('current')
if mibBuilder.loadTexts: rlCliTimer.setDescription('CLI Timer')
rlCliFileEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCliFileEnable.setStatus('current')
if mibBuilder.loadTexts: rlCliFileEnable.setDescription('CLI File Enable/Disable')
rlCliFileEnableAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCliFileEnableAfterReset.setStatus('current')
if mibBuilder.loadTexts: rlCliFileEnableAfterReset.setDescription('CLI File Enable/Disable After Reset')
mibBuilder.exportSymbols("DLINK-3100-CLI-MIB", rlCliFileEnable=rlCliFileEnable, rlCliMibVersion=rlCliMibVersion, rlCliPassword=rlCliPassword, rlCli=rlCli, PYSNMP_MODULE_ID=rlCli, rlCliFileEnableAfterReset=rlCliFileEnableAfterReset, rlCliTimer=rlCliTimer)
