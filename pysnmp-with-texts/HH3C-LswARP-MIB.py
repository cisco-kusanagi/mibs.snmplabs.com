#
# PySNMP MIB module HH3C-LswARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-LswARP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:27:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
hh3clswCommon, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3clswCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, MibIdentifier, NotificationType, IpAddress, Counter32, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Integer32, Bits, Counter64, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "MibIdentifier", "NotificationType", "IpAddress", "Counter32", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Integer32", "Bits", "Counter64", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cLswArpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4))
hh3cLswArpMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hh3cLswArpMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hh3cLswArpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hh3cLswArpMib.setOrganization('Hangzhou H3C Tech. Co., Ltd.')
if mibBuilder.loadTexts: hh3cLswArpMib.setContactInfo('Platform Team Hangzhou H3C Tech. Co., Ltd. Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085 ')
if mibBuilder.loadTexts: hh3cLswArpMib.setDescription('')
hh3cLswProxyArpObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1))
if mibBuilder.loadTexts: hh3cLswProxyArpObject.setStatus('current')
if mibBuilder.loadTexts: hh3cLswProxyArpObject.setDescription('Description.')
hh3cLswProxyArpEnableTable = MibTable((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1), )
if mibBuilder.loadTexts: hh3cLswProxyArpEnableTable.setStatus('current')
if mibBuilder.loadTexts: hh3cLswProxyArpEnableTable.setDescription('Contains information that if proxy ARP enabled for every VLAN interface. ')
hh3cLswProxyArpEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1, 1), ).setIndexNames((0, "HH3C-LswARP-MIB", "hh3cLswIfIndex"))
if mibBuilder.loadTexts: hh3cLswProxyArpEnableEntry.setStatus('current')
if mibBuilder.loadTexts: hh3cLswProxyArpEnableEntry.setDescription('Contains information that if proxy ARP enabled for VLAN interface.')
hh3cLswIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hh3cLswIfIndex.setStatus('current')
if mibBuilder.loadTexts: hh3cLswIfIndex.setDescription(' Vlan interface index ')
hh3cLswProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25506, 8, 35, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hh3cLswProxyArpStatus.setStatus('current')
if mibBuilder.loadTexts: hh3cLswProxyArpStatus.setDescription(' Proxy ARP status for this VLAN interface.')
mibBuilder.exportSymbols("HH3C-LswARP-MIB", hh3cLswArpMib=hh3cLswArpMib, hh3cLswProxyArpStatus=hh3cLswProxyArpStatus, hh3cLswProxyArpEnableEntry=hh3cLswProxyArpEnableEntry, hh3cLswProxyArpObject=hh3cLswProxyArpObject, hh3cLswProxyArpEnableTable=hh3cLswProxyArpEnableTable, PYSNMP_MODULE_ID=hh3cLswArpMib, hh3cLswIfIndex=hh3cLswIfIndex)
