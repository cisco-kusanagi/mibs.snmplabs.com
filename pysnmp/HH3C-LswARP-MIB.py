#
# PySNMP MIB module HH3C-LswARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LswARP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:15:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
hh3clswCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3clswCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, ModuleIdentity, TimeTicks, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Bits, Integer32, Counter64, IpAddress, Unsigned32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "ModuleIdentity", "TimeTicks", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Bits", "Integer32", "Counter64", "IpAddress", "Unsigned32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cLswArpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4))
hh3cLswArpMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hh3cLswArpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hh3cLswArpMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
hh3cLswProxyArpObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1))
if mibBuilder.loadTexts: hh3cLswProxyArpObject.setStatus('current')
hh3cLswProxyArpEnableTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1), )
if mibBuilder.loadTexts: hh3cLswProxyArpEnableTable.setStatus('current')
hh3cLswProxyArpEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1, 1), ).setIndexNames((0, "HH3C-LswARP-MIB", "hh3cLswIfIndex"))
if mibBuilder.loadTexts: hh3cLswProxyArpEnableEntry.setStatus('current')
hh3cLswIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLswIfIndex.setStatus('current')
hh3cLswProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLswProxyArpStatus.setStatus('current')
mibBuilder.exportSymbols("HH3C-LswARP-MIB", hh3cLswArpMib=hh3cLswArpMib, hh3cLswProxyArpObject=hh3cLswProxyArpObject, hh3cLswProxyArpStatus=hh3cLswProxyArpStatus, hh3cLswProxyArpEnableEntry=hh3cLswProxyArpEnableEntry, hh3cLswProxyArpEnableTable=hh3cLswProxyArpEnableTable, hh3cLswIfIndex=hh3cLswIfIndex, PYSNMP_MODULE_ID=hh3cLswArpMib)
