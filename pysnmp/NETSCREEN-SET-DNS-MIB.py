#
# PySNMP MIB module NETSCREEN-SET-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-SET-DNS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:10:34 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
netscreenSetting, netscreenSettingMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibIdentifier, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, ObjectIdentity, ModuleIdentity, Unsigned32, Bits, IpAddress, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Bits", "IpAddress", "Counter32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
netscreenSetDnsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 3))
netscreenSetDnsMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-10 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))
if mibBuilder.loadTexts: netscreenSetDnsMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenSetDnsMibModule.setOrganization('Juniper Networks, Inc.')
nsSetDNS = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 3))
nsConfigDnsPriSer = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 3, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsConfigDnsPriSer.setStatus('current')
nsConfigDnsSecSer = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 3, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsConfigDnsSecSer.setStatus('current')
nsConfigDnsRefEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsConfigDnsRefEnable.setStatus('current')
nsConfigDnsRefTime = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsConfigDnsRefTime.setStatus('current')
mibBuilder.exportSymbols("NETSCREEN-SET-DNS-MIB", nsConfigDnsPriSer=nsConfigDnsPriSer, nsSetDNS=nsSetDNS, netscreenSetDnsMibModule=netscreenSetDnsMibModule, nsConfigDnsRefTime=nsConfigDnsRefTime, nsConfigDnsSecSer=nsConfigDnsSecSer, PYSNMP_MODULE_ID=netscreenSetDnsMibModule, nsConfigDnsRefEnable=nsConfigDnsRefEnable)
