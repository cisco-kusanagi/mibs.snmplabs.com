#
# PySNMP MIB module NETSCREEN-VSYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-VSYS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
netscreenVsys, = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenVsys")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, ModuleIdentity, TimeTicks, Bits, NotificationType, ObjectIdentity, MibIdentifier, Gauge32, iso, IpAddress, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "ModuleIdentity", "TimeTicks", "Bits", "NotificationType", "ObjectIdentity", "MibIdentifier", "Gauge32", "iso", "IpAddress", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenVsysMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 15, 0))
netscreenVsysMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-13 00:00', '2001-09-28 00:00', '2000-05-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netscreenVsysMibModule.setRevisionsDescriptions(('Modified copyright and contact information', 'Converted to SMIv2 by Longview Software', 'Correct spelling mistake', 'no comment', 'Creation Date',))
if mibBuilder.loadTexts: netscreenVsysMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenVsysMibModule.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: netscreenVsysMibModule.setContactInfo('Customer Support 1194 North Mathilda Avenue Sunnyvale, California 94089-1206 USA Tel: 1-800-638-8296 E-mail: customerservice@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: netscreenVsysMibModule.setDescription('This module defines the object that are use to monitor all the virtual systems')
nsVsysCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 15, 1))
nsVsysCfgTable = MibTable((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1), )
if mibBuilder.loadTexts: nsVsysCfgTable.setStatus('current')
if mibBuilder.loadTexts: nsVsysCfgTable.setDescription('NetScreen-500, NetScreen-1000 and above series support virtual system. This table collects the vsys configuration in NetScreen device.')
nsVsysCfgEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1), ).setIndexNames((0, "NETSCREEN-VSYS-MIB", "nsVsysCfgId"))
if mibBuilder.loadTexts: nsVsysCfgEntry.setStatus('current')
if mibBuilder.loadTexts: nsVsysCfgEntry.setDescription('Each entry in the table holds a set of configuration parameters associated with an instance of virtual system.')
nsVsysCfgId = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVsysCfgId.setStatus('current')
if mibBuilder.loadTexts: nsVsysCfgId.setDescription('A unique ID for each virtual system.')
nsVsysCfgName = MibTableColumn((1, 3, 6, 1, 4, 1, 3224, 15, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsVsysCfgName.setStatus('current')
if mibBuilder.loadTexts: nsVsysCfgName.setDescription('virtual system name.')
mibBuilder.exportSymbols("NETSCREEN-VSYS-MIB", nsVsysCfg=nsVsysCfg, netscreenVsysMibModule=netscreenVsysMibModule, PYSNMP_MODULE_ID=netscreenVsysMibModule, nsVsysCfgName=nsVsysCfgName, nsVsysCfgEntry=nsVsysCfgEntry, nsVsysCfgTable=nsVsysCfgTable, nsVsysCfgId=nsVsysCfgId)
