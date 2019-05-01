#
# PySNMP MIB module HUAWEI-LswARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LswARP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:46:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
lswCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "lswCommon")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, iso, Integer32, NotificationType, IpAddress, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, MibIdentifier, TimeTicks, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "Integer32", "NotificationType", "IpAddress", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwLswArpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4))
hwLswArpMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwLswArpMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hwLswArpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswArpMib.setOrganization('')
if mibBuilder.loadTexts: hwLswArpMib.setContactInfo('')
if mibBuilder.loadTexts: hwLswArpMib.setDescription('')
hwLswProxyArpObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1))
if mibBuilder.loadTexts: hwLswProxyArpObject.setStatus('current')
if mibBuilder.loadTexts: hwLswProxyArpObject.setDescription('Description.')
hwLswProxyArpEnableTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1), )
if mibBuilder.loadTexts: hwLswProxyArpEnableTable.setStatus('current')
if mibBuilder.loadTexts: hwLswProxyArpEnableTable.setDescription('Contains information that if proxy ARP enabled for every VLAN interface. ')
hwLswProxyArpEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1, 1), ).setIndexNames((0, "HUAWEI-LswARP-MIB", "hwLswIfIndex"))
if mibBuilder.loadTexts: hwLswProxyArpEnableEntry.setStatus('current')
if mibBuilder.loadTexts: hwLswProxyArpEnableEntry.setDescription('Contains information that if proxy ARP enabled for VLAN interface.')
hwLswIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLswIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwLswIfIndex.setDescription(' Vlan interface index ')
hwLswProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLswProxyArpStatus.setStatus('current')
if mibBuilder.loadTexts: hwLswProxyArpStatus.setDescription(' Proxy ARP status for this VLAN interface.')
mibBuilder.exportSymbols("HUAWEI-LswARP-MIB", hwLswProxyArpEnableTable=hwLswProxyArpEnableTable, hwLswProxyArpEnableEntry=hwLswProxyArpEnableEntry, hwLswProxyArpObject=hwLswProxyArpObject, PYSNMP_MODULE_ID=hwLswArpMib, hwLswArpMib=hwLswArpMib, hwLswProxyArpStatus=hwLswProxyArpStatus, hwLswIfIndex=hwLswIfIndex)
