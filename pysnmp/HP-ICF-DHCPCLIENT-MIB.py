#
# PySNMP MIB module HP-ICF-DHCPCLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-DHCPCLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetVersion, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetVersion")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ObjectIdentity, ModuleIdentity, iso, Counter32, Unsigned32, Gauge32, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Integer32, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "iso", "Counter32", "Unsigned32", "Gauge32", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Integer32", "Bits", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpicfDhcpClient = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57))
hpicfDhcpClient.setRevisions(('2013-06-01 00:00', '2012-05-31 00:00', '2010-08-09 00:00', '2009-03-18 00:00', '2008-10-30 00:00', '2008-08-27 00:38',))
if mibBuilder.loadTexts: hpicfDhcpClient.setLastUpdated('201306010000Z')
if mibBuilder.loadTexts: hpicfDhcpClient.setOrganization('HP Networking.')
hpicfDhcpClientOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1))
hpicfDhcpClientOptionsConf = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2))
hpicfDhcpClientVendorSpecOptionStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDhcpClientVendorSpecOptionStatus.setStatus('current')
hpicfDhcpClientHostNameOption = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDhcpClientHostNameOption.setStatus('current')
hpicfDhcpClientImageFileUpdate = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDhcpClientImageFileUpdate.setStatus('current')
hpicfDhcpClientintfTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 4), )
if mibBuilder.loadTexts: hpicfDhcpClientintfTable.setStatus('current')
hpicfDhcpClientintfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: hpicfDhcpClientintfEntry.setStatus('current')
hpicfDhcpClientAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("md5", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDhcpClientAuthType.setStatus('current')
hpicfDhcpClientKeyChain = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDhcpClientKeyChain.setStatus('current')
hpicfDhcpClientStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5), )
if mibBuilder.loadTexts: hpicfDhcpClientStatisticsTable.setStatus('current')
hpicfDhcpClientStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "HP-ICF-DHCPCLIENT-MIB", "hpicfIPVersion"))
if mibBuilder.loadTexts: hpicfDhcpClientStatisticsEntry.setStatus('current')
hpicfIPVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5, 1, 1), InetVersion())
if mibBuilder.loadTexts: hpicfIPVersion.setStatus('current')
hpicfDhcpClientPktTx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpClientPktTx.setStatus('current')
hpicfDhcpClientPktRx = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpClientPktRx.setStatus('current')
hpicfDhcpClientPktAuthFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpClientPktAuthFailed.setStatus('current')
hpicfDhcpv6ClientDuid = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(25, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfDhcpv6ClientDuid.setStatus('current')
hpicfDhcpClientTR069AcsUrlOptionStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfDhcpClientTR069AcsUrlOptionStatus.setStatus('current')
hpicfDhcpClientGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1))
hpicfDhcpClientCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2))
hpicfDhcpClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2, 1)).setObjects(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientOptionsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpClientCompliance = hpicfDhcpClientCompliance.setStatus('current')
hpicfDhcpClientVendorSpecOptionsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2, 2)).setObjects(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientVendorSpecOptionsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpClientVendorSpecOptionsCompliance = hpicfDhcpClientVendorSpecOptionsCompliance.setStatus('current')
hpicfDhcpClientAuthCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2, 3)).setObjects(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientAuthGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpClientAuthCompliance = hpicfDhcpClientAuthCompliance.setStatus('current')
hpicfDhcpv6ClientCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2, 4)).setObjects(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpv6ClientGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpv6ClientCompliance = hpicfDhcpv6ClientCompliance.setStatus('current')
hpicfDhcpClientTR069OptionsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 2, 5)).setObjects(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientTR069OptionsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpClientTR069OptionsCompliance = hpicfDhcpClientTR069OptionsCompliance.setStatus('current')
hpicfDhcpClientOptionsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1, 1)).setObjects(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientVendorSpecOptionStatus"), ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientHostNameOption"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpClientOptionsGroup = hpicfDhcpClientOptionsGroup.setStatus('current')
hpicfDhcpClientVendorSpecOptionsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1, 2)).setObjects(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientImageFileUpdate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpClientVendorSpecOptionsGroup = hpicfDhcpClientVendorSpecOptionsGroup.setStatus('current')
hpicfDhcpClientAuthGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1, 3)).setObjects(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientAuthType"), ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientKeyChain"), ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientPktTx"), ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientPktRx"), ("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientPktAuthFailed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpClientAuthGroup = hpicfDhcpClientAuthGroup.setStatus('current')
hpicfDhcpv6ClientGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1, 4)).setObjects(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpv6ClientDuid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpv6ClientGroup = hpicfDhcpv6ClientGroup.setStatus('current')
hpicfDhcpClientTR069OptionsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 57, 2, 1, 5)).setObjects(("HP-ICF-DHCPCLIENT-MIB", "hpicfDhcpClientTR069AcsUrlOptionStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfDhcpClientTR069OptionsGroup = hpicfDhcpClientTR069OptionsGroup.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-DHCPCLIENT-MIB", hpicfDhcpClientCompliances=hpicfDhcpClientCompliances, hpicfDhcpClientTR069AcsUrlOptionStatus=hpicfDhcpClientTR069AcsUrlOptionStatus, hpicfDhcpClientVendorSpecOptionStatus=hpicfDhcpClientVendorSpecOptionStatus, hpicfDhcpv6ClientCompliance=hpicfDhcpv6ClientCompliance, hpicfDhcpClient=hpicfDhcpClient, hpicfDhcpClientVendorSpecOptionsGroup=hpicfDhcpClientVendorSpecOptionsGroup, hpicfDhcpv6ClientGroup=hpicfDhcpv6ClientGroup, hpicfDhcpClientintfTable=hpicfDhcpClientintfTable, hpicfDhcpv6ClientDuid=hpicfDhcpv6ClientDuid, hpicfDhcpClientCompliance=hpicfDhcpClientCompliance, hpicfDhcpClientPktAuthFailed=hpicfDhcpClientPktAuthFailed, hpicfDhcpClientAuthCompliance=hpicfDhcpClientAuthCompliance, hpicfDhcpClientintfEntry=hpicfDhcpClientintfEntry, hpicfDhcpClientHostNameOption=hpicfDhcpClientHostNameOption, hpicfDhcpClientPktRx=hpicfDhcpClientPktRx, PYSNMP_MODULE_ID=hpicfDhcpClient, hpicfDhcpClientOptionsConf=hpicfDhcpClientOptionsConf, hpicfDhcpClientPktTx=hpicfDhcpClientPktTx, hpicfIPVersion=hpicfIPVersion, hpicfDhcpClientAuthType=hpicfDhcpClientAuthType, hpicfDhcpClientTR069OptionsGroup=hpicfDhcpClientTR069OptionsGroup, hpicfDhcpClientStatisticsTable=hpicfDhcpClientStatisticsTable, hpicfDhcpClientAuthGroup=hpicfDhcpClientAuthGroup, hpicfDhcpClientOptions=hpicfDhcpClientOptions, hpicfDhcpClientKeyChain=hpicfDhcpClientKeyChain, hpicfDhcpClientGroups=hpicfDhcpClientGroups, hpicfDhcpClientTR069OptionsCompliance=hpicfDhcpClientTR069OptionsCompliance, hpicfDhcpClientVendorSpecOptionsCompliance=hpicfDhcpClientVendorSpecOptionsCompliance, hpicfDhcpClientImageFileUpdate=hpicfDhcpClientImageFileUpdate, hpicfDhcpClientStatisticsEntry=hpicfDhcpClientStatisticsEntry, hpicfDhcpClientOptionsGroup=hpicfDhcpClientOptionsGroup)
