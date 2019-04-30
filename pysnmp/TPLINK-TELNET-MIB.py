#
# PySNMP MIB module TPLINK-TELNET-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-TELNET-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:18:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, IpAddress, Counter64, TimeTicks, ObjectIdentity, Integer32, Bits, Unsigned32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "Counter64", "TimeTicks", "ObjectIdentity", "Integer32", "Bits", "Unsigned32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tplinkMgmt, = mibBuilder.importSymbols("TPLINK-MIB", "tplinkMgmt")
tplinkTelnet = ModuleIdentity((1, 3, 6, 1, 4, 1, 11863, 6, 52))
tplinkTelnet.setRevisions(('2016-02-26 11:10',))
if mibBuilder.loadTexts: tplinkTelnet.setLastUpdated('201602261110Z')
if mibBuilder.loadTexts: tplinkTelnet.setOrganization('TPLINK')
tplinkTelnetMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 52, 1))
tplinkTelnetMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 6, 52, 2))
telnetConfig = MibScalar((1, 3, 6, 1, 4, 1, 11863, 6, 52, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: telnetConfig.setStatus('current')
mibBuilder.exportSymbols("TPLINK-TELNET-MIB", tplinkTelnetMIBNotifications=tplinkTelnetMIBNotifications, tplinkTelnet=tplinkTelnet, tplinkTelnetMIBObjects=tplinkTelnetMIBObjects, PYSNMP_MODULE_ID=tplinkTelnet, telnetConfig=telnetConfig)
