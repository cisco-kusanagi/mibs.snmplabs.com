#
# PySNMP MIB module Fore-Channel-Config-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Fore-Channel-Config-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:03:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
asx, = mibBuilder.importSymbols("Fore-Common-MIB", "asx")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, iso, Counter32, MibIdentifier, Counter64, IpAddress, NotificationType, ObjectIdentity, ModuleIdentity, Unsigned32, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "iso", "Counter32", "MibIdentifier", "Counter64", "IpAddress", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
channelControlGroup = ModuleIdentity((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 11))
if mibBuilder.loadTexts: channelControlGroup.setLastUpdated('9911050000Z')
if mibBuilder.loadTexts: channelControlGroup.setOrganization('FORE')
channelConfigTable = MibTable((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 11, 1), )
if mibBuilder.loadTexts: channelConfigTable.setStatus('current')
channelConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 11, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: channelConfigEntry.setStatus('current')
channelConfigMode = MibTableColumn((1, 3, 6, 1, 4, 1, 326, 2, 2, 1, 1, 11, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("sts12c", 0), ("sts3cX4", 1), ("ds3X12", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: channelConfigMode.setStatus('current')
mibBuilder.exportSymbols("Fore-Channel-Config-MIB", channelConfigMode=channelConfigMode, channelConfigTable=channelConfigTable, PYSNMP_MODULE_ID=channelControlGroup, channelControlGroup=channelControlGroup, channelConfigEntry=channelConfigEntry)
