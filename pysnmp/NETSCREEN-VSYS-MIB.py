#
# PySNMP MIB module NETSCREEN-VSYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-VSYS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:10:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
netscreenVsys, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVsys")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, IpAddress, Counter64, ModuleIdentity, Gauge32, MibIdentifier, Integer32, iso, Counter32, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "IpAddress", "Counter64", "ModuleIdentity", "Gauge32", "MibIdentifier", "Integer32", "iso", "Counter32", "Unsigned32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenVsysMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 15, 0))
netscreenVsysMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-13 00:00', '2001-09-28 00:00', '2000-05-08 00:00',))
if mibBuilder.loadTexts: netscreenVsysMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenVsysMibModule.setOrganization('Juniper Networks, Inc.')
nsVsysCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 15, 1))
nsVsysCfgTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1), )
if mibBuilder.loadTexts: nsVsysCfgTable.setStatus('current')
nsVsysCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1), ).setIndexNames((0, "NETSCREEN-VSYS-MIB", "nsVsysCfgId"))
if mibBuilder.loadTexts: nsVsysCfgEntry.setStatus('current')
nsVsysCfgId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVsysCfgId.setStatus('current')
nsVsysCfgName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVsysCfgName.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-VSYS-MIB", PYSNMP_MODULE_ID=netscreenVsysMibModule, nsVsysCfgName=nsVsysCfgName, nsVsysCfgTable=nsVsysCfgTable, nsVsysCfg=nsVsysCfg, netscreenVsysMibModule=netscreenVsysMibModule, nsVsysCfgId=nsVsysCfgId, nsVsysCfgEntry=nsVsysCfgEntry)
