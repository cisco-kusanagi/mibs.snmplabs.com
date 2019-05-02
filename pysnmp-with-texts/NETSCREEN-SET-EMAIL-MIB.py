#
# PySNMP MIB module NETSCREEN-SET-EMAIL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NETSCREEN-SET-EMAIL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:20:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
netscreenSetting, netscreenSettingMibModule = mibBuilder.importSymbols("NETSCREEN-SMI", "netscreenSetting", "netscreenSettingMibModule")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32, Integer32, ModuleIdentity, Counter64, TimeTicks, Gauge32, IpAddress, NotificationType, ObjectIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32", "Integer32", "ModuleIdentity", "Counter64", "TimeTicks", "Gauge32", "IpAddress", "NotificationType", "ObjectIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
netscreenSetEmailMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 3224, 7, 0, 7))
netscreenSetEmailMibModule.setRevisions(('2004-05-03 00:00', '2004-03-03 00:00', '2003-11-10 00:00', '2001-09-28 00:00', '2001-05-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netscreenSetEmailMibModule.setRevisionsDescriptions(('Modified copyright and contact information', 'Converted to SMIv2 by Longview Software', 'Correct wrong title', 'No Comment', 'Creation Date',))
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setLastUpdated('200405032022Z')
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setContactInfo('Customer Support 1194 North Mathilda Avenue Sunnyvale, California 94089-1206 USA Tel: 1-800-638-8296 E-mail: customerservice@juniper.net HTTP://www.juniper.net')
if mibBuilder.loadTexts: netscreenSetEmailMibModule.setDescription('This module defines the object that are used to monitor the email notification setting')
nsSetEmail = MibIdentifier((1, 3, 6, 1, 4, 1, 3224, 7, 7))
nsSetEmailEnable = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailEnable.setStatus('current')
if mibBuilder.loadTexts: nsSetEmailEnable.setDescription('Enable E-mail Notification for Alarms')
nsSetEmailSMTP = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailSMTP.setStatus('current')
if mibBuilder.loadTexts: nsSetEmailSMTP.setDescription('SMTP server name')
nsSetEmailLog = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailLog.setStatus('current')
if mibBuilder.loadTexts: nsSetEmailLog.setDescription('Include Traffic Log in email')
nsSetEmailAddr1 = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailAddr1.setStatus('current')
if mibBuilder.loadTexts: nsSetEmailAddr1.setDescription('E-mail receiver address one')
nsSetEmailAddr2 = MibScalar((1, 3, 6, 1, 4, 1, 3224, 7, 7, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsSetEmailAddr2.setStatus('current')
if mibBuilder.loadTexts: nsSetEmailAddr2.setDescription('E-mail receiver address two')
mibBuilder.exportSymbols("NETSCREEN-SET-EMAIL-MIB", nsSetEmailEnable=nsSetEmailEnable, nsSetEmail=nsSetEmail, nsSetEmailAddr1=nsSetEmailAddr1, PYSNMP_MODULE_ID=netscreenSetEmailMibModule, nsSetEmailSMTP=nsSetEmailSMTP, nsSetEmailAddr2=nsSetEmailAddr2, nsSetEmailLog=nsSetEmailLog, netscreenSetEmailMibModule=netscreenSetEmailMibModule)
