#
# PySNMP MIB module HPN-ICF-LswARP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-LswARP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:27:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
hpnicflswCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicflswCommon")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, ObjectIdentity, Gauge32, Unsigned32, Integer32, Counter64, MibIdentifier, Counter32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "Gauge32", "Unsigned32", "Integer32", "Counter64", "MibIdentifier", "Counter32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hpnicfLswArpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4))
hpnicfLswArpMib.setRevisions(('2001-06-29 00:00',))
if mibBuilder.loadTexts: hpnicfLswArpMib.setLastUpdated('200106290000Z')
if mibBuilder.loadTexts: hpnicfLswArpMib.setOrganization('')
hpnicfLswProxyArpObject = ObjectIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1))
if mibBuilder.loadTexts: hpnicfLswProxyArpObject.setStatus('current')
hpnicfLswProxyArpEnableTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1), )
if mibBuilder.loadTexts: hpnicfLswProxyArpEnableTable.setStatus('current')
hpnicfLswProxyArpEnableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1), ).setIndexNames((0, "HPN-ICF-LswARP-MIB", "hpnicfLswIfIndex"))
if mibBuilder.loadTexts: hpnicfLswProxyArpEnableEntry.setStatus('current')
hpnicfLswIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpnicfLswIfIndex.setStatus('current')
hpnicfLswProxyArpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 4, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpnicfLswProxyArpStatus.setStatus('current')
mibBuilder.exportSymbols("HPN-ICF-LswARP-MIB", hpnicfLswArpMib=hpnicfLswArpMib, hpnicfLswIfIndex=hpnicfLswIfIndex, PYSNMP_MODULE_ID=hpnicfLswArpMib, hpnicfLswProxyArpEnableEntry=hpnicfLswProxyArpEnableEntry, hpnicfLswProxyArpObject=hpnicfLswProxyArpObject, hpnicfLswProxyArpStatus=hpnicfLswProxyArpStatus, hpnicfLswProxyArpEnableTable=hpnicfLswProxyArpEnableTable)
