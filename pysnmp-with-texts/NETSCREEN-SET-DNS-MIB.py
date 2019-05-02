#
# PySNMP MIB module NETSCREEN-SET-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-SET-DNS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
netscreenSetting, netscreenSettingMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Counter64, Counter32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, ModuleIdentity, Bits, IpAddress, ObjectIdentity, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "Counter32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "ModuleIdentity", "Bits", "IpAddress", "ObjectIdentity", "iso", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenSetDnsMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 3))
netscreenSetDnsMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-10 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netscreenSetDnsMibModule.setRevisionsDescriptions(('Modified copyright and contact information', 'Converted to SMIv2 by Longview Software', 'Correct wrong title', 'No Comment', 'Creation Date',))
if mibBuilder.loadTexts: netscreenSetDnsMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenSetDnsMibModule.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: netscreenSetDnsMibModule.setContactInfo('Customer Support 1194 North Mathilda Avenue Sunnyvale, California 94089-1206 USA Tel: 1-800-638-8296 E-mail: customerservice@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: netscreenSetDnsMibModule.setDescription('This module defines the object that are used to monitor all the configuration info')
nsSetDNS = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 3))
nsConfigDnsPriSer = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 3, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsConfigDnsPriSer.setStatus('current')
if mibBuilder.loadTexts: nsConfigDnsPriSer.setDescription('Primary DNS server ip address')
nsConfigDnsSecSer = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 3, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsConfigDnsSecSer.setStatus('current')
if mibBuilder.loadTexts: nsConfigDnsSecSer.setDescription('Secondary DNS server ip address')
nsConfigDnsRefEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsConfigDnsRefEnable.setStatus('current')
if mibBuilder.loadTexts: nsConfigDnsRefEnable.setDescription('Enable refresh DNS every day.')
nsConfigDnsRefTime = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 3, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsConfigDnsRefTime.setStatus('current')
if mibBuilder.loadTexts: nsConfigDnsRefTime.setDescription('DNS refresh time.')
mibBuilder.exportSymbols("NETSCREEN-SET-DNS-MIB", nsConfigDnsRefTime=nsConfigDnsRefTime, nsConfigDnsPriSer=nsConfigDnsPriSer, nsSetDNS=nsSetDNS, nsConfigDnsSecSer=nsConfigDnsSecSer, netscreenSetDnsMibModule=netscreenSetDnsMibModule, nsConfigDnsRefEnable=nsConfigDnsRefEnable, PYSNMP_MODULE_ID=netscreenSetDnsMibModule)
