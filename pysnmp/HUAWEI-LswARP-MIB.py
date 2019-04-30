#
# PySNMP MIB module HUAWEI-LswARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HUAWEI-LswARP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:34:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
lswCommon, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "lswCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Bits, Counter64, ModuleIdentity, TimeTicks, ObjectIdentity, Integer32, iso, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Bits", "Counter64", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "Integer32", "iso", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hwLswArpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4))
hwLswArpMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hwLswArpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hwLswArpMib.setOrganization('')
hwLswProxyArpObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1))
if mibBuilder.loadTexts: hwLswProxyArpObject.setStatus('current')
hwLswProxyArpEnableTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1), )
if mibBuilder.loadTexts: hwLswProxyArpEnableTable.setStatus('current')
hwLswProxyArpEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1, 1), ).setIndexNames((0, "HUAWEI-LswARP-MIB", "hwLswIfIndex"))
if mibBuilder.loadTexts: hwLswProxyArpEnableEntry.setStatus('current')
hwLswIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hwLswIfIndex.setStatus('current')
hwLswProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 2, 23, 1, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hwLswProxyArpStatus.setStatus('current')
mibBuilder.exportSymbols("HUAWEI-LswARP-MIB", hwLswProxyArpEnableTable=hwLswProxyArpEnableTable, hwLswProxyArpStatus=hwLswProxyArpStatus, hwLswArpMib=hwLswArpMib, hwLswProxyArpEnableEntry=hwLswProxyArpEnableEntry, hwLswProxyArpObject=hwLswProxyArpObject, PYSNMP_MODULE_ID=hwLswArpMib, hwLswIfIndex=hwLswIfIndex)
