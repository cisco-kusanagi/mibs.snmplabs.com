#
# PySNMP MIB module A3COM-HUAWEI-LswARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/A3COM-HUAWEI-LswARP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:05:43 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
lswCommon, = mibBuilder.importSymbols("A3COM-HUAWEI-OID-MIB", "lswCommon")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Gauge32, iso, IpAddress, MibIdentifier, NotificationType, ModuleIdentity, Integer32, Unsigned32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "iso", "IpAddress", "MibIdentifier", "NotificationType", "ModuleIdentity", "Integer32", "Unsigned32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hwLswArpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4))
hwLswArpMib.setRevisions(('2001-06-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hwLswArpMib.setRevisionsDescriptions(('',))
if mibBuilder.loadTexts: hwLswArpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswArpMib.setOrganization('')
if mibBuilder.loadTexts: hwLswArpMib.setContactInfo('')
if mibBuilder.loadTexts: hwLswArpMib.setDescription('')
hwLswProxyArpObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1))
if mibBuilder.loadTexts: hwLswProxyArpObject.setStatus('current')
if mibBuilder.loadTexts: hwLswProxyArpObject.setDescription('Description.')
hwLswProxyArpEnableTable = MibTable((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1), )
if mibBuilder.loadTexts: hwLswProxyArpEnableTable.setStatus('current')
if mibBuilder.loadTexts: hwLswProxyArpEnableTable.setDescription('Contains information that if proxy ARP enabled for every VLAN interface. ')
hwLswProxyArpEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1, 1), ).setIndexNames((0, "A3COM-HUAWEI-LswARP-MIB", "hwLswIfIndex"))
if mibBuilder.loadTexts: hwLswProxyArpEnableEntry.setStatus('current')
if mibBuilder.loadTexts: hwLswProxyArpEnableEntry.setDescription('Contains information that if proxy ARP enabled for VLAN interface.')
hwLswIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLswIfIndex.setStatus('current')
if mibBuilder.loadTexts: hwLswIfIndex.setDescription(' Vlan interface index ')
hwLswProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 43, 45, 1, 2, 23, 1, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLswProxyArpStatus.setStatus('current')
if mibBuilder.loadTexts: hwLswProxyArpStatus.setDescription(' Proxy ARP status for this VLAN interface.')
mibBuilder.exportSymbols("A3COM-HUAWEI-LswARP-MIB", hwLswProxyArpStatus=hwLswProxyArpStatus, hwLswProxyArpEnableEntry=hwLswProxyArpEnableEntry, hwLswProxyArpObject=hwLswProxyArpObject, hwLswArpMib=hwLswArpMib, hwLswProxyArpEnableTable=hwLswProxyArpEnableTable, hwLswIfIndex=hwLswIfIndex, PYSNMP_MODULE_ID=hwLswArpMib)
