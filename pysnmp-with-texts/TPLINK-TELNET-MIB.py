#
# PySNMP MIB module TPLINK-TELNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-TELNET-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:04 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Counter64, NotificationType, Bits, Gauge32, iso, TimeTicks, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Counter64", "NotificationType", "Bits", "Gauge32", "iso", "TimeTicks", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkTelnet = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 52))
tplinkTelnet.setRevisions(('2016-02-26 11:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tplinkTelnet.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tplinkTelnet.setLastUpdated('201602261110Z')
if mibBuilder.loadTexts: tplinkTelnet.setOrganization('TPLINK')
if mibBuilder.loadTexts: tplinkTelnet.setContactInfo('www.tplink.com.cn')
if mibBuilder.loadTexts: tplinkTelnet.setDescription('Private MIB for Telnet configuration.')
tplinkTelnetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 52, 1))
tplinkTelnetMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 52, 2))
telnetConfig = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 52, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetConfig.setStatus('current')
if mibBuilder.loadTexts: telnetConfig.setDescription('0. disable 1. enable')
mibBuilder.exportSymbols("TPLINK-TELNET-MIB", telnetConfig=telnetConfig, tplinkTelnet=tplinkTelnet, PYSNMP_MODULE_ID=tplinkTelnet, tplinkTelnetMIBNotifications=tplinkTelnetMIBNotifications, tplinkTelnetMIBObjects=tplinkTelnetMIBObjects)
