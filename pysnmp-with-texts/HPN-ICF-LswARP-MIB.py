#
# PySNMP MIB module HPN-ICF-LswARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LswARP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:39:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, iso, Integer32, NotificationType, ModuleIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, Bits, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "iso", "Integer32", "NotificationType", "ModuleIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "Bits", "Counter32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hpnicfLswArpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4))
hpnicfLswArpMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpnicfLswArpMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hpnicfLswArpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hpnicfLswArpMib.setOrganization('')
if mibBuilder.loadTexts: hpnicfLswArpMib.setContactInfo('')
if mibBuilder.loadTexts: hpnicfLswArpMib.setDescription('')
hpnicfLswProxyArpObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1))
if mibBuilder.loadTexts: hpnicfLswProxyArpObject.setStatus('current')
if mibBuilder.loadTexts: hpnicfLswProxyArpObject.setDescription('Description.')
hpnicfLswProxyArpEnableTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1), )
if mibBuilder.loadTexts: hpnicfLswProxyArpEnableTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfLswProxyArpEnableTable.setDescription('Contains information that if proxy ARP enabled for every VLAN interface. ')
hpnicfLswProxyArpEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-LswARP-MIB", "hpnicfLswIfIndex"))
if mibBuilder.loadTexts: hpnicfLswProxyArpEnableEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfLswProxyArpEnableEntry.setDescription('Contains information that if proxy ARP enabled for VLAN interface.')
hpnicfLswIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLswIfIndex.setStatus('current')
if mibBuilder.loadTexts: hpnicfLswIfIndex.setDescription(' Vlan interface index ')
hpnicfLswProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfLswProxyArpStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfLswProxyArpStatus.setDescription(' Proxy ARP status for this VLAN interface.')
mibBuilder.exportSymbols("HPN-ICF-LswARP-MIB", PYSNMP_MODULE_ID=hpnicfLswArpMib, hpnicfLswProxyArpObject=hpnicfLswProxyArpObject, hpnicfLswProxyArpStatus=hpnicfLswProxyArpStatus, hpnicfLswArpMib=hpnicfLswArpMib, hpnicfLswProxyArpEnableEntry=hpnicfLswProxyArpEnableEntry, hpnicfLswIfIndex=hpnicfLswIfIndex, hpnicfLswProxyArpEnableTable=hpnicfLswProxyArpEnableTable)
