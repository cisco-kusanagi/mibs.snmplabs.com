#
# PySNMP MIB module DLINK-3100-CLI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-CLI-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:33:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, TimeTicks, Gauge32, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, IpAddress, Counter32, Bits, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "TimeTicks", "Gauge32", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "IpAddress", "Counter32", "Bits", "Counter64", "iso")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
rlCli = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52))
rlCli.setRevisions(('2007-01-02 00:00',))
if mibBuilder.loadTexts: rlCli.setLastUpdated('200701020000Z')
if mibBuilder.loadTexts: rlCli.setOrganization('Dlink, Inc. Dlink Semiconductor, Inc.')
rlCliMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCliMibVersion.setStatus('current')
rlCliPassword = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCliPassword.setStatus('current')
rlCliTimer = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 3600))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCliTimer.setStatus('current')
rlCliFileEnable = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCliFileEnable.setStatus('current')
rlCliFileEnableAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 52, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCliFileEnableAfterReset.setStatus('current')
mibBuilder.exportSymbols("DLINK-3100-CLI-MIB", rlCliFileEnableAfterReset=rlCliFileEnableAfterReset, rlCliPassword=rlCliPassword, rlCli=rlCli, PYSNMP_MODULE_ID=rlCli, rlCliFileEnable=rlCliFileEnable, rlCliTimer=rlCliTimer, rlCliMibVersion=rlCliMibVersion)
